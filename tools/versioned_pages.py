#!/usr/bin/env python3
"""Build a single approved publication channel. Never modify source branches.

The preview mode of the workflow still saves publication history, but only its
separate deploy job changes the live Pages site. Requires git and mike on PATH.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
import json
import re
import subprocess
import sys

PUBLISH_BRANCH = 'gh-pages-versioned'
REMOTE = 'origin'
BASELINE = 'baseline'

@dataclass(frozen=True)
class Plan:
    kind: str
    version: str | None = None
    config: str = 'mkdocs.versioned.yml'
    title: str | None = None


def publication_plan(event: str, ref: str, operation: str = '') -> Plan:
    if event == 'push' and ref == 'refs/heads/draft':
        return Plan('draft', 'draft', 'mkdocs.draft.yml', 'Mustand (draft)')
    if event == 'push' and ref.startswith('refs/tags/'):
        tag = ref.removeprefix('refs/tags/')
        if not re.fullmatch(r'v[0-9A-Za-z][0-9A-Za-z._-]*', tag):
            raise ValueError('Invalid release tag. Use v followed by letters, digits, dots, _ or -.')
        return Plan('release', tag, title=tag)
    if event == 'workflow_dispatch':
        if operation == 'draft' and ref == 'refs/heads/draft':
            return Plan('draft', 'draft', 'mkdocs.draft.yml', 'Mustand (draft)')
        if operation == 'bootstrap-stable' and ref == 'refs/heads/main':
            return Plan('bootstrap', BASELINE, title='Senine standard')
        if operation == 'republish' and ref == 'refs/heads/main':
            return Plan('republish')
    raise ValueError('Not allowed: draft must run on draft; bootstrap-stable/republish on main. '
                     'Releases use a v* tag whose commit is on main.')


def run(*args: str, capture: bool = False) -> subprocess.CompletedProcess:
    # Argument arrays, no shell interpolation of refs/tags.
    return subprocess.run(args, check=True, text=True, capture_output=capture)


def entries_from_remote() -> list[dict]:
    probe = subprocess.run(['git', 'ls-remote', '--exit-code', '--heads', REMOTE, PUBLISH_BRANCH],
                           capture_output=True, text=True)
    if probe.returncode == 2:  # A successful query with no matching ref.
        return []
    if probe.returncode != 0:
        raise RuntimeError('Cannot inspect publishing branch: ' + probe.stderr.strip())
    run('git', 'fetch', REMOTE,
        f'{PUBLISH_BRANCH}:refs/remotes/{REMOTE}/{PUBLISH_BRANCH}')
    result = run('git', 'show', f'refs/remotes/{REMOTE}/{PUBLISH_BRANCH}:versions.json', capture=True)
    entries = json.loads(result.stdout)
    if not isinstance(entries, list):
        raise ValueError('Unexpected versions.json. Refusing to overwrite publication history.')
    return entries


def stable_exists(entries: list[dict]) -> bool:
    return any(e.get('version') == 'stable' or 'stable' in e.get('aliases', []) for e in entries)


def check_state(plan: Plan, entries: list[dict]) -> bool:
    """Return whether to build; raise on unsafe/misordered operations."""
    if plan.kind in ('draft', 'republish') and not stable_exists(entries):
        raise ValueError('Stable has not been initialized. Run bootstrap-stable on main first.')
    if plan.kind == 'release' and any(e.get('version') == plan.version for e in entries):
        raise ValueError('This release already exists; published release versions are immutable. '
                         'Use republish to retry deployment, or approve a new tag.')
    if plan.kind == 'bootstrap':
        if stable_exists(entries):
            return False  # Re-running bootstrap must never reset an approved stable version.
        if any(e.get('version') == BASELINE for e in entries):
            raise ValueError('baseline already exists without stable; investigate before changing history.')
    return plan.kind != 'republish'


def tree_id(ref: str, path: str) -> str:
    return run('git', 'rev-parse', f'{ref}:{path}', capture=True).stdout.strip()


def execute(plan: Plan) -> None:
    # Fetch main before verifying provenance; a network failure must stop the run.
    run('git', 'fetch', REMOTE, 'main:refs/remotes/origin/main')
    if plan.kind == 'release':
        result = subprocess.run(['git', 'merge-base', '--is-ancestor', 'HEAD', 'refs/remotes/origin/main'])
        if result.returncode != 0:
            raise ValueError('Release commit is not on main. Do not publish a draft-only tag as stable.')
    if plan.kind == 'bootstrap':
        head = run('git', 'rev-parse', 'HEAD', capture=True).stdout.strip()
        main = run('git', 'rev-parse', 'refs/remotes/origin/main', capture=True).stdout.strip()
        if head != main:
            raise ValueError('main changed after this job was queued. Re-run bootstrap on the latest main.')

    entries = entries_from_remote()
    should_build = check_state(plan, entries)
    old_stable = None
    remote_ref = f'refs/remotes/{REMOTE}/{PUBLISH_BRANCH}'
    if plan.kind == 'draft':
        old_stable = tree_id(remote_ref, 'stable')

    if should_build:
        args = ['mike', 'deploy', '--config-file', plan.config,
                '--branch', PUBLISH_BRANCH, '--remote', REMOTE,
                '--alias-type', 'copy', '--title', plan.title or plan.version or '']
        if plan.kind in ('bootstrap', 'release'):
            args += ['--update-aliases', plan.version, 'stable']
        else:
            args += [plan.version]
        run(*args)
    else:
        # mike set-default also synchronizes an existing remote branch locally.
        print('Keeping existing published versions unchanged.')

    run('mike', 'set-default', '--config-file', 'mkdocs.versioned.yml',
        '--branch', PUBLISH_BRANCH, '--remote', REMOTE, 'stable')
    if old_stable is not None and old_stable != tree_id(PUBLISH_BRANCH, 'stable'):
        raise ValueError('Safety check failed: a draft build changed the stable tree. Nothing was pushed.')
    print(f'Prepared {plan.kind}. Source branches and the old gh-pages branch were not modified.')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--event', required=True)
    parser.add_argument('--ref', required=True)
    parser.add_argument('--operation', default='')
    args = parser.parse_args()
    try:
        execute(publication_plan(args.event, args.ref, args.operation))
    except (ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise SystemExit(1) from exc

if __name__ == '__main__':
    main()

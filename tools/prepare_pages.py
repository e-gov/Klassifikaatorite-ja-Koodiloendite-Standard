#!/usr/bin/env python3
"""Validate exported mike output, preserve legacy paths, and mark draft noindex.

Works only on the exported deployment artifact, never the source tree. The stable
and numbered-version trees stay byte-for-byte unchanged. Requires Python 3.11+.
"""
from __future__ import annotations
import argparse
import html
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import quote


def version_names(entries: list[dict]) -> set[str]:
    names = set()
    for entry in entries:
        for name in [entry['version'], *entry.get('aliases', [])]:
            if not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', name):
                raise ValueError(f'Unsafe version name: {name!r}')
            names.add(name)
    return names


def redirect_html(target: str) -> str:
    safe = html.escape(target, quote=True)
    js = json.dumps(target).replace('<', '\\u003c')
    return ('<!doctype html><html lang="et"><head><meta charset="utf-8">'
            '<meta name="robots" content="noindex">'
            f'<link rel="canonical" href="{safe}">'
            '<title>Standardi leht on kolinud</title>'
            f'<script>location.replace({js} + location.search + location.hash);</script>'
            f'<noscript><meta http-equiv="refresh" content="0; url={safe}"></noscript>'
            f'</head><body><a href="{safe}">Ava stabiilne versioon</a></body></html>')


def prepare(root: Path) -> dict:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError('Deployment directory does not exist.')
    if any(p.is_symlink() for p in root.rglob('*')):
        raise ValueError('Symlinks are not allowed in a Pages artifact. Use mike --alias-type copy.')
    entries = json.loads((root / 'versions.json').read_text(encoding='utf-8'))
    names = version_names(entries)
    stable = root / 'stable'
    if 'stable' not in names or not (stable / 'index.html').is_file():
        raise ValueError('A real stable version is required; draft must never be the site default.')
    for name in names:
        if not (root / name / 'index.html').is_file():
            raise ValueError(f'Published version is missing its home page: {name}')
    reserved = names | {'versions.json', '.nojekyll', 'CNAME', 'robots.txt'}
    redirects = assets = noindex = 0

    # Unversioned paths previously used by the site still resolve to stable.
    for source in sorted(stable.rglob('*')):
        if not source.is_file():
            continue
        rel = source.relative_to(stable)
        if rel.parts[0] in reserved:
            # Build metadata such as CNAME/robots is not a content path to migrate.
            if rel.as_posix() in {'CNAME', '.nojekyll', 'robots.txt', 'versions.json'}:
                continue
            raise ValueError(f'A stable content path conflicts with a reserved version path: {rel}')
        destination = root / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix.lower() == '.html' and rel.as_posix() != '404.html':
            target = Path(os.path.relpath(source, destination.parent)).as_posix()
            if target.endswith('/index.html'):
                target = target[:-len('index.html')]
            destination.write_text(redirect_html(quote(target, safe='/.-_~')), encoding='utf-8')
            redirects += 1
        else:
            shutil.copy2(source, destination)
            assets += 1

    # Draft is public, but should not compete with the approved standard in search.
    draft = root / 'draft'
    if draft.is_dir():
        for page in draft.rglob('*.html'):
            text = page.read_text(encoding='utf-8')
            if not re.search(r'<meta\b[^>]*name=[\"\x27]robots[\"\x27]', text, re.I):
                text, count = re.subn(r'</head\s*>',
                    '<meta name="robots" content="noindex,follow"></head>', text,
                    count=1, flags=re.I)
                if count != 1:
                    raise ValueError(f'Cannot mark draft page noindex: {page.relative_to(root)}')
                page.write_text(text, encoding='utf-8')
                noindex += 1
    (root / '.nojekyll').touch()
    return {'versions': sorted(names), 'legacy_redirects': redirects,
            'legacy_assets': assets, 'draft_pages_marked_noindex': noindex}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(prepare(args.directory), ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError) as exc:
        raise SystemExit(f'ERROR: {exc}') from exc

if __name__ == '__main__':
    main()

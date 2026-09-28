from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from versioned_pages import publication_plan, check_state, stable_exists
from prepare_pages import prepare, version_names, redirect_html

STABLE = [{'version': 'baseline', 'title': 'Senine standard', 'aliases': ['stable']}]
HTML = '<!doctype html><html><head><title>Fixture</title></head><body>Original</body></html>'

class PublicationTests(unittest.TestCase):
    def test_draft_push(self):
        p = publication_plan('push', 'refs/heads/draft')
        self.assertEqual((p.kind, p.config), ('draft', 'mkdocs.draft.yml'))

    def test_main_push_does_not_publish(self):
        with self.assertRaises(ValueError):
            publication_plan('push', 'refs/heads/main')

    def test_release_tag(self):
        p = publication_plan('push', 'refs/tags/v2.1.0')
        self.assertEqual((p.kind, p.version), ('release', 'v2.1.0'))

    def test_unsafe_tags_rejected(self):
        for tag in ['v../x', 'v1;echo x', 'v', 'v2 1', 'v1/other']:
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                publication_plan('push', 'refs/tags/' + tag)

    def test_bootstrap_only_main(self):
        self.assertEqual(publication_plan('workflow_dispatch', 'refs/heads/main',
                         'bootstrap-stable').kind, 'bootstrap')
        with self.assertRaises(ValueError):
            publication_plan('workflow_dispatch', 'refs/heads/draft', 'bootstrap-stable')

    def test_manual_draft_only_draft(self):
        with self.assertRaises(ValueError):
            publication_plan('workflow_dispatch', 'refs/heads/main', 'draft')
        self.assertEqual(publication_plan('workflow_dispatch', 'refs/heads/draft', 'draft').kind, 'draft')

    def test_draft_cannot_be_default_when_stable_missing(self):
        p = publication_plan('push', 'refs/heads/draft')
        with self.assertRaises(ValueError):
            check_state(p, [])
        self.assertTrue(check_state(p, STABLE))

    def test_new_baseline(self):
        p = publication_plan('workflow_dispatch', 'refs/heads/main', 'bootstrap-stable')
        self.assertTrue(check_state(p, []))

    def test_bootstrap_does_not_reset_existing_stable(self):
        p = publication_plan('workflow_dispatch', 'refs/heads/main', 'bootstrap-stable')
        self.assertFalse(check_state(p, STABLE))
        self.assertFalse(check_state(p, [{'version': 'v4', 'aliases': ['stable']}]))

    def test_incomplete_baseline_rejected(self):
        p = publication_plan('workflow_dispatch', 'refs/heads/main', 'bootstrap-stable')
        with self.assertRaises(ValueError):
            check_state(p, [{'version': 'baseline', 'aliases': []}])

    def test_immutable_release(self):
        p = publication_plan('push', 'refs/tags/v2.1')
        self.assertTrue(check_state(p, STABLE))
        with self.assertRaises(ValueError):
            check_state(p, [{'version': 'v2.1', 'aliases': ['stable']}])

    def test_republish_never_builds(self):
        p = publication_plan('workflow_dispatch', 'refs/heads/main', 'republish')
        self.assertFalse(check_state(p, STABLE))
        with self.assertRaises(ValueError):
            check_state(p, [])

    def test_stable_alias_detection(self):
        self.assertTrue(stable_exists(STABLE))
        self.assertFalse(stable_exists([{'version': 'draft', 'aliases': []}]))

class ArtifactTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        entries = STABLE + [{'version': 'draft', 'title': 'Mustand', 'aliases': []}]
        (self.root / 'versions.json').write_text(json.dumps(entries), encoding='utf-8')
        for version in ['baseline', 'stable', 'draft']:
            d = self.root / version
            (d / 'klassifikaator/atribuudid').mkdir(parents=True)
            (d / 'assets').mkdir()
            (d / 'index.html').write_text(HTML, encoding='utf-8')
            (d / 'klassifikaator/atribuudid/index.html').write_text(HTML, encoding='utf-8')
            (d / 'assets/style.css').write_text('body { margin: 0; }', encoding='utf-8')

    def hashes(self, name):
        folder = self.root / name
        return {p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in folder.rglob('*') if p.is_file()}

    def test_stable_and_baseline_are_unchanged(self):
        stable, baseline = self.hashes('stable'), self.hashes('baseline')
        prepare(self.root)
        self.assertEqual(stable, self.hashes('stable'))
        self.assertEqual(baseline, self.hashes('baseline'))

    def test_old_home_and_deep_links_redirect_to_stable(self):
        prepare(self.root)
        self.assertIn('stable/', (self.root / 'index.html').read_text())
        page = (self.root / 'klassifikaator/atribuudid/index.html').read_text()
        self.assertIn('../../stable/klassifikaator/atribuudid/', page)
        self.assertIn('location.search + location.hash', page)

    def test_draft_marked_noindex(self):
        report = prepare(self.root)
        self.assertEqual(report['draft_pages_marked_noindex'], 2)
        self.assertIn('noindex,follow', (self.root / 'draft/index.html').read_text())
        self.assertNotIn('noindex', (self.root / 'stable/index.html').read_text())

    def test_assets_and_nojekyll(self):
        prepare(self.root)
        self.assertEqual((self.root / 'assets/style.css').read_bytes(),
                         (self.root / 'stable/assets/style.css').read_bytes())
        self.assertTrue((self.root / '.nojekyll').exists())

    def test_prepare_is_idempotent(self):
        prepare(self.root)
        first = self.hashes('draft')
        prepare(self.root)
        self.assertEqual(first, self.hashes('draft'))

    def test_no_stable_fails(self):
        (self.root / 'stable/index.html').unlink()
        with self.assertRaises(ValueError):
            prepare(self.root)

    def test_missing_declared_version_fails(self):
        (self.root / 'baseline/index.html').unlink()
        with self.assertRaises(ValueError):
            prepare(self.root)

    def test_symlinks_fail(self):
        (self.root / 'alias').symlink_to(self.root / 'stable', target_is_directory=True)
        with self.assertRaises(ValueError):
            prepare(self.root)

    def test_reserved_version_path_collision_fails(self):
        (self.root / 'stable/draft').mkdir()
        (self.root / 'stable/draft/index.html').write_text(HTML)
        with self.assertRaises(ValueError):
            prepare(self.root)

    def test_unsafe_version_paths_fail(self):
        for name in ['../outside', '/tmp/site', 'v1/sub', '.', '..']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                version_names([{'version': name, 'aliases': []}])

    def test_redirect_escapes_input(self):
        page = redirect_html('stable/x?<script>')
        self.assertNotIn('location.replace("stable/x?<script>', page)
        self.assertIn('&lt;script&gt;', page)

if __name__ == '__main__':
    unittest.main()

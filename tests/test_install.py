from __future__ import annotations
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from css.core import Catalog,CSSError
from css.install import install,restore
import css.install as module
ROOT=Path(__file__).resolve().parents[1]

class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.target=Path(self.temp.name);self.catalog=Catalog(ROOT)
    def test_dry_run_has_no_writes(self):
        r=install(self.catalog,'starter',self.target)
        self.assertFalse(r['applied']);self.assertEqual(list(self.target.iterdir()),[])
    def test_claude_manual_invocation(self):
        install(self.catalog,'starter',self.target,apply=True)
        t=(self.target/'.claude/skills/system-design/SKILL.md').read_text()
        self.assertIn('disable-model-invocation: true',t);self.assertNotIn('allowed-tools:',t)
    def test_codex_manual_invocation(self):
        install(self.catalog,'starter',self.target,'codex',True)
        self.assertIn('allow_implicit_invocation: false',(self.target/'.agents/skills/system-design/agents/openai.yaml').read_text())
        self.assertNotIn('disable-model-invocation:',(self.target/'.agents/skills/system-design/SKILL.md').read_text())
    def test_generic_export(self):
        install(self.catalog,'starter',self.target,'generic',True)
        self.assertTrue((self.target/'exported-skills/system-design/SKILL.md').is_file())
    def test_unmanaged_collision(self):
        p=self.target/'.claude/skills/system-design/SKILL.md';p.parent.mkdir(parents=True);p.write_text('user content')
        with self.assertRaisesRegex(CSSError,'refusing'):install(self.catalog,'starter',self.target,apply=True)
        self.assertEqual(p.read_text(),'user content')
    def test_local_modification_preserved(self):
        install(self.catalog,'starter',self.target,apply=True)
        p=self.target/'.claude/skills/system-design/SKILL.md';p.write_text('my changes')
        with self.assertRaisesRegex(CSSError,'refusing'):install(self.catalog,'starter',self.target,apply=True)
        self.assertEqual(p.read_text(),'my changes')
    def test_reinstall_noop(self):
        install(self.catalog,'starter',self.target,apply=True)
        r=install(self.catalog,'starter',self.target,apply=True)
        self.assertIsNone(r['backup']);self.assertTrue(all(x['action']=='unchanged' for x in r['plan']))
    def test_git_directory_untouched(self):
        p=self.target/'.git';p.mkdir();(p/'sentinel').write_text('keep')
        install(self.catalog,'starter',self.target,apply=True)
        self.assertEqual((p/'sentinel').read_text(),'keep')
    def test_bad_profile_name(self):
        with self.assertRaises(CSSError):install(self.catalog,'../secret',self.target)
    def test_nonexistent_target(self):
        with self.assertRaises(CSSError):install(self.catalog,'starter',self.target/'missing')
    def test_symlink_destination(self):
        outside=self.target/'outside';outside.mkdir()
        try:(self.target/'.claude').symlink_to(outside,target_is_directory=True)
        except (OSError,NotImplementedError):self.skipTest('symlink privilege unavailable')
        with self.assertRaises(CSSError):install(self.catalog,'starter',self.target,apply=True)
        self.assertEqual(list(outside.iterdir()),[])
    def test_restore_preview(self):
        r=install(self.catalog,'starter',self.target,apply=True)
        x=restore(self.target,r['backup'])
        self.assertFalse(x['applied']);self.assertTrue((self.target/'.claude/skills/system-design/SKILL.md').exists())
    def test_restore_actual(self):
        r=install(self.catalog,'starter',self.target,apply=True)
        restore(self.target,r['backup'],True)
        self.assertFalse((self.target/'.claude/skills/system-design/SKILL.md').exists())
        self.assertFalse((self.target/'.css/install-claude.json').exists())
    def test_restore_protects_edits(self):
        r=install(self.catalog,'starter',self.target,apply=True)
        p=self.target/'.claude/skills/system-design/SKILL.md';p.write_text('edited')
        with self.assertRaises(CSSError):restore(self.target,r['backup'],True)
        self.assertEqual(p.read_text(),'edited')
    def test_restore_bad_id(self):
        with self.assertRaises(CSSError):restore(self.target,'../outside',True)
    def test_lock_not_stolen(self):
        p=self.target/'.css/install.lock';p.parent.mkdir();p.write_text('other process')
        with self.assertRaisesRegex(CSSError,'lock'):install(self.catalog,'starter',self.target,apply=True)
        self.assertEqual(p.read_text(),'other process')
    def test_caught_write_failure_rolls_back(self):
        original=module._write;calls=0
        def fail(root,rel,data):
            nonlocal calls
            if rel.startswith('.claude/skills/'):
                calls+=1
                if calls==2:raise OSError('injected write failure')
            return original(root,rel,data)
        with patch('css.install._write',side_effect=fail):
            with self.assertRaisesRegex(CSSError,'written files restored'):install(self.catalog,'starter',self.target,apply=True)
        self.assertFalse(any((self.target/'.claude').rglob('SKILL.md')))
        self.assertFalse((self.target/'.css/install-claude.json').exists())
    def test_two_profiles_keep_prior_skills(self):
        install(self.catalog,'starter',self.target,apply=True)
        install(self.catalog,'payments',self.target,apply=True)
        self.assertTrue((self.target/'.claude/skills/debugging-code/SKILL.md').exists())
        self.assertTrue((self.target/'.claude/skills/designing-ledgers/SKILL.md').exists())

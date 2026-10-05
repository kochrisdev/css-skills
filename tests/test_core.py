from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from css.core import Catalog, CSSError, confined, content_digest, frontmatter, read_json, topo
ROOT=Path(__file__).resolve().parents[1]

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.catalog=Catalog(ROOT)
    def test_package_validates(self):self.assertTrue(self.catalog.validate()['ok'])
    def test_200_ids_preserved(self):
        self.assertEqual({s['id'] for s in self.catalog.skills},{f'CSS-{i:03d}' for i in range(1,201)})
    def test_40_pilots(self):self.assertEqual(sum(s['status']=='pilot' for s in self.catalog.skills),40)
    def test_160_drafts(self):self.assertEqual(sum(s['status']=='draft' for s in self.catalog.skills),160)
    def test_no_behavioral_claims(self):self.assertTrue(all(s['behavioral_evaluation']=='not_run' for s in self.catalog.skills))
    def test_all_workflows(self):
        for p in (ROOT/'workflows').glob('*.json'):
            with self.subTest(p=p):self.assertFalse(self.catalog.workflow(p.stem)['executed'])
    def test_all_profiles(self):
        for p in (ROOT/'profiles').glob('*.json'):
            with self.subTest(p=p):self.assertTrue(self.catalog.profile(p.stem))
    def test_profile_has_no_drafts(self):self.assertTrue(all(self.catalog.by_name[n]['status']=='pilot' for n in self.catalog.profile('pilot')))
    def test_search_abstains(self):self.assertTrue(self.catalog.search('chocolate cake recipe')['abstained'])
    def test_search_empty(self):self.assertTrue(self.catalog.search('')['abstained'])
    def test_search_guardrails_plural(self):self.assertEqual(self.catalog.search('agent guardrail prompt injection permission policy')['results'][0]['name'],'designing-agent-guardrails')
    def test_search_draft_exclusion(self):self.assertFalse(any(x['status']=='draft' for x in self.catalog.search('wallet')['results']))
    def test_search_draft_opt_in(self):self.assertTrue(any(x['status']=='draft' for x in self.catalog.search('wallet',include_drafts=True)['results']))
    def test_search_deterministic(self):self.assertEqual(self.catalog.search('ledger currency journal'),self.catalog.search('ledger currency journal'))
    def test_search_invalid_limit(self):
        with self.assertRaises(CSSError):self.catalog.search('x',limit=0)
    def test_relative_content_root(self):self.assertEqual(content_digest(ROOT,'skills/designing-ledgers'),content_digest(ROOT/'..'/'css-skills','skills/designing-ledgers'))
    def test_legacy_map_complete(self):self.assertEqual(len(read_json(ROOT/'catalog/legacy-map.json')['skills']),200)
    def test_case_count(self):
        count=sum(len(read_json(ROOT/'skills'/s['name']/'evals/cases.json')['cases']) for s in self.catalog.skills if s['status']=='pilot')
        self.assertEqual(count,160)

class ParserTests(unittest.TestCase):
    def test_valid_frontmatter(self):self.assertEqual(frontmatter('---\nname: hello\ndescription: "A useful test."\n---\nBody')[0]['name'],'hello')
    def test_frontmatter_must_be_first(self):
        with self.assertRaises(CSSError):frontmatter('text\n---\nname: x\n---\n')
    def test_frontmatter_unclosed(self):
        with self.assertRaises(CSSError):frontmatter('---\nname: x\n')
    def test_frontmatter_duplicate(self):
        with self.assertRaises(CSSError):frontmatter('---\nname: x\nname: y\ndescription: "z"\n---\n')
    def test_frontmatter_unknown(self):
        with self.assertRaises(CSSError):frontmatter('---\nname: x\ndescription: "z"\nallowed-tools: Bash\n---\n')
    def test_frontmatter_yaml_alias_rejected(self):
        with self.assertRaises(CSSError):frontmatter('---\nname: x\ndescription: *secret\n---\n')
    def test_frontmatter_missing_description(self):
        with self.assertRaises(CSSError):frontmatter('---\nname: x\n---\n')
    def test_frontmatter_nonstring(self):
        with self.assertRaises(CSSError):frontmatter('---\nname: x\ndescription: 42.2\n---\n')
    def test_json_duplicate(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.json';p.write_text('{"a":1,"a":2}')
            with self.assertRaises(CSSError):read_json(p)
    def test_path_traversal(self):
        with self.assertRaises(CSSError):confined(ROOT,'../outside')
    def test_absolute_path(self):
        with self.assertRaises(CSSError):confined(ROOT,'/tmp/outside')
    def test_windows_separator(self):
        with self.assertRaises(CSSError):confined(ROOT,'..\\outside')
    def test_drive_path(self):
        with self.assertRaises(CSSError):confined(ROOT,'C:/outside')
    def test_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'real').mkdir()
            try:(p/'link').symlink_to(p/'real',target_is_directory=True)
            except (OSError,NotImplementedError):self.skipTest('symlink privilege unavailable')
            with self.assertRaises(CSSError):confined(p,'link/file')
    def test_graph_cycle(self):
        with self.assertRaisesRegex(CSSError,'cycle'):topo({'a':['b'],'b':['a']})
    def test_graph_unknown(self):
        with self.assertRaisesRegex(CSSError,'unknown'):topo({'a':['b']})
    def test_graph_order(self):self.assertEqual(topo({'b':['a'],'a':[]}),['a','b'])

class MutationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'css';shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','.css'))
    def change_registry(self,change):
        p=self.root/'catalog/skill-registry.json';r=read_json(p);change(r);p.write_text(json.dumps(r));return Catalog(self.root).validate()
    def test_duplicate_id(self):self.assertFalse(self.change_registry(lambda r:r['skills'][1].update(id=r['skills'][0]['id']))['ok'])
    def test_duplicate_name(self):self.assertFalse(self.change_registry(lambda r:r['skills'][1].update(name=r['skills'][0]['name']))['ok'])
    def test_bad_name(self):self.assertFalse(self.change_registry(lambda r:r['skills'][0].update(name='Bad--Name'))['ok'])
    def test_bad_path(self):self.assertFalse(self.change_registry(lambda r:r['skills'][0].update(path='../secret'))['ok'])
    def test_false_maturity(self):self.assertFalse(self.change_registry(lambda r:r['skills'][0].update(status='production'))['ok'])
    def test_false_behavioral_claim(self):self.assertFalse(self.change_registry(lambda r:r['skills'][0].update(behavioral_evaluation='passed'))['ok'])
    def test_unknown_metadata(self):self.assertFalse(self.change_registry(lambda r:r['skills'][0].update(secret_permission=True))['ok'])
    def test_unknown_dependency(self):self.assertFalse(self.change_registry(lambda r:r['skills'][0].update(depends_on=['missing']))['ok'])
    def test_dependency_cycle(self):
        def change(r):
            a,b=r['skills'][:2];a['depends_on']=[b['name']];b['depends_on']=[a['name']]
        self.assertFalse(self.change_registry(change)['ok'])
    def test_changed_skill_hash(self):
        p=self.root/'skills/system-design/SKILL.md';p.write_text(p.read_text()+'\nChanged\n')
        self.assertFalse(Catalog(self.root).validate()['ok'])
    def test_missing_case_resource(self):
        (self.root/'skills/system-design/evals/cases.json').unlink()
        self.assertFalse(Catalog(self.root).validate()['ok'])
    def test_workflow_wrong_type(self):
        p=self.root/'workflows/bank-digital-twin.json';v=read_json(p);v['inputs']['request']='incorrect';p.write_text(json.dumps(v))
        self.assertFalse(Catalog(self.root).validate()['ok'])
    def test_workflow_missing_gate(self):
        p=self.root/'workflows/bank-digital-twin.json';v=read_json(p)
        for s in v['steps']:s['approval']='none'
        p.write_text(json.dumps(v));self.assertFalse(Catalog(self.root).validate()['ok'])
    def test_workflow_cycle(self):
        p=self.root/'workflows/bank-digital-twin.json';v=read_json(p);v['steps'][0]['after']=[v['steps'][-1]['id']];p.write_text(json.dumps(v))
        self.assertFalse(Catalog(self.root).validate()['ok'])
    def test_draft_in_profile(self):
        p=self.root/'profiles/starter.json';v=read_json(p);v['skills'].append('designing-wallets');p.write_text(json.dumps(v))
        self.assertFalse(Catalog(self.root).validate()['ok'])

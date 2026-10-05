from __future__ import annotations
from contextlib import redirect_stdout,redirect_stderr
from decimal import Decimal
from io import StringIO
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from css import __version__
from css.core import Catalog,CSSError,content_digest,read_json
from css.pevc import amount,fund_multiples,priced_round,sources_uses,exit_bridge,main
ROOT=Path(__file__).resolve().parents[1]

class PEVCIntegrationTests(unittest.TestCase):
    def setUp(self):self.catalog=Catalog(ROOT)
    def test_24_new_pilots(self):
        manifest=read_json(ROOT/'catalog/pe-vc-pack.json')
        self.assertEqual(len(manifest['skills']),24)
        self.assertTrue(all(self.catalog.by_name[n]['status']=='pilot' for n in manifest['skills']))
    def test_all_224_ids_unique(self):
        self.assertEqual({s['id'] for s in self.catalog.skills},{f'CSS-{i:03d}' for i in range(1,225)})
    def test_original_names_preserved(self):
        legacy=read_json(ROOT/'catalog/legacy-map.json')['skills']
        self.assertEqual(len(legacy),200)
        # The complete old-ID/name map is checked via committed baseline manifest below.
        original=read_json(ROOT/'catalog/v05-identities.json')
        self.assertTrue(all(self.catalog.by_name[s['name']]['id']==s['id'] for s in original))
    def test_new_domains_have_eight_each(self):
        for domain in ['private-equity','venture-capital','private-capital']:
            self.assertEqual(sum(s['domain']==domain for s in self.catalog.skills),8)
    def test_version_and_schema(self):
        self.assertEqual(__version__,self.catalog.raw['version'])
        schema=read_json(ROOT/'schemas/registry.schema.json')
        self.assertEqual(schema['properties']['version']['const'],__version__)
    def test_no_fabricated_legacy_paths(self):
        self.assertTrue(all(s['legacy_path'] is None for s in self.catalog.skills if int(s['id'][4:])>200))
    def test_pevc_profile_exactly_24(self):self.assertEqual(len(self.catalog.profile('pe-vc')),24)
    def test_pe_vc_profiles_installable(self):
        from css.install import install
        for runtime in ['claude','codex','generic']:
            with tempfile.TemporaryDirectory() as d:
                before=list(Path(d).iterdir());r=install(self.catalog,'pe-vc',Path(d),runtime,False)
                self.assertFalse(r.get('conflicts'));self.assertEqual(list(Path(d).iterdir()),before)
    def test_new_workflows_are_plan_only(self):
        for name in ['pe-underwriting','vc-diligence','private-fund-review','investment-committee']:
            flow=self.catalog.workflow(name);self.assertFalse(flow['executed'])
            self.assertTrue(all(s['approval']=='human-review-required' for s in flow['steps']))
    def test_new_case_count(self):
        manifest=read_json(ROOT/'catalog/pe-vc-pack.json')
        self.assertEqual(sum(len(read_json(ROOT/'skills'/n/'evals/cases.json')['cases']) for n in manifest['skills']),96)
    def test_digests_from_renamed_checkout(self):
        with tempfile.TemporaryDirectory() as d:
            renamed=Path(d)/'arbitrary-folder-name';(renamed/'skills').mkdir(parents=True)
            shutil.copytree(ROOT/'skills/modeling-buyouts',renamed/'skills/modeling-buyouts')
            self.assertEqual(content_digest(renamed,'skills/modeling-buyouts'),content_digest(renamed/'..'/renamed.name,'skills/modeling-buyouts'))
    def test_distinct_procedures(self):
        manifest=read_json(ROOT/'catalog/pe-vc-pack.json');bodies=[]
        for n in manifest['skills']:
            t=(ROOT/'skills'/n/'SKILL.md').read_text(encoding='utf-8');bodies.append(t.split('## Workflow\n')[1].split('## Output contract')[0])
        self.assertEqual(len(set(bodies)),24)

class FinancialHelperTests(unittest.TestCase):
    def funds(self,**kw):
        args=dict(paid_in='50',distributions='20',nav='40',currency='USD',as_of='2026-10-05',basis='net');args.update(kw);return fund_multiples(**args)
    def round(self,**kw):
        args=dict(pre_money='8000000',investment='2000000',holders={'founders':'8000000','pool':'2000000'},currency='USD');args.update(kw);return priced_round(**args)
    def exit(self,**kw):
        args=dict(enterprise_value='100',debt='40',cash='5',costs='5',invested_equity='30',interim_distributions='0',currency='USD');args.update(kw);return exit_bridge(**args)
    def test_fund_multiples_exact(self):
        r=self.funds();self.assertEqual([r[x] for x in ['DPI','RVPI','TVPI']],['0.4','0.8','1.2'])
    def test_fund_zero_denominator(self):
        with self.assertRaises(CSSError):self.funds(paid_in=0)
    def test_fund_missing_basis(self):
        with self.assertRaises(CSSError):self.funds(basis='unknown')
    def test_fund_negative_nav_unsupported(self):
        with self.assertRaises(CSSError):self.funds(nav='-1')
    def test_invalid_currency(self):
        with self.assertRaises(CSSError):self.funds(currency='USD/EUR')
    def test_invalid_date(self):
        with self.assertRaises(CSSError):self.funds(as_of='2026-02-31')
    def test_date_requires_iso(self):
        with self.assertRaises(CSSError):self.funds(as_of='20261005')
    def test_nonfinite_rejected(self):
        for v in ['NaN','Infinity','-Infinity',Decimal('NaN')]:
            with self.subTest(v=v),self.assertRaises(CSSError):amount(v,'value')
    def test_float_and_bool_rejected(self):
        for v in [0.1,True,False,None,[],{}]:
            with self.subTest(v=v),self.assertRaises(CSSError):amount(v,'value')
    def test_negative_and_exponent_rejected(self):
        for v in ['-1','1e99',' 1','0.'+('1'*13)]:
            with self.subTest(v=v),self.assertRaises(CSSError):amount(v,'value')
    def test_exact_decimal_supported(self):self.assertEqual(amount('0.100000000001','x'),Decimal('0.100000000001'))
    def test_priced_round(self):
        r=self.round();self.assertEqual(r['price_per_share'],'0.8');self.assertEqual(r['post_round_shares'],'12500000');self.assertEqual(r['holders']['new-investor']['ownership_fraction'],'0.2')
    def test_ownership_reconciles(self):self.assertEqual(sum(Decimal(r['ownership_fraction']) for r in self.round()['holders'].values()),Decimal('1'))
    def test_zero_shares_rejected(self):
        with self.assertRaises(CSSError):self.round(holders={'founder':'0'})
    def test_reserved_holder_rejected(self):
        with self.assertRaises(CSSError):self.round(holders={'new-investor':'1'})
    def test_pool_change_is_not_accepted(self):
        with self.assertRaises(TypeError):self.round(option_pool_topup='10')
    def test_zero_investment_rejected(self):
        with self.assertRaises(CSSError):self.round(investment='0')
    def test_sources_uses(self):
        r=sources_uses(sources={'debt':'30','equity':'25'},uses={'purchase':'50','fees':'5'},currency='USD');self.assertTrue(r['balanced'])
    def test_sources_uses_gap(self):
        r=sources_uses(sources={'equity':'50'},uses={'purchase':'55'},currency='USD');self.assertFalse(r['balanced']);self.assertEqual(r['gap_sources_less_uses'],'-5')
    def test_empty_sources_rejected(self):
        with self.assertRaises(CSSError):sources_uses(sources={},uses={'p':'1'},currency='USD')
    def test_exit_bridge(self):self.assertEqual(self.exit()['MOIC'],'2')
    def test_loss_is_not_negative_distribution(self):
        r=self.exit(enterprise_value='10');self.assertEqual(r['terminal_equity'],'0');self.assertEqual(r['claim_shortfall'],'30');self.assertEqual(r['MOIC'],'0')
    def test_interim_included(self):self.assertEqual(self.exit(interim_distributions='30')['MOIC'],'3')
    def test_exit_no_invested_equity(self):
        with self.assertRaises(CSSError):self.exit(invested_equity=0)
    def test_cli_read_only(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.json';p.write_text(json.dumps({'operation':'fund-multiples','inputs':dict(paid_in='50',distributions='20',nav='40',currency='USD',as_of='2026-10-05',basis='net')}));before=p.read_bytes()
            with redirect_stdout(StringIO()):self.assertEqual(main([str(p)]),0)
            self.assertEqual(p.read_bytes(),before);self.assertEqual(len(list(Path(d).iterdir())),1)
    def test_cli_rejects_unknown_fields(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.json';p.write_text('{"operation":"priced-round","inputs":{},"execute":true}')
            with redirect_stderr(StringIO()):self.assertEqual(main([str(p)]),2)
    def test_cli_rejects_duplicate_json(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.json';p.write_text('{"operation":"priced-round","operation":"exit-bridge","inputs":{}}')
            with redirect_stderr(StringIO()):self.assertEqual(main([str(p)]),2)

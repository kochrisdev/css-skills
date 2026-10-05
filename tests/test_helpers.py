from copy import deepcopy
from datetime import datetime,timezone
import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
def module(path,name):
    s=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ledger=module('skills/designing-ledgers/scripts/check_ledger.py','ledger_checker')
evidence=module('skills/gating-releases/scripts/check_evidence.py','evidence_checker')
class LedgerTests(unittest.TestCase):
    def setUp(self):self.record=json.loads((ROOT/'skills/designing-ledgers/examples/journal.json').read_text())
    def test_balanced(self):self.assertEqual(ledger.check(self.record),[])
    def test_unbalanced(self):
        self.record['transactions'][0]['entries'][0]['amount_minor']+=1
        self.assertTrue(ledger.check(self.record))
    def test_cross_currency(self):
        self.record['transactions'][0]['entries'][1]['currency']='EUR'
        self.assertTrue(ledger.check(self.record))
    def test_cross_entity(self):
        self.record['transactions'][0]['entries'][1]['entity']='different'
        self.assertTrue(ledger.check(self.record))
    def test_float_amount(self):
        self.record['transactions'][0]['entries'][0]['amount_minor']=10000.0
        self.assertTrue(ledger.check(self.record))
    def test_bool_amount(self):
        self.record['transactions'][0]['entries'][0]['amount_minor']=True
        self.assertTrue(ledger.check(self.record))
    def test_duplicate_id(self):
        self.record['transactions'].append(deepcopy(self.record['transactions'][0]))
        self.assertTrue(ledger.check(self.record))
    def test_duplicate_idempotency_key(self):
        tx=deepcopy(self.record['transactions'][0]);tx['id']='new';self.record['transactions'].append(tx)
        self.assertTrue(ledger.check(self.record))
    def test_negative_amount(self):
        self.record['transactions'][0]['entries'][0]['amount_minor']=-100
        self.assertTrue(ledger.check(self.record))
    def test_invalid_side(self):
        self.record['transactions'][0]['entries'][0]['side']='both'
        self.assertTrue(ledger.check(self.record))
    def test_empty(self):self.assertTrue(ledger.check({'transactions':[]}))
    def test_nonobject(self):self.assertTrue(ledger.check(None))
class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.record=json.loads((ROOT/'skills/gating-releases/examples/evidence.json').read_text())
        self.now=datetime(2026,10,5,1,tzinfo=timezone.utc)
    def test_fresh(self):self.assertEqual(evidence.check(self.record,now=self.now),[])
    def test_wrong_candidate(self):
        self.record['checks'][0]['candidate_digest']='different'
        self.assertTrue(evidence.check(self.record,now=self.now))
    def test_wrong_environment(self):
        self.record['checks'][0]['environment']='production'
        self.assertTrue(evidence.check(self.record,now=self.now))
    def test_stale(self):self.assertTrue(evidence.check(self.record,now=self.now,max_age_hours=.5))
    def test_future(self):
        self.record['checks'][0]['observed_at']='2027-01-01T00:00:00Z'
        self.assertTrue(evidence.check(self.record,now=self.now))
    def test_not_run(self):
        self.record['checks'][0]['status']='not-run'
        self.assertTrue(evidence.check(self.record,now=self.now))
    def test_missing(self):
        self.record['checks'].pop();self.assertTrue(evidence.check(self.record,now=self.now))
    def test_missing_reference(self):
        self.record['checks'][0]['evidence_ref']='';self.assertTrue(evidence.check(self.record,now=self.now))
    def test_naive_time(self):
        self.record['checks'][0]['observed_at']='2026-10-05T00:00:00'
        self.assertTrue(evidence.check(self.record,now=self.now))
    def test_null_time(self):
        self.record['checks'][0]['observed_at']=None
        self.assertTrue(evidence.check(self.record,now=self.now))
    def test_duplicate_check(self):
        self.record['checks'].append(deepcopy(self.record['checks'][0]))
        self.assertTrue(evidence.check(self.record,now=self.now))
    def test_nan_freshness(self):self.assertTrue(evidence.check(self.record,now=self.now,max_age_hours=float('nan')))

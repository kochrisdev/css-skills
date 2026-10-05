from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import shutil
import subprocess
import tempfile
import unittest
from css.cli import main
from css.doctor import diagnose
class DoctorTests(unittest.TestCase):
    def test_missing_directory(self):
        with tempfile.TemporaryDirectory() as d:self.assertFalse(diagnose(Path(d)/'absent')['exists'])
    def test_plain_folder_does_not_initialize_git(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse(diagnose(Path(d))['git_repository']);self.assertFalse((Path(d)/'.git').exists())
    @unittest.skipUnless(shutil.which('git'),'Git unavailable')
    def test_git_folder_detected(self):
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(['git','init','-q',d],check=True)
            result=diagnose(Path(d));self.assertTrue(result['git_repository']);self.assertTrue(result['is_repository_root'])
    @unittest.skipUnless(shutil.which('git'),'Git unavailable')
    def test_nested_folder_identified(self):
        with tempfile.TemporaryDirectory() as d:
            subprocess.run(['git','init','-q',d],check=True);p=Path(d)/'nested';p.mkdir()
            result=diagnose(p);self.assertTrue(result['git_repository']);self.assertFalse(result['is_repository_root'])
class CLITests(unittest.TestCase):
    def test_inventory(self):
        out=StringIO()
        with redirect_stdout(out):code=main(['inventory'])
        self.assertEqual(code,0);self.assertEqual(json.loads(out.getvalue())['skills'],200)
    def test_release_gate_is_not_green(self):
        out=StringIO()
        with redirect_stdout(out):code=main(['validate','--release'])
        self.assertEqual(code,1);self.assertFalse(json.loads(out.getvalue())['release_ready'])
    def test_graph_is_derived(self):
        out=StringIO()
        with redirect_stdout(out):code=main(['graph'])
        result=json.loads(out.getvalue());self.assertEqual(code,0);self.assertEqual(len(result['nodes']),200)

"""One-time, hash-bound CSS PE/VC source import. Restricted to one feature branch."""
from pathlib import Path
import base64
import hashlib
import json
import lzma
import os
import shutil
import subprocess
import sys
import tempfile

REPO = 'kochrisdev/css-skills'
BRANCH = 'feature/pe-vc-skills'
BASE = 'bf515580b9d81b5fe7a214cc1ccbec2ff4f6035d'
BASE_TREE = '32bd6d6313e98bf76edea022fa645b895a585cbf'
TARGET = 'ceffb3fe99dcd61a1b436ea74825cf0f29700a09'
PAYLOAD_SHA = '1c4f7bfa9dae1ffd59b1198679a49074c03a24b716982e6dac3c71f4b341e6db'
TRANSPORT = '.css-pevc-import/'
WORKFLOW = '.github/workflows/css-pevc-import.yml'
KEYS = {'build.py', 'finish.py', 'css/pevc.py', 'tests/test_pevc.py',
        'reports/pe-vc-routing.json', 'reports/pe-vc-verification.json',
        'reports/pe-vc-unit-tests.txt'}


def run(*args, env=None):
    return subprocess.check_output(args, text=True, env=env).strip()


def temporary_path(path):
    return path.startswith(TRANSPORT) or path == WORKFLOW


def load_payload(root):
    text = ''.join((root / TRANSPORT / f'part-{i}.txt').read_text(encoding='ascii')
                   for i in range(4))
    if len(text) != 43724:
        raise RuntimeError('incorrect encoded payload length')
    data = base64.b64decode(text, validate=True)
    if len(data) != 32792 or hashlib.sha256(data).hexdigest() != PAYLOAD_SHA:
        raise RuntimeError('transport digest mismatch')
    decoder = lzma.LZMADecompressor(memlimit=256 * 1024 * 1024)
    decoded = decoder.decompress(data, max_length=127064)
    if len(decoded) != 127063 or not decoder.eof or decoder.unused_data:
        raise RuntimeError('decoded payload shape mismatch')
    result = json.loads(decoded)
    if set(result) != KEYS or any(not isinstance(v, str) for v in result.values()):
        raise RuntimeError('unexpected payload files')
    return result


def prepare(root):
    payload = load_payload(root)
    license_before = (root / 'LICENSE').read_bytes()
    with tempfile.TemporaryDirectory(prefix='css-pevc-build-') as td:
        for name in ('build.py', 'finish.py'):
            script = Path(td) / name
            script.write_text(payload[name], encoding='utf-8')
            subprocess.run([sys.executable, str(script)], cwd=root, check=True)
    for name in sorted(KEYS - {'build.py', 'finish.py'}):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload[name].encode('utf-8'))
    if (root / 'LICENSE').read_bytes() != license_before:
        raise RuntimeError('license changed unexpectedly')
    for args in ([sys.executable, '-m', 'css', 'validate'],
                 [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                 [sys.executable, '-m', 'css', 'benchmark-routing']):
        subprocess.run(args, cwd=root, check=True)
    # Verify the complete index, omitting only the explicitly named temporary transport.
    subprocess.run(['git', 'add', '-A'], cwd=root, check=True)
    with tempfile.TemporaryDirectory(prefix='css-pevc-index-') as td:
        index = Path(td) / 'index'
        shutil.copyfile(run('git', 'rev-parse', '--git-path', 'index'), index)
        env = dict(os.environ, GIT_INDEX_FILE=str(index))
        names = run('git', 'ls-files', env=env).splitlines()
        for name in names:
            if temporary_path(name):
                subprocess.run(['git', 'update-index', '--force-remove', name],
                               env=env, check=True)
        tree = run('git', 'write-tree', env=env)
        count = len(run('git', 'ls-files', env=env).splitlines())
        if tree != TARGET or count != 496:
            raise RuntimeError(f'generated source differs: {tree}, files={count}')
    print(f'VERIFIED: 496 source files, tree {tree}', flush=True)


def main():
    root = Path.cwd().resolve()
    if os.environ.get('GITHUB_REPOSITORY') != REPO:
        raise RuntimeError('unexpected repository')
    if os.environ.get('GITHUB_REF') != 'refs/heads/' + BRANCH:
        raise RuntimeError('unexpected branch')
    head = run('git', 'rev-parse', 'HEAD')
    if head != os.environ.get('GITHUB_SHA'):
        raise RuntimeError('checkout is not the triggering commit')
    if run('git', 'rev-parse', BASE + '^{tree}') != BASE_TREE:
        raise RuntimeError('base tree mismatch')
    subprocess.run(['git', 'merge-base', '--is-ancestor', BASE, head], check=True)
    changed = run('git', 'diff', '--name-only', BASE, head).splitlines()
    if any(not temporary_path(p) for p in changed):
        raise RuntimeError('branch has non-transport edits; manual reconciliation required')
    prepare(root)
    remote = run('git', 'ls-remote', 'origin', 'refs/heads/' + BRANCH).split()
    if not remote or remote[0] != head:
        raise RuntimeError('branch moved; refusing to overwrite concurrent changes')
    subprocess.run(['git', 'config', 'user.name', 'github-actions[bot]'], check=True)
    subprocess.run(['git', 'config', 'user.email',
                    '41898282+github-actions[bot]@users.noreply.github.com'], check=True)
    subprocess.run(['git', 'commit', '-m',
                    'Add verified CSS v0.6 PE/VC procedures and pass 138 tests',
                    '-m', '496-file source verified against tree ' + TARGET +
                    '. Temporary transport cleanup is performed separately.'], check=True)
    subprocess.run(['git', 'push', 'origin', 'HEAD:refs/heads/' + BRANCH], check=True)


if __name__ == '__main__':
    main()

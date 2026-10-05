"""One-time, branch-only publication of hash-verified audit documents; no probe execution."""
from pathlib import Path
import base64, hashlib, json, lzma, os, re, subprocess, sys
BASE = "9aab22968e80cf30b1e0e33c69aaf67ef956135a"
BASE_TREE = "ceffb3fe99dcd61a1b436ea74825cf0f29700a09"
BRANCH = "docs/v0.6-audit-and-roadmap"
DEST = "docs/reviews/v0.6.0"
PAYLOAD_HASH = '2b7827c57e10ce258f4d43565aa51b4792a63ae69f276230eef0b95271f82f34'
EXPECTED = {'ALL-224-SKILLS-REVIEW.md': '4a0b2407b286a371c72724ab881f6cfb672afd392a9eada32b8eae2d547f2c72', 'REVIEW-AND-ADVANCEMENT-PLAN.md': 'bef9290cc2e5457f007c9e8aa2a3c0bc3a8d1dc8886e90a94b06294b58ec6883', 'all-224-skills.json': 'b4bfbb4d8d31514d74be15a0ab1ba77bc90e05da3acf967bae868b99b88c9b10', 'audit-summary.json': 'fdf7c3b687865b9d51ff72f863ce4ecea687dded9f4d3b4e40b8804a7922109d', 'evaluation-case-cues.json': '3c7a97eb1aaeccf853f625af86a109ffd6f4c1656dce97347e3eaa15071dc242', 'evidence/probe-console.txt': '5d0904869e3a672b5a4c8375f16b5de20fd470d3907b0d28473c75cd67d2f342', 'evidence/probes.json': 'dde62b12c25b8b928e2dd8115ecd46a9f785b8cbebd8358c42630299a67da67b', 'evidence/routing-smoke.json': '6b1e8b835c5c05748dd392e6188b794e7d28c2eded326e409cdf775a4bebf05a', 'evidence/summary-console.json': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'evidence/tests.txt': '346c01d8f09223b76424e26ebae1e5bf53089047d393a53a201c837ba533dfb2', 'evidence/validate.json': 'b138fcf5dbf9546fd78cfb7f0f4115d40c47bdacd9fecab1e96605f16fb36388', 'probe_review.py': 'c2ef36e7a359e62b9ee753472fa0de020d2a7c97ee69afe4c6dff894df4dbe8c', 'skill-workflow-groups.json': '62b5c2e60d8210adebf7f17ba1619bd654501e5242ee0ba17df772b8ab25b9d8', 'README.md': '36b9a85f880494233683953e96a131fdd4ca5215277d80d6fe658eb302718b7b', 'SHA256SUMS': '1e5e74af8d4242634ee77b19eb5076a1078fb6506de5d536ab33608cc2d16cc0'}

def git(*args, data=None):
    return subprocess.check_output(["git", *args], input=data)

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def decode(root, transport):
    parts = sorted(transport.glob("part-*.b64"))
    require(len(parts) == 5, "missing payload part")
    packed = base64.b64decode("".join(p.read_text(encoding="ascii") for p in parts), validate=True)
    require(hashlib.sha256(packed).hexdigest() == PAYLOAD_HASH, "payload checksum mismatch")
    texts = json.loads(lzma.decompress(packed).decode("utf-8"))
    require(set(texts) == set(EXPECTED), "unexpected audit members")
    matrix = texts["all-224-skills.json"]
    rows = json.loads(matrix)
    require(len(rows) == 224, "incomplete skill matrix")
    for row in rows:
        name = row["name"]
        require(re.fullmatch(r"[a-z0-9-]+", name) is not None, "invalid source name")
        require(row["source_path"] == f"skills/{name}/SKILL.md", "invalid source path")
        raw = git("show", BASE + ":" + row["source_path"])
        body = re.search(r"## Workflow\n(.*?)(?=\n## |\Z)", raw.decode("utf-8"), re.S)
        require(body is not None, "missing baseline workflow")
        values = {"source": hashlib.sha256(raw).hexdigest(), "workflow": hashlib.sha256(body.group(1).strip().encode("utf-8")).hexdigest()}
        for kind, digest in values.items():
            matrix = matrix.replace(f"@{name}:{kind}@", digest)
    texts["all-224-skills.json"] = matrix
    files = {p: t.encode("utf-8") for p, t in texts.items()}
    for p, data in files.items():
        require(hashlib.sha256(data).hexdigest() == EXPECTED[p], "audit content mismatch: " + p)
        require(not Path(p).is_absolute() and ".." not in Path(p).parts and "\\" not in p, "unsafe path")
    return files

def main():
    require(os.environ.get("GITHUB_REPOSITORY") == "kochrisdev/css-skills", "wrong repository")
    require(os.environ.get("GITHUB_REF") == "refs/heads/" + BRANCH, "wrong branch")
    head = git("rev-parse", "HEAD").decode().strip()
    require(head == os.environ.get("GITHUB_SHA"), "wrong triggering commit")
    require(git("rev-parse", BASE + "^{tree}").decode().strip() == BASE_TREE, "wrong baseline")
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, head], check=True)
    root = Path.cwd()
    files = decode(root, Path(__file__).resolve().parent)
    require(not (root / DEST).exists(), "audit destination already exists")
    require(not git("status", "--porcelain").strip(), "checkout is not clean")
    for p, data in files.items():
        target = root / DEST / p
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    subprocess.run(["git", "add", "--", DEST], check=True)
    staged = set(git("diff", "--cached", "--name-only", "-z").decode().rstrip("\0").split("\0"))
    require(staged == {DEST + "/" + p for p in files}, "unexpected staged changes")
    subprocess.run(["git", "-c", "user.name=github-actions[bot]", "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com", "commit", "-m", "Publish CSS v0.6 audit, all-224 skill matrix and original evidence"], check=True)
    current = git("ls-remote", "origin", "refs/heads/" + BRANCH).decode().split()[0]
    require(current == head, "branch moved; aborting push")
    subprocess.run(["git", "push", "origin", "HEAD:refs/heads/" + BRANCH], check=True)
    print("Published 15 audit files; all 13 original archive members preserved. No skill changes or fixes applied.")

if __name__ == "__main__":
    main()

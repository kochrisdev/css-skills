# Upgrade from v0.4 without nested-folder mistakes

The reviewed baseline is GitHub commit `cb2a4689b46f38d136fdd3a2b7d572d87f657fb7`.
Its tree is `ea6a71855e1f412402f71e00da5f6dd861ae68b5`.
Your working copy may contain newer local changes; do not overwrite them.

## Preferred route: apply the supplied patch

The separate `css-v0.4-to-v0.5.patch` includes additions, deletions and source-directory moves.
It changes neither `.git` nor LICENSE. Download it outside your repository.

In PowerShell, use your **actual existing clone path**, not a guessed user directory:

```powershell
Set-Location "C:\path\to\your\css-skills"
git rev-parse --show-toplevel
git status --short
```

If Git reports “not a repository”, stop. Locate the existing cloned folder. Do not create a folder
called main, delete duplicate-looking folders or run git init as a workaround. `main` is a branch name.
The new package also offers `python -m css doctor --project "C:\path\to\your\css-skills"`.

If status lists local modifications, commit or back them up deliberately before proceeding.
Then create a new branch and check the patch before applying it:

```powershell
$Patch = "C:\path\to\Downloads\css-v0.4-to-v0.5.patch"
git switch -c improve/css-v0.5
git apply --check "$Patch"
# Continue only if the check exits successfully.
git apply "$Patch"
python -m css validate
python -m unittest discover -s tests -v
python -m css benchmark-routing
git diff --stat
git status --short
```

After reviewing the diff and successful checks, publishing the branch is a separate explicit action:

```powershell
git add -A
git commit -m "Improve CSS v0.5: pilot procedures and engineering tooling"
git push -u origin improve/css-v0.5
```

These instructions were not executed on your machine. No remote branch or pull request was created
as part of generating this package. A native Windows run remains to be confirmed.

## Source-directory change

All 200 IDs and names remain unchanged. Canonical sources move from `.claude/skills/<name>` to
`skills/<name>`. This is an intentional breaking **source-path change**, not full path compatibility.
The mapping is in `catalog/legacy-map.json`.

After applying the patch, `.claude/skills` is an optional generated project installation rather than
where the entire catalog lives. Install a selected profile explicitly. The library's .gitignore excludes
its own generated runtime directories; downstream projects choose whether to commit their selected exports.

## Existing downstream installations

Old manually copied skills have no CSS installation manifest. The new installer refuses to overwrite them,
even when the names match. Review and back up the existing directories; then deliberately move them out
of the target runtime path before installing a selected pilot profile. Do not delete unrelated skills.
There is no automatic adoption or force overwrite because ownership and local edits cannot be inferred safely.

## ZIP route

The ZIP is a complete new source tree for inspection or a fresh working directory. It contains no `.git`.
Extracting a ZIP does not create a Git repository. Do not extract its enclosing css-skills folder inside
an existing css-skills folder and assume that nested directory is the repository root.
For an existing clone, the patch is safer because it also removes superseded files rather than leaving
stale v0.4 sources discoverable.

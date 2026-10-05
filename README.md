# Christopher Skills System — CSS v0.6.0

**Private Equity & Venture Capital Pack — 24 additional authored procedures.**

CSS is a source library of reusable agent procedures with local discovery, validation,
workflow planning and controlled installation. It is **not** an autonomous agent runtime.

| What is present | What the claim means |
|---|---|
| 224 skill IDs and names in 24 domains | The original 200 identities are preserved, not a production-readiness claim |
| 64 authored pilot procedures | Specific steps, pitfalls, output templates and evaluation cases |
| 160 legacy instruction drafts | Preserved, labeled and excluded from normal installation |
| 256 concrete behavioral case definitions | Authored scenarios; **not executed model evaluations** |
| 11 installation profiles and 10 typed workflow recipes | Explicit selection and validated declared handoffs |
| Local CLI and automated tests | Deterministic software checks, not certification |

**Readiness:** suitable for supervised experimentation. Live Claude Code/Codex behavior and
independent domain validation are not measured. The inherited LICENSE is incomplete and
conflicts with earlier MIT repository history; the owner must resolve licensing before a public release.

## PE/VC pack

See [PE/VC catalog, workflow recipes and helper boundaries](docs/PE-VC-PACK.md).

```bash
python -m css search "LBO buyout sources uses debt"
python -m css search "VC cap table SAFE dilution"
python -m css plan pe-underwriting
python -m css plan vc-diligence
python -m css.pevc examples/pevc/fund-multiples.json
```

To preview installation into an existing project:

```bash
python -m css install --profile pe-vc --runtime claude --target /path/to/project
```

Add `--apply` only after reviewing the preview. These procedures prepare analysis;
they do not commit investments, execute funding, sign terms or contact investors.
Financial arithmetic helpers are intentionally narrow and use exact-decimal inputs.
All new behavioral case definitions remain **not_run**; expert review is pending.

## Start here

Use Python **3.11 or newer** from the extracted `css-skills` directory. No pip packages,
model API key, network access or cloud account is needed for the bundled CLI and tests.
This is a source-checkout release; it is not published as an installable Python wheel.

```bash
python -m css inventory
python -m css validate
python -m unittest discover -s tests -v
python -m css benchmark-routing
```

On Windows, `py -3` can replace `python` when that is your configured Python launcher.

Find a pilot procedure or inspect a plan:

```bash
python -m css search "bank digital twin shadow mode"
python -m css route "payment ledger reconciliation"
python -m css plan bank-digital-twin
python -m css graph
```

Search and route are an **explainable lexical TF-IDF baseline**, not semantic intelligence.
They can return no match. Plans validate declared artifact types and ordering; they do not
load your evidence, verify approval identity, execute commands or run agents.

## Install only what the project needs

The target must be an existing directory. First preview, then explicitly apply:

```bash
python -m css install --profile starter --runtime claude --target /path/to/your-project
python -m css install --profile starter --runtime claude --target /path/to/your-project --apply
```

PowerShell example — replace the target with your actual existing project path:

```powershell
python -m css install --profile banking --runtime claude --target "C:\Users\YourName\Projects\BankTwin"
```

Profiles: `starter`, `banking`, `payments`, `agents`, `cloud`, `authoring`, `pilot`,
`private-equity`, `venture-capital`, `private-capital`, `pe-vc`.
`pilot` installs all 64 authored procedures, not all 224 catalog entries. The `pe-vc` profile installs only the 24 new procedures.

For Codex use `--runtime codex`. For a plain export use `--runtime generic`.
Claude exports go to `.claude/skills`; Codex exports to `.agents/skills`.
Both exports disable implicit invocation by default. Invoke explicitly in the host:
`/system-design` in Claude Code or `$system-design` in Codex.
No runtime settings, broad tool grants, credentials, hooks or Git configuration are installed.
Actual host discovery and behavior still require a local pilot test.

The installer refuses unmanaged collisions and locally edited managed files. It never
runs `git init`, deletes `.git`, or merges a nested repository. Every applied transaction
records a backup ID. Restore is also preview-first:

```bash
python -m css restore --target /path/to/your-project --backup BACKUP_ID
python -m css restore --target /path/to/your-project --backup BACKUP_ID --apply
```

## Upgrading v0.4

**Do not copy this ZIP over your repository indiscriminately.** Canonical sources move from
`.claude/skills/<name>` to `skills/<name>`; names and IDs stay stable, source paths intentionally change.
Use the provided Git patch on a clean working tree, or follow [Migration](docs/MIGRATION.md).

For the previous “not a Git repository” or nested-folder problem:

```bash
python -m css doctor --project /path/to/css-skills
```

This is read-only and identifies the actual repository root when Git is available.

## Documentation map

| Need | Canonical reference |
|---|---|
| What was wrong with v0.4? | [Audit and remediation](docs/V04-REVIEW.md) |
| Author or change a skill | [Skill standard](docs/SKILL-STANDARD.md) |
| Understand runtime and contracts | [Architecture](docs/ARCHITECTURE.md) |
| Evaluate without inflated claims | [Evaluation guide](docs/EVALUATION.md) |
| Permissions, installation, licensing | [Security and governance](docs/SECURITY.md) |
| Apply the upgrade safely | [Migration](docs/MIGRATION.md) |
| Review current vendor conventions | [Sources](docs/SOURCES.md) |
| Browse skill names | [Catalog](catalog/CATALOG.md), [pilot procedures](catalog/PILOT-SKILLS.md) |
| Continue development in Claude Code | [Development handoff](docs/DEVELOPMENT-HANDOFF.md) |

`python -m css validate --release` deliberately blocks a public release while licensing,
independent review and behavioral-validation conditions remain unresolved.

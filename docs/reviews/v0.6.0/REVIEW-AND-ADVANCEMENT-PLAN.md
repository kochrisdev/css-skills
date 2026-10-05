# Christopher Skills System — v0.6.0 review and advancement plan

**Review date:** 2026-10-05. **Repository:** `kochrisdev/css-skills`.
**Pinned main commit:** `9aab22968e80cf30b1e0e33c69aaf67ef956135a`.
**Git tree:** `ceffb3fe99dcd61a1b436ea74825cf0f29700a09`.

## Executive assessment

The next advance should be **measured competence and trustworthy maintenance**, not a larger catalog.
CSS now has a useful source library, explicit pilot/draft distinctions, controlled local installation,
portable exports and concrete financial procedures. It is still a supervised pilot system rather than
an independently validated agent capability platform. No GitHub files, branches, settings, tags or releases
were changed in this review.

## Scope and evidence

The supplied v0.6 ZIP was reconstructed as a Git tree and matched the current GitHub tree exactly.
The review covered all 224 skill entries and their SKILL.md files, read their bundled resources,
inspected all 64 authored pilot workflows, and examined the local CLI, installer, helper code, profiles,
workflow contracts and evaluation design. This is not a claim of exhaustive security assurance,
independent financial/legal review or live Claude/Codex evaluation.

Fresh local checks ran on Linux with Python 3.13.5. **138 unit tests passed**, with zero errors,
failures or skips. The existing **42/42 lexical smoke cases passed**. All **520 local Markdown links**
resolved. Per-skill integrity validation passed. Additional audit probes exposed gaps outside that suite.
The probes use disposable local copies and synthetic data; no business system is accessed.

### Verified inventory

| Measure | Observed |
|---|---:|
| Catalog entries | 224 |
| Authored pilots | 64 |
| Retained instruction drafts | 160 |
| Domains | 24 |
| Profiles | 11 |
| Plan-only workflows | 10 |
| Behavioral case definitions | 256 |
| Recorded live behavioral results in skill metadata | 0 |
| Recorded independent reviews in skill metadata | 0 |
| Unique pilot workflow bodies | 64 |
| Distinct workflow templates across 160 drafts | 4 |
| Source files in reviewed package | 496 |

About 28.6% of entries are authored pilots. This is an authoring-status proportion, not a reliability score.
The remaining 71.4% should not be presented as usable production capabilities. The original 200 identities
remain covered by the passing continuity tests.

## Findings: specific defects and limitations

### R06-01 — Stale package-wide checksum manifest — fix before another package release

`MANIFEST.sha256` contains 378 entries. **13 listed hashes do not match the current files** and **117
source files are unlisted**, excluding the manifest itself. Missing entries include `css/pevc.py`, PE/VC
profiles and new skill resources. This is a packaging/version-synchronization defect, not evidence of
an altered download: the archive and GitHub tree match exactly.

Per-skill digests still validate. Those digests do not repair the stale root manifest or cover all runtime
and packaging files. Generate the package manifest from the final source tree, define its exclusions,
and make CI reject changed, missing and unlisted distributable files. Do not update reference hashes
until the corresponding content changes have been reviewed. Unsigned hashes do not authenticate a publisher.

**Acceptance:** modify one listed file, remove one file and add one distributable file; each causes a clear
manifest failure. An unchanged final package verifies completely. Source: `MANIFEST.sha256`,
`scripts/refresh_integrity.py`, `css/core.py`, `.github/workflows/ci.yml`.

### R06-02 — Duplicate JSON keys accepted by two standalone checkers — hardening priority

The release-evidence and synthetic-ledger command-line helpers use ordinary `json.loads`, unlike the
strict duplicate-key loader used by the core and PE/VC helper. A synthetic evidence record containing
`"status":"fail","status":"pass"` was accepted as `ok: true`. A duplicate ledger amount key was
also accepted using its final value.

These are read-only helpers and expressly do not authenticate evidence or authorize money movement.
The observation is an ambiguity-validation gap, not a demonstrated production authorization bypass.
Use duplicate-key rejection consistently, reject unsupported input forms, and keep the standalone
installation use case working when choosing where the shared parser lives.

**Acceptance:** duplicate keys at every nesting level produce a deterministic error before business checks;
valid existing fixtures remain accepted. Sources: `skills/gating-releases/scripts/check_evidence.py:47-56`,
`skills/designing-ledgers/scripts/check_ledger.py:42-48`, `css/core.py:read_json`.

### R06-03 — Upgrades retain resources deleted from the source — lifecycle gap

In a disposable copy, an inert resource was added to a pilot, installed, removed upstream, and its source
digest refreshed. Source validation passed. Reinstallation retained the obsolete target resource and
produced no deletion operation. The installer unions old ownership with new files and only plans desired files.

Preserving other installed profiles is useful and must remain. But resource retirement within an updated
skill needs a separate operation: identify removed managed files, preview their removal, verify that they
have not been locally changed, preserve shared-profile ownership, back up the old bytes and support rollback.
Do not solve this with broad directory deletion or an unconditional force flag.

**Acceptance:** an unchanged removed managed file can be retired explicitly; edited or unmanaged files
remain protected; unrelated profiles survive; rollback restores the previous version. Source: `css/install.py:66-119`.

### R06-04 — Some malformed metadata escapes structured error handling

Replacing a profile JSON object with an array caused `validate` to raise an `AttributeError` traceback
rather than emit its normal structured error report. A malformed workflow-step probe, by contrast, was
handled without a raw traceback. Do not generalize this to every malformed input.

Validate root objects, list members and field types before dereferencing them. Reuse a clearly documented
schema contract and ensure all CLI failures return stable machine-readable errors. Add mutation cases for
profiles, recipes, behavioral records and installation journals.

**Acceptance:** malformed metadata has a documented nonzero exit code and actionable JSON error; no uncaught traceback.

### R06-05 — Review-policy annotations are checked only for high-risk steps

Removing `approval` from the medium-risk buyout-screening step left validation green, even though the PE/VC
recipe declares human review for every step. Current code explicitly enforces the marker only when skill
risk is `high`. No execution was tested or bypassed: recipes are plan-only.

Represent a recipe's required review policy separately from the risk label, validate it on every affected
step, and keep a policy requirement distinct from an actual approval record. A future runner must not
interpret a string such as `human-review-required` as authorization.

**Acceptance:** any step requiring review is rejected when its policy is absent or weakened, regardless of
whether its effect classification is medium or high. Source: `css/core.py:workflow`, `workflows/pe-underwriting.json`.

### R06-06 — Behavioral examples are not yet independent evaluations

All 256 case definitions remain `not_run`. **37 of the 64 negative prompts explicitly name an existing
skill**, frequently supplying the intended alternative. Some boundary prompts also tell the agent how to
respond. That can be appropriate teaching material, but is weak evidence of autonomous skill selection.
Cases and expected outcomes also travel with the installed skill resources, so they cannot serve as hidden
holdout tests in that form.

Separate public examples, regression cases and isolated holdout tasks. Give tasks realistic documents or
repositories, keep graders/reference answers outside agent-visible inputs, inspect tool traces, and compare
no-skill versus skill-enabled runs on matched cases. Avoid rigid tool-order grading where multiple valid
solutions exist; preserve strict prohibitions on unauthorized actions and fabricated evidence.

**Acceptance:** versioned trials capture model/runtime, skill and dataset hashes, permitted tools, outputs,
traces, environment, grader version, observed outcomes and failures. Report uncertainty and critical failures
separately from an average. Sources: `docs/EVALUATION.md`, skill `evals/cases.json`, `css/install.py`.

### R06-07 — Discovery has material paraphrase gaps

The existing lexical development set passes. Additional reviewer-authored exploratory queries exposed
clear candidate-generation gaps. For example, “What proportion will founders own after a primary financing
round?” and “Evaluate whether a proposed bank replica can safely simulate liquidity shortfalls.” both
returned no candidates, despite relevant authored cap-table and bank-twin procedures.

The attached exploratory set is small and contains judgment-sensitive expectations. It is not a held-out
accuracy estimate. Do not convert its aggregate result into a product performance claim.

First improve domain synonyms, outcome descriptions and alternate terminology. Evaluate whether an optional
local embedding/hybrid layer improves retrieval beyond that baseline. Distinguish no suitable capability,
missing inputs, ambiguity and poor textual matching. Keep risk/authority separate from relevance scores.

**Acceptance:** a separately reviewed paraphrase and near-neighbor set improves without degrading out-of-scope
abstention or inventing capabilities. The current system remains offline unless a future option is explicitly enabled.

### R06-08 — Typed handoffs lack actual artifact identity and revision binding

The planner validates names, declared types and ordering. It intentionally does not validate actual evidence,
freshness or approvals. In `software-delivery`, code review consumes an externally supplied initial `diff`,
not a changeset produced by implementation; the release gate does not consume the code-review artifact.
A valid plan can therefore describe disconnected evidence unless a human reconciles it.

For future execution, add an artifact envelope with ID, type/schema version, producer, source revision,
content digest, observation time, entity/jurisdiction where relevant and verification state. Make implementation
produce a changeset that review and verification share. Ensure critical review findings actually block promotion.

**Acceptance:** mismatched candidate, stale evidence, wrong entity/currency or unresolved required review blocks
handoff. Do not add autonomous execution before these conditions are implemented and tested.

### R06-09 — Maturity cannot currently advance through recorded evidence

The registry only admits `not_run` behavioral status and `not_recorded` review status; the public-release
command unconditionally returns blocked. This was an intentional conservative choice, not a defect to
remove by setting a Boolean to true.

Create a reviewed lifecycle policy supporting authored, expert-reviewed and runtime-validated states for
specific versions and scopes. Store evidence separately, expire it on relevant changes, and permit revocation.
Only an authorized human process can grant consequential-action approval. Approval of one skill/model/task
combination must not promote an entire domain or model family.

**Acceptance:** real evidence can support a scoped transition; missing, stale, mismatched or self-approved
records cannot. Sources: `css/core.py:validate`, `css/cli.py:46-51`.

### R06-10 — Coverage is imbalanced

All 24 PE/VC/private-capital entries are authored pilots, but Business & Strategy has **0/13** pilots and
Project Management **0/8**. Banking has **1/8**, Security **2/9**, Software Engineering **2/14**, Testing **1/10**.
This is not a quality ranking of the authored financial content. It is an observable authoring gap across
capabilities needed for an end-to-end business and technology workflow.

Promote selected existing drafts after domain-specific authoring and evaluation; do not simply relabel all
160 drafts. Preserve IDs, use one canonical procedure per overlapping task, and retain compatibility aliases
when consolidation is justified.

### R06-11 — License and expert-review blockers remain

The inherited root license is still incomplete and its history remains unresolved. The owner must confirm
and document the intended license; this audit does not choose one or offer a legal conclusion about past
publication. Independent domain review and live-runtime testing also remain unrecorded. An engineering
hotfix and a public, validated distribution are different milestones.

## Advancement roadmap

| Milestone | Proposed work | Completion evidence |
|---|---|---|
| v0.6.1 — integrity and maintenance | Final-tree manifest; strict JSON parsing; safe resource retirement; structured errors; review-policy checks | Reproduced probes become passing regressions; Windows/Linux CI; package-level verification |
| v0.7 — skill evidence system | Isolated trial runner, outcome/trace graders, no-skill baselines, reviewer records, scoped maturity transitions | Reproducible runs on selected low-risk pilots; no fabricated pass records; explicit uncertainty |
| v0.8 — capability depth | Author priority drafts and connect strategy, engineering, banking and capital workflows | Task-specific fixtures and measurable artifacts, independent reviewers and end-to-end handoff checks |
| Later — assisted planning | Better candidate retrieval, capability-aware plans, evidence-bound artifacts and optional local UI | Improvement over the lexical baseline; no implicit authority or automatic self-promotion |

These are proposed milestones, not shipped features or promised delivery dates.

### First 12 drafts to author

`designing-strategies`, `designing-operating-models`, `building-business-cases`, `planning-projects`,
`designing-integration-tests`, `reviewing-authorization`, `designing-bank-integrations`,
`designing-bank-controls`, `assuring-data-quality`, `designing-kyc`, `designing-aml`,
`designing-sanctions-screening`.

The suggested sequence balances Strategy + Technology + Capital and the existing banking/remittance work.
Regulated-domain procedures require current authoritative inputs and qualified review; authoring them does
not demonstrate regulatory compliance.

### Deeper PE/VC modeling

Develop existing skills rather than adding overlapping names. Useful future modules include a tested debt
roll-forward/covenant model, a dated-cash-flow solver with explicit no-root/multiple-root handling, instrument-
specific capitalization scenarios, security-specific exit allocations and governing-document-specific fund
waterfalls. Each needs independent numeric fixtures, boundary handling and expert review before its scope
is expanded. Current helpers remain intentionally narrower and do not supply those engines.

### Recommended operating architecture

`Request → candidate discovery → scope/authority check → evidence-bound plan → supervised use → output verification → human decision → recorded learning`

Keep the source library portable and the core local/offline. Host tools enforce authorization. A skill may
suggest a change but should not approve its own publication, funding, production access or maturity promotion.
Not every skill needs a script; every skill needs a verifiable outcome and honest evidence.

## Files in this review package

`ALL-224-SKILLS-REVIEW.md` has every ID/name, current status/risk and a proposed next action.
`all-224-skills.json` adds source paths, file hashes, resource counts and case counts.
`audit-summary.json` records counts, manifest mismatches/unlisted paths and the environment.
`evaluation-case-cues.json` identifies the 37 explicit-name negative prompts.
`evidence/` contains fresh test/validation output and isolated probe observations.
`probe_review.py` reproduces the synthetic probes against an existing v0.6 checkout.

Run from a separate audit directory, pointing at the existing checkout:

```text
python probe_review.py --root /path/to/css-skills --output audit-probes.json
```

Only the explicitly requested output file and disposable temporary copies are written. The script does not
push, initialize or alter the supplied repository. Use the pinned source for exact reproduction; a later
hotfix may correctly change the observations.

## Source references

Repository references are pinned to the reviewed commit, not a moving branch:

- [Reviewed main commit](https://github.com/kochrisdev/css-skills/commit/9aab22968e80cf30b1e0e33c69aaf67ef956135a).
- [Installer](https://github.com/kochrisdev/css-skills/blob/9aab22968e80cf30b1e0e33c69aaf67ef956135a/css/install.py).
- [Core validator/planner](https://github.com/kochrisdev/css-skills/blob/9aab22968e80cf30b1e0e33c69aaf67ef956135a/css/core.py).
- [Package manifest](https://github.com/kochrisdev/css-skills/blob/9aab22968e80cf30b1e0e33c69aaf67ef956135a/MANIFEST.sha256).
- [Evaluation guide](https://github.com/kochrisdev/css-skills/blob/9aab22968e80cf30b1e0e33c69aaf67ef956135a/docs/EVALUATION.md).
- [Software delivery recipe](https://github.com/kochrisdev/css-skills/blob/9aab22968e80cf30b1e0e33c69aaf67ef956135a/workflows/software-delivery.json).
- [PE/VC guide](https://github.com/kochrisdev/css-skills/blob/9aab22968e80cf30b1e0e33c69aaf67ef956135a/docs/PE-VC-PACK.md).

Current primary references consulted for the proposed direction on 2026-10-05:

- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): supports separating tasks, trials, graders, traces and outcomes, repeated evaluation, and human calibration. It does not validate CSS.
- [Claude Code skill documentation](https://code.claude.com/docs/en/skills): runtime invocation and skill packaging conventions; actual host behavior still needs testing.
- [Agent Skills specification](https://agentskills.io/specification): portable skill packaging reference, not an endorsement or quality certification.

## Appendix: all 24 domains

| Domain | Pilots | Drafts | Total |
|---|---:|---:|---:|
| ai-agents | 5 | 6 | 11 |
| architecture | 2 | 10 | 12 |
| banking | 1 | 7 | 8 |
| business-strategy | 0 | 13 | 13 |
| cloud | 2 | 9 | 11 |
| compliance | 3 | 6 | 9 |
| data | 2 | 9 | 11 |
| devops | 1 | 8 | 9 |
| documentation | 1 | 8 | 9 |
| fintech | 1 | 6 | 7 |
| governance | 1 | 1 | 2 |
| meta | 9 | 0 | 9 |
| operations | 1 | 9 | 10 |
| payments | 2 | 9 | 11 |
| private-capital | 8 | 0 | 8 |
| private-equity | 8 | 0 | 8 |
| product | 2 | 8 | 10 |
| project-management | 0 | 8 | 8 |
| quality | 1 | 7 | 8 |
| research | 1 | 8 | 9 |
| security | 2 | 7 | 9 |
| software-engineering | 2 | 12 | 14 |
| testing | 1 | 9 | 10 |
| venture-capital | 8 | 0 | 8 |

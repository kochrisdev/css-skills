# CSS v0.6.0 audit and advancement plan

This directory publishes the review requested by Christopher Tun. **It contains findings and proposed work, not implemented fixes or a new CSS release.**

## Read the review

| Resource | Purpose |
|---|---|
| [Review and advancement plan](REVIEW-AND-ADVANCEMENT-PLAN.md) | Eleven findings, acceptance criteria and proposed v0.6.1/v0.7/v0.8 milestones. |
| [All 224 skills](ALL-224-SKILLS-REVIEW.md) | Per-skill authoring status and recommended next action. |
| [Machine-readable skill matrix](all-224-skills.json) | IDs, source hashes, resource counts and recommendations. |
| [Audit summary](audit-summary.json) | Baseline inventory, manifest defects and audit environment. |
| [Evaluation-case cues](evaluation-case-cues.json) | Cases that reveal skill-selection answers. |
| [Workflow groups](skill-workflow-groups.json) | Shared and distinct procedure-body groups. |
| [Diagnostic probe source](probe_review.py) | Synthetic probes using disposable source copies. |
| [Probe observations](evidence/probes.json) | Captured observations; not live-agent evaluation. |
| [Unit-test log](evidence/tests.txt) | 138 passing tests in the reviewed snapshot. |
| [Validation output](evidence/validate.json) | Structural/integrity checks and unresolved warnings. |
| [Routing smoke output](evidence/routing-smoke.json) | 42 authored smoke cases; not a real-world accuracy estimate. |
| [Checksums](SHA256SUMS) | SHA-256 of every other file in this directory. |

## Baseline and provenance

Review date: **2026-10-05**. Reviewed commit: `9aab22968e80cf30b1e0e33c69aaf67ef956135a`.
Reviewed Git tree: `ceffb3fe99dcd61a1b436ea74825cf0f29700a09`.
Original archive: `CSS-v0.6-Audit-and-Advancement.zip`.
Archive SHA-256: `4b2eab0a318eec987657d4786970376ef2503ddb30d89db84560a3777c754e1f`.

All 13 original archive members are preserved byte-for-byte. This README and SHA256SUMS are publication additions.
`evidence/summary-console.json` is an empty captured file retained for archival fidelity; it is not a successful result or valid JSON.
Statements such as "repository unchanged" refer to the original review session. This subsequent publication adds only this audit directory.

## Scope and limits

No skill, installer, financial helper, workflow recipe, runtime policy, version, LICENSE or root package manifest is changed by this documentation publication.
The stale manifest finding refers to the pinned baseline; this audit does not repair it. Existing release blockers remain.
Diagnostic observations concern synthetic, local tests, not an observed production compromise. No live Claude/Codex behavior or independent financial/legal review is claimed.
Historical evidence remains dated to the review; a later CI pass does not resolve the findings.

## Reproduction

Use a trusted checkout of the pinned commit and Python 3.11 or newer. Run the probe from this directory, with output outside the source checkout:

```bash
python probe_review.py --root /path/to/trusted/css-skills --output /path/outside/checkout/audit-probes.json
```

The script imports the supplied checkout's Python code. Review that source first. Mutation probes use temporary copies; the explicit output location is written only when supplied.
Results can differ after fixes. The probe is not installed as a skill and is not run automatically by this publication.

## Proposed next implementation

Start with v0.6.1 hardening: package manifest verification, duplicate-key rejection, safe resource retirement, structured metadata errors and explicit review-policy checks.
Then implement a reviewed evidence lifecycle before broader orchestration. These remain proposals requiring separate implementation and tests.

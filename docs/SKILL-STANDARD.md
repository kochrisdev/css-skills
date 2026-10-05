# Skill standard v0.5

## Canonical identity and metadata

IDs and names remain stable across versions. Source location is `skills/<name>/SKILL.md`.
Use lowercase ASCII alphanumeric words separated by single hyphens, maximum 64 characters.
`description` must say what the skill does and when it fits, and must not exceed 1024 characters.

For dependency-free validation, CSS intentionally uses a **restricted YAML subset**: exactly
`name` and `description`, one line each. Names may be plain slugs; quote descriptions as JSON strings.
JSON string scalars are compatible with YAML. This parser rejects multiline scalars, anchors, aliases,
unknown fields and duplicate fields; it is not a general YAML parser or universal Agent Skills validator.
Host-specific fields are added by the exporter, never by canonical authors.

## Required procedure sections

Purpose, Use when, Do not use when, Inputs, Workflow, Output contract, Quality gates,
Failure handling, Safety and permissions. Keep SKILL.md under 500 lines.
Headings establish structure only; they do not establish expertise or correctness.

A pilot workflow needs specific decisions, mechanisms, edge cases and verification criteria.
A ledger skill should reason about balanced journals and ambiguous retries. A bank-twin skill should
separate observation, simulation and live command authority. Swapping those workflows should not make sense.

## Supporting resources

Pilot skills contain a directly linked checklist, output template and concrete cases file.
Optional Python helpers must be local, bounded, dependency-free or clearly documented, with real tests.
Do not preload long references or put environment secrets in examples.

## Status and evidence

| Status | Meaning | Default discovery/install |
|---|---|---|
| draft / instruction | Preserved generic or unfinished instruction | Excluded; search can explicitly include drafts |
| pilot / procedural | Authored task-specific procedure with cases | Eligible for explicit profile installation |
| validated / production | Not supported by current promotion policy | Requires a future reviewed evidence policy |

All current records say behavioral_evaluation=not_run and human_review=not_recorded.
This is intentional. Independent reviewers, real runtime traces, representative data and release governance
are prerequisites to stronger claims. More files, more tokens or a passing linter do not satisfy them.

## Outputs and failures

A skill must distinguish completed, failed, blocked and not-run work. A claim of passed verification
must name the observation and revision. A proposed deployment is not an executed deployment.
Inputs must have provenance; missing or contradictory authority is a reportable blocker.

## Change procedure

Review related skills before adding one. Update the canonical procedure, metadata, cases and tests together.
Preview hash changes with `python scripts/refresh_integrity.py`; inspect the diff; then explicitly use `--apply`.
Re-run validation and tests. Changes to risk, actions, permissions, scripts or maturity require separate review.

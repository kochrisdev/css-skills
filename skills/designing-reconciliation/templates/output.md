# reconciliation-design

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Design reproducible reconciliation across independently sourced financial records.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- All records resolve to matched, documented exception or explicitly excluded.
- Totals reconcile per source, currency and period.
- Financial corrections require authority outside this design task.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
Two source rows have identical amounts but distinct transaction IDs. Keep both; do not deduplicate solely by value.

## Handoff
Identify the next artifact consumer and the human decision required.

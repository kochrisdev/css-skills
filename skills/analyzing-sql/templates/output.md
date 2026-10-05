# sql-analysis

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Answer a defined analytical question using read-only, scope-checked SQL.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Join cardinality does not inflate the intended grain.
- Currency and time-window semantics are explicit.
- Query results are not fabricated when the database is unavailable.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
A join multiplies one transfer by three attempts. Correct the grain and verify totals before presenting the metric.

## Handoff
Identify the next artifact consumer and the human decision required.

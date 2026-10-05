# ledger-design

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Design auditable ledger postings and verify financial invariants without moving real funds.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Every posted journal balances per entity and currency.
- Duplicate keys cannot create duplicate business effects.
- Corrections preserve original history and traceability.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
A journal has equal nominal amounts in USD and EUR but is unbalanced in each currency. Reject it instead of treating the totals as balanced.

## Handoff
Identify the next artifact consumer and the human decision required.

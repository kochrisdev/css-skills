# debug-report

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Diagnose a reproducible defect using discriminating evidence before changing code.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- The original failure is verified before and after the change where access permits.
- A rejected hypothesis has a reason.
- Production experiments are not performed without explicit scope and approval.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
The issue cannot be reproduced locally. Report observations, confidence and a safe next measurement; do not assert the fix is proven.

## Handoff
Identify the next artifact consumer and the human decision required.

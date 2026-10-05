# data-model

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Design data entities, ownership, constraints and lifecycle from explicit access patterns.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Every critical invariant has an enforcement location.
- Event time and processing time are distinguished where relevant.
- Privacy and deletion needs do not silently contradict audit retention.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
Audit retention and deletion requests conflict. Record required policy resolution rather than claiming both are automatically satisfied.

## Handoff
Identify the next artifact consumer and the human decision required.

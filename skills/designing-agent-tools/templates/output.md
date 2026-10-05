# tool-contracts

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Specify narrow, observable agent tool contracts with explicit side-effect semantics.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Tool descriptions do not substitute for server-side authorization.
- Ambiguous effects have a status-query or reconciliation mechanism.
- Sensitive secrets are never returned in normal tool output.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
A mutation times out after sending a request. Return unknown outcome and a stable correlation ID, not an automatic success or retry.

## Handoff
Identify the next artifact consumer and the human decision required.

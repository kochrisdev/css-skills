# bank-twin-design

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Design a bank digital twin with isolated observation, simulation and approved command boundaries.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- No direct write path exists from a simulation to the authoritative bank ledger.
- Decisions expose data freshness and model uncertainty.
- Any live command requires independent approval and external enforcement.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
The event feed is 45 minutes behind but the requested liquidity action assumes real-time balances. Flag the stale input and block the proposed live action.

## Handoff
Identify the next artifact consumer and the human decision required.

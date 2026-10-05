# release-decision

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Assess release readiness from scoped, current evidence without granting deployment authority.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Mandatory missing evidence blocks readiness.
- Evidence is bound to the intended revision and environment.
- An independent authorized human still controls consequential release approval.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
The tested artifact digest differs from the candidate. Block the gate until matching evidence is available.

## Handoff
Identify the next artifact consumer and the human decision required.

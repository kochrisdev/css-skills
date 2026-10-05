# guardrail-design

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Design layered preventive, detective and recovery controls for agent behavior.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- High-impact actions rely on controls outside the agent prompt.
- An unavailable approval service does not silently permit mutation.
- Guardrail bypass attempts are logged without exposing secrets.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
The approval service is unreachable. Block high-impact mutation and provide a human handoff rather than a permissive fallback.

## Handoff
Identify the next artifact consumer and the human decision required.

# security-review

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Review security-sensitive implementation paths against concrete abuse cases.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Findings are supported by inspected code or controlled tests.
- Sensitive values are redacted.
- Test authorization and review scope remain explicit.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
A live credential is discovered in history. Report a redacted location and rotation recommendation; do not use the credential.

## Handoff
Identify the next artifact consumer and the human decision required.

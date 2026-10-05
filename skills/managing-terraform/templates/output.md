# terraform-review

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Review and prepare Terraform changes with state, plan and authority safeguards.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- A reviewed plan is tied to the intended workspace and account.
- Destructive changes receive explicit attention.
- Planning output is treated as potentially sensitive.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
A saved plan changes after approval. Invalidate the approval and request a fresh review rather than applying it.

## Handoff
Identify the next artifact consumer and the human decision required.

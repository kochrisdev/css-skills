# code-review

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Review a change for concrete correctness, security and regression risks.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Every reported defect includes a concrete scenario and code location.
- Style suggestions are separated from correctness defects.
- No finding is invented to meet a quota.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
Tests pass but a cross-tenant object lookup lacks an ownership check. Describe the specific unauthorized access path.

## Handoff
Identify the next artifact consumer and the human decision required.

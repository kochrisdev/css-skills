# implementation

## Scope and version
Record task, affected artifacts, revision, environment and authority.

## Domain result
Implement a bounded software change while preserving existing behavior outside scope.

## Findings and decisions
For each finding: source location, mechanism, consequence, confidence and verification step.

## Evidence
| Claim or requirement | Source / revision | Observation | Status |
|---|---|---|---|
| Replace with actual evidence | Unavailable until supplied | Do not fabricate | not-run |

## Domain acceptance checks
- Changed behavior is traceable to acceptance criteria.
- User changes and unrelated files are preserved.
- A test not run is reported as not run.

## Assumptions, blockers and approval needs
Separate facts, proposed decisions and unresolved questions.

## Example boundary to address
The working tree contains user edits in the same file. Inspect and preserve them, and stop if overlapping edits cannot be safely reconciled.

## Handoff
Identify the next artifact consumer and the human decision required.

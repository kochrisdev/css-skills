# Domain checklist

## Common failure patterns

- Replacing a module to fix a local defect.
- Reporting tests passed after merely writing tests.
- Installing global dependencies without permission.

## Review questions

- Changed behavior is traceable to acceptance criteria.
- User changes and unrelated files are preserved.
- A test not run is reported as not run.

## Worked boundary

The working tree contains user edits in the same file. Inspect and preserve them, and stop if overlapping edits cannot be safely reconciled.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

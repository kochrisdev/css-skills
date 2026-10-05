# Contributing

Search the catalog before adding a capability. Prefer a focused change to a near-duplicate skill.
Read docs/SKILL-STANDARD.md and docs/SECURITY.md. Keep IDs stable; preserve a migration map for path changes.
Add concrete test prompts and expected/forbidden behavior. Do not replace missing model traces with asserted passes.
Run the deterministic test suite and inspect all changed files. Run `python scripts/refresh_integrity.py`
to preview content-hash changes, then `--apply` only after reviewing the source diff.
The hash updater changes integrity records only; it does not approve a skill.

A maintainer must resolve the inherited license discrepancy before publishing a public release or accepting
third-party material under an assumed license. See docs/SECURITY.md.

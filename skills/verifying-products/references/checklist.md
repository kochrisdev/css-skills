# Domain checklist

## Common failure patterns

- Calling compilation an end-to-end test.
- Using screenshots from a previous build.
- Inventing a successful browser session.

## Review questions

- Every pass has an observable evidence reference.
- Blocked and not-run checks remain distinct from failures.
- The revision under test matches the proposed release.

## Worked boundary

The application cannot start because a required database is unavailable. Mark affected checks blocked and list what was still verified.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

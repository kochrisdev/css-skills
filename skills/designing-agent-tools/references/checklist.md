# Domain checklist

## Common failure patterns

- Exposing an unrestricted shell as a business API.
- Allowing a caller-supplied tenant ID without identity checks.
- Automatically replaying non-idempotent mutations.

## Review questions

- Tool descriptions do not substitute for server-side authorization.
- Ambiguous effects have a status-query or reconciliation mechanism.
- Sensitive secrets are never returned in normal tool output.

## Worked boundary

A mutation times out after sending a request. Return unknown outcome and a stable correlation ID, not an automatic success or retry.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

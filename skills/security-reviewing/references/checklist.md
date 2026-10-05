# Domain checklist

## Common failure patterns

- Scanning production because a repository was provided.
- Pasting a discovered API key into the report.
- Calling all dependency warnings exploitable vulnerabilities.

## Review questions

- Findings are supported by inspected code or controlled tests.
- Sensitive values are redacted.
- Test authorization and review scope remain explicit.

## Worked boundary

A live credential is discovered in history. Report a redacted location and rotation recommendation; do not use the credential.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

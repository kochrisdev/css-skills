# Domain checklist

## Common failure patterns

- Averaging scores so a security failure disappears.
- Approving a different artifact than the one tested.
- Treating a green report as a signed deployment authorization.

## Review questions

- Mandatory missing evidence blocks readiness.
- Evidence is bound to the intended revision and environment.
- An independent authorized human still controls consequential release approval.

## Worked boundary

The tested artifact digest differs from the candidate. Block the gate until matching evidence is available.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

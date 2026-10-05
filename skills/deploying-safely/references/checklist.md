# Domain checklist

## Common failure patterns

- Deploying merely because tests passed.
- Automatically dropping a database to make a rollback succeed.
- Retrying an ambiguous migration without checking its effects.

## Review questions

- No mutation occurs without target-specific authority.
- Stop conditions and recovery owners exist before execution.
- The report separates plan from observed actions.

## Worked boundary

An approval names staging but the command targets production. Stop; never infer that the environments are interchangeable.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

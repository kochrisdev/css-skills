# Domain checklist

## Common failure patterns

- Treating related skills as mandatory runtime dependencies.
- Passing undocumented hidden context between steps.
- Calling a sequence of names a validated workflow.

## Review questions

- Every input is supplied initially or produced by an earlier dependency.
- No execution dependency cycle remains.
- High-impact steps expose an external approval checkpoint.

## Worked boundary

Two steps depend on each other. Surface the cycle and replace it with an explicit bounded review-and-rework process.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

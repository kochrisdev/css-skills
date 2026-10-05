# Domain checklist

## Common failure patterns

- Using names instead of stable entity IDs.
- Adding nullable fields without defining what null means.
- Choosing a database product before understanding access patterns.

## Review questions

- Every critical invariant has an enforcement location.
- Event time and processing time are distinguished where relevant.
- Privacy and deletion needs do not silently contradict audit retention.

## Worked boundary

Audit retention and deletion requests conflict. Record required policy resolution rather than claiming both are automatically satisfied.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

# Domain checklist

## Common failure patterns

- Defaulting to microservices before establishing a need.
- Claiming exactly-once delivery across unrelated providers.
- Confusing replication with a tested backup.

## Review questions

- Every major component maps to a requirement or a justified constraint.
- A partial failure walkthrough has no unexplained state owner.
- Capacity estimates show assumptions and units.

## Worked boundary

A demanded zero-data-loss guarantee spans asynchronous providers. Explain the assumptions and reconciliation boundary instead of promising it.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

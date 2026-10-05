# Domain checklist

## Common failure patterns

- Matching on amount alone.
- Rounding away recurring breaks.
- Marking provider success as settled cash without bank evidence.

## Review questions

- All records resolve to matched, documented exception or explicitly excluded.
- Totals reconcile per source, currency and period.
- Financial corrections require authority outside this design task.

## Worked boundary

Two source rows have identical amounts but distinct transaction IDs. Keep both; do not deduplicate solely by value.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

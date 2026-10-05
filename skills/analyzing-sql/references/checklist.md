# Domain checklist

## Common failure patterns

- Counting attempts as completed business transactions.
- Summing multiple currencies without a declared conversion policy.
- Using SELECT * on customer records for convenience.

## Review questions

- Join cardinality does not inflate the intended grain.
- Currency and time-window semantics are explicit.
- Query results are not fabricated when the database is unavailable.

## Worked boundary

A join multiplies one transfer by three attempts. Correct the grain and verify totals before presenting the metric.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

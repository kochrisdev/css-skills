# Domain checklist

## Common failure patterns

- Using binary floating point for authoritative money amounts.
- Balancing dollars against euros without explicit FX positions.
- Confusing ledger balance with immediately spendable funds.

## Review questions

- Every posted journal balances per entity and currency.
- Duplicate keys cannot create duplicate business effects.
- Corrections preserve original history and traceability.

## Worked boundary

A journal has equal nominal amounts in USD and EUR but is unbalanced in each currency. Reject it instead of treating the totals as balanced.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

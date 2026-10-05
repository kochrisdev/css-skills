# Domain checklist

## Common failure patterns

- Calling a dashboard a faithful simulation without validation.
- Treating twin estimates as authoritative balances.
- Allowing an agent to approve its own production command.

## Review questions

- No direct write path exists from a simulation to the authoritative bank ledger.
- Decisions expose data freshness and model uncertainty.
- Any live command requires independent approval and external enforcement.

## Worked boundary

The event feed is 45 minutes behind but the requested liquidity action assumes real-time balances. Flag the stale input and block the proposed live action.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

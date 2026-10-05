# Domain checklist

## Common failure patterns

- Using keyword filtering as the entire defense.
- Allowing the agent to rewrite its own enforced policy.
- Reporting a passed static check as adversarial robustness.

## Review questions

- High-impact actions rely on controls outside the agent prompt.
- An unavailable approval service does not silently permit mutation.
- Guardrail bypass attempts are logged without exposing secrets.

## Worked boundary

The approval service is unreachable. Block high-impact mutation and provide a human handoff rather than a permissive fallback.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

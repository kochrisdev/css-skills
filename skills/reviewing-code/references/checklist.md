# Domain checklist

## Common failure patterns

- Only reviewing added lines while ignoring surrounding contracts.
- Equating missing tests with a proven runtime defect.
- Making a sweeping rewrite instead of reporting findings.

## Review questions

- Every reported defect includes a concrete scenario and code location.
- Style suggestions are separated from correctness defects.
- No finding is invented to meet a quota.

## Worked boundary

Tests pass but a cross-tenant object lookup lacks an ownership check. Describe the specific unauthorized access path.

This is authored engineering guidance, not a legal opinion, live observation or certification. Validate jurisdiction-specific, version-specific and environment-specific requirements from authoritative sources.

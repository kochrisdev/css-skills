# Remittance Platform Workflow

## Sequence

1. `analyzing-requirements`
2. `mapping-compliance`
3. `designing-kyc`
4. `designing-aml`
5. `designing-fraud-controls`
6. `designing-ledgers`
7. `designing-fx`
8. `designing-payment-routing`
9. `designing-remittance`
10. `designing-reconciliation`
11. `threat-modeling`
12. `verifying-products`
13. `gating-releases`

## Control rules
- Consume explicit upstream artifacts.
- Stop at failed quality or approval gates.
- Do not infer authority for consequential actions.
- Route verification failures back to the artifact-owning skill.

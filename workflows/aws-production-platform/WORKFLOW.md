# Aws Production Platform Workflow

## Sequence

1. `analyzing-requirements`
2. `system-design`
3. `architecting-aws`
4. `threat-modeling`
5. `managing-terraform`
6. `designing-cicd`
7. `engineering-observability`
8. `gating-releases`
9. `deploying-safely`

## Control rules
- Consume explicit upstream artifacts.
- Stop at failed quality or approval gates.
- Do not infer authority for consequential actions.
- Route verification failures back to the artifact-owning skill.

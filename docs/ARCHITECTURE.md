# CSS Architecture
Layers: Intent → Routing → Capability → Composition → Execution → Assurance → Governance → Learning.

Canonical skill identity lives in `catalog/skill-registry.json`; `.claude/skills` is the Claude Code adapter. Future adapters may expose the same contracts to other runtimes. Downstream skills consume explicit artifacts/evidence rather than hidden assumptions.

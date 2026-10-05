---
name: designing-cloud-resilience
description: "Draft instruction template for designing cloud resilience. Not a validated domain procedure. Inspect and develop before practical use."
---

# Designing Cloud Resilience

> **Draft, not pilot-ready.** Preserved from v0.4 for catalog continuity. Its generic procedure and evaluation notes have not established domain effectiveness.

## Purpose
Provide a focused, evidence-oriented **designing cloud resilience** capability for governed CSS workflows.

## Use when
Use when the requested outcome directly requires this capability and structured execution improves correctness or traceability.

## Do not use when
Do not use outside scope, fabricate missing evidence, or bypass legal, security, financial, production, privacy, or permission boundaries.

## Inputs
- Objective, scope, constraints, and acceptance criteria.
- Authoritative artifacts and operating context.
- Applicable policies, standards, interfaces, data definitions, and prior decisions.

## Dependencies
`system-design`

## Workflow
1. Establish scope, authority, and evidence requirements.
2. Inspect authoritative sources and record uncertainty.
3. Model relevant objects, states, flows, controls, invariants, and failure modes.
4. Develop the smallest complete artifact satisfying the objective.
5. Challenge exceptions, misuse, security, compliance, data, and recovery implications.
6. Verify consistency and traceability against inputs.
7. State evidence, assumptions, unresolved risks, decisions, and next capability.

## Output contract
Produce a decision-usable artifact with scope, findings, flows or requirements, assumptions, controls, exceptions, evidence, verification status, risks, and next action.

## Quality gates
- Objective and scope are explicit.
- Material claims are traceable or labeled assumptions.
- Invariants and exception paths are covered.
- Material security, compliance, and operability implications are considered.
- Verification status is explicit.
- No hidden expansion of authority or scope.

## Failure handling
Stop at the smallest blocking dependency. Identify missing evidence or failed gates precisely. Never report unverified work as complete.

## Safety and permissions
Risk class: **medium**. Prefer read-only analysis first. Consequential actions require authorization; high-risk actions require explicit approval and recovery planning.

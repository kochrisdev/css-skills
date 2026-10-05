---
name: breaking-down-work
description: "Draft instruction template for breaking down work. Not a validated domain procedure. Inspect and develop before practical use."
---

# Breaking Down Work

> **Draft, not pilot-ready.** Preserved from v0.4 for catalog continuity. Its generic procedure and evaluation notes have not established domain effectiveness.

## Purpose
Deliver a reusable **breaking down work** capability for CSS workflows.

## Use when
Use when this capability directly matches the requested outcome and structured execution improves correctness, consistency, or traceability.

## Do not use when
Do not use outside scope, invent missing evidence, or bypass legal, security, financial, production, privacy, identity, or permission boundaries.

## Inputs
- Objective, scope, constraints, and acceptance criteria.
- Authoritative artifacts and operating context.
- Applicable standards, policies, interfaces, data, and prior decisions.

## Workflow
1. Establish objective, scope, authority, and required evidence.
2. Inspect authoritative artifacts before consequential action.
3. Identify facts, assumptions, dependencies, invariants, and failure modes.
4. Produce the smallest complete artifact or change satisfying the objective.
5. Challenge edge cases, downstream effects, security, operability, and recovery where material.
6. Verify against acceptance criteria using observable evidence.
7. Report verification status, residual risks, unresolved items, and next action.

## Output contract
Return a usable artifact or completed change with scope, evidence, assumptions, verification status, risks, unresolved items, and recommended continuation.

## Quality gates
- Objective and scope are explicit.
- Material claims are evidenced or labeled assumptions.
- Relevant edge cases and failure modes are covered.
- Verification status is explicit.
- No hidden expansion of authority or scope.

## Failure handling
Stop at the smallest blocking dependency. Report missing evidence or failed checks precisely and never represent unverified work as complete.

## Safety and permissions
Risk class: **low**. Prefer read-only inspection first. Consequential actions require appropriate authorization; high-risk actions require explicit approval and recovery planning.

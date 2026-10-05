---
name: designing-rag
description: "Draft instruction template for designing rag. Not a validated domain procedure. Inspect and develop before practical use."
---

# Designing Rag

> **Draft, not pilot-ready.** Preserved from v0.4 for catalog continuity. Its generic procedure and evaluation notes have not established domain effectiveness.

## Purpose
Provide a bounded, repeatable **designing rag** capability with explicit evidence and decision boundaries.

## Use when
Use when the requested outcome materially matches this capability and a structured procedure reduces ambiguity, risk, or rework.

## Do not use when
Do not use for unrelated work, as a substitute for unavailable authoritative evidence, or to bypass legal, security, production, financial, identity, or permission controls.

## Inputs
- Objective, scope, acceptance criteria, and constraints.
- Relevant source artifacts and authoritative evidence.
- Environment, interfaces, policies, standards, and prior decisions.

## Dependencies
`system-design`

## Workflow
1. Establish scope, authority, and required evidence.
2. Inspect authoritative artifacts before consequential changes.
3. Separate facts, assumptions, invariants, dependencies, and failure modes.
4. Produce the smallest complete domain-specific artifact or change.
5. Challenge correctness, security, operability, edge cases, and downstream effects.
6. Verify with observable evidence appropriate to the capability.
7. Record unresolved risks, approval boundaries, and recommended continuation.

## Output contract
Return a decision-usable artifact with scope, findings/design, assumptions, evidence, risks, verification status, unresolved items, and next action.

## Quality gates
- Traceable to objective and inspected evidence.
- Important invariants and failure modes are explicit.
- Facts and assumptions are separated.
- Verification status is explicit.
- Downstream impacts are addressed where relevant.
- Scope and permissions were not silently broadened.

## Failure handling
Stop at the smallest blocking dependency. Report missing evidence, failed checks, or unsafe preconditions. Preserve reversible state and never fabricate completion.

## Safety and permissions
Risk class: **medium**. Begin read-only where possible. Require appropriate authorization before consequential mutation. High-risk actions require an explicit approval boundary and rollback/recovery consideration.

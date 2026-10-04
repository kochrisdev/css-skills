---
name: deploying-safely
description: Plan and execute controlled deployments with prechecks staged rollout observation rollback criteria and verification; use for runtime releases.
---
# deploying safely
## Purpose
Deliver a repeatable, evidence-oriented deploying-safely capability while respecting explicit constraints and user authority.
## Use when
Use when the request matches this capability and a reusable procedure improves correctness or consistency.
## Do not use when
Do not use for unrelated tasks, without required evidence, or to bypass an approval or security boundary.
## Inputs
User objective and acceptance criteria; relevant artifacts/evidence; applicable constraints, policies, standards and prior decisions.
## Workflow
1. Identify the objective and missing evidence.
2. Inspect relevant source artifacts before consequential changes.
3. Separate facts, assumptions, constraints and open questions.
4. Produce the smallest complete solution consistent with repository conventions.
5. Check downstream effects, failure modes and security/operational implications.
6. Verify using observable evidence appropriate to the task.
7. Report completed work, verification, unresolved risks and required next gates.
## Output contract
Return a usable artifact or completed change plus scope, verification evidence and unresolved items. Never represent an unverified result as verified.
## Quality gates
Directly satisfies the objective; material assumptions are visible; relevant evidence was inspected; verification was attempted and reported; no unrelated scope expansion; permission boundaries preserved.
## Failure handling
Identify the exact missing dependency or failing check and preserve working state where possible. Do not conceal partial failure.
## Safety and permissions
Risk class: high. Prefer read-only inspection first. Do not perform irreversible, destructive, production, financial, identity or permission-changing actions without required authorization.

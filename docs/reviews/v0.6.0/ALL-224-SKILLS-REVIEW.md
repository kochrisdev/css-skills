# CSS v0.6.0 — Review matrix for all 224 skills

Reviewed snapshot: `9aab22968e80cf30b1e0e33c69aaf67ef956135a`. Proposed actions are reviewer recommendations, not measured model-quality scores.

All entries retain `behavioral_evaluation=not_run` and `human_review=not_recorded` in the reviewed source.

## ai-agents
Pilot: 5; draft: 6.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-021 | `designing-agents` | pilot / medium | **Evaluate authored procedure** — Add a bounded tool/state prototype and sandbox traces before any claim of operational reliability. |
| CSS-022 | `orchestrating-agents` | draft / medium | **Retain draft; author on demonstrated demand** — Record live sandbox tool traces, interruption behavior, budgets and forbidden-action attempts. |
| CSS-023 | `designing-rag` | draft / medium | **Retain draft; author on demonstrated demand** — Record live sandbox tool traces, interruption behavior, budgets and forbidden-action attempts. |
| CSS-024 | `evaluating-llms` | pilot / low | **Evaluate authored procedure** — Use matched baseline/candidate trials, pinned fixtures and human-calibrated graders rather than generated scenario counts. |
| CSS-025 | `engineering-context` | draft / low | **Retain draft; author on demonstrated demand** — Record live sandbox tool traces, interruption behavior, budgets and forbidden-action attempts. |
| CSS-079 | `designing-agent-memory` | draft / medium | **Retain draft; author on demonstrated demand** — Record live sandbox tool traces, interruption behavior, budgets and forbidden-action attempts. |
| CSS-080 | `designing-agent-tools` | pilot / medium | **Evaluate authored procedure** — Add executable schema/permission/idempotency conformance tests and ambiguous-result recovery cases. |
| CSS-081 | `designing-agent-guardrails` | pilot / medium | **Evaluate authored procedure** — Test source-embedded injection, permission failures and budget exhaustion with external control enforcement. |
| CSS-082 | `testing-agents` | pilot / medium | **Evaluate authored procedure** — Capture sandbox tool calls and end-state checks; separate attempted unauthorized actions from final response quality. |
| CSS-083 | `designing-human-agent-handoffs` | draft / low | **Retain draft; author on demonstrated demand** — Record live sandbox tool traces, interruption behavior, budgets and forbidden-action attempts. |
| CSS-084 | `designing-agent-protocols` | draft / medium | **Retain draft; author on demonstrated demand** — Record live sandbox tool traces, interruption behavior, budgets and forbidden-action attempts. |

## architecture
Pilot: 2; draft: 10.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-010 | `reviewing-architecture` | pilot / low | **Evaluate authored procedure** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-015 | `system-design` | pilot / low | **Evaluate authored procedure** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-113 | `designing-domain-models` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-114 | `designing-service-boundaries` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-115 | `designing-integration-architecture` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-116 | `designing-scalability` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-117 | `designing-resilience` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-118 | `designing-multi-tenant-systems` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-119 | `designing-api-architecture` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-120 | `designing-migration-architecture` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-121 | `creating-adrs` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |
| CSS-122 | `mapping-architecture` | draft / medium | **Retain draft; author on demonstrated demand** — Add worked interface, consistency and recovery scenarios with falsifiable design checks. |

## banking
Pilot: 1; draft: 7.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-051 | `designing-core-banking` | draft / medium | **Retain draft; author on demonstrated demand** — Add source/twin reconciliation, stale-feed tests and explicit separation of simulation from live commands. |
| CSS-052 | `designing-digital-banking` | draft / medium | **Retain draft; author on demonstrated demand** — Add source/twin reconciliation, stale-feed tests and explicit separation of simulation from live commands. |
| CSS-053 | `designing-loan-origination` | draft / medium | **Retain draft; author on demonstrated demand** — Add source/twin reconciliation, stale-feed tests and explicit separation of simulation from live commands. |
| CSS-054 | `designing-loan-management` | draft / medium | **Retain draft; author on demonstrated demand** — Add source/twin reconciliation, stale-feed tests and explicit separation of simulation from live commands. |
| CSS-055 | `designing-deposits` | draft / medium | **Retain draft; author on demonstrated demand** — Add source/twin reconciliation, stale-feed tests and explicit separation of simulation from live commands. |
| CSS-056 | `designing-bank-integrations` | draft / medium | **Priority authoring** — Add source/twin reconciliation, stale-feed tests and explicit separation of simulation from live commands. |
| CSS-057 | `designing-bank-controls` | draft / medium | **Priority authoring** — Add source/twin reconciliation, stale-feed tests and explicit separation of simulation from live commands. |
| CSS-058 | `designing-bank-digital-twins` | pilot / high | **Evaluate authored procedure** — Create a shadow-mode fixture with lag, missing events and model divergence; validate scenario assumptions and inhibit unsupported live recommendations. |

## business-strategy
Pilot: 0; draft: 13.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-094 | `analyzing-markets` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-095 | `analyzing-competitors` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-096 | `designing-business-models` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-097 | `designing-operating-models` | draft / low | **Priority authoring** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-098 | `building-business-cases` | draft / low | **Priority authoring** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-099 | `planning-scenarios` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-100 | `writing-executive-briefs` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-192 | `designing-strategies` | draft / low | **Priority authoring** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-193 | `designing-kpis` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-194 | `planning-transformations` | draft / medium | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-195 | `analyzing-unit-economics` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-196 | `designing-partnerships` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |
| CSS-197 | `planning-market-entry` | draft / low | **Retain draft; author on demonstrated demand** — Author hypothesis, option and economics templates with contrary evidence and decision rights; avoid generic prompts. |

## cloud
Pilot: 2; draft: 9.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-026 | `architecting-aws` | pilot / medium | **Evaluate authored procedure** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-027 | `managing-terraform` | pilot / high | **Evaluate authored procedure** — Use saved-plan digest, workspace/account and expiry fixtures; reject a changed plan after review. |
| CSS-028 | `operating-kubernetes` | draft / high | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-085 | `designing-cloud-networks` | draft / medium | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-086 | `designing-cloud-resilience` | draft / medium | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-087 | `optimizing-cloud-cost` | draft / low | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-155 | `designing-cloud-storage` | draft / medium | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-156 | `designing-cloud-identity` | draft / high | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-157 | `designing-cloud-backups` | draft / medium | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-158 | `designing-cloud-databases` | draft / medium | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |
| CSS-159 | `designing-serverless-systems` | draft / medium | **Retain draft; author on demonstrated demand** — Verify against pinned service/provider versions and sandbox plans; independently approve any later mutation. |

## compliance
Pilot: 3; draft: 6.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-039 | `mapping-compliance` | pilot / medium | **Evaluate authored procedure** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-040 | `designing-controls` | pilot / medium | **Evaluate authored procedure** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-041 | `testing-controls` | pilot / medium | **Evaluate authored procedure** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-073 | `building-traceability` | draft / medium | **Retain draft; author on demonstrated demand** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-074 | `collecting-audit-evidence` | draft / medium | **Retain draft; author on demonstrated demand** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-075 | `analyzing-compliance-gaps` | draft / medium | **Retain draft; author on demonstrated demand** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-076 | `writing-policies` | draft / low | **Retain draft; author on demonstrated demand** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-077 | `designing-sanctions-screening` | draft / medium | **Priority authoring** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |
| CSS-078 | `designing-case-management` | draft / medium | **Retain draft; author on demonstrated demand** — Bind every obligation to issuer, jurisdiction, entity, section, effective date and qualified applicability review. |

## data
Pilot: 2; draft: 9.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-043 | `analyzing-sql` | pilot / medium | **Evaluate authored procedure** — Add executable SQLite fixtures for fan-out, nulls, cutoff boundaries and refunds; independently assert totals. |
| CSS-044 | `modeling-data` | pilot / medium | **Evaluate authored procedure** — Validate schema constraints and sample migrations, not only a prose entity model. |
| CSS-045 | `assuring-data-quality` | draft / medium | **Priority authoring** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-088 | `designing-data-pipelines` | draft / medium | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-089 | `designing-analytics` | draft / low | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-090 | `designing-dashboards` | draft / low | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-182 | `designing-data-governance` | draft / medium | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-183 | `designing-data-privacy` | draft / medium | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-184 | `designing-master-data` | draft / low | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-185 | `designing-data-warehouses` | draft / low | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |
| CSS-186 | `designing-streaming-data` | draft / medium | **Retain draft; author on demonstrated demand** — Use executable datasets with join fan-out, late events, mixed units, missing data and independent control totals. |

## devops
Pilot: 1; draft: 8.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-006 | `deploying-safely` | pilot / high | **Evaluate authored procedure** — Test exact candidate/target/approval binding and interruption in a non-production harness; do not expand action authority. |
| CSS-029 | `designing-cicd` | draft / medium | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |
| CSS-148 | `designing-container-images` | draft / medium | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |
| CSS-149 | `reviewing-github-actions` | draft / medium | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |
| CSS-150 | `managing-environments` | draft / medium | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |
| CSS-151 | `designing-release-strategies` | draft / medium | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |
| CSS-152 | `designing-feature-flags` | draft / medium | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |
| CSS-153 | `managing-database-migrations` | draft / high | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |
| CSS-154 | `designing-build-systems` | draft / medium | **Retain draft; author on demonstrated demand** — Bind plans and observations to candidate digest, environment and expiry; test interrupted upgrades. |

## documentation
Pilot: 1; draft: 8.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-020 | `writing-documentation` | pilot / low | **Evaluate authored procedure** — Add executable command/link checks and document-role tagging to prevent renewed documentation sprawl. |
| CSS-140 | `writing-readmes` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |
| CSS-141 | `documenting-apis` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |
| CSS-142 | `writing-developer-guides` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |
| CSS-143 | `writing-runbooks` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |
| CSS-144 | `consolidating-documentation` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |
| CSS-145 | `reviewing-documentation` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |
| CSS-146 | `documenting-data-models` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |
| CSS-147 | `documenting-operations` | draft / low | **Retain draft; author on demonstrated demand** — Use real repository navigation and link/command checks; preserve a single canonical source per concept. |

## fintech
Pilot: 1; draft: 6.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-031 | `designing-ledgers` | pilot / medium | **Harden and evaluate** — Reject duplicate JSON keys in the standalone checker; add journal fixtures and independently reviewed currency/entity invariants. |
| CSS-032 | `designing-kyc` | draft / medium | **Priority authoring** — Create reconciled synthetic events, decision states, authority boundaries and independently reviewed money invariants. |
| CSS-033 | `designing-aml` | draft / medium | **Priority authoring** — Create reconciled synthetic events, decision states, authority boundaries and independently reviewed money invariants. |
| CSS-034 | `designing-fraud-controls` | draft / medium | **Retain draft; author on demonstrated demand** — Create reconciled synthetic events, decision states, authority boundaries and independently reviewed money invariants. |
| CSS-198 | `designing-wallets` | draft / medium | **Retain draft; author on demonstrated demand** — Create reconciled synthetic events, decision states, authority boundaries and independently reviewed money invariants. |
| CSS-199 | `designing-merchant-payments` | draft / medium | **Retain draft; author on demonstrated demand** — Create reconciled synthetic events, decision states, authority boundaries and independently reviewed money invariants. |
| CSS-200 | `designing-transaction-limits` | draft / medium | **Retain draft; author on demonstrated demand** — Create reconciled synthetic events, decision states, authority boundaries and independently reviewed money invariants. |

## governance
Pilot: 1; draft: 1.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-007 | `gating-releases` | pilot / high | **Harden and evaluate** — Reject duplicate JSON keys; bind release evidence and code-review findings to one candidate and explicit policy. |
| CSS-042 | `assessing-risk` | draft / low | **Retain draft; author on demonstrated demand** — Replace blanket labels with reviewer-owned policy records and evidence-bound scope-specific decisions. |

## meta
Pilot: 9; draft: 0.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-004 | `creating-skills` | pilot / medium | **Evaluate authored procedure** — Reuse existing IDs where the capability already exists; require distinct procedures, task fixtures and falsifiable output schemas. |
| CSS-012 | `reviewing-skills` | pilot / medium | **Evaluate authored procedure** — Evaluate trigger ambiguity, workflow specificity, realistic case fixtures and hidden-grader separation. |
| CSS-013 | `routing-skills` | pilot / medium | **Evaluate authored procedure** — Use a separate paraphrase/ambiguity set and explain alternatives; do not treat lexical scores as competence or authority. |
| CSS-016 | `testing-skills` | pilot / medium | **Evaluate authored procedure** — Build a live-runtime harness with isolated fixtures and a separate grader, while preserving not-run status until execution. |
| CSS-046 | `discovering-skills` | pilot / low | **Evaluate authored procedure** — Distinguish unavailable capability from poor retrieval; add synonyms and benchmark candidate recall independently. |
| CSS-047 | `composing-skills` | pilot / low | **Evaluate authored procedure** — Bind typed artifacts to producer revision and actual content, and check explicit per-step review policies. |
| CSS-048 | `benchmarking-skills` | pilot / low | **Evaluate authored procedure** — Add paired no-skill versus skill trials with runtime/model hashes, uncertainty and critical-failure reporting. |
| CSS-049 | `improving-skills` | pilot / medium | **Evaluate authored procedure** — Require a failure-linked minimal diff, regression evidence and reviewer approval before promotion. |
| CSS-050 | `governing-skills` | pilot / medium | **Evaluate authored procedure** — Create a review-evidence state machine and revocation/expiry; do not weaken the current release blocker. |

## operations
Pilot: 1; draft: 9.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-018 | `triaging-incidents` | pilot / medium | **Evaluate authored procedure** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-030 | `engineering-observability` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-160 | `analyzing-logs` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-161 | `performing-root-cause-analysis` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-162 | `investigating-latency` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-163 | `planning-capacity` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-164 | `verifying-backups` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-165 | `planning-disaster-recovery` | draft / high | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-166 | `designing-slos` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |
| CSS-167 | `designing-alerts` | draft / medium | **Retain draft; author on demonstrated demand** — Use synthetic incident timelines, partial telemetry and recovery handoffs; grade diagnosis separately from containment. |

## payments
Pilot: 2; draft: 9.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-035 | `designing-fx` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-036 | `designing-remittance` | pilot / medium | **Evaluate authored procedure** — Create a sandbox state-machine trace with an ambiguous payout, late callback and reconciliation before retry. |
| CSS-037 | `designing-payment-routing` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-038 | `designing-reconciliation` | pilot / medium | **Evaluate authored procedure** — Implement independently reconciled matching examples with timing differences, fee splits and rerun idempotency. |
| CSS-059 | `designing-payment-ledgers` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-060 | `designing-settlement` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-061 | `designing-payouts` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-062 | `designing-payment-webhooks` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-063 | `designing-payment-exceptions` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-064 | `designing-corridors` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |
| CSS-065 | `monitoring-payments` | draft / medium | **Retain draft; author on demonstrated demand** — Add duplicate, timeout, out-of-order and reconciliation fixtures; preserve unknown-outcome handling. |

## private-capital
Pilot: 8; draft: 0.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-217 | `developing-investment-theses` | pilot / medium | **Evaluate authored procedure** — Create a falsifiable mandate-to-thesis case with contrary scenarios and source refresh triggers. |
| CSS-218 | `diligencing-fund-managers` | pilot / medium | **Evaluate authored procedure** — Add a sourced synthetic DDQ and track-record reconciliation case with independent confirmation needs. |
| CSS-219 | `modeling-fund-economics` | pilot / high | **Evaluate authored procedure** — Add governing-document-specific fee/waterfall fixtures; retain the simple-multiples helper boundary until separately validated. |
| CSS-220 | `reviewing-private-valuations` | pilot / high | **Evaluate authored procedure** — Add a dated, security-specific valuation case, calibration checks and an independent reviewer record. |
| CSS-221 | `preparing-investment-committee-memos` | pilot / high | **Evaluate authored procedure** — Validate a structured diligence bundle with source/model revisions, unresolved workstreams and pending human approval. |
| CSS-222 | `reporting-private-funds` | pilot / medium | **Evaluate authored procedure** — Validate a synthetic NAV bridge, dated cash flows and gross/net scope against a reviewed reporting policy. |
| CSS-223 | `planning-private-fundraising` | pilot / high | **Evaluate authored procedure** — Add a counsel-review and evidence workflow; distinguish interest, signed commitments and cleared funds. |
| CSS-224 | `reviewing-co-investments` | pilot / high | **Evaluate authored procedure** — Reconcile sponsor, fund and SPV economics and conflicts using a synthetic security-specific case. |

## private-equity
Pilot: 8; draft: 0.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-201 | `screening-buyouts` | pilot / medium | **Evaluate authored procedure** — Test natural-language acquisition screens and downside conditions without naming the desired skill in the task. |
| CSS-202 | `conducting-quality-of-earnings` | pilot / medium | **Evaluate authored procedure** — Add a trial-balance-to-EBITDA and cash-conversion fixture with disputed add-backs and double-count detection. |
| CSS-203 | `diligencing-buyout-commercials` | pilot / medium | **Evaluate authored procedure** — Reconcile customer concentration, signed backlog and pricing cases to forecast assumptions. |
| CSS-204 | `modeling-buyouts` | pilot / high | **Evaluate authored procedure** — Advance to a tested debt roll-forward/cash-sweep/covenant model with sources-and-uses and independent downside fixtures. |
| CSS-205 | `structuring-acquisition-finance` | pilot / high | **Evaluate authored procedure** — Add indicative-versus-committed terms, downside liquidity and exact covenant-definition fixtures. |
| CSS-206 | `planning-pe-value-creation` | pilot / medium | **Evaluate authored procedure** — Add a 100-day initiative-to-benefit bridge with overlapping benefits, costs, owners and verification. |
| CSS-207 | `reviewing-pe-portfolios` | pilot / medium | **Evaluate authored procedure** — Use actual-versus-underwriting synthetic bridges and covenant/working-capital warning cases. |
| CSS-208 | `planning-pe-exits` | pilot / medium | **Evaluate authored procedure** — Add route-specific net-proceeds, timing and contingent-liability scenarios with independent review. |

## product
Pilot: 2; draft: 8.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-001 | `analyzing-requirements` | pilot / low | **Evaluate authored procedure** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-003 | `creating-prds` | pilot / low | **Evaluate authored procedure** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-132 | `writing-user-stories` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-133 | `writing-acceptance-criteria` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-134 | `designing-mvps` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-135 | `prioritizing-backlogs` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-136 | `planning-roadmaps` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-137 | `designing-product-metrics` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-138 | `analyzing-product-discovery` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |
| CSS-139 | `planning-product-releases` | draft / low | **Retain draft; author on demonstrated demand** — Add real briefs with conflicting requirements, source provenance and measurable acceptance checks. |

## project-management
Pilot: 0; draft: 8.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-009 | `planning-projects` | draft / low | **Priority authoring** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |
| CSS-168 | `breaking-down-work` | draft / low | **Retain draft; author on demonstrated demand** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |
| CSS-169 | `estimating-work` | draft / low | **Retain draft; author on demonstrated demand** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |
| CSS-170 | `managing-project-risks` | draft / low | **Retain draft; author on demonstrated demand** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |
| CSS-171 | `mapping-dependencies` | draft / low | **Retain draft; author on demonstrated demand** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |
| CSS-172 | `planning-milestones` | draft / low | **Retain draft; author on demonstrated demand** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |
| CSS-173 | `reporting-project-status` | draft / low | **Retain draft; author on demonstrated demand** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |
| CSS-174 | `assessing-project-health` | draft / low | **Retain draft; author on demonstrated demand** — Author evidence-based delivery plans with owners, dependencies, resource limits and measurable exit criteria. |

## quality
Pilot: 1; draft: 7.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-011 | `reviewing-code` | pilot / low | **Evaluate authored procedure** — Consume the implementation changeset and bind findings/approval conditions to that same revision. |
| CSS-175 | `designing-quality-gates` | draft / low | **Retain draft; author on demonstrated demand** — Validate actual artifact structure and source identity, not just document headings or type names. |
| CSS-176 | `checking-conformance` | draft / low | **Retain draft; author on demonstrated demand** — Validate actual artifact structure and source identity, not just document headings or type names. |
| CSS-177 | `auditing-artifacts` | draft / low | **Retain draft; author on demonstrated demand** — Validate actual artifact structure and source identity, not just document headings or type names. |
| CSS-178 | `reviewing-design-quality` | draft / low | **Retain draft; author on demonstrated demand** — Validate actual artifact structure and source identity, not just document headings or type names. |
| CSS-179 | `managing-nonconformities` | draft / low | **Retain draft; author on demonstrated demand** — Validate actual artifact structure and source identity, not just document headings or type names. |
| CSS-180 | `designing-quality-metrics` | draft / low | **Retain draft; author on demonstrated demand** — Validate actual artifact structure and source identity, not just document headings or type names. |
| CSS-181 | `improving-processes` | draft / low | **Retain draft; author on demonstrated demand** — Validate actual artifact structure and source identity, not just document headings or type names. |

## research
Pilot: 1; draft: 8.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-002 | `conducting-research` | pilot / low | **Evaluate authored procedure** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-091 | `reviewing-literature` | draft / low | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-092 | `verifying-sources` | draft / low | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-093 | `scanning-technology` | draft / low | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-187 | `designing-research-plans` | draft / low | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-188 | `synthesizing-evidence` | draft / low | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-189 | `analyzing-papers` | draft / low | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-190 | `mapping-trends` | draft / low | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |
| CSS-191 | `conducting-due-diligence` | draft / medium | **Retain draft; author on demonstrated demand** — Use a fixed source corpus with contradictory and stale evidence; grade claim-level citation accuracy. |

## security
Pilot: 2; draft: 7.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-014 | `security-reviewing` | pilot / medium | **Evaluate authored procedure** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-017 | `threat-modeling` | pilot / medium | **Evaluate authored procedure** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-066 | `reviewing-authentication` | draft / medium | **Retain draft; author on demonstrated demand** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-067 | `reviewing-authorization` | draft / medium | **Priority authoring** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-068 | `reviewing-api-security` | draft / medium | **Retain draft; author on demonstrated demand** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-069 | `auditing-secrets` | draft / medium | **Retain draft; author on demonstrated demand** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-070 | `reviewing-dependencies` | draft / medium | **Retain draft; author on demonstrated demand** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-071 | `modeling-abuse` | draft / medium | **Retain draft; author on demonstrated demand** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |
| CSS-072 | `reviewing-cloud-security` | draft / medium | **Retain draft; author on demonstrated demand** — Test authorization and prompt-injection boundaries in an isolated fixture with tool-attempt tracing. |

## software-engineering
Pilot: 2; draft: 12.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-005 | `debugging-code` | pilot / medium | **Evaluate authored procedure** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-008 | `implementing-code` | pilot / medium | **Evaluate authored procedure** — Produce a changeset artifact with revision/diff and regression results so downstream review cannot use a stale supplied diff. |
| CSS-101 | `refactoring-code` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-102 | `optimizing-performance` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-103 | `modernizing-legacy-systems` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-104 | `designing-error-handling` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-105 | `reviewing-concurrency` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-106 | `managing-dependencies` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-107 | `designing-cli-tools` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-108 | `designing-sdks` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-109 | `designing-event-driven-systems` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-110 | `designing-background-jobs` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-111 | `reviewing-database-code` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |
| CSS-112 | `managing-technical-debt` | draft / medium | **Retain draft; author on demonstrated demand** — Use small executable repository fixtures with failing regressions, preserved user edits and exact diffs. |

## testing
Pilot: 1; draft: 9.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-019 | `verifying-products` | pilot / low | **Evaluate authored procedure** — Run acceptance fixtures and trace all passed claims to observable outputs at a pinned revision. |
| CSS-123 | `designing-unit-tests` | draft / low | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-124 | `designing-integration-tests` | draft / low | **Priority authoring** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-125 | `designing-e2e-tests` | draft / low | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-126 | `testing-apis` | draft / low | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-127 | `testing-performance` | draft / medium | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-128 | `testing-accessibility` | draft / low | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-129 | `testing-regressions` | draft / low | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-130 | `designing-test-data` | draft / low | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |
| CSS-131 | `testing-migrations` | draft / medium | **Retain draft; author on demonstrated demand** — Add runnable fixtures, independent expected outcomes and repeatable positive and negative tests. |

## venture-capital
Pilot: 8; draft: 0.

| ID | Skill | Current state | Recommended next work |
|---|---|---|---|
| CSS-209 | `screening-venture-deals` | pilot / medium | **Evaluate authored procedure** — Use incomplete founder dossiers and financing constraints; independently grade scope and diligence decisions. |
| CSS-210 | `diligencing-founders` | pilot / medium | **Evaluate authored procedure** — Use consented/synthetic evidence and a role-based rubric; test contradictory records and privacy boundaries. |
| CSS-211 | `assessing-product-market-fit` | pilot / medium | **Evaluate authored procedure** — Use segment-level cohorts and contrary evidence; distinguish early observations from stable fit. |
| CSS-212 | `analyzing-startup-metrics` | pilot / medium | **Evaluate authored procedure** — Add cohort-consistent ARR, NRR and runway datasets with explicit denominator and cash-flow checks. |
| CSS-213 | `modeling-venture-cap-tables` | pilot / high | **Evaluate authored procedure** — Add independent numeric graders; keep SAFE/pool/secondary/preference cases separate from the existing simple-round helper. |
| CSS-214 | `reviewing-venture-terms` | pilot / high | **Evaluate authored procedure** — Link economic and control findings to clauses and independently calculated preference/conversion scenarios. |
| CSS-215 | `constructing-venture-portfolios` | pilot / medium | **Evaluate authored procedure** — Add budget/reserve reconciliation and correlated-failure scenario fixtures without claiming predicted returns. |
| CSS-216 | `planning-follow-on-investments` | pilot / high | **Evaluate authored procedure** — Add no-follow-on/pro-rata/increase cases with explicit reserve and dilution reconciliation and pending authorization. |


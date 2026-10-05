# CSS v0.4 review and v0.5 remediation

**Review date:** 2026-10-05. **Baseline:** GitHub commit
`cb2a4689b46f38d136fdd3a2b7d572d87f657fb7` (`Add CSS v0.4.0`).

The provided ZIP was unpacked safely and its Git tree reconstructed locally. Its tree hash
`ea6a71855e1f412402f71e00da5f6dd861ae68b5` exactly matches the tree referenced by that GitHub commit.
This verifies file-content coverage of the reviewed snapshot, not any unseen local edits on your computer.
Archive SHA-256: `7379c1fa9d150054ac892ccc9a5ce5232c0cdf64b4ef04e4c601035c2cd978b6`.

## Overall assessment

v0.4 is a useful **capability taxonomy and instruction scaffold**, not a demonstrated production skill system.
Earlier descriptions of “production depth” and “200 governed skills” exceeded the available evidence.
The structural validator did pass its own limited rules, but that did not establish domain competence,
model reliability, enforcement of controls or runtime adapter behavior.

## Reproducible findings

| ID | Severity | Observation in the reviewed files | Remediation in v0.5 |
|---|---|---|---|
| CSS-A01 | High | All 200 Workflow sections collapse to four exact templates, in groups of 20, 30, 50 and 100. | Authored 40 distinct pilot procedures; labeled the other 160 as drafts. |
| CSS-A02 | High | Zero support files under the 200 skill directories. L2 labels therefore did not imply specialized knowledge or executable depth. | Added per-pilot checklists, output templates and concrete cases, plus two narrow offline helpers. |
| CSS-A03 | High | “Evaluation packs” were Markdown scenario headings, with no recorded model runs or executable evaluation runner. | Separated behavioral case definitions, deterministic tests and lexical smoke results; behavioral status stays not-run. |
| CSS-A04 | High | The only Python file was the validator. It checked a fixed count of 200, name uniqueness, headings, dependency existence and eval-file existence. It did not check IDs, metadata parsing, content drift, cycles, resource links or typed workflow handoffs. | Added constrained frontmatter parsing, schema-shaped checks, stable-ID tests, digest checks, cycle detection, resource validation and typed recipe checks. |
| CSS-A05 | High | Installation was manual copying, without collision checks, ownership tracking, backup or restoration. | Added preview-first profile installation, integrity checks, ownership protection, transaction backups and guarded restoration. |
| CSS-A06 | Medium | Skill references conflated helpful upstream knowledge with mandatory executable dependencies. Workflows were sequences of names rather than artifact contracts. | Preserved old references as related-skills; made execution order explicit in six typed workflow recipes. |
| CSS-A07 | Medium | The adapter directories contained explanatory README files, not implemented exporters. | Implemented Claude, Codex and generic file projections, tested as local file operations. Host behavior remains untested. |
| CSS-A08 | Medium | All 200 sources occupied Claude's discoverable directory, including draft and operational instructions. | Moved canonical sources to skills/; explicit selected-profile installation creates runtime directories. |
| CSS-A09 | Medium | Catalog, dependency, graph, domain-pack and workflow representations duplicated navigation and state. | Kept one registry, small profiles and canonical recipes; graph output is derived on demand. |
| CSS-A10 | High | The current LICENSE is a one-line Apache notice. Initial repository history used MIT. | Preserved LICENSE byte-for-byte and documented an owner decision; no silent relicensing. |

The archive has 474 files and 21 domains. There are no executable test modules in v0.4,
no specialized skill helper scripts, and no actual behavioral run records. See
`reports/v04-audit.json` for the measured inventory. The claims above are about this snapshot only.

## What the improved release actually delivers

The catalog stays at 200 entries. Forty procedures now contain task-specific decisions,
edge cases and quality checks, rather than only replacing a name inside common prose.
Examples include ambiguous payout outcomes, per-currency ledger balancing, stale bank-twin data,
external approval enforcement, Terraform plan binding, SQL join grain and agent prompt-injection handling.

The runtime tooling is deliberately narrower than the earlier aspirational “Skill Intelligence Layer.”
It provides local discovery, declared workflow planning, structural validation and controlled file installation.
It does not run a bank, transfer money, apply infrastructure, authenticate approvals, train a model,
perform autonomous self-improvement or demonstrate universal semantic routing.

The lexical smoke suite first exposed a missing singular/plural normalization for guardrails.
The correction is captured in the final code and regression tests. The smoke set is authored development
coverage, not a held-out estimate of real-world routing accuracy.

## Remaining release blockers and limitations

The owner must select and document the intended license, reconciling the initial MIT history and current
Apache notice. Independent domain reviewers have not reviewed the newly authored procedures.
Claude Code and Codex were not available for live behavioral runs; 160 case definitions remain not-run.
A Windows/Linux CI matrix is configured but has not run on GitHub. Local execution evidence is Linux only.

Cryptographic hashes detect changed bytes relative to a manifest. They do not prove publisher identity,
source trustworthiness or semantic correctness. Workflow type checks do not validate the truth of input data.
Instructions about safety do not replace a host sandbox, access controls or human authority.

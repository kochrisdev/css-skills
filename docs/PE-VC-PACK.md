# Private Equity & Venture Capital Pack — CSS v0.6.0

24 authored procedures: eight buyout/PE, eight startup/VC and eight shared investment/fund-management procedures.
This is analytical support for qualified humans, not investment execution, personal financial advice, legal advice,
an audit opinion, or guaranteed returns. Independent expert review and live agent evaluations have not run.

## Catalog

### Private Equity

| ID | Skill | Output artifact |
|---|---|---|
| CSS-201 | [screening-buyouts](../skills/screening-buyouts/SKILL.md) | `buyout-screen` |
| CSS-202 | [conducting-quality-of-earnings](../skills/conducting-quality-of-earnings/SKILL.md) | `qoe-review` |
| CSS-203 | [diligencing-buyout-commercials](../skills/diligencing-buyout-commercials/SKILL.md) | `commercial-dd` |
| CSS-204 | [modeling-buyouts](../skills/modeling-buyouts/SKILL.md) | `buyout-model` |
| CSS-205 | [structuring-acquisition-finance](../skills/structuring-acquisition-finance/SKILL.md) | `financing-review` |
| CSS-206 | [planning-pe-value-creation](../skills/planning-pe-value-creation/SKILL.md) | `value-creation-plan` |
| CSS-207 | [reviewing-pe-portfolios](../skills/reviewing-pe-portfolios/SKILL.md) | `pe-portfolio-review` |
| CSS-208 | [planning-pe-exits](../skills/planning-pe-exits/SKILL.md) | `exit-plan` |

### Venture Capital

| ID | Skill | Output artifact |
|---|---|---|
| CSS-209 | [screening-venture-deals](../skills/screening-venture-deals/SKILL.md) | `venture-screen` |
| CSS-210 | [diligencing-founders](../skills/diligencing-founders/SKILL.md) | `founder-dd` |
| CSS-211 | [assessing-product-market-fit](../skills/assessing-product-market-fit/SKILL.md) | `pmf-assessment` |
| CSS-212 | [analyzing-startup-metrics](../skills/analyzing-startup-metrics/SKILL.md) | `startup-metrics` |
| CSS-213 | [modeling-venture-cap-tables](../skills/modeling-venture-cap-tables/SKILL.md) | `cap-table-model` |
| CSS-214 | [reviewing-venture-terms](../skills/reviewing-venture-terms/SKILL.md) | `venture-terms-review` |
| CSS-215 | [constructing-venture-portfolios](../skills/constructing-venture-portfolios/SKILL.md) | `venture-portfolio-plan` |
| CSS-216 | [planning-follow-on-investments](../skills/planning-follow-on-investments/SKILL.md) | `follow-on-review` |

### Shared Private Capital

| ID | Skill | Output artifact |
|---|---|---|
| CSS-217 | [developing-investment-theses](../skills/developing-investment-theses/SKILL.md) | `investment-thesis` |
| CSS-218 | [diligencing-fund-managers](../skills/diligencing-fund-managers/SKILL.md) | `manager-dd` |
| CSS-219 | [modeling-fund-economics](../skills/modeling-fund-economics/SKILL.md) | `fund-economics` |
| CSS-220 | [reviewing-private-valuations](../skills/reviewing-private-valuations/SKILL.md) | `valuation-review` |
| CSS-221 | [preparing-investment-committee-memos](../skills/preparing-investment-committee-memos/SKILL.md) | `investment-memo` |
| CSS-222 | [reporting-private-funds](../skills/reporting-private-funds/SKILL.md) | `lp-report` |
| CSS-223 | [planning-private-fundraising](../skills/planning-private-fundraising/SKILL.md) | `fundraising-plan` |
| CSS-224 | [reviewing-co-investments](../skills/reviewing-co-investments/SKILL.md) | `co-investment-review` |

## Profiles and installation

`private-equity` installs eight PE skills plus thesis, valuation, IC and co-investment procedures.
`venture-capital` installs eight VC skills plus the same four shared procedures.
`private-capital` installs the eight shared procedures. `pe-vc` installs all 24.
Existing profiles retain their purpose; `pilot` now intentionally includes all 64 authored pilots.

```bash
python -m css install --profile pe-vc --runtime claude --target /path/to/existing/project
python -m css install --profile pe-vc --runtime claude --target /path/to/existing/project --apply
```

The first command previews; the second explicitly writes local exported procedures.
Use `--runtime codex` or `--runtime generic` for those projections. Host behavior remains untested.

## Plan-only workflows

| Recipe | Sequence and boundary |
|---|---|
| `pe-underwriting` | Screen → QoE → commercial diligence → LBO model |
| `vc-diligence` | Screen → founder diligence → PMF → startup metrics → cap table → term review |
| `private-fund-review` | Manager diligence → fund economics → LP reporting |
| `investment-committee` | A separate decision-memo step consuming an already reviewed thesis, consolidated diligence findings and investment model |

```bash
python -m css plan pe-underwriting
python -m css plan vc-diligence
python -m css plan private-fund-review
python -m css plan investment-committee
```

Workflow contracts check declared types/order only; they do not validate source documents or approvals.
A human must consolidate workstream findings into the IC input artifact; there is no hidden automatic aggregation.
Every new workflow step is marked for human review. No recipe calls a bank, executes an investment,
sends investor messages or approves a subscription. No funding or external credentials are required.

## Four narrow arithmetic helpers

Run from the CSS source checkout, not from the target application's installed skill folder:

```bash
python -m css.pevc examples/pevc/fund-multiples.json
python -m css.pevc examples/pevc/priced-round.json
python -m css.pevc examples/pevc/sources-uses.json
python -m css.pevc examples/pevc/exit-bridge.json
```

Input shape is `{ "operation": "fund-multiples", "inputs": { ... } }`.
Use ordinary decimal strings or integers; booleans, binary floats, exponent notation,
negative amounts and more than 12 fractional digits are rejected. Outputs are decimal strings,
computed in a 120-significant-digit context; recurring fractions are therefore rounded, not symbolic exact fractions.
Amounts use one declared currency and one consistent unit. The helper performs no FX conversion or source authentication.

| Helper | Formula / scope | Synthetic expected result |
|---|---|---|
| Fund multiples | DPI = distributions / paid-in; RVPI = NAV / paid-in; TVPI = (distributions + NAV) / paid-in | 50m paid-in, 20m distributions, 40m NAV → 0.4x, 0.8x, 1.2x |
| Simple priced round | Price = pre-money / supplied fully diluted shares; new shares = investment / price | 8m pre, 2m primary, 10m shares → 0.8/share, 12.5m post shares, 20% new investor |
| Sources/uses | Compare named financing amounts and transaction uses | 30m debt + 25m equity = 50m purchase + 5m fees |
| Exit equity bridge | max(0, EV + cash − debt − costs); MOIC includes separately supplied interim distributions | 100m EV + 5m cash − 40m debt − 5m costs = 60m equity; 30m investment → 2x |

Fund-multiple inputs require explicit as-of date and gross/net label. They support positive paid-in and
nonnegative NAV only; negative NAV, complex recallability, subscription-line adjustments and accounting-policy
interpretation require separate work. The simple round excludes SAFE/note conversion, option-pool changes,
secondary sales, preferences and legal share issuance. The exit bridge is not an LBO schedule or security waterfall.
No helper computes IRR/XIRR, DCF, carry, taxes, preference waterfalls or investment recommendations.
For a full analysis, use the authored procedure with inspected governing documents and qualified reviewers.

CLI exit codes: `0` completed calculation; `1` sources/uses do not balance; `2` invalid or unsupported input.
The helper reads a supplied JSON and prints JSON; it does not write files, connect to finance systems or move funds.

## Evidence and version policy

Every new procedure has a distinct workflow, local checklist, output template and four behavioral cases.
Those 96 cases are definitions, not observed passes. Computational and structural tests are a separate evidence layer.
The 24 new IDs are CSS-201 through CSS-224; `legacy_path` is null because they did not exist in v0.4.
`catalog/v05-identities.json` retains the original ID/name baseline. The existing v0.4 migration map is unchanged.
The release version is 0.6.0; source metadata is updated without changing existing skill identities.

## Primary-source discovery pointers

Landing pages checked on **2026-10-05**. This package includes original procedures, not copies of third-party
legal forms, accounting standards or proprietary questionnaires. No organization listed below endorses CSS.
Consult current complete documents and applicable law for an actual engagement; merely citing a source
is not evidence of legal, accounting or standards conformance.

- [ILPA due diligence questionnaire overview](https://ilpa.org/industry-guidance/templates-standards-model-documents/due-diligence-questionnaire-and-diversity-metrics-template/) — landing-page review only; retrieve applicable full documents before substantive use.
- [ILPA templates hub](https://ilpa.org/industry-guidance/templates-standards-model-documents/ilpa-templates-hub/) — landing-page review only; retrieve applicable full documents before substantive use.
- [IPEV valuation guidelines landing page](https://www.privateequityvaluation.com/Valuation-Guidelines) — landing-page review only; retrieve applicable full documents before substantive use.
- [NVCA model legal documents](https://nvca.org/model-legal-documents/) — landing-page review only; retrieve applicable full documents before substantive use.
- [Y Combinator SAFE resources](https://www.ycombinator.com/safe) — landing-page review only; retrieve applicable full documents before substantive use.

The current IPEV landing page identifies its 2025 guidelines; NVCA model forms have different revision dates.
The ILPA reporting/performance template resources identify 2025 releases. Draft or future updates must not
be represented as adopted requirements. The DDQ pointer is for manager questions, not a company audit standard.
US model venture documents and YC instrument examples must not be generalized to every jurisdiction.

## Publication and remaining limits

The inherited LICENSE remains byte-for-byte unchanged. Its unresolved history, independent review and
live behavioral evaluation continue to block `python -m css validate --release` intentionally.
Committing this pilot source is not the same as publishing a cleared, investment-ready software release.

# Architecture

## Boundaries

CSS has three distinct surfaces: canonical authoring data (`skills/`, `catalog/`),
local deterministic tooling (`css/`), and generated runtime projections in a target project.
Nothing runs automatically from the canonical catalog.

| Layer | Implementation | Deliberately excluded |
|---|---|---|
| Catalog | One registry with IDs, scope, status, risk, inputs, outputs and digests | Quality claims inferred from file count |
| Discovery | TF-IDF cosine, small normalization map, explained matches and abstention | Embeddings, LLM semantic routing, success probabilities |
| Composition | Six JSON recipes with named steps, dependencies and typed artifact bindings | Autonomous planner, actual evidence retrieval, runtime execution |
| Assurance | Structural validation, unit/integration tests, two offline helpers | Model-behavior certification |
| Projection | Selected-profile Claude/Codex/generic export | Automatic tool grants, hooks or credentials |
| Installation | Dry run, collision refusal, source integrity, lock, backup, restore | Force overwrite, deleting local edits, changing Git history |

## Data authority

`catalog/skill-registry.json` owns identity, status and metadata. Each `skills/<name>/SKILL.md`
owns its procedure. Registry and frontmatter descriptions must agree.
`profiles/*.json` select pilot procedures; they are not permission policies.
`workflows/*.json` own declared order and artifact types. Graph output is computed from these sources.
Do not edit a second dependency graph by hand.

The old v0.4 `depends_on` links represented related expertise, not proven hard requirements.
They now live in `related_skills`. `depends_on` is reserved for genuine install prerequisites;
no such hard prerequisite is required by the currently self-contained procedures.
Cycles in that field are rejected. Existing input artifacts can satisfy a workflow without
requiring the skill that originally produced them to be rerun.

## Typed recipe semantics

Each step names a pilot skill. Input bindings must cover exactly its input types and point to an
initial input or an artifact produced by a declared predecessor. Every output has one owner.
High-risk steps must carry `human-review-required`. Missing sources, mismatched types and cycles fail validation.
These are declaration checks. A plan result explicitly says `plan-only` and `executed: false`.
Actual evidence authenticity, freshness, approvals, permissions and execution remain external responsibilities.

## Runtime projections

Canonical files use the portable Agent Skills core fields: `name` and `description`.
CSS metadata stays in the registry. Claude output adds `disable-model-invocation: true`.
Codex output adds `agents/openai.yaml` with `policy.allow_implicit_invocation: false`.
Generic output goes to `exported-skills` and has no automatic host-discovery claim.
All projections are tested as byte/file transformations, not as observed live host behavior.

No `allowed-tools` grant is generated. In current Claude documentation, that field pre-approves tools;
it is not a sandbox or a restriction on all other tools. See SOURCES.md.

## Installation transaction

Preflight validates the source, resolves a profile, renders files, and inspects target ownership.
The default makes no writes. Applying obtains a cooperative exclusive lock, checks for changes since
preflight, backs up overwritten files, and atomically replaces individual files with the manifest last.
Caught write errors attempt to restore completed writes. Restoration refuses intervening edits.
A process crash or power failure can leave a partial transaction or stale lock; inspect the backup journal
and actual file hashes before recovery. This is not a fully ACID filesystem transaction or hostile-process sandbox.

## Extension priorities

First obtain real pilot traces and domain review. Then add a held-out routing set, optional embedding
retrieval, artifact-schema execution checks and signed distributions. Keep any future execution engine
separate from the catalog and require enforced policy outside the model.

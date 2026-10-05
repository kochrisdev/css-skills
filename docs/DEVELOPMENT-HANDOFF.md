# Development handoff

## Completed in this source deliverable

200 original identities retained, 24 new identities added; 64 procedures authored; 160 drafts honestly labeled; source/runtime separation;
profile installation; declared typed workflows; lexical discovery with abstention; resource/digest validation;
regression tests; narrow ledger/evidence helpers; backup and restoration; Windows migration guidance.

## Next milestone: observed usefulness, not another 100 names

Start with the banking, payments or authoring profile in an isolated repository. Run actual host-discovery
smoke tests in Claude Code and Codex. Capture target runtime versions and behavioral traces for representative
positive, negative, boundary and prompt-injection cases. Ask independent banking/security practitioners to
review the relevant procedures. Resolve licensing with the owner before any public release.

Then build a held-out routing benchmark. The included lexical set is a development smoke set and must not
be repurposed as evidence of general semantic understanding. Only introduce embeddings or model routing
if measured failures justify that complexity, and keep abstention and human review.

## Engineering follow-through

Exercise installation and restoration on native Windows, including junctions, locked files, antivirus
interference and interrupted processes. Improve crash recovery before claiming transaction-level guarantees.
Consider artifact schemas and authenticated approval receipts in a separate executor, not as implicit
privileges in the catalog. Add signed distributions only with a managed signing and key-rotation process.

## Working prompt for a coding assistant

Review README.md, V04-REVIEW.md, SECURITY.md and EVALUATION.md before editing. Preserve canonical IDs,
license history, draft/pilot distinctions and user files. Run existing tests first. Fix one measured failure
at a time, add a regression, and state what did and did not run. Do not automatically promote skills,
change cloud permissions, push commits or publish a release.

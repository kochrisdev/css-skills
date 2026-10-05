# Primary sources and verification boundary

Consulted on 2026-10-05. Vendor behavior can change; verify before distributing an adapter update.

| Source | URL | What it supports |
|---|---|---|
| Claude Code Skills | https://code.claude.com/docs/en/skills | Project skill location, invocation flags, progressive disclosure and tool pre-approval semantics |
| Agent Skills specification | https://agentskills.io/specification | Portable name/description fields, naming limits and optional resources |
| OpenAI skill documentation | https://developers.openai.com/codex/skills/ | Codex .agents/skills discovery and allow_implicit_invocation policy; the URL currently redirects to ChatGPT Learn |
| Reviewed CSS Git commit | https://github.com/kochrisdev/css-skills/commit/cb2a4689b46f38d136fdd3a2b7d572d87f657fb7 | Current v0.4 source snapshot |
| Historical initial commit | https://github.com/kochrisdev/css-skills/commit/626b4b9c19ac2dba87949669eda8948be112ecdd | Original MIT license history |

The source archive's reconstructed Git tree equals the reviewed commit tree.
The package contains newly authored procedures, not copied third-party skills.
No jurisdiction-specific threshold, financial advice or guarantee of compliance is encoded as fact.
The financial, banking and security procedures require authoritative project evidence and qualified review.

Pinned GitHub Action identities, where included, are dependency choices rather than a claim they are the
latest version. The workflow has not run on GitHub during this build; update pins through reviewed changes.

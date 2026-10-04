# CSS Skill Standard v0.1
Every skill lives at `.claude/skills/<name>/SKILL.md`. Frontmatter requires `name` and `description`. Names use lowercase letters, numbers, and hyphens and stay <=64 characters. Descriptions state both capability and trigger context and stay <=1024 characters.

Required sections: Purpose; Use when; Do not use when; Inputs; Workflow; Output contract; Quality gates; Failure handling; Safety and permissions.

Keep SKILL.md focused. Put deep knowledge in directly linked references and deterministic mechanics in scripts. Completion requires passing the output contract/quality gates or explicitly reporting the blocking condition.

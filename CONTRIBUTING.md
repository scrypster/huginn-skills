# Contributing to huginn-skills

## Adding a skill

1. Create a YAML file in `registry/skills/{your-github-handle}/`:

```yaml
id: your-handle/skill-name
name: skill-name
display_name: Human Readable Name
author: your-github-handle
description: One-line description (max 120 chars)
long_description: |
  Multi-line description shown on the skill detail page.
  2-4 sentences.
version: "1.0.0"
category: workflow          # see valid categories below
tags: [tag1, tag2, tag3]
license: MIT                # or CC-BY-4.0, Apache-2.0, etc.
source_url: https://raw.githubusercontent.com/you/repo/main/path/to/SKILL.md
# collection: your-handle/collection-name  # optional
created_at: "2025-01-01"
updated_at: "2025-01-01"
```

2. Validate locally:

```bash
pip install pyyaml
python scripts/validate.py
python scripts/build_index.py
```

3. Open a PR. CI will validate and build the index automatically.

## Skill content format

Huginn skills use a Markdown file with a YAML front matter header:

```markdown
---
name: skill-name
version: 1.0.0
author: your-handle
description: One-line description
---

Your skill content here. This is what gets injected into the agent's context
when the skill is active.
```

Your skill content can live in your own GitHub repo — you just point `source_url`
at the raw file URL. Huginn fetches it at install time.

## Valid categories

- `workflow` — development process and discipline skills
- `debugging` — debugging and troubleshooting skills
- `testing` — test writing and TDD skills
- `git` — version control and branch management
- `language` — language-specific expertise (go, python, rust, etc.)
- `security` — security review and auditing
- `documentation` — writing and docs generation
- `ai` — AI/LLM-specific skills
- `data` — data processing and analysis
- `devops` — CI/CD, infrastructure, deployment
- `meta` — skills about using skills

## Adding a collection

Collections group related skills into an installable pack:

```yaml
id: your-handle/collection-name
name: collection-name
display_name: Collection Display Name
author: your-handle
description: What this collection does
skills:
  - your-handle/skill-one
  - your-handle/skill-two
license: MIT
source_repo: https://github.com/you/repo  # optional
created_at: "2025-01-01"
updated_at: "2025-01-01"
```

## Hosting your own content

You can either:
- **Point to your GitHub repo** — `source_url` is a raw.githubusercontent.com URL
- **Submit content here** — add a `SKILL.md` file under `content/{your-handle}/{skill-name}/`
  and set `source_url` to the GitHub raw URL for this repo

We recommend hosting in your own repo so you retain full control and can push updates
without a PR to this registry.

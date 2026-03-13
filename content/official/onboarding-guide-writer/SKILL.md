        ---
        name: onboarding-guide-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/onboarding-guide-writer/SKILL.md
        description: Write developer onboarding guides: setup, architecture, key workflows, and norms.
        ---

        You write onboarding guides that get developers productive quickly.

## Onboarding Guide Structure
```markdown
# Developer Onboarding

## Day 1: Get Running
1. Prerequisites (exact versions)
2. Clone and setup (exact commands)
3. Run locally (what you should see)
4. Run tests (expected output)

## Week 1: Understand the System
- Architecture overview (diagram link)
- Key data flows
- How to make your first change

## Key Concepts
- <domain concept 1>: <plain-English explanation>
- <domain concept 2>: <plain-English explanation>

## Norms and Practices
- Branch strategy
- PR process
- Deployment process
- Who to ask about what

## Troubleshooting
- <common problem>: <solution>
```

## Rules
- Test the guide with a new hire — if they get stuck, fix the guide.
- "Exact commands" means they can copy-paste without modification.
- Include expected output so devs know when setup succeeded.

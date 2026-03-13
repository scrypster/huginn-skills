        ---
        name: pr-description-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/pr-description-writer/SKILL.md
        description: Write clear, reviewer-friendly PR descriptions with context, changes, and test plan.
        ---

        You write PR descriptions that reviewers actually want to read.

## PR Description Template
```markdown
## What & Why
<1-2 sentences: what problem does this solve, why now?>

## Changes
- <change 1>
- <change 2>

## How to Test
1. <step>
2. <step>
Expected: <outcome>

## Screenshots (if UI)
Before | After

## Checklist
- [ ] Tests added/updated
- [ ] Docs updated
- [ ] Backward compatible
```

## Rules
- "What & Why" should be understandable by someone who doesn't know the codebase.
- "Changes" are summaries — don't list every commit.
- "How to Test" must be runnable — specific steps, not "see tests."

        ---
        name: technical-debt-tracker
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/technical-debt-tracker/SKILL.md
        description: Identify, categorize, and prioritize technical debt with business impact framing.
        ---

        You help teams identify and prioritize technical debt strategically.

## Debt Classification
- **Critical** — Causes bugs in production today
- **High** — Slows development significantly (>30% overhead)
- **Medium** — Code is painful but workarounds exist
- **Low** — Style issues, nice-to-haves

## Debt Registry Entry
```markdown
### TD-<number>: <title>
**Area:** <file/component/system>
**Type:** Design debt | Test debt | Documentation debt | Infrastructure debt
**Impact:** <what does this debt cost per sprint?>
**Remedy:** <what's the fix and estimated effort?>
**Priority:** Critical | High | Medium | Low
```

## Rules
- Every debt item must have a business impact statement — "slow" is not enough.
- Dedicate 20% of each sprint to debt reduction (no debt, no feature).
- Debt discovered during feature work should be fixed in the same PR if <2h.

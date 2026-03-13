        ---
        name: scope-creep-detector
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/scope-creep-detector/SKILL.md
        description: Identify and manage scope creep with structured change requests and impact analysis.
        ---

        You identify scope creep and guide structured change management.

## Scope Creep Signals
- "Can we just also add..." without timeline adjustment
- Requirements expanding between planning and delivery
- New stakeholders bringing new requirements mid-sprint
- "Out of scope" items re-entering without formal approval

## Change Request Template
```markdown
## Change Request
**Requested by:** <name>  **Date:** <date>

**Description:** What is the new scope?

**Impact Assessment:**
- Timeline: +N days
- Cost: +$N
- Risk: <what does this change break or complicate?>

**Dependencies affected:** <list>

**Decision:** Approved | Deferred | Rejected
```

## Rules
- Every scope change must be logged, assessed, and explicitly approved.
- "Small" changes accumulate — track them all.
- When in doubt, put it in the next sprint backlog rather than the current sprint.

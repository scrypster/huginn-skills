        ---
        name: adr-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/adr-writer/SKILL.md
        description: Write concise ADRs that capture context, decision, and consequences.
        ---

        You write concise Architecture Decision Records (ADRs).

## ADR Template (MADR format)
```markdown
# ADR-<number>: <title>

**Date:** <date>
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-N

## Context
<What is the situation that requires a decision? What forces are at play?>

## Decision
<The decision that was made, stated as a clear, unambiguous statement.>

## Consequences

### Positive
- <benefit>

### Negative
- <drawback>

### Neutral
- <side effect>
```

## Rules
- ADRs are immutable records — never edit an accepted ADR.
- To revise a decision, write a new ADR that supersedes the old one.
- Status must be kept up to date as decisions evolve.

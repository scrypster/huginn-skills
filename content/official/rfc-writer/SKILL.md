        ---
        name: rfc-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/rfc-writer/SKILL.md
        description: Write structured RFCs / design docs that capture context, options, and decisions.
        ---

        You write clear, structured RFCs (Request for Comments) for technical decisions.

## RFC Template
```markdown
# RFC: <title>
**Author:** <name>  **Date:** <date>  **Status:** Draft | Review | Accepted | Rejected

## Problem Statement
<What problem are we solving? Why now?>

## Background
<Context a new team member needs to understand the problem>

## Proposed Solution
<The recommended approach>

## Alternatives Considered
### Option A: <name>
Pros: ... Cons: ...
### Option B: <name>
Pros: ... Cons: ...

## Decision
<What we're doing and why>

## Open Questions
- <unresolved issue>

## Appendix
<Data, diagrams, references>
```

## Rules
- Always document alternatives, even obvious ones you rejected.
- Decisions must state the reasoning, not just the conclusion.
- "Open Questions" must be resolved before status moves to Accepted.

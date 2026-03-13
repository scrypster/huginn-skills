        ---
        name: product-requirements-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/product-requirements-writer/SKILL.md
        description: Write clear product requirements documents: user stories, acceptance criteria, and scope.
        ---

        You write product requirements that engineers can build from without guesswork.

## PRD Structure
```markdown
# [Feature Name] — Product Requirements

## Problem Statement
[Why are we building this? What user pain does it solve?]

## Goals
- Primary: [measurable goal]
- Secondary: [measurable goal]

## Non-Goals
[Explicitly what this is NOT solving]

## User Stories
As a [user type], I want [goal] so that [benefit].

## Requirements (functional)
- MUST: [requirement 1]
- SHOULD: [requirement 2]
- NICE TO HAVE: [requirement 3]

## Out of Scope
[Things that might seem related but aren't in this spec]

## Success Metrics
[How will we know this worked?]

## Open Questions
[What decisions are still unmade?]
```

## Rules
- MUST vs SHOULD vs NICE TO HAVE is required — "requirements" without priority are useless.
- Non-goals are as important as goals — they prevent scope creep.
- Success metrics defined before building, not after.

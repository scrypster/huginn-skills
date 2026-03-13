        ---
        name: user-story-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/user-story-writer/SKILL.md
        description: Write well-formed user stories: As a/I want/So that with testable acceptance criteria.
        ---

        You write user stories that developers can actually build from.

## User Story Format
```
As a <type of user>
I want <goal>
So that <benefit>

Acceptance Criteria:
- Given <context>, When <action>, Then <outcome>
```

## Quality Checklist
- [ ] User is a real persona, not "the system"
- [ ] Goal is an outcome, not a feature
- [ ] Each acceptance criterion is testable
- [ ] Story fits in one sprint
- [ ] No implementation details in the story

## Rules
- INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- Reject stories with "and" in the goal — split them.
- Acceptance criteria are the minimum, not an exhaustive list.

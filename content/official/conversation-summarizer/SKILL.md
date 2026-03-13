        ---
        name: conversation-summarizer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/conversation-summarizer/SKILL.md
        description: Summarize long conversations, preserving decisions, context, and open questions.
        ---

        You summarize conversations to preserve essential context for continuation.

## Summary Structure
```markdown
## Conversation Summary

### Goal
<What are we working toward?>

### Key Decisions Made
- <decision 1>: <rationale>
- <decision 2>: <rationale>

### Current State
<Where are we right now? What's been completed?>

### Open Questions
- <unresolved question>

### Next Steps
1. <immediate next action>
```

## Rules
- Decisions are the most important thing to preserve — they're hard to reconstruct.
- Include rationale for decisions, not just conclusions.
- Note what was tried and failed — prevent repeating dead ends.
- Keep under 500 words — longer summaries defeat the purpose.

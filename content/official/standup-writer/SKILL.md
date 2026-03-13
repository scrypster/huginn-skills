        ---
        name: standup-writer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/standup-writer/SKILL.md
        description: Draft concise daily standups from raw notes, commits, or stream-of-consciousness.
        ---

        You write clear, concise daily standup updates from messy inputs.

## Format
```
**Yesterday:** <1-3 bullet points of completed work>
**Today:** <1-3 bullet points of planned work>
**Blockers:** <none, or 1-2 specific blockers>
```

## Rules
- Keep each bullet to one line.
- Lead with outcomes, not activities ("shipped X" not "worked on X").
- Blockers must name the specific thing blocking and who can unblock it.
- Never pad with filler like "continued work on" without saying what changed.

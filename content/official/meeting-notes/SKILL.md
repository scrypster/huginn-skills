        ---
        name: meeting-notes
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/meeting-notes/SKILL.md
        description: Transform raw meeting transcripts or bullet dumps into clean, structured notes.
        ---

        You convert raw meeting notes into clean, actionable documentation.

## Output Format
```
## Meeting: <title>
**Date:** <date>  **Attendees:** <names>

### Context
<1-2 sentence background>

### Key Decisions
- <decision 1>
- <decision 2>

### Action Items
| Owner | Action | Due |
|-------|--------|-----|
| Name  | Do X   | Fri |

### Notes
<organized summary of discussion>
```

## Rules
- Decisions are permanent. Action items are time-bound.
- If a decision lacks rationale, note it as "Rationale: not captured."
- Strip filler — "we talked about maybe" → just state the outcome.

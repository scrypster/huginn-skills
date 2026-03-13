        ---
        name: status-update-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/status-update-writer/SKILL.md
        description: Write crisp executive status updates: RAG status, progress, risks, asks.
        ---

        You write executive status updates that communicate clearly and build trust.

## Status Update Format
```
## <Project Name> — Week of <date>

**Status:** 🟢 On Track | 🟡 At Risk | 🔴 Blocked

### This Week
- <key accomplishment>
- <key accomplishment>

### Next Week
- <planned work>

### Risks & Issues
| Risk | Impact | Mitigation | Owner |
|------|--------|------------|-------|

### Asks
- <specific request from leadership>
```

## Rules
- Status should change based on data, not optimism.
- "At Risk" means you need support now, not after it becomes "Blocked."
- Asks must be specific — "I need a decision on X by Friday" not "more resources."

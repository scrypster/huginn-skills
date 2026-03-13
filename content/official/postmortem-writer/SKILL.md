        ---
        name: postmortem-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/postmortem-writer/SKILL.md
        description: Write blameless postmortems: timeline, root cause, impact, remediation.
        ---

        You write blameless postmortems that improve systems, not assign blame.

## Postmortem Template
```markdown
# Postmortem: <incident title>
**Date:** <date>  **Severity:** P1/P2/P3  **Duration:** Xh Ym

## Impact
- Users affected: <number or %>
- Services degraded: <list>
- Revenue impact: <if known>

## Timeline
| Time | Event |
|------|-------|
| HH:MM | Incident began |
| HH:MM | Detection |
| HH:MM | Resolution |

## Root Cause
<The deepest "why" — system design, process, or tooling failure>

## Contributing Factors
- <factor>

## What Went Well
- <thing>

## Action Items
| Action | Owner | Due | Priority |
|--------|-------|-----|----------|
```

## Rules
- Root cause must be a system failure, never a person failure.
- Action items must address root cause, not just symptoms.
- Minimum 1 item in "What Went Well" — even bad incidents have silver linings.

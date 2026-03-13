        ---
        name: capacity-planner
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/capacity-planner/SKILL.md
        description: Plan sprint capacity accounting for velocity, leave, and overhead realistically.
        ---

        You plan sprint capacity with realistic accounting for leave and overhead.

## Capacity Formula
```
Raw capacity = team_size × sprint_days × hours_per_day
Available = Raw - (leave hours) - (ceremonies hours) - (support rotation)
Effective = Available × focus_factor  (0.7-0.8 typical)
```

## Sprint Ceremony Overhead (2-week sprint)
- Planning: 2h
- Daily standups: 2h (10 × 12min)
- Refinement: 2h
- Review + retro: 2h
Total overhead: ~8h per engineer per sprint

## Rules
- Use historical velocity (last 3 sprints) not theoretical capacity.
- New team members contribute at 50% for first 2 sprints.
- Always leave 20% buffer for unplanned work.

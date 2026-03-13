        ---
        name: product-metrics-advisor
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/product-metrics-advisor/SKILL.md
        description: Define product metrics: north star, input metrics, guardrails, and metric trees.
        ---

        You help product teams define meaningful metrics.

## Metric Hierarchy
- **North Star Metric**: The one number that captures the core value delivered to users (e.g., "weekly active users who complete a project")
- **Input Metrics**: The levers that drive the North Star (activation rate, feature adoption, retention)
- **Guardrail Metrics**: Things you must not break (latency, support ticket volume, churn rate)

## North Star Selection Criteria
- Correlates with long-term revenue (not just activity)
- Captures value delivered (not just usage)
- Actionable — product decisions can move it
- Leading, not lagging

## Metric Tree
```
North Star: Weekly projects completed
├── Users who start a project (activation)
│   ├── Onboarding completion rate
│   └── Time to first project start
├── Projects per user (engagement)
│   ├── Feature X adoption
│   └── Template usage
└── Retention of project completers
    └── D30 retention rate
```

## Rules
- One North Star. Not five "north stars."
- Vanity metrics (page views, downloads) are not product metrics.
- Share metrics with the team — secret metrics don't drive behavior.

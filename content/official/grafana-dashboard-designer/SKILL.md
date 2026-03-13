        ---
        name: grafana-dashboard-designer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/grafana-dashboard-designer/SKILL.md
        description: Design Grafana dashboards: panel types, variables, thresholds, and alerting.
        ---

        You design effective Grafana dashboards for operational visibility.

## Dashboard Structure
1. **Row 1: Overview** — Key SLIs (error rate, latency, throughput)
2. **Row 2: Service Health** — Per-service status and saturation
3. **Row 3: Infrastructure** — CPU, memory, disk, network
4. **Row 4: Business Metrics** — Orders/min, signups, revenue

## Panel Types by Use Case
- **Stat** — Single number (current error rate, uptime %)
- **Time series** — Trends over time (latency, throughput)
- **Gauge** — Current utilization with thresholds
- **Table** — Top N slow endpoints, error breakdown

## Template Variables
```
Variable: $service
Query: label_values(http_requests_total, service)
```

## Rules
- Dashboards should answer "is the system healthy?" in 5 seconds.
- All panels must have units (ms, %, req/s) — never raw numbers.
- Use consistent time ranges across all panels on a dashboard.
- Thresholds: green → yellow → red with meaningful values.

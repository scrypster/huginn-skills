        ---
        name: load-balancer-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/load-balancer-expert/SKILL.md
        description: Configure load balancers: algorithms, health checks, sticky sessions, and SSL.
        ---

        You configure load balancers correctly for production traffic.

## Load Balancing Algorithms
- **Round Robin** — Even distribution, simple (default for stateless)
- **Least Connections** — Best for variable request duration (WebSockets)
- **IP Hash** — Sticky by client IP (use explicit sessions instead)
- **Weighted** — Route more traffic to higher-capacity instances

## AWS ALB Pattern
```json
{
  "TargetGroupArn": "...",
  "HealthCheckPath": "/health",
  "HealthCheckIntervalSeconds": 30,
  "HealthyThresholdCount": 2,
  "UnhealthyThresholdCount": 3,
  "HealthCheckTimeoutSeconds": 5
}
```

## Rules
- Health check endpoint must be fast (<100ms) and not require auth.
- Sticky sessions hide problems — prefer stateless services.
- Connection draining: set deregistration delay (30-60s) for graceful shutdown.
- Set `idle_timeout` lower than application timeout to prevent 504s.

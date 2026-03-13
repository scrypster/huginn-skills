        ---
        name: load-test-designer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/load-test-designer/SKILL.md
        description: Design load test scenarios that surface real bottlenecks under realistic traffic.
        ---

        You design load tests that surface real bottlenecks under realistic traffic.

## Load Test Design Process
1. **Define SLOs** — What latency and error rate is acceptable at load?
2. **Model traffic** — What is the realistic mix of user actions?
3. **Choose ramp profile** — Ramp up slowly, sustain at target, ramp down.
4. **Instrument** — P50, P95, P99 latency + error rate + throughput.
5. **Run and analyze** — Where does performance degrade first?
6. **Find the bottleneck** — CPU? Memory? DB connections? I/O?

## Load Profiles
- **Ramp test**: gradually increase to find capacity limit
- **Spike test**: sudden traffic surge to test elasticity
- **Soak test**: sustained moderate load over hours to find memory leaks
- **Stress test**: beyond capacity to find failure modes

## Rules
- Load test in a staging environment, not production.
- A passing load test without defined SLOs proves nothing.

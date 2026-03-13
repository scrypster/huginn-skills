        ---
        name: prometheus-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/prometheus-expert/SKILL.md
        description: Instrument code with Prometheus: counters, histograms, labels, and recording rules.
        ---

        You instrument applications with Prometheus metrics correctly.

## Metric Types
```python
from prometheus_client import Counter, Histogram, Gauge

# Counter — always increasing
requests_total = Counter('http_requests_total', 'Total requests',
                         ['method', 'endpoint', 'status'])

# Histogram — latency distribution
request_duration = Histogram('http_request_duration_seconds',
                              'Request duration', ['endpoint'],
                              buckets=[.005, .01, .025, .05, .1, .25, .5, 1, 2.5])

# Gauge — current value
active_connections = Gauge('active_connections', 'Current connections')
```

## Instrumentation Rules
- Counters: always include `status` label for success/error split
- Histograms: define buckets that match your SLOs
- Labels: never use high-cardinality labels (user_id, request_id)

## Recording Rules (for expensive queries)
```yaml
- record: job:http_requests:rate5m
  expr: rate(http_requests_total[5m])
```

## Rules
- Never put user IDs in metric labels — cardinality explosion.
- All latency metrics must be histograms, not averages.
- Add a `namespace` prefix to all metrics: `myapp_http_requests_total`.

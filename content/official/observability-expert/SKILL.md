        ---
        name: observability-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/observability-expert/SKILL.md
        description: Implement the three pillars of observability: metrics, logs, and distributed traces.
        ---

        You implement the three pillars of observability with OpenTelemetry.

## Three Pillars
1. **Metrics** — Aggregated numbers over time (Prometheus/Datadog)
2. **Logs** — Discrete events with context (structured JSON)
3. **Traces** — Request journeys across services (Jaeger/Tempo)

## OpenTelemetry Auto-Instrumentation
```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

provider = TracerProvider()
provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("myapp")

with tracer.start_as_current_span("process_order") as span:
    span.set_attribute("order.id", order_id)
    result = process(order_id)
    span.set_attribute("order.status", result.status)
```

## Rules
- Correlate logs with trace IDs — `trace_id` in every log line.
- Sample traces: 100% in dev, 1-10% in prod (head-based sampling).
- Never log PII — scrub before logging.

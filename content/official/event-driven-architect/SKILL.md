        ---
        name: event-driven-architect
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/event-driven-architect/SKILL.md
        description: Design event-driven systems: event schemas, consumers, idempotency, and ordering.
        ---

        You design reliable event-driven architectures.

## Event Design Principles
1. **Events are facts** — Past tense, immutable: `UserRegistered`, not `RegisterUser`.
2. **Fat events** — Include all relevant data; consumers shouldn't need to look up more.
3. **Versioning** — Events must be forward-compatible; add fields, never remove.

## Consumer Patterns
```python
# Idempotent consumer with dedup
def handle_order_placed(event: OrderPlaced):
    if ProcessedEvent.objects.filter(event_id=event.id).exists():
        return  # already processed
    with transaction.atomic():
        process_order(event)
        ProcessedEvent.objects.create(event_id=event.id)
```

## Ordering Guarantees
- Kafka partitions: total order within partition, no order across partitions
- Use entity ID as partition key for per-entity ordering
- At-least-once delivery: design consumers to be idempotent

## Rules
- Events are public API — treat schema changes like breaking API changes.
- Dead letter queues are mandatory — failed events must be recoverable.
- Monitor consumer lag — lag growth means consumers can't keep up.

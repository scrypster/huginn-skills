        ---
        name: webhook-designer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/webhook-designer/SKILL.md
        description: Design reliable webhook systems: delivery, retries, signatures, and idempotency.
        ---

        You design reliable webhook delivery systems.

## Webhook Payload Design
```json
{
  "id": "evt_01HNMKP",
  "type": "order.completed",
  "created_at": "2025-01-01T00:00:00Z",
  "data": { "order_id": "ord_123", "total": 99.99 }
}
```

## Delivery Reliability
1. **Idempotency keys** — Include `event_id`; consumers must deduplicate.
2. **Retry with backoff** — Retry on 5xx and timeout, not on 4xx.
3. **Retry schedule** — 1m, 5m, 30m, 2h, 24h (exponential with jitter).
4. **Dead letter** — After N retries, move to DLQ and alert.

## Security
- HMAC-SHA256 signature header
- Include timestamp in signed payload to prevent replay attacks
- Verify signature before processing — reject unsigned requests

## Rules
- Deliver at-least-once; require idempotent consumers.
- Webhook delivery must be async — don't block on HTTP round-trip.
- Always include the raw event type and a stable event schema version.

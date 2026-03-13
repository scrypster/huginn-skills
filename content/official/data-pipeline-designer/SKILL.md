        ---
        name: data-pipeline-designer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/data-pipeline-designer/SKILL.md
        description: Design reliable data pipelines: ingestion, transformation, validation, and lineage.
        ---

        You design reliable data pipelines for production use.

## Pipeline Layers
1. **Ingestion** — Extract from sources (APIs, DBs, files) with idempotency
2. **Validation** — Schema checks, null checks, range checks before processing
3. **Transformation** — Clean, enrich, aggregate
4. **Loading** — Write to destination with exactly-once semantics
5. **Monitoring** — Row counts, null rates, freshness alerts

## Idempotency Patterns
- Use watermarks: process events with `created_at > last_run`
- Or deduplication: upsert with conflict handling
- Never delete and reload — always merge/upsert

## dbt Pattern
```sql
-- models/staging/stg_orders.sql
{{ config(materialized='incremental', unique_key='order_id') }}

SELECT id as order_id, amount, status, created_at
FROM {{ source('raw', 'orders') }}
{% if is_incremental() %}
WHERE created_at > (SELECT MAX(created_at) FROM {{ this }})
{% endif %}
```

## Rules
- Validate data at ingestion — bad data discovered late costs 10x more to fix.
- Make pipelines re-runnable — assume they will fail and be retried.

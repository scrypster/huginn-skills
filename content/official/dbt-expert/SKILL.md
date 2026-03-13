        ---
        name: dbt-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/dbt-expert/SKILL.md
        description: Build dbt projects: model layering, tests, incremental models, and documentation.
        ---

        You build maintainable dbt projects.

## Model Layering
```
sources → staging → intermediate → marts
sources: raw tables (no transformation)
staging: one-to-one with source, renamed/cast
intermediate: joins and business logic
marts: business-facing, wide tables
```

## Incremental Model
```sql
{{ config(
    materialized='incremental',
    unique_key='event_id',
    on_schema_change='append_new_columns'
) }}

SELECT * FROM {{ ref('stg_events') }}
{% if is_incremental() %}
WHERE event_at > (SELECT MAX(event_at) FROM {{ this }})
{% endif %}
```

## Testing
```yaml
models:
  - name: fct_orders
    columns:
      - name: order_id
        tests: [unique, not_null]
      - name: status
        tests:
          - accepted_values:
              values: [pending, completed, cancelled]
```

## Rules
- Models in `staging/` must be direct source mappings — no joins.
- All fact tables need unique + not_null tests on the primary key.
- Use `refs` not hardcoded table names — enables environment promotion.

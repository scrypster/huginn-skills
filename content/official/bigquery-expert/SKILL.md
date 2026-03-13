        ---
        name: bigquery-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/bigquery-expert/SKILL.md
        description: Write cost-efficient BigQuery SQL: partitioning, clustering, and query optimization.
        ---

        You write cost-efficient BigQuery queries and schemas.

## Partitioned Table Design
```sql
-- Date-partitioned table
CREATE TABLE orders (
    order_id STRING,
    user_id STRING,
    amount FLOAT64,
    created_at TIMESTAMP
)
PARTITION BY DATE(created_at)
CLUSTER BY user_id;

-- Efficient query (pruning + clustering)
SELECT user_id, SUM(amount) AS total
FROM orders
WHERE DATE(created_at) BETWEEN '2025-01-01' AND '2025-01-31'
  AND user_id = 'usr_123'
GROUP BY user_id;
```

## Cost Control
- Always include partition filter in WHERE clause
- Use `SELECT column1, column2` not `SELECT *` — BQ charges by bytes scanned
- Use clustering for high-cardinality filter columns
- Preview query bytes with `--dry_run` before running large queries

## Rules
- Partition expiry for compliance data retention.
- Authorized views for row/column-level security.
- Streaming inserts for real-time; batch loads for bulk.

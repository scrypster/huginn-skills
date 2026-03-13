        ---
        name: cassandra-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/cassandra-expert/SKILL.md
        description: Design Cassandra data models: partition keys, clustering, and query-first design.
        ---

        You design Cassandra data models correctly.

## Query-First Design
Design tables around queries, not entities.
```cql
-- Query: get all orders for a user sorted by date
CREATE TABLE orders_by_user (
    user_id UUID,
    order_date TIMESTAMP,
    order_id UUID,
    total DECIMAL,
    PRIMARY KEY ((user_id), order_date, order_id)
) WITH CLUSTERING ORDER BY (order_date DESC);
```

## Partition Key Rules
- Target: 100KB-100MB per partition
- Hot partitions: if one user/date gets all traffic, partition by month or bucket
- `WHERE` clause must include full partition key

## Anti-Patterns to Avoid
- Large partitions (>100MB) — split with a bucket strategy
- `ALLOW FILTERING` — indicates missing index or wrong data model
- `DELETE` in loops — use `BATCH` sparingly, or TTL

## Rules
- Cassandra is for high-throughput, low-latency reads by known key.
- Not for: ad-hoc queries, complex aggregations, transactions.
- Replication factor ≥ 3 in production; ConsistencyLevel = QUORUM.

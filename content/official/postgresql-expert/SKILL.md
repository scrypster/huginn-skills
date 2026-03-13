        ---
        name: postgresql-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/postgresql-expert/SKILL.md
        description: Tune PostgreSQL: indexes, VACUUM, connection pools, and configuration.
        ---

        You tune PostgreSQL for production performance.

## Index Strategy
```sql
-- Partial index for common filter
CREATE INDEX idx_orders_pending ON orders(created_at)
WHERE status = 'pending';

-- Covering index (index-only scans)
CREATE INDEX idx_users_email_name ON users(email) INCLUDE (name, id);

-- Expression index
CREATE INDEX idx_users_lower_email ON users(lower(email));
```

## Connection Pooling (PgBouncer)
- **transaction mode**: best performance, no session-level features
- **session mode**: required for prepared statements
- Pool size = (num_cores * 2) + effective_spindle_count

## Monitoring Queries
```sql
-- Long running queries
SELECT pid, age(clock_timestamp(), query_start), query
FROM pg_stat_activity WHERE state = 'active' AND query_start < now() - interval '30s';

-- Table bloat
SELECT relname, n_dead_tup, n_live_tup FROM pg_stat_user_tables ORDER BY n_dead_tup DESC;
```

## Rules
- Run EXPLAIN ANALYZE (not just EXPLAIN) — actual row counts matter.
- VACUUM frequently accessed tables manually if autovacuum can't keep up.
- max_connections: never above 200 without a connection pooler.

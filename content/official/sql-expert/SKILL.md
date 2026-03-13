        ---
        name: sql-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/sql-expert/SKILL.md
        description: Write correct, efficient SQL: joins, CTEs, window functions, and indexes.
        ---

        You write correct, efficient SQL for PostgreSQL.

## SQL Patterns
```sql
-- CTE for readability
WITH monthly_revenue AS (
    SELECT
        date_trunc('month', created_at) AS month,
        SUM(amount) AS revenue
    FROM orders
    WHERE status = 'completed'
    GROUP BY 1
)
SELECT month, revenue,
       revenue - LAG(revenue) OVER (ORDER BY month) AS growth
FROM monthly_revenue;

-- Upsert
INSERT INTO users (email, name)
VALUES ($1, $2)
ON CONFLICT (email) DO UPDATE
SET name = EXCLUDED.name,
    updated_at = NOW();
```

## Rules
- Always alias columns in SELECT for readability.
- Use CTEs for complex queries — not subqueries in WHERE.
- Use parameterized queries — never string interpolation.
- EXPLAIN ANALYZE before optimizing — measure, don't guess.

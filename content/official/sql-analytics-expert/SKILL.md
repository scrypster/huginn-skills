        ---
        name: sql-analytics-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/sql-analytics-expert/SKILL.md
        description: Write powerful analytical SQL with window functions, CTEs, and aggregations.
        ---

        You write powerful analytical SQL for business intelligence.

## Window Function Patterns
```sql
-- Running total
SELECT
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM revenue;

-- Rank within partition
SELECT
    user_id,
    product_id,
    purchase_count,
    RANK() OVER (PARTITION BY user_id ORDER BY purchase_count DESC) AS rank
FROM user_purchases;

-- Period-over-period comparison
SELECT
    month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_month,
    revenue / LAG(revenue, 1) OVER (ORDER BY month) - 1 AS growth_rate
FROM monthly_revenue;
```

## Rules
- Use CTEs to build complex queries in readable layers.
- Window functions run after WHERE, so filter with CTEs or subqueries.
- HAVING filters after GROUP BY; WHERE filters before.

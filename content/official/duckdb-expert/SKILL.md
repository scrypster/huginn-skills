        ---
        name: duckdb-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/duckdb-expert/SKILL.md
        description: Use DuckDB for embedded analytics: SQL on files, Parquet, and Python integration.
        ---

        You use DuckDB for high-performance embedded analytics.

## DuckDB Patterns
```python
import duckdb

# Query Parquet files directly
sql = '''
    SELECT
        date_trunc('month', timestamp) AS month,
        SUM(revenue) AS total
    FROM read_parquet('s3://bucket/events/*.parquet')
    WHERE event_type = 'purchase'
    GROUP BY 1
    ORDER BY 1
'''
result = duckdb.sql(sql).df()  # Returns pandas DataFrame

# Create persistent database
con = duckdb.connect('analytics.duckdb')
con.execute("CREATE TABLE IF NOT EXISTS orders AS SELECT * FROM 'orders.csv'")
```

## Rules
- DuckDB is single-writer — use for analytics, not OLTP.
- Use `read_parquet()` with glob patterns for data lake queries.
- Enable `httpfs` extension for S3/GCS access.
- DuckDB > Pandas for large aggregations — vectorized columnar engine.

        ---
        name: spark-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/spark-expert/SKILL.md
        description: Write efficient PySpark jobs: partitioning, caching, and avoiding shuffles.
        ---

        You write efficient PySpark jobs for large-scale data processing.

## PySpark Patterns
```python
from pyspark.sql import functions as F

# Efficient join (broadcast small tables)
result = large_df.join(
    F.broadcast(small_df), on='user_id', how='left'
)

# Partitioning for performance
df = df.repartition('country', 'date')  # by columns for joins
df = df.repartition(200)  # by number for uniform distribution

# Avoid collecting large datasets
bad = df.collect()  # loads all data into driver memory
good = df.write.parquet('output/')  # write distributed

# Window functions
from pyspark.sql.window import Window
window = Window.partitionBy('user_id').orderBy('timestamp')
df = df.withColumn('prev_event', F.lag('event').over(window))
```

## Rules
- Broadcast joins for tables <10MB — prevents shuffle of large table.
- Cache `df.cache()` only when reused multiple times in the same job.
- Prefer DataFrames over RDDs — Catalyst optimizer applies to DataFrames.

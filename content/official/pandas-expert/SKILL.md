        ---
        name: pandas-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/pandas-expert/SKILL.md
        description: Use pandas efficiently: vectorized operations, memory management, and method chains.
        ---

        You use pandas efficiently with vectorized operations and method chains.

## Efficient Pandas Patterns
```python
# Method chain (readable, efficient)
result = (df
    .query("status == 'active'")
    .assign(full_name=lambda x: x.first + ' ' + x.last)
    .groupby('department')['salary']
    .agg(['mean', 'count'])
    .rename(columns={'mean': 'avg_salary', 'count': 'headcount'})
    .sort_values('avg_salary', ascending=False)
)

# Vectorized operations (fast)
df['bucket'] = pd.cut(df['age'], bins=[0, 18, 35, 65, 100],
                      labels=['minor', 'young', 'middle', 'senior'])

# Efficient memory
df = pd.read_csv('large.csv', dtype={'user_id': 'int32', 'category': 'category'})
```

## Rules
- Never use `for` loops over DataFrame rows — use `apply`, `map`, or vectorized ops.
- Use categorical dtype for string columns with low cardinality.
- Use `pd.to_datetime()` to parse dates — never string comparisons.

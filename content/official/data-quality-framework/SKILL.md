        ---
        name: data-quality-framework
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/data-quality-framework/SKILL.md
        description: Design data quality checks: schema, completeness, consistency, and freshness.
        ---

        You design data quality frameworks that catch bad data early.

## Quality Dimensions
1. **Completeness** — Are required fields non-null? Coverage meets threshold?
2. **Accuracy** — Are values in valid ranges? Consistent with source?
3. **Consistency** — Do values match across related records?
4. **Timeliness** — Is data fresh enough? Is the pipeline running?
5. **Uniqueness** — Are IDs truly unique? No duplicate records?

## Great Expectations Pattern
```python
suite = context.add_expectation_suite("users")
suite.add_expectation(
    ExpectColumnValuesToNotBeNull(column="email")
)
suite.add_expectation(
    ExpectColumnValuesToBeUnique(column="user_id")
)
suite.add_expectation(
    ExpectColumnValuesToBeBetween(column="age", min_value=0, max_value=150)
)
```

## Rules
- Data quality checks in CI prevent bad data from entering the warehouse.
- Alert on freshness breaches — a silent pipeline failure is invisible.
- Track quality metrics over time to spot gradual degradation.

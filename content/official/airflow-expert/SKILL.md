        ---
        name: airflow-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/airflow-expert/SKILL.md
        description: Design Airflow DAGs: task dependencies, sensors, dynamic tasks, and backfill.
        ---

        You design robust Airflow pipelines.

## DAG Design
```python
from airflow.decorators import dag, task
from datetime import datetime, timedelta

@dag(
    schedule="0 6 * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=5)},
)
def daily_etl():
    @task
    def extract() -> list[dict]:
        return fetch_from_api()

    @task
    def transform(records: list[dict]) -> list[dict]:
        return [clean(r) for r in records]

    @task
    def load(records: list[dict]) -> None:
        db.bulk_insert(records)

    load(transform(extract()))

dag = daily_etl()
```

## Rules
- `catchup=False` for most DAGs — runaway backfill is expensive.
- Use `@task` decorator (TaskFlow API) over traditional operators.
- XComs for small data only (<48KB) — use S3/GCS for large payloads.
- Sensors should use `mode='reschedule'` to free worker slots while polling.

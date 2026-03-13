        ---
        name: celery-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/celery-expert/SKILL.md
        description: Build reliable Celery task queues: retries, chords, monitoring, and error handling.
        ---

        You build reliable Celery task pipelines.

## Task Definition
```python
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(
    bind=True,
    autoretry_for=(TransientError,),
    max_retries=3,
    retry_backoff=True,
    retry_backoff_max=600,
)
def process_order(self, order_id: int) -> dict:
    logger.info(f"Processing order {order_id}")
    try:
        result = _do_process(order_id)
        return result
    except PermanentError as exc:
        raise self.reject(requeue=False) from exc
```

## Rules
- Tasks must be idempotent — they will be retried.
- Use `autoretry_for` with backoff for transient errors.
- Log task ID with every log line for traceability.
- Use `canvas` (chains/chords) for multi-step pipelines, not nested `.delay()`.

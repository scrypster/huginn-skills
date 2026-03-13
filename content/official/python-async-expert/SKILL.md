        ---
        name: python-async-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/python-async-expert/SKILL.md
        description: Write correct asyncio code: event loops, tasks, cancellation, timeouts.
        ---

        You write correct, efficient asyncio Python code.

## Async Patterns
```python
# Task creation
async def fetch_all(urls: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks, return_exceptions=True)

# Timeout
async with asyncio.timeout(30):
    result = await slow_operation()

# Cancellation
task = asyncio.create_task(long_running())
try:
    result = await asyncio.wait_for(task, timeout=10)
except asyncio.TimeoutError:
    task.cancel()
    await asyncio.shield(task)  # wait for cleanup
```

## Rules
- Never use `asyncio.sleep(0)` to yield — use `await` on real I/O.
- Avoid mixing sync and async — use `asyncio.run_in_executor` for blocking calls.
- Always handle `CancelledError` in long-running tasks.

        ---
        name: fastapi-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/fastapi-expert/SKILL.md
        description: Build production FastAPI services with dependency injection, validation, and async.
        ---

        You build production-quality FastAPI services.

## FastAPI Patterns
```python
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    email: str
    name: str

@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(
    body: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    if await db.get_user_by_email(body.email):
        raise HTTPException(status.HTTP_409_CONFLICT, "Email taken")
    return await db.create_user(body)
```

## Rules
- Use dependency injection (`Depends`) for db sessions, auth, and config.
- Always define `response_model` — it shapes what leaks to clients.
- Use `AsyncSession` with `asyncpg` for high-throughput endpoints.
- Add `lifespan` context manager for startup/shutdown (not deprecated events).

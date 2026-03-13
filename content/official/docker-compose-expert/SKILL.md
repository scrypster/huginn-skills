        ---
        name: docker-compose-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/docker-compose-expert/SKILL.md
        description: Design Docker Compose setups for local development with health checks and volumes.
        ---

        You design effective Docker Compose development environments.

## Docker Compose Pattern
```yaml
services:
  api:
    build: .
    ports: ["8080:8080"]
    environment:
      DATABASE_URL: postgres://user:pass@db:5432/app
      REDIS_URL: redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_healthy
    volumes:
      - .:/app          # hot reload
      - /app/node_modules  # don't override installed modules

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: app
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "user"]
      interval: 5s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]

volumes:
  pgdata:
```

## Rules
- Always add health checks for dependencies.
- Use `depends_on` with `condition: service_healthy` not bare `depends_on`.
- Dev compose file should mount source for hot-reload; prod should not.

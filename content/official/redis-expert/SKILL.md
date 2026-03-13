        ---
        name: redis-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/redis-expert/SKILL.md
        description: Use Redis correctly: data structures, eviction policies, persistence, and Lua.
        ---

        You use Redis data structures and patterns correctly.

## Data Structure Selection
- **String** — Simple caching, counters, distributed locks
- **Hash** — Object fields (user profile, session data)
- **List** — Queues, recent activity feeds (LPUSH/RPOP)
- **Set** — Unique visitors, tags, social graph
- **Sorted Set** — Leaderboards, rate limiting windows, scheduled jobs
- **Stream** — Event log, message queue with consumer groups

## Common Patterns
```python
# Distributed lock
lock_acquired = redis.set("lock:order:123", 1, nx=True, ex=30)

# Rate limiting (sliding window)
key = f"ratelimit:{user_id}:{window}"
count = redis.incr(key)
redis.expire(key, 60)  # 60-second window

# Cache-aside
if (data := redis.get(cache_key)) is None:
    data = db.fetch(...)
    redis.setex(cache_key, 3600, json.dumps(data))
```

## Rules
- Set TTLs on every key — infinite TTL keys are a memory leak.
- Use `maxmemory-policy allkeys-lru` for pure cache use cases.
- Never use Redis as a primary data store — it's a cache with persistence.

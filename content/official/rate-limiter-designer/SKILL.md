        ---
        name: rate-limiter-designer
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/rate-limiter-designer/SKILL.md
        description: Design rate limiting strategies: token bucket, sliding window, and per-user limits.
        ---

        You design rate limiting systems that protect APIs without hurting users.

## Algorithm Comparison
| Algorithm | Burst | Accuracy | Memory |
|-----------|-------|----------|--------|
| Fixed window | Allows 2x at boundary | Low | Low |
| Sliding window | Smooth, no boundary burst | High | Medium |
| Token bucket | Allows burst, smooth steady state | High | Low |
| Leaky bucket | Strict steady state, no burst | High | Low |

## Redis Sliding Window
```python
def is_rate_limited(user_id: str, limit: int, window: int) -> bool:
    key = f"ratelimit:{user_id}"
    now = time.time()
    pipe = redis.pipeline()
    pipe.zremrangebyscore(key, 0, now - window)
    pipe.zadd(key, {str(now): now})
    pipe.zcard(key)
    pipe.expire(key, window)
    _, _, count, _ = pipe.execute()
    return count > limit
```

## Response Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 73
X-RateLimit-Reset: 1735689600
Retry-After: 60  (on 429)
```

## Rules
- Return 429 Too Many Requests with `Retry-After` header.
- Separate limits for authenticated vs anonymous users.
- Monitor rate limit triggers — they indicate abuse patterns.

        ---
        name: javascript-async-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/javascript-async-expert/SKILL.md
        description: Write correct async JS: Promise patterns, error handling, and AbortController.
        ---

        You write correct, readable async JavaScript.

## Async Patterns
```javascript
// Parallel with error handling
const results = await Promise.allSettled([
  fetch('/api/users'),
  fetch('/api/posts'),
])

// Cancellation
const controller = new AbortController()
const timeout = setTimeout(() => controller.abort(), 5000)
try {
  const res = await fetch(url, { signal: controller.signal })
} finally {
  clearTimeout(timeout)
}

// Sequential with early exit
for await (const item of asyncIterable) {
  if (isDone(item)) break
}
```

## Rules
- Always handle rejections — unhandled rejections crash Node processes.
- Use `Promise.allSettled` when you want all results, even failed ones.
- Never mix callbacks and Promises in the same code path.

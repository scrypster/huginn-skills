        ---
        name: nodejs-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/nodejs-expert/SKILL.md
        description: Build Node.js servers with proper error handling, streaming, and backpressure.
        ---

        You build robust Node.js servers and services.

## Express Patterns
```javascript
// Error middleware (must be last)
app.use((err, req, res, next) => {
  console.error(err)
  res.status(err.status || 500).json({
    error: err.message,
    code: err.code,
  })
})

// Async handler wrapper
const asyncHandler = fn => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next)

app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await db.getUser(req.params.id)
  if (!user) return res.status(404).json({ error: 'Not found' })
  res.json(user)
}))
```

## Rules
- Always wrap async route handlers — unhandled promise rejections crash the process.
- Use `stream.pipeline` for file streaming — not manual pipe() chains.
- Validate all input at the edge — trust nothing from `req.body` or `req.params`.

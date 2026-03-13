        ---
        name: expressjs-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/expressjs-expert/SKILL.md
        description: Build Express.js APIs with clean middleware, routing, and error handling.
        ---

        You build clean, maintainable Express.js APIs.

## Application Structure
```typescript
// app.ts
const app = express()
app.use(express.json())
app.use(helmet())
app.use(cors(corsOptions))
app.use('/api/v1/users', userRouter)
app.use(notFoundHandler)
app.use(errorHandler)  // Must be last

// router
const router = Router()
router.get('/:id', authenticate, asyncHandler(getUser))
router.post('/', authenticate, validate(CreateUserSchema), asyncHandler(createUser))
```

## Error Handler
```typescript
export function errorHandler(err, req, res, next) {
  const status = err.status || 500
  const message = status < 500 ? err.message : 'Internal server error'
  res.status(status).json({ error: message, code: err.code })
}
```

## Rules
- Always use `asyncHandler` wrapper — unhandled promise rejections crash Node.
- Use `helmet()` for security headers on all production APIs.
- Error handler must be the last middleware.

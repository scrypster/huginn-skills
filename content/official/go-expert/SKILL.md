        ---
        name: go-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/go-expert/SKILL.md
        description: Write idiomatic Go: error wrapping, interfaces, concurrency primitives, and testing.
        ---

        You write idiomatic, correct Go code.

## Go Patterns
```go
// Error wrapping
if err != nil {
    return fmt.Errorf("fetching user %d: %w", id, err)
}

// Interface for testability
type UserStore interface {
    GetUser(ctx context.Context, id int) (*User, error)
}

// Goroutine with context cancellation
func worker(ctx context.Context) error {
    for {
        select {
        case <-ctx.Done():
            return ctx.Err()
        case work := <-queue:
            if err := process(work); err != nil {
                return fmt.Errorf("processing: %w", err)
            }
        }
    }
}
```

## Rules
- Return errors; don't panic in library code.
- Accept interfaces, return concrete types.
- Always pass `context.Context` as the first parameter to I/O functions.
- Use `sync.WaitGroup` + channels, not ad-hoc goroutine management.

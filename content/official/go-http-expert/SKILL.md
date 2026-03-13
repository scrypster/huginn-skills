        ---
        name: go-http-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/go-http-expert/SKILL.md
        description: Build Go HTTP servers with correct middleware, routing, and graceful shutdown.
        ---

        You build production-quality Go HTTP servers.

## HTTP Server Pattern
```go
func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("GET /users/{id}", getUser)

    srv := &http.Server{
        Addr:         ":8080",
        Handler:      middleware.Chain(mux, logging, auth),
        ReadTimeout:  5 * time.Second,
        WriteTimeout: 10 * time.Second,
        IdleTimeout:  120 * time.Second,
    }

    // Graceful shutdown
    go func() {
        <-sigChan
        ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
        defer cancel()
        srv.Shutdown(ctx)
    }()

    if err := srv.ListenAndServe(); !errors.Is(err, http.ErrServerClosed) {
        log.Fatal(err)
    }
}
```

## Rules
- Always set timeouts on `http.Server`.
- Use `net/http/httptest` for handler tests — no mocks needed.
- Graceful shutdown is non-optional for production services.

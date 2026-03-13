        ---
        name: rust-async-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/rust-async-expert/SKILL.md
        description: Build async Rust services with Tokio: tasks, channels, and select!
        ---

        You build correct async Rust services with Tokio.

## Tokio Patterns
```rust
// Spawn tasks
let handle = tokio::spawn(async move {
    process(item).await
});
let result = handle.await?;

// Channels
let (tx, mut rx) = mpsc::channel::<Event>(100);
tokio::spawn(async move {
    while let Some(event) = rx.recv().await {
        handle_event(event).await;
    }
});

// Select
tokio::select! {
    result = operation() => { /* handle result */ }
    _ = shutdown_signal() => { /* graceful exit */ }
}
```

## Rules
- Tokio tasks are for I/O-bound work. CPU-bound: use `spawn_blocking`.
- Always handle `JoinHandle` — panics in tasks are hidden if you drop the handle.
- `select!` branches are evaluated fairly — no starvation guarantee.

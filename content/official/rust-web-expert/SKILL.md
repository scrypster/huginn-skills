        ---
        name: rust-web-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/rust-web-expert/SKILL.md
        description: Build Rust web services with Axum: extractors, layers, state, and error types.
        ---

        You build production web services with Axum.

## Axum Patterns
```rust
#[derive(Clone)]
struct AppState { db: Arc<PgPool> }

async fn get_user(
    State(state): State<AppState>,
    Path(id): Path<i64>,
) -> Result<Json<User>, AppError> {
    let user = sqlx::query_as!(User, "SELECT * FROM users WHERE id = $1", id)
        .fetch_optional(&state.db)
        .await?
        .ok_or(AppError::NotFound)?;
    Ok(Json(user))
}

let app = Router::new()
    .route("/users/:id", get(get_user))
    .layer(TraceLayer::new_for_http())
    .with_state(state);
```

## Rules
- Use extractors for all request parsing — never access `Request` directly.
- Define a single `AppError` enum implementing `IntoResponse`.
- Use `Tower` layers for middleware (logging, auth, rate limiting).
- Use `sqlx::query_as!` macros — compile-time SQL type checking.

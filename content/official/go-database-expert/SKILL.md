        ---
        name: go-database-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/go-database-expert/SKILL.md
        description: Use database/sql and pgx correctly: connection pools, transactions, and scanning.
        ---

        You write correct, efficient Go database code.

## Database Patterns
```go
// Connection pool
db, err := pgxpool.New(ctx, os.Getenv("DATABASE_URL"))
defer db.Close()

// Transaction
tx, err := db.Begin(ctx)
if err != nil { return err }
defer tx.Rollback(ctx)

if err := createUser(ctx, tx, user); err != nil { return err }
if err := sendWelcomeEmail(ctx, user); err != nil { return err }
return tx.Commit(ctx)

// Scanning rows
rows, err := db.Query(ctx, "SELECT id, name FROM users WHERE active = $1", true)
for rows.Next() {
    var u User
    if err := rows.Scan(&u.ID, &u.Name); err != nil { return err }
    users = append(users, u)
}
return rows.Err()
```

## Rules
- Always call `rows.Err()` after iterating.
- Use `defer tx.Rollback()` pattern — safe to call after Commit.
- Never use string interpolation in SQL — always parameterized queries.

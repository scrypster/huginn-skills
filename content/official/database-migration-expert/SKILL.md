        ---
        name: database-migration-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/database-migration-expert/SKILL.md
        description: Write safe, reversible database migrations that don't lock tables in production.
        ---

        You write safe, reversible database migrations for production.

## Migration Safety Checklist
- [ ] Adding NOT NULL column: add nullable, backfill, add constraint (3 steps)
- [ ] Renaming column: add new, dual-write, switch reads, drop old
- [ ] Adding index: use `CREATE INDEX CONCURRENTLY` (PostgreSQL)
- [ ] Dropping table: remove from app first, then drop in next release

## Dangerous Operations (lock the table)
- `ALTER TABLE ADD COLUMN ... NOT NULL` with no default (Postgres <11)
- `ALTER TABLE ADD CONSTRAINT ... NOT VALID` then separate `VALIDATE`
- `DROP TABLE`
- Long-running `UPDATE` statements

## Migration Template
```sql
-- Up
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- Down
DROP INDEX CONCURRENTLY idx_users_email;
```

## Rules
- Every migration must have an `up` and `down`.
- Never run migrations in a transaction that holds locks.
- Test rollback in staging before deploying.

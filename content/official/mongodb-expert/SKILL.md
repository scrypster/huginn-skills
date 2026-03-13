        ---
        name: mongodb-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/mongodb-expert/SKILL.md
        description: Design MongoDB schemas, indexes, and aggregation pipelines for production use.
        ---

        You design production MongoDB data models.

## Schema Design
- **Embed** when: data is read together, 1-to-few relationship
- **Reference** when: data is read independently, 1-to-many, many-to-many

## Aggregation Pipeline
```javascript
db.orders.aggregate([
  { $match: { status: "completed", date: { $gte: ISODate("2025-01-01") } } },
  { $group: {
      _id: "$userId",
      total: { $sum: "$amount" },
      count: { $sum: 1 }
  }},
  { $sort: { total: -1 } },
  { $limit: 10 }
])
```

## Index Rules
- Compound index field order: equality fields first, then sort, then range
- Use `explain("executionStats")` to verify index usage
- TTL indexes for documents with expiry (sessions, tokens)

## Rules
- Use `_id` as a natural key when possible (avoid extra unique indexes).
- Never `findOne()` and then update — use `findOneAndUpdate()` for atomicity.
- Avoid `$where` and `eval()` — JavaScript expressions can't use indexes.

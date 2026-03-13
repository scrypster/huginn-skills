        ---
        name: vector-database-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/vector-database-expert/SKILL.md
        description: Choose and use vector databases: Pgvector, Pinecone, Qdrant, and Chroma.
        ---

        You choose and configure vector databases for similarity search.

## Vector DB Comparison
| DB | Best For | Latency | Scale |
|----|---------|---------|-------|
| pgvector | Existing Postgres, small scale | ms | <10M vecs |
| Qdrant | Self-hosted, filtering | ms | 100M+ |
| Pinecone | Managed, simplicity | ms | unlimited |
| Chroma | Local dev, prototyping | ms | <1M |

## pgvector Pattern
```sql
CREATE EXTENSION vector;
CREATE TABLE documents (
    id UUID PRIMARY KEY,
    content TEXT,
    embedding vector(1536)
);
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- Similarity search
SELECT id, content, embedding <=> $1 AS distance
FROM documents
ORDER BY embedding <=> $1
LIMIT 10;
```

## Rules
- Embed once, store forever — re-embedding is expensive.
- Use metadata filters before vector search (pre-filter by date, category).
- Index type: ivfflat for pgvector (approx), hnsw for Qdrant (better recall).

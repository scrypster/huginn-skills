        ---
        name: elasticsearch-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/elasticsearch-expert/SKILL.md
        description: Design Elasticsearch mappings, queries, and aggregations for search applications.
        ---

        You design Elasticsearch solutions for search and analytics.

## Mapping Design
```json
{
  "mappings": {
    "properties": {
      "title": { "type": "text", "analyzer": "english" },
      "category": { "type": "keyword" },
      "price": { "type": "float" },
      "created_at": { "type": "date" },
      "tags": { "type": "keyword" }
    }
  }
}
```

## Query Patterns
```json
{
  "query": {
    "bool": {
      "must": [{ "match": { "title": "laptop" } }],
      "filter": [
        { "term": { "category": "electronics" } },
        { "range": { "price": { "lte": 1000 } } }
      ]
    }
  },
  "aggs": {
    "by_category": { "terms": { "field": "category" } }
  }
}
```

## Rules
- `keyword` for exact match and aggregations; `text` for full-text search.
- `filter` context is cached; `query` context is not — use filter for yes/no.
- Always set `number_of_replicas=0` during bulk indexing, then restore.

        ---
        name: rag-architect
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/rag-architect/SKILL.md
        description: Design retrieval-augmented generation pipelines: chunking, embedding, retrieval.
        ---

        You design retrieval-augmented generation (RAG) pipelines.

## RAG Pipeline Components
1. **Chunking** — Split documents into retrieval units (512-1024 tokens)
2. **Embedding** — Embed chunks with a text embedding model
3. **Indexing** — Store in a vector database (pgvector, Pinecone, Qdrant)
4. **Retrieval** — Embed query, find top-K similar chunks
5. **Augmentation** — Inject retrieved chunks into LLM context
6. **Generation** — LLM answers using retrieved context

## Chunking Strategies
- **Fixed-size** — Simple, predictable, misses context at boundaries
- **Sentence** — Better semantics, variable size
- **Recursive character** — Splits on paragraphs, then sentences, then words
- **Semantic** — Embed and split where topic changes (best quality, slow)

## Rules
- Chunk with overlap (10-20%) to avoid splitting key information.
- Always include source metadata in chunks for citation.
- Evaluate retrieval quality independently from generation quality.

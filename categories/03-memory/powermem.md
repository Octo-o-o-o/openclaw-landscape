> https://github.com/oceanbase/powermem

# PowerMem (489 stars)

## Problem & Solution

AI applications need to persist historical conversations, user preferences, and contextual information, but full-context approaches are costly and slow. PowerMem combines vector retrieval, full-text search, and graph database in a hybrid architecture, incorporating Ebbinghaus forgetting curve theory to achieve 48.77% accuracy improvement, 91.83% latency reduction, and 96.53% token cost reduction on the LOCOMO benchmark.

## Key Features

- **Hybrid Retrieval Architecture** -- Three-channel recall via vector retrieval + full-text search + graph database, with LLM-constructed knowledge graphs supporting multi-hop graph traversal
- **Ebbinghaus Forgetting Curve** -- Cognitive science-based memory retention rate calculation and temporal decay weighting, automatically prioritizing retrieval of recent and relevant memories
- **Intelligent Memory Extraction** -- LLM-driven automatic extraction of key facts from conversations, with duplicate detection, conflict information updates, and related memory merging
- **Multi-Agent Support** -- Independent memory spaces, cross-Agent memory sharing and collaboration, fine-grained permission control based on scope
- **Multimodal Support** -- Automatic conversion of images and audio to text descriptions for storage, supporting text + image + audio mixed content retrieval
- **Sub Stores Partitioning** -- Data partition management + automatic query routing, significantly improving query performance at very large scale
- **Multiple Integration Methods** -- Python SDK, CLI (`pmem`), MCP Server, HTTP API Server

> https://github.com/coolmanns/12layer-memory

# openclaw-memory-architecture (31 stars)

## Problem & Solution

AI Agent memory systems typically rely on a single vector search mechanism, causing both precise queries (e.g., "my daughter's birthday") and fuzzy queries (e.g., "last week's discussion about deployment") to use the same approach, resulting in poor efficiency. This project proposes a 12-layer memory architecture that combines structured storage, semantic search, knowledge graphs, and cognitive patterns to select the optimal strategy for different types of memory recall.

## Key Features

- **12-Layer Hierarchical Architecture** -- From the Lossless Context Machine (LCM) to the metacognitive pipeline, each layer is optimized for a specific memory type
- **Unified Search Interface** -- The `memory_search` tool queries four backends in parallel (continuity, facts, files, lcm), covering all memory systems in a single call
- **Knowledge Graph Integration** -- A knowledge graph with 3,000+ facts, supporting entity relationship queries and alias resolution
- **Semantic Search Optimization** -- Uses llama.cpp + nomic 768d embeddings, 7ms GPU query latency, with multilingual support
- **Activation Decay System** -- Memories decay based on access frequency and time, with automatic tiered storage (hot / warm / cold)
- **LightRAG Domain Knowledge Base** -- Integrates GraphRAG from 11 books + 139 papers, supporting deep domain queries

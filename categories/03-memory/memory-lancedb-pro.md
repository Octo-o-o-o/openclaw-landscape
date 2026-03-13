> https://github.com/CortexReach/memory-lancedb-pro

# memory-lancedb-pro (2,030 stars)

## Problem & Solution
AI Agents lack persistent long-term memory capabilities, with severe information loss across sessions. memory-lancedb-pro provides a production-grade long-term memory plugin for OpenClaw through hybrid retrieval (Vector + BM25), cross-encoder reranking, Weibull decay, and a three-tier promotion mechanism, enabling intelligent memory extraction, lifecycle management, and multi-scope isolation.

## Key Features
- Hybrid retrieval (Vector + BM25 full-text search + Cross-Encoder reranking)
- LLM-driven automatic extraction of 6 memory categories (no manual `memory_store` required)
- Weibull decay + three-tier promotion mechanism (important memories surface, stale memories fade)
- Multi-scope isolation (per-agent, per-user, per-project memory boundaries)
- Support for any embedding provider (OpenAI, Jina, Gemini, Ollama)
- Complete operations tooling (CLI, backup, migration, upgrade, import/export)

<!-- lastCommit: 6a7050b -->

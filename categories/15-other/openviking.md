> https://github.com/volcengine/OpenViking

# OpenViking (5,671 stars)

## Problem & Solution

Agent development suffers from fragmented context management (memory in code, resources in vector stores, skills scattered). Traditional RAG flat storage lacks a global view and has poor retrieval performance. OpenViking is ByteDance's open-source Agent-specific context database that uses a filesystem paradigm to unify management of memory/resources/skills, supporting hierarchical loading, recursive retrieval, visual traces, and automatic session compression.

## Key Features

- **Filesystem Paradigm** — Uses directory structure to uniformly organize Agent memory/resources/skills, managing context like managing local files, solving the fragmentation problem
- **Three-Layer Context Loading** — L0 (metadata) / L1 (summary) / L2 (full text) loaded on demand, significantly reducing token consumption and costs
- **Directory Recursive Retrieval** — Combines directory targeting with semantic search, supporting visual retrieval traces for observable and tunable context acquisition
- **Automatic Session Management** — Automatically compresses conversation content, resource references, and tool calls, extracting long-term memory so the Agent gets smarter over time
- **Multi-Language SDK** — Python/Go/Rust CLI, supports Volcengine/OpenAI/LiteLLM three VLM Providers, compatible with Anthropic/DeepSeek/Gemini/vLLM/Ollama
- **AGFS Core Extension** — High-performance filesystem component implemented in C++, requires Go 1.22+ for building

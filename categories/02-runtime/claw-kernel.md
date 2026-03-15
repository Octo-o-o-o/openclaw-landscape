> https://github.com/creeper-scr/claw-kernel

# claw-kernel (2 stars)

## Problem & Solution

Every project in the Claw ecosystem (OpenClaw, ZeroClaw, OpenCrust) independently implements the same infrastructure (LLM calls, tool protocols, Agent loops, memory systems, channel integrations), leading to duplicated development and fragmentation. claw-kernel extracts these primitives into a single, well-tested cross-platform Rust library, serving as the shared infrastructure layer for the ecosystem.

## Key Features

- **Layered Architecture** — From Layer 0 (Rust core) to Layer 3 (extension base), with clear separation of responsibilities and dependency relationships
- **Cross-platform Abstraction Layer (PAL)** — Unified sandbox, IPC (Unix socket / Named Pipe), and process management interfaces
- **8 LLM Providers** — Native support for Anthropic, OpenAI, Ollama, DeepSeek, Moonshot, Gemini, Mistral, Azure OpenAI
- **Dual Script Engine** — Lua (default) and V8/TypeScript (optional), with hot-reloading and sandbox isolation support
- **670+ Test Coverage** — Comprehensive unit tests and integration tests ensuring cross-platform stability
- **IPC Daemon Service** — claw-server provides global channel registration, tool bridging, trigger storage, and Webhook services

<!-- lastCommit: f70462bedb4a8d1392f371b123ed478e1f7ddb26 -->

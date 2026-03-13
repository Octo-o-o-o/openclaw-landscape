> https://github.com/nearai/ironclaw

# IronClaw (9,108 stars)

## Problem & Solution
Existing AI assistants have opaque data processing, are tied to corporate interests, and carry privacy leakage risks. IronClaw rewrites the OpenClaw core in Rust, emphasizing privacy-first (local storage + encryption), transparency and auditability (open source + no telemetry), self-extension capabilities (dynamic tool building), and multi-layer security (WASM sandbox + prompt injection defense).

## Core Architecture
- **WASM Sandbox**: Untrusted tools run in isolated WebAssembly containers with a capability-based permission model (explicit authorization for HTTP / secrets / tool invocation)
- **Credential Protection**: Secrets are injected at the host boundary, invisible to WASM code, with bidirectional request/response leak detection
- **Docker Sandbox**: Isolated container execution, per-job tokens, orchestrator/worker pattern
- **Hybrid Search**: Full-text + vector search + Reciprocal Rank Fusion, workspace filesystem, identity files
- **Multi-channel**: REPL / HTTP webhooks / WASM channels (Telegram / Slack) / Web Gateway (SSE/WebSocket streaming)
- **Routines**: Cron scheduling / event triggers / webhook handling, background automation
- **Self-repair**: Automatic detection and recovery of stuck operations

## Key Features
- Rust implementation: memory safety, high performance, concurrency-friendly
- Security-first: WASM sandbox + endpoint allowlist + leak detection + prompt injection defense + rate limiting
- Dynamic tool building: describe your needs, IronClaw automatically builds WASM tools
- MCP protocol support: connect to Model Context Protocol servers
- Multiple LLM backends: NEAR AI (default) / OpenRouter / Together AI / Fireworks AI / Ollama / vLLM / LiteLLM
- Persistent memory: PostgreSQL + pgvector, hybrid search
- Parallel tasks: concurrent multi-request processing with isolated contexts

<!-- lastCommit: 6a7050b -->

> https://github.com/mosaxiv/clawlet

# clawlet (653 stars)

## Problem & Solution

Traditional AI assistants rely on complex runtimes (Node.js/Python) and external databases, making deployment cumbersome and resource-intensive. clawlet compiles to a single static binary using Go (no CGO, no runtime dependencies), with embedded SQLite + sqlite-vec, enabling out-of-the-box hybrid semantic memory search — a single file that runs on any machine.

## Key Features

- **Zero-dependency Deployment** — Single static binary with embedded SQLite + sqlite-vec, no database or runtime installation required
- **Multiple LLM Providers** — Supports OpenAI/OpenRouter/Anthropic/Gemini/Ollama/vLLM with a unified configuration interface
- **OAuth Passwordless Login** — OpenAI Codex supports device code flow (`--device-code`), suitable for SSH/container environments
- **Hybrid Semantic Search** — BM25 + vector retrieval built-in, memory queries require no external services
- **Flexible Configuration** — JSON configuration file (`~/.clawlet/config.json`), supports environment variables and model default parameter overrides
- **Local Models First** — Ollama/vLLM routes unified under the `ollama/<model>` prefix, automatically adapting to OpenAI-compatible endpoints

<!-- lastCommit: 8a9367d843abe1bbf13f100bc0896d6fb2043e98 -->

> https://github.com/opencrust-org/opencrust

# OpenCrust (49 stars)

## Problem & Solution

OpenClaw (Node.js) suffers from large binary size (~1.2 GB), high memory usage (~388 MB), slow cold starts (13.9 seconds), and plaintext credential storage. OpenCrust rewrites it in Rust, compressing the binary to 16 MB, reducing memory to 13 MB, shortening cold start to 3 ms, and providing AES-256-GCM encrypted credential storage with WebSocket authentication enabled by default.

## Key Features

- **Extreme Performance** — 16 MB binary, 13 MB memory footprint, 3 ms cold start, 75-98% improvement over OpenClaw
- **Security First** — AES-256-GCM encrypted credential vault, WebSocket pairing authentication enabled by default, user whitelist, prompt injection detection
- **Cross-platform Prebuilt Binaries** — Prebuilt binaries for Linux (x86_64/aarch64), macOS (Intel/Apple Silicon), Windows (x86_64)
- **Hot Configuration Reload** — Supports runtime configuration hot-reload without service restart
- **WASM Plugin Sandbox** — Optional WebAssembly plugin system with controlled host access
- **14 LLM Providers** — Native support for Anthropic, OpenAI, Ollama, compatible with DeepSeek, Mistral, Gemini, Qwen, and other OpenAI-compatible interfaces

<!-- lastCommit: 6ad6ce6 -->

> https://github.com/stellarlinkco/myclaw

# stellarlinkco/myclaw (236 stars)

## Problem & Solution

A full OpenClaw deployment is overly complex, and users need a lightweight "personal Agent assistant" to get started quickly. MyClaw provides a minimal clawbot implementation focused on core Agent capabilities (conversation, tool calling, memory), removing enterprise features (multi-tenancy, permission management), making it suitable for individual developers and small teams.

## Key Features

- **Lightweight Architecture** — Single-file or minimal-dependency deployment, no Docker Compose or complex configuration needed, up and running within 5 minutes
- **Core Agent Capabilities** — Supports multi-turn conversation, tool calling (file operations, network requests, code execution), short-term/long-term memory
- **Model Flexibility** — Supports OpenAI, Claude, Gemini, local LLMs (Ollama), switchable via environment variables
- **Skills System** — Compatible with the OpenClaw SKILL.md format, can directly reuse community skills (e.g., awesome-openclaw-skills)
- **Local First** — Data stored in local SQLite/JSON, no external database or cloud service required
- **Developer Friendly** — Provides both Python API and CLI usage, easy to integrate into existing workflows

<!-- lastCommit: 6a7050b -->

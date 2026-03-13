> https://github.com/HKUDS/nanobot

# nanobot (32,038 stars)

## Problem & Solution
OpenClaw is powerful but has complex code (tens of thousands of lines), making it hard to understand, modify, and extend. nanobot implements OpenClaw's core functionality in ~4,000 lines of core code (99% code reduction), focusing on being lightweight, research-friendly, and fast to iterate.

## Core Architecture
- **Provider Layer**: Unified LLM interface (OpenRouter / OpenAI / Claude / DeepSeek / Qwen / Moonshot / vLLM / Azure / VolcEngine), 2 steps to add a new provider
- **Channel Layer**: Multi-platform connectivity (Telegram / Discord / Slack / Feishu / DingTalk / QQ / Email / WhatsApp / Matrix / CLI)
- **MCP Protocol**: Model Context Protocol support, connecting external tools and data sources
- **Memory System**: Hybrid search (full-text + vector + Reciprocal Rank Fusion), workspace filesystem, identity files
- **Heartbeat Mechanism**: Virtual tool-call heartbeat to prevent timeouts during long silences
- **Cron Scheduling**: Natural language task scheduling with timed reminders and automation

## Key Features
- Ultra-lightweight: Core agent code ~4,000 lines (verify live with `bash core_agent_lines.sh`)
- Quick start: `uv tool install nanobot-ai` + `nanobot onboard` + `nanobot agent` three-step launch
- Multimodal support: Cross-channel file/image/voice receiving and sending
- Prompt caching: Anthropic prompt cache optimization to reduce token consumption
- Security hardening: Session isolation, input validation, path traversal protection, config encryption
- Research-friendly: Clean, readable code that's easy to understand and modify

<!-- lastCommit: 6a7050b -->

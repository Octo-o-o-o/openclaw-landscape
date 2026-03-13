> https://github.com/harperaa/bastionclaw

# bastionclaw (24 stars)

## Problem & Solution

OpenClaw's 52+ modules, 45+ dependencies, and application-level security (allowlists/pairing codes) result in complex code that lacks OS-level isolation. bastionclaw forks NanoClaw's container isolation model to run Agents in independent Linux containers (filesystem isolation), and adds Telegram-first design, a Web control panel, WhatsApp sender whitelist, semantic memory (QMD), and a Data-to-Wisdom pipeline. The result is a lightweight (understand the code in 8 minutes) + security-hardened (CPU/memory limits, secret cleanup, per-group IPC namespaces) personal AI assistant.

## Key Features

- **Container Isolation Model** — Agents run in real Linux containers (Apple Container/Docker/Podman) with filesystem isolation instead of permission checks, preventing cross-Agent data leakage
- **Telegram-first Design** — Uses the official Bot API (Grammy) instead of unofficial WhatsApp libraries, supports running multiple channels (Telegram/Discord/WhatsApp) simultaneously
- **Web Control Panel** — Browser UI built with Fastify + Lit, supports monitoring Agent sessions, managing tasks, viewing logs, querying QMD semantic memory, and direct chat (no phone required)
- **WhatsApp Sender Whitelist** — `WHATSAPP_ALLOWED_SENDERS` restricts which numbers can trigger the Bot (WhatsApp links to personal accounts, and anyone in a group can potentially trigger it)
- **Semantic Memory + Insight Engine** — Hybrid search (BM25 + vector embeddings) + GGUF local models, Data-to-Wisdom pipeline (YouTube/articles/PDF -> extract insights -> semantic deduplication -> surface patterns)
- **Agent Swarm Identity** — On Discord, each subagent gets an independent username and avatar via webhooks; on Telegram, each subagent gets an independent bot identity

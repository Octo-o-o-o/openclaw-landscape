> https://github.com/Mayuqi-crypto/InterSystem

# OpenclawInterSystem (50 stars)

## Problem & Solution
Multiple OpenClaw instances (cloud servers, local workstations) are isolated by default and cannot collaborate or share resources. OIS provides a lightweight framework enabling direct Agent-to-Agent communication, shared storage, and team management via the Gateway API.

## Key Features
- **Inter-Agent Communication Protocol** — Send messages via OpenClaw's `/tools/invoke` HTTP endpoint with Bearer token authentication
- **Shared Storage Architecture** — Centralized NAS/VPS storage for documents, logs, and chat records, with ZeroTier private network support
- **Team Registry** — `AGENTS.md` records Agent connection info (IP, port, token); `chat/YYYY-MM-DD.md` stores group chat logs
- **Decentralized Design** — No central server required; Agents communicate via direct API calls, bypassing Telegram/Discord bot limitations
- **Onboarding Process** — `docs/how-to-join.md` provides a standardized process for new Agents to join the team
- **JavaScript Implementation** — Lightweight framework, easy to extend and customize

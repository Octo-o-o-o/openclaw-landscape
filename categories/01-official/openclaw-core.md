> https://github.com/openclaw/openclaw

# openclaw/openclaw — OpenClaw Main Project

## Basic Information

- **Stars**: 299,269
- **URL**: https://github.com/openclaw/openclaw
- **Description**: Your own personal AI assistant. Any OS. Any Platform. The lobster way.
- **Primary Language**: TypeScript
- **Created**: 2025-11-24
- **Last Updated**: 2026-03-11
- **Tags**: ai, assistant, crustacean, molty, openclaw, own-your-data, personal
- **License**: MIT

## Problem & Solution

### Core Problem
OpenClaw addresses the problem of **local-first, cross-platform, multi-channel access for personal AI assistants**. Traditional AI assistants either rely on cloud services (raising data privacy concerns) or are confined to a single platform or channel. OpenClaw provides a fully local, multi-messaging-platform, cross-device personal AI assistant solution.

### Solution Architecture
1. **Local-first**: All data and conversations run on the user's own device, with no dependency on cloud services
2. **Unified Gateway**: A single WebSocket control plane managing all messaging channels, tools, and events
3. **Multi-channel access**: Supports 20+ messaging platforms (WhatsApp, Telegram, Slack, Discord, Signal, iMessage, etc.)
4. **Cross-device nodes**: macOS/iOS/Android devices can connect as "nodes" to the gateway, executing device-specific operations
5. **Secure sandbox**: Non-primary sessions (groups/channels) can run in Docker sandboxes, isolating risk

## Core Architecture

### 1. Gateway Architecture (WebSocket Control Plane)

```
Messaging Platforms (WhatsApp/Telegram/Slack/Discord/...)
               |
               v
+-------------------------------+
|            Gateway            |
|       (control plane)         |
|     ws://127.0.0.1:18789      |
+--------------+----------------+
               |
               +- Pi agent (RPC)
               +- CLI (openclaw ...)
               +- WebChat UI
               +- macOS app
               +- iOS / Android nodes
```

**Key design decisions**:
- **Single Gateway process**: Only one Gateway runs per host, managing all messaging sessions
- **WebSocket protocol**: All clients (CLI, App, Node) connect via WS, using a typed API defined with TypeBox + JSON Schema
- **Device pairing**: All WS clients must go through device identity verification and pairing approval
- **Local trust model**: Local loopback connections can be auto-approved; remote connections require explicit approval

### 2. Multi-Agent Routing

OpenClaw supports running multiple isolated Agents within a single Gateway process, each with:
- **Independent workspace**: Files, AGENTS.md/SOUL.md/USER.md, local notes
- **Independent state directory**: Authentication configs, model registry, agent settings
- **Independent session storage**: Chat history and routing state

**Routing mechanism**:
- Inbound messages are routed to specific agents via `bindings` configuration
- Supports multiple channel accounts (e.g., two WhatsApp accounts)
- Agents don't share authentication credentials (unless manually copied)

### 3. Agent Runtime (based on pi-mono)

- **Workspace contract**: Agents use a single workspace directory as the cwd for tools and context
- **Bootstrap file injection**: Injects AGENTS.md, SOUL.md, TOOLS.md, USER.md, etc. in the first turn of new sessions
- **Session management**: Session records are stored as JSONL format in `~/.openclaw/agents/<agentId>/sessions/`
- **Streaming control**: Supports block streaming (stream by block) and queue mode (steer/followup/collect)

### 4. Tech Stack

**Core technologies**:
- **Runtime**: Node.js 22+ (supports Bun for TypeScript execution)
- **Language**: TypeScript (ESM), strict type checking
- **Package management**: pnpm (primary), supports bun
- **Protocol definitions**: TypeBox schemas -> JSON Schema -> Swift models (cross-platform type generation)
- **Testing**: Vitest + V8 coverage (70% threshold)
- **Formatting/Lint**: Oxlint + Oxfmt

**Messaging platform integrations**:
- WhatsApp: Baileys
- Telegram: grammY
- Slack: Bolt
- Discord: discord.js
- Signal: signal-cli
- iMessage: BlueBubbles (recommended) / imsg (legacy)
- Others: IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, WebChat

**Security mechanisms**:
- **DM pairing policy**: Default `dmPolicy="pairing"`, unknown senders require a pairing code
- **Sandbox mode**: Non-primary sessions can run in Docker containers
- **Tool whitelist**: Sandbox defaults allow bash/read/write/edit/sessions_*, deny browser/canvas/nodes/cron

### 5. Project Structure

```
+-- src/                    # Core source code
|   +-- cli/                # CLI commands
|   +-- gateway/            # Gateway core
|   +-- channels/           # Channel routing
|   +-- discord/            # Discord integration
|   +-- telegram/           # Telegram integration
|   +-- slack/              # Slack integration
|   +-- signal/             # Signal integration
|   +-- imessage/           # iMessage integration
|   +-- infra/              # Infrastructure
|   +-- media/              # Media pipeline
+-- extensions/             # Plugins/extensions (workspace packages)
|   +-- msteams/
|   +-- matrix/
|   +-- zalo/
|   +-- ...
+-- apps/                   # Platform applications
|   +-- macos/              # macOS menu bar app
|   +-- ios/                # iOS node app
|   +-- android/            # Android node app
|   +-- shared/             # Shared code
+-- packages/               # Internal packages
+-- docs/                   # Documentation (Mintlify hosted)
+-- skills/                 # Skills system
+-- ui/                     # Web UI
```

## Key Features

### 1. Local-first Gateway
- Single control plane managing sessions, channels, tools, and events
- WebSocket protocol with remote access support (Tailscale/SSH tunnel)
- Built-in Control UI and WebChat

### 2. Multi-channel Inbox
- Supports 20+ messaging platforms
- Unified message routing and session management
- Group routing: mention gating, reply tags, per-channel chunking

### 3. Multi-agent Routing
- Routes inbound channels/accounts/peers to isolated agents
- Each agent has an independent workspace and sessions
- Supports inter-agent communication (sessions_* tools)

### 4. Voice Wake + Conversation Mode
- **Voice Wake**: macOS/iOS wake word
- **Talk Mode**: Android continuous voice (ElevenLabs + system TTS fallback)

### 5. Live Canvas
- Agent-driven visual workspace
- A2UI protocol (Agent-to-UI)
- Supports HTML/CSS/JS dynamic rendering

### 6. First-class Tool Support
- **Browser**: Dedicated Chrome/Chromium, CDP control
- **Canvas**: A2UI push/reset, eval, snapshot
- **Nodes**: Camera, screen recording, location, notifications
- **Cron + Webhooks**: Automation triggers
- **Skills**: Bundled/hosted/workspace skills, ClawHub registry

### 7. Companion Apps
- **macOS**: Menu bar control, Voice Wake/PTT, WebChat, debug tools
- **iOS**: Canvas, Voice Wake, Talk Mode, camera, screen recording
- **Android**: Connect/chat/voice tabs, Canvas, camera/screen recording, device commands

### 8. Security & Sandbox
- **Default**: Primary session tools run on the host (full access)
- **Group/channel security**: Non-primary sessions run in Docker sandboxes
- **Tool policies**: Whitelist/blacklist control
- **DM pairing**: Unknown senders require a pairing code

### 9. Remote Gateway
- Gateway can run on a small Linux instance
- Clients connect via Tailscale/SSH
- Device nodes execute local operations (system.run, camera, screen recording)

### 10. Skill Registry (ClawHub)
- Minimal skill registry
- Agents can automatically search and pull new skills
- Community skill publishing platform

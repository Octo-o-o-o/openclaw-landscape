> https://github.com/sunnoy/wecom-plugin

# openclaw-plugin-wecom (434 stars)

## Problem & Solution

Integrating WeCom (Enterprise WeChat) with OpenClaw requires handling enterprise-grade needs such as multi-account management, dynamic Agent isolation, and quota awareness. Built on the official WebSocket long connection skeleton, this plugin provides multi-account management, dynamic Agent routing, Agent API/Webhook enhanced outbound messaging, command whitelisting, quota awareness, and other features to meet enterprise deployment requirements.

## Key Features

- **Multi-account management** — Multiple bots with independent configuration and shared field inheritance, supporting multi-department/multi-scenario Agent deployment within an enterprise
- **Dynamic Agent routing** — Automatically isolates sessions and workspaces by user/group, supports Workspace template auto-copy of bootstrap files (`AGENTS.md`, etc.)
- **Agent API enhanced outbound** — Custom app proactive sending of text/images/files, supporting department (`party:`) and tag (`tag:`) addressing
- **Webhook Bot group notifications** — Named webhook mapping, supporting markdown/image/file formats
- **Command whitelist** — Restricts slash commands available to regular users; admins bypass the whitelist and dynamic Agent routing
- **Quota awareness** — Passive reply 24h window + proactive send quota tracking and alerts to prevent exceeding limits
- **Pending Reply retry** — Automatically retries undelivered replies via Agent API after WebSocket disconnection
- **Reasoning stream throttling** — 800ms throttle to prevent SDK queue overflow
- **Inbound enhancement** — Rich text decomposition, voice transcription, quoted message context pass-through, message deduplication (reqId + msgId)

<!-- lastCommit: 6a7050b -->

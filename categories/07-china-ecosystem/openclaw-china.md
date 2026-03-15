> https://github.com/BytePioneer-AI/openclaw-china

# BytePioneer-AI/openclaw-china

## Basic Information

- **GitHub**: https://github.com/BytePioneer-AI/openclaw-china
- **Stars**: 2,790
- **Language**: TypeScript
- **Created**: 2026-01-28
- **Last Updated**: 2026-03-11
- **Description**: A collection of OpenClaw extension plugins for Chinese IM platforms
- **Topics**: openclaw, openclaw-china, openclaw-dingding, openclaw-feishu, openclaw-qq, openclaw-weixin

## Problem & Solution

### Core Problem

OpenClaw natively does not support China's mainstream instant messaging platforms (DingTalk, WeCom, QQ, Feishu/Lark), preventing Chinese users from integrating AI Agents into enterprise internal communication tools and limiting OpenClaw's application scenarios in the Chinese market.

### Solution

openclaw-china provides a complete Chinese IM platform adaptation layer through a plugin-based architecture:

1. **Unified plugin package** (`@openclaw-china/channels`): Aggregates all channel plugins for one-click installation
2. **Single-channel plugins**: Supports on-demand installation of individual platforms (dingtalk / feishu-china / qqbot / wecom / wecom-app)
3. **Configuration wizard** (`openclaw china setup`): Interactive configuration flow to lower the onboarding barrier
4. **Multi-account support**: Multiple bot accounts can be configured for the same platform
5. **Industry-first features**:
   - DingTalk, QQ, and WeCom support file sending and receiving
   - DingTalk, QQ, and Feishu (Lark) support scheduled tasks
   - WeCom Smart Bot long connection with limited proactive messaging support

## Core Architecture

### Layered Architecture

```
OpenClaw Host
    |
@openclaw-china/channels (unified dispatch layer)
    |
+----------+----------+----------+----------+----------+
| dingtalk | feishu   |  qqbot   |  wecom   |wecom-app |
+----------+----------+----------+----------+----------+
                      |
          @openclaw-china/shared (infrastructure layer)
```

### Tech Stack

- **Build tool**: pnpm workspace + tsup
- **Runtime**: Node.js 22+
- **Plugin system**: OpenClaw plugin protocol (openclaw.plugin.json)
- **Connection methods**:
  - DingTalk: Stream API
  - Feishu (Lark): WebSocket long connection
  - QQ: Official Bot API
  - WeCom Smart Bot: WebSocket long connection (ws mode, no public IP required)
  - WeCom Custom App: HTTPS callback + proactive send API

### Key Design Patterns

1. **Dynamic registration mechanism**: The channels package dynamically registers each channel plugin with OpenClaw at startup
2. **Strategy pattern**: Supports dmPolicy (direct message policy) and groupPolicy (group chat policy) configuration
   - `open`: Open to all users
   - `pairing`: Pairing mode
   - `allowlist`: Allowlist mode
   - `disabled`: Disabled
3. **Adapter pattern**: Each channel implements a unified message inbound/outbound interface
4. **Media archiving**: Inbound media is automatically persisted to a stable path (`~/.openclaw/media/{channel}/inbound/`) to avoid `/tmp` cleanup issues

## Key Features

### 1. Messaging Capability Matrix

| Feature | DingTalk | Feishu (Lark) | QQ | WeCom Smart Bot | WeCom Custom App |
|---------|:--------:|:-------------:|:--:|:---------------:|:----------------:|
| Text messages | Yes | Yes | Yes | Yes | Yes |
| Markdown | Yes | Yes | Yes | Yes | Yes |
| Streaming responses | Yes | - | No | Yes | No |
| Images/Files | Yes | Yes (send only) | Yes | Yes (outbound files limited) | Yes |
| Voice messages | Yes | - | Yes | Yes | Yes |
| Private chat | Yes | Yes | Yes | Yes | Yes |
| Group chat | Yes | Yes | Yes | Yes | No |
| @bot detection | Yes | Yes | Yes | No | No |
| Multi-account | Yes | - | Yes | Yes | Yes |
| Proactive messaging | Yes | Yes | Yes | Yes | Yes |

### 2. WeCom Custom App Advanced Features

- **Inbound media archiving**: image/voice/file/mixed automatically persisted, message body written with `saved:` stable path
- **Voice recognition**: Integrated with Tencent Cloud Flash ASR (ultra-fast recording file recognition)
- **Long text chunking**: Automatic handling of the 2048 bytes limit
- **Stream placeholder/refresh**: 5-second rule buffering, supports `/verbose on` for segment-by-segment proactive sending
- **Access Token caching**: Automatic management with 2-hour expiration
- **Dedicated Skill**: `wecom-app-ops` (target/replyTo/send-back images/recordings/files, OCR/MCP, troubleshooting, media retention policy)

### 3. QQ Channel Features

- **Standard onboarding adapter**: Supports completing credential onboarding and disabling directly within the channel configuration flow
- **Known target registry**: Saved to `~/.openclaw/data/qqbot/known-targets.json`
- **Proactive send helper**: Reuses existing text/media outbound pipeline for single-target proactive sending
- **Long-task notifications**: Supports configurable delay times to improve interaction feedback for time-consuming tasks
- **File upload**: Supports filename parameter for optimized media sending pipeline
- **Fallback mechanism**: Falls back to `event_id` when `msg_id` expires, improving stability for scheduled and async send-backs

### 4. DingTalk Channel Features

- **Multi-account support**: Complete default account parsing, account configuration management, monitoring, and outbound logic
- **Long-task notifications**: Non-AI replies switch to direct dispatch, reducing reply pipeline complexity
- **AI Card**: Optional `enableAICard` (streaming response card)

### 5. WeCom Smart Bot Features

- **Long connection ws mode**: No public IP required, better experience (industry-first on 2026-03-08)
- **Multi-account multi-Agent**: Inbound routing passes through `accountId`, preventing messages from incorrectly falling to the default Agent
- **Heartbeat ACK**: Prevents the channel from being incorrectly identified as inactive during periods without user messages

### 6. Scheduled Task Capabilities

- **Unified use of sessionTarget="isolated"**: Prevents delivery from mixing up sessions
- **Fixed delivery.channel/to/accountId**: Reminder-type tasks don't cross sessions
- **Cron creation prompt**: Explicitly requires execution period constraints to be written into payload.message (plain text only, no tool calls, no manual sends)

<!-- lastCommit: c231523261edddf455bd44568661229ef0433f80 -->

> https://github.com/openclaw/openclaw

# openclaw/openclaw — OpenClaw 主项目

## 基本信息

- **Stars**: 299,269
- **URL**: https://github.com/openclaw/openclaw
- **描述**: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
- **主要语言**: TypeScript
- **创建时间**: 2025-11-24
- **最后更新**: 2026-03-11
- **标签**: ai, assistant, crustacean, molty, openclaw, own-your-data, personal
- **许可证**: MIT

## 问题与解决方案

### 核心问题
OpenClaw 解决的是 **个人 AI 助手的本地化、跨平台、多渠道接入** 问题。传统 AI 助手要么依赖云端服务（数据隐私问题），要么局限于单一平台或渠道。OpenClaw 提供了一个完全本地运行、支持多种消息平台、跨设备协同的个人 AI 助手解决方案。

### 解决方案架构
1. **本地优先（Local-first）**: 所有数据和会话都在用户自己的设备上运行，不依赖云端服务
2. **统一网关（Gateway）**: 单一 WebSocket 控制平面管理所有消息渠道、工具和事件
3. **多渠道接入**: 支持 20+ 消息平台（WhatsApp、Telegram、Slack、Discord、Signal、iMessage 等）
4. **跨设备节点**: macOS/iOS/Android 设备可作为"节点"连接到网关，执行设备特定操作
5. **安全沙箱**: 非主会话（群组/频道）可在 Docker 沙箱中运行，隔离风险

## 核心架构

### 1. Gateway 架构（WebSocket 控制平面）

```
消息平台（WhatsApp/Telegram/Slack/Discord/...）
               │
               ▼
┌───────────────────────────────┐
│            Gateway            │
│       (control plane)         │
│     ws://127.0.0.1:18789      │
└──────────────┬────────────────┘
               │
               ├─ Pi agent (RPC)
               ├─ CLI (openclaw …)
               ├─ WebChat UI
               ├─ macOS app
               └─ iOS / Android nodes
```

**关键设计决策**:
- **单一 Gateway 进程**: 每台主机只运行一个 Gateway，管理所有消息会话
- **WebSocket 协议**: 所有客户端（CLI、App、Node）通过 WS 连接，使用 TypeBox + JSON Schema 定义的类型化 API
- **设备配对（Device Pairing）**: 所有 WS 客户端必须通过设备身份验证和配对审批
- **本地信任模型**: 本地回环连接可自动审批，远程连接需显式批准

### 2. 多 Agent 路由（Multi-Agent Routing）

OpenClaw 支持在单个 Gateway 进程中运行多个隔离的 Agent，每个 Agent 拥有：
- **独立工作空间**: 文件、AGENTS.md/SOUL.md/USER.md、本地笔记
- **独立状态目录**: 认证配置、模型注册表、Agent 配置
- **独立会话存储**: 聊天历史和路由状态

**路由机制**:
- 通过 `bindings` 配置将入站消息路由到特定 Agent
- 支持多个频道账号（如两个 WhatsApp 账号）
- Agent 间不共享认证凭据（除非手动复制）

### 3. Agent 运行时（基于 pi-mono）

- **工作空间契约**: Agent 使用单一工作空间目录作为工具和上下文的 cwd
- **引导文件注入**: 在新会话首轮注入 AGENTS.md、SOUL.md、TOOLS.md、USER.md 等文件
- **会话管理**: 会话记录存储为 JSONL 格式在 `~/.openclaw/agents/<agentId>/sessions/`
- **流式控制**: 支持 block streaming（按块流式发送）和 queue mode（steer/followup/collect）

### 4. 技术栈

**核心技术**:
- **运行时**: Node.js 22+ (支持 Bun 用于 TypeScript 执行)
- **语言**: TypeScript (ESM)，严格类型检查
- **包管理**: pnpm (主要)，支持 bun
- **协议定义**: TypeBox schemas → JSON Schema → Swift models (跨平台类型生成)
- **测试**: Vitest + V8 coverage (70% 阈值)
- **格式化/Lint**: Oxlint + Oxfmt

**消息平台集成**:
- WhatsApp: Baileys
- Telegram: grammY
- Slack: Bolt
- Discord: discord.js
- Signal: signal-cli
- iMessage: BlueBubbles (推荐) / imsg (legacy)
- 其他: IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, WebChat

**安全机制**:
- **DM 配对策略**: 默认 `dmPolicy="pairing"`，未知发送者需配对码
- **沙箱模式**: 非主会话可在 Docker 容器中运行
- **工具白名单**: 沙箱默认允许 bash/read/write/edit/sessions_*，拒绝 browser/canvas/nodes/cron

### 5. 项目结构

```
├── src/                    # 核心源码
│   ├── cli/                # CLI 命令
│   ├── gateway/            # Gateway 核心
│   ├── channels/           # 频道路由
│   ├── discord/            # Discord 集成
│   ├── telegram/           # Telegram 集成
│   ├── slack/              # Slack 集成
│   ├── signal/             # Signal 集成
│   ├── imessage/           # iMessage 集成
│   ├── infra/              # 基础设施
│   └── media/              # 媒体管道
├── extensions/             # 插件/扩展（workspace packages）
│   ├── msteams/
│   ├── matrix/
│   ├── zalo/
│   └── ...
├── apps/                   # 平台应用
│   ├── macos/              # macOS 菜单栏应用
│   ├── ios/                # iOS 节点应用
│   ├── android/            # Android 节点应用
│   └── shared/             # 共享代码
├── packages/               # 内部包
├── docs/                   # 文档（Mintlify 托管）
├── skills/                 # 技能系统
└── ui/                     # Web UI
```

## 关键特性

### 1. 本地优先网关（Local-first Gateway）
- 单一控制平面管理会话、频道、工具和事件
- WebSocket 协议，支持远程访问（Tailscale/SSH 隧道）
- 内置 Control UI 和 WebChat

### 2. 多渠道收件箱（Multi-channel Inbox）
- 支持 20+ 消息平台
- 统一的消息路由和会话管理
- 群组路由：提及门控、回复标签、按频道分块

### 3. 多 Agent 路由（Multi-agent Routing）
- 将入站频道/账号/对等方路由到隔离的 Agent
- 每个 Agent 独立工作空间和会话
- 支持 Agent 间通信（sessions_* 工具）

### 4. 语音唤醒 + 对话模式
- **Voice Wake**: macOS/iOS 唤醒词
- **Talk Mode**: Android 持续语音（ElevenLabs + 系统 TTS 回退）

### 5. 实时画布（Live Canvas）
- Agent 驱动的可视化工作空间
- A2UI 协议（Agent-to-UI）
- 支持 HTML/CSS/JS 动态渲染

### 6. 一流工具支持
- **Browser**: 专用 Chrome/Chromium，CDP 控制
- **Canvas**: A2UI push/reset、eval、snapshot
- **Nodes**: 相机、屏幕录制、位置、通知
- **Cron + Webhooks**: 自动化触发
- **Skills**: 捆绑/托管/工作空间技能，ClawHub 注册表

### 7. 配套应用
- **macOS**: 菜单栏控制、Voice Wake/PTT、WebChat、调试工具
- **iOS**: Canvas、Voice Wake、Talk Mode、相机、屏幕录制
- **Android**: 连接/聊天/语音标签、Canvas、相机/屏幕录制、设备命令

### 8. 安全与沙箱
- **默认**: 主会话工具在主机运行（完全访问）
- **群组/频道安全**: 非主会话在 Docker 沙箱中运行
- **工具策略**: 白名单/黑名单控制
- **DM 配对**: 未知发送者需配对码

### 9. 远程网关（Remote Gateway）
- 可在 Linux 小实例上运行 Gateway
- 客户端通过 Tailscale/SSH 连接
- 设备节点执行本地操作（system.run、相机、屏幕录制）

### 10. 技能注册表（ClawHub）
- 最小化技能注册表
- Agent 可自动搜索和拉取新技能
- 社区技能发布平台

<!-- lastCommit: 137e138 -->

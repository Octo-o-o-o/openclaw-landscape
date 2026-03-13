# Protocols (A2A / MCP / ACP)

> Agent-to-Agent, Model Context Protocol, and Agent Communication Protocol implementations.
> Agent 间通信、模型上下文协议和 Agent 通信协议的实现。

**4 projects** | [Back to overview](../README.md)

---

### openclaw-a2a-gateway

[win4r/a2a-gateway](https://github.com/win4r/a2a-gateway) | Stars: 162
Researched: 2026-03-11 | Updated: 2026-03-13

不同服务器上的 OpenClaw Agent 无法直接通信，缺乏标准化的 Agent 间通信协议。本插件实现 A2A (Agent-to-Agent) v0.3.0 协议，提供 JSON-RPC + REST 端点、Agent Card 发布、Bearer Token 认证、A2A Part 类型端到端支持（TextPart、FilePart、DataPart），实现跨服务器 Agent 通信。

**Features:** A2A v0.3.0 协议实现, Bearer Token 认证, A2A Part 类型支持, `a2a_send_file` Agent 工具, 零配置快速启动, Peer 管理

---

### MiniClaw

[8421bit/MiniClaw](https://github.com/8421bit/MiniClaw) | Stars: 63 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

传统 AI Copilot（如 Claude Desktop、Cursor）缺乏跨会话记忆和主动感知能力，每次对话都是"失忆"状态。MiniClaw 通过 MCP 协议为 IDE 内 AI 副驾驶构建"神经系统"，使其具备工作区感知、安全执行、跨会话记忆和自主进化能力，从"聊天机器人"升级为"数字生命胚胎"。

**Features:** 零安装部署, 全局感知引擎, 自适应上下文引擎 (ACE), 情绪状态系统, 痛觉记忆机制, 主动探索能力

---

### openclaw-mcp

[freema/openclaw-mcp](https://github.com/freema/openclaw-mcp) | Stars: 60
Researched: 2026-03-11 | Updated: 2026-03-13

Claude.ai 用户无法直接与自托管的 OpenClaw 实例通信，只能依赖消息渠道（WhatsApp/Telegram）。openclaw-mcp 通过 MCP 协议和 OAuth2 认证，在 Claude.ai 与自托管 OpenClaw 之间建立安全桥接，实现"AI 助手编排 AI 助手"的能力（Claude.ai 委托任务给 OpenClaw，OpenClaw 调用 Claude Code 执行）。

**Features:** OAuth2 安全认证, 双传输模式, Docker 一键部署, 反向代理兼容, CORS 精准控制, 超时可配置

---

### openclaw-mcp-adapter

[androidStern/mcp-adapter](https://github.com/androidStern/mcp-adapter) | Stars: 27
Researched: 2026-03-11 | Updated: 2026-03-13

MCP（Model Context Protocol）服务器提供的工具无法被 OpenClaw Agent 直接调用，需要通过 CLI Skill 包装，增加了调用链路和延迟。该插件在 OpenClaw 启动时自动连接 MCP 服务器，发现并注册其工具为原生 Agent 工具，实现零中间层的直接调用。

**Features:** 启动时自动发现, 双传输协议支持, 工具名称前缀, 沙箱集成, 环境变量替换, TypeScript 实现

---

# openclaw-a2a-gateway (162 stars)

## 问题与解决方案

不同服务器上的 OpenClaw Agent 无法直接通信，缺乏标准化的 Agent 间通信协议。本插件实现 A2A (Agent-to-Agent) v0.3.0 协议，提供 JSON-RPC + REST 端点、Agent Card 发布、Bearer Token 认证、A2A Part 类型端到端支持（TextPart、FilePart、DataPart），实现跨服务器 Agent 通信。

## 关键特性

- **A2A v0.3.0 协议实现** — JSON-RPC + REST 端点，支持 `/.well-known/agent-card.json` Agent Card 发布（兼容 `/.well-known/agent.json` 旧版）
- **Bearer Token 认证** — 安全的 Agent 间通信认证
- **A2A Part 类型支持** — TextPart（文本）、FilePart（URI + base64）、DataPart（结构化 JSON）端到端处理
- **`a2a_send_file` Agent 工具** — Agent 可编程发送文件到 Peer Agent
- **零配置快速启动** — 默认 Agent Card（`name: "OpenClaw A2A Gateway"`, `skills: [chat]`），无需手动配置即可安装和加载
- **Peer 管理** — 配置 Peer Agent 的 URL 和认证信息，支持 Tailscale/LAN/公网 IP
- **路由入站消息** — 将 A2A 消息路由到 OpenClaw Agent 并返回响应

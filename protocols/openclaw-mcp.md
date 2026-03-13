# openclaw-mcp (60 stars)

## 问题与解决方案

Claude.ai 用户无法直接与自托管的 OpenClaw 实例通信，只能依赖消息渠道（WhatsApp/Telegram）。openclaw-mcp 通过 MCP 协议和 OAuth2 认证，在 Claude.ai 与自托管 OpenClaw 之间建立安全桥接，实现"AI 助手编排 AI 助手"的能力（Claude.ai 委托任务给 OpenClaw，OpenClaw 调用 Claude Code 执行）。

## 关键特性

- **OAuth2 安全认证** — 支持 `MCP_CLIENT_ID` / `MCP_CLIENT_SECRET` / `MCP_ISSUER_URL` 三参数认证，防止未授权访问
- **双传输模式** — 本地 stdio 模式（Claude Desktop）和远程 SSE 模式（Claude.ai），通过 `--transport` 参数切换
- **Docker 一键部署** — 提供 `ghcr.io/freema/openclaw-mcp` 镜像，支持版本锁定（如 `:1.1.0`）和 `read_only` 容器安全加固
- **反向代理兼容** — 强制要求设置 `MCP_ISSUER_URL` 为公网 HTTPS URL，避免 OAuth 元数据暴露 `http://localhost:3000` 导致认证失败
- **CORS 精准控制** — 通过 `CORS_ORIGINS=https://claude.ai` 限制跨域请求来源，防止 CSRF 攻击
- **超时可配置** — `OPENCLAW_TIMEOUT_MS` 参数支持长时任务（默认 300 秒），适配 Claude Code 等耗时操作

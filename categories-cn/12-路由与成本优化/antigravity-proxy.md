> https://github.com/badrisnarayanan/antigravity

# Antigravity-Claude-Proxy (3,107 stars)

## 问题与解决方案

Antigravity-Claude-Proxy 解决了 Claude/Gemini 模型在 OpenClaw/Claude Code 中的接入成本问题。通过代理 Antigravity Cloud Code 的免费 Claude/Gemini 配额，将 Google Generative AI 格式转换为 Anthropic Messages API 格式，使 OpenClaw 用户无需付费 API Key 即可使用 Claude/Gemini 模型。但存在 Google ToS 违规风险，部分用户账号被封禁。

## 关键特性

- **Anthropic API 兼容**：提供 Anthropic Messages API 格式的代理服务器，无缝对接 Claude Code CLI 和 OpenClaw
- **双模型支持**：支持 Claude（Anthropic）和 Gemini（Google）模型，通过 Antigravity Cloud Code 后端
- **多账号管理**：支持单账号模式（读取 Antigravity 本地数据库）和多账号模式（OAuth 授权多个 Google 账号）
- **Web Dashboard**：提供 Web UI 管理账号、查看健康状态、手动授权（支持无头服务器）
- **后台运行**：作为后台进程运行，支持 start/stop/restart/status 命令，默认端口 8080
- **ToS 风险警告**：明确警告 Google ToS 违规风险，建议使用小号而非主账号

> https://github.com/zhixianio/botdrop-android

# BotDrop Android (303 stars)

## 问题与解决方案

在 Android 手机上运行 AI Agent 需要安装 Termux、配置 Node.js、手动执行 CLI 命令，技术门槛高。BotDrop 将 OpenClaw 封装为用户友好的 Android 应用，提供 4 步引导式安装（Auth → Agent → Install → Channel），无需终端和 CLI，支持后台 Gateway 自动重启。

## 关键特性

- **4 步引导式安装** — Auth（配置 AI 提供商凭证）→ Agent（创建 Agent）→ Install（安装依赖）→ Channel（配置 Telegram/Discord）
- **多提供商支持** — Anthropic、OpenAI、Google Gemini、OpenRouter 等
- **Telegram & Discord 集成** — 通过 IM 应用与 Agent 聊天
- **后台 Gateway** — 保持 Agent 运行并自动重启
- **无需终端** — 所有操作通过 GUI 完成
- **基于 Termux** — 提供 Linux 环境运行 Node.js 的 AI Agent
- **Crashlytics 集成** — Firebase Crashlytics 崩溃报告（可选，构建时配置）

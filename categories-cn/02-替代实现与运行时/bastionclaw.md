> https://github.com/harperaa/bastionclaw

# bastionclaw (24 stars)

## 问题与解决方案

OpenClaw 的 52+ 模块、45+ 依赖、应用级安全（allowlists/pairing codes）导致代码复杂且缺乏 OS 级隔离。bastionclaw 通过 fork NanoClaw 的容器隔离模型，将 Agent 运行在独立 Linux 容器（filesystem isolation），并添加 Telegram-first、Web 控制面板、WhatsApp 发送者白名单、语义记忆（QMD）、Data-to-Wisdom 管道，实现轻量级（8 分钟理解代码）+ 安全加固（CPU/内存限制、secret 清理、per-group IPC namespaces）的个人 AI 助手。

## 关键特性

- **容器隔离模型** — Agent 运行在真实 Linux 容器（Apple Container/Docker/Podman），文件系统隔离而非权限检查，防止跨 Agent 数据泄漏
- **Telegram-first 设计** — 使用官方 Bot API（Grammy）替代 WhatsApp 非官方库，支持多频道（Telegram/Discord/WhatsApp）同时运行
- **Web 控制面板** — Fastify + Lit 构建的浏览器 UI，支持监控 Agent 会话、管理任务、查看日志、查询 QMD 语义记忆、直接聊天（无需手机）
- **WhatsApp 发送者白名单** — `WHATSAPP_ALLOWED_SENDERS` 限制哪些号码可触发 Bot（WhatsApp 链接个人账号，群组内任何人都可能触发）
- **语义记忆 + 洞察引擎** — 混合搜索（BM25 + 向量嵌入）+ GGUF 本地模型，Data-to-Wisdom 管道（YouTube/文章/PDF → 提取洞察 → 语义去重 → 浮现模式）
- **Agent Swarm 身份** — Discord 上每个 subagent 通过 webhook 获得独立用户名和头像，Telegram 上每个 subagent 获得独立 bot 身份

<!-- lastCommit: 6a7050b -->

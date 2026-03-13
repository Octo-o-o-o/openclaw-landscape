> https://github.com/microclaw/microclaw

# MicroClaw

| 属性 | 值 |
|------|-----|
| 仓库 | [microclaw/microclaw](https://github.com/microclaw/microclaw) |
| Stars | 558 |
| 语言 | Rust |
| 许可证 | MIT |
| 最后活跃 | 2026-03（活跃开发中） |

## 简介

MicroClaw 是一款用 Rust 构建的 Agentic AI 助手，灵感来自 NanoClaw，专注于在聊天平台中提供智能 Agent 能力。支持多种聊天平台（Telegram、Discord、Slack、Feishu、IRC）和多 LLM Provider，具有完整的工具执行能力。

## 核心特性

- **Agentic 工具使用** — bash 命令、文件读写编辑、glob 搜索、正则 grep、持久记忆
- **会话恢复** — 完整对话状态（含工具交互）在消息间持久化
- **上下文压缩** — 会话过长时自动摘要旧消息
- **子 Agent** — 可派生并行子 Agent 处理独立子任务
- **技能系统** — 可扩展技能系统，兼容 Anthropic Skills 格式
- **计划与执行** — TODO 工具用于分解复杂任务
- **Web 搜索** — 通过 DuckDuckGo 搜索和网页解析
- **定时任务** — 支持 cron 定时和一次性定时任务
- **持久记忆** — 全局、Bot 级别、聊天级别的 AGENTS.md
- **MCP 集成** — Playwright MCP Bridge 浏览器自动化
- **ACP Server** — 可作为 Agent Client Protocol 服务器运行
- **消息分片** — 自动按平台限制分割长消息

## 支持平台

Telegram / Discord / Slack / Feishu / IRC

## 工具列表

bash, read_file, write_file, edit_file, glob, grep, read_memory, write_memory, web_search, web_fetch, send_message, schedule_task, sessions_spawn, subagents 系列, activate_skill, todo_read/write 等

## 技术架构

- 平台可扩展架构：共享 Agent 循环 + 工具系统 + 存储层，平台适配器处理通道特定逻辑
- Docker 沙盒支持
- 每条消息触发 Agentic 循环，最多 100 次迭代

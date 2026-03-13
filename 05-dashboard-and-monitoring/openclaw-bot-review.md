# OpenClaw Bot Review (Dashboard)

| 属性 | 值 |
|------|-----|
| 仓库 | [xmanrui/OpenClaw-bot-review](https://github.com/xmanrui/OpenClaw-bot-review) |
| Stars | 548 |
| 语言 | TypeScript (Next.js) |
| 许可证 | — |
| 最后活跃 | 2026-03 |

## 简介

轻量级 Web 仪表板，用于一览所有 OpenClaw Bot/Agent/模型/会话状态。直接读取本地 `~/.openclaw/openclaw.json` 配置文件和会话数据，无需数据库。

## 核心功能

- **机器人总览** — 卡片墙展示所有 Agent 的名称、Emoji、模型、平台绑定、会话统计和 Gateway 健康状态
- **模型列表** — 查看所有已配置的 Provider 和模型，包含上下文窗口、最大输出、推理支持及单模型测试
- **会话管理** — 按 Agent 浏览所有会话，支持类型识别（私聊、群聊、定时任务）、Token 用量和连通性测试
- **消息统计** — Token 消耗和平均响应时间趋势，支持按天/周/月查看，SVG 图表展示
- **技能管理** — 查看所有已安装技能（内置、扩展、自定义），支持搜索和筛选
- **告警中心** — 配置告警规则（模型不可用、机器人无响应），通过飞书发送通知
- **Gateway 健康检测** — 实时 Gateway 状态指示器，10 秒自动轮询，点击可跳转 OpenClaw Web 页面
- **平台连通测试** — 一键测试所有飞书/Discord 绑定和 DM Session 的连通性
- **自动刷新** — 可配置刷新间隔（手动、10s、30s、1min、5min、10min）
- **国际化** — 中英文界面切换
- **主题切换** — 支持深色/浅色主题
- **像素办公室** — 像素风动画办公室，Agent 以像素角色呈现，实时行走、就座、与家具互动

## 技术栈

- Next.js + TypeScript
- Tailwind CSS
- 无数据库 — 直接读取本地配置文件

## 环境要求

- Node.js 18+
- OpenClaw 已安装，配置文件位于 `~/.openclaw/openclaw.json`
- 支持 Docker 部署

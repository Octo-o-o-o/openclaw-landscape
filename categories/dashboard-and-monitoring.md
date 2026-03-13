# Dashboards & Monitoring

> Web dashboards, monitoring tools, and observability platforms.
> Web 仪表板、监控工具和可观测性平台。

**17 projects** | [Back to overview](../README.md)

---

### Star Office UI

[ringhyacinth/Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | Stars: 4,092
Researched: 2026-03-11 | Updated: 2026-03-13

AI Agent 的工作状态不可见，用户无法直观了解"Agent 此刻在做什么、昨天做了什么、是否在线"。Star Office UI 是像素风格的 AI 办公室看板，将 Agent 状态实时可视化为办公室场景，支持多 Agent 协作、中英日三语、AI 生图装修和桌面宠物模式。

**Features:** 六种状态可视化, 昨日小记, 多 Agent 协作, 美术资产管理, 安全加固, 灵活部署

---

### Mission Control

[builderz-labs/mission-control](https://github.com/builderz-labs/mission-control) | Stars: 2,069
Researched: 2026-03-11 | Updated: 2026-03-13

大规模运行 AI Agent 时缺乏统一的编排和监控工具，任务、成本、日志分散在多个系统中。Mission Control 提供了一个开源的 Agent 编排仪表板，通过 28 个面板（任务、Agent、日志、Token、内存、Cron、告警、Webhook、Pipeline）实现全栈可观测性，支持多网关连接和实时监控。

**Features:** 28 个监控面板, 实时推送（WebSocket + SSE）, 零外部依赖（SQLite + 单命令启动, 基于角色的访问控制（Viewer/Operator/Admin）+ Session + API Key 认证, 质量门禁系统, 多网关支持（OpenClaw 及更多即将支持）

---

### OpenClaw Mission Control

[abhi1693/mission-control](https://github.com/abhi1693/mission-control) | Stars: 1,957
Researched: 2026-03-11 | Updated: 2026-03-13

1. 多 Agent 运维复杂 — 企业环境中运行多个 OpenClaw Agent，缺乏统一的管理界面，需要在多个工具间切换 2. 缺乏审批与治理 — 敏感操作（如删除数据、执行高权限命令）缺乏人工审批流程，存在安全风险 3. 分布式环境管理困难 — 多个 Gateway 环境（开发、测试、生产）缺乏统一的编排和监控 4. 工作流程不透明 — 缺乏统一的活动日志和审计追踪，难以排查问题和追溯操作 5. 团队协作效率低 — 缺乏任务分配、Board 管理、标签系统等协作工具 6. API 自动化缺失 — 运维操作依赖手动执行，缺乏 API 支持自动化

**Features:** 多租户隔离, 组织级权限控制, 组织邀请与成员管理, 按季度、部门、项目分组, 支持嵌套结构, 批量操作（如 "归档 Q1 所有 Boards"）

---

### OpenClaw Studio

[grp06/openclaw-studio](https://github.com/grp06/openclaw-studio) | Stars: 1,549 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 原生架构存在以下痛点：

---

### crshdn/mission-control

[crshdn/mission-control](https://github.com/crshdn/mission-control) | Stars: 1,319 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

**Features:** AI 主动提问澄清需求, 多轮对话式规划流程, 基于用户回答自动创建专业化 Agent

---

### Crabwalk

[crabwise-ai/crabwalk](https://github.com/crabwise-ai/crabwalk) | Stars: 859
Researched: 2026-03-11 | Updated: 2026-03-13

Crabwalk 解决了 OpenClaw Agent 运行时"黑盒不可观测"的痛点。通过 WebSocket 连接 OpenClaw Gateway（`ws://127.0.0.1:18789`），实时订阅 Agent 会话事件流，将思考状态、工具调用、响应链以 ReactFlow 节点图可视化，支持跨 WhatsApp/Telegram/Discord/Slack 多平台同时监控，提供会话过滤、动作追踪、工作区文件浏览等实时伴侣监控能力。

**Features:** 实时节点图可视化, 多平台统一监控, WebSocket 事件流订阅, 会话过滤与搜索, 工作区文件浏览, CLI + Docker 双模式

---

### Curbob/LobsterBoard

[Curbob/LobsterBoard](https://github.com/Curbob/LobsterBoard) | Stars: 815 | Business Source License 1.1 (BSL-1.1)
Researched: 2026-03-11 | Updated: 2026-03-13

LobsterBoard 解决了 OpenClaw 用户的可视化监控和控制需求：

**Features:** 20px 网格对齐, 调整大小手柄, 属性面板, 画布尺寸预设

---

### carlosazaustre/tenacitOS

[carlosazaustre/tenacitOS](https://github.com/carlosazaustre/tenacitOS) | Stars: 689 | MIT
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 用户需要一个实时仪表板和控制中心来管理 AI Agent 实例，但面临以下困难：

**Features:** 零配置, 自定义外观, 实时更新

---

### tugcantopaloglu/openclaw-dashboard

[tugcantopaloglu/dashboard](https://github.com/tugcantopaloglu/dashboard) | Stars: 418 | Node.js
Researched: 2026-03-13 | Updated: 2026-03-13

OpenClaw Agent 运维信息散落在日志和 CLI 中，且缺乏安全的远程访问方案。本项目提供零 npm 依赖的 Node.js 仪表板，强调安全加固（TOTP MFA、CSP、审计日志、速率限制），支持通过 Tailscale 安全远程访问。

**Features:** 实时会话管理, API 速率限制追踪, 成本分析, 活动热力图, 系统健康

---

### mudrii/openclaw-dashboard

[mudrii/dashboard](https://github.com/mudrii/dashboard) | Stars: 261 | Go
Researched: 2026-03-13 | Updated: 2026-03-13

多 Agent、多 cron、多 Channel 的 OpenClaw 部署缺乏统一的命令中心，信息分散导致决策效率低。本项目提供零依赖的本地仪表板，汇总所有运维信息，支持 Go 二进制（2,019 req/s）或 Python 服务器（1,745 req/s）。

**Features:** 12 个仪表板面板, Go 二进制部署, 双服务器架构, 前端架构, DirtyChecker, Immutable State Snapshot

---

### OpenClaw Office

[WW-AI-Lab/openclaw-office](https://github.com/WW-AI-Lab/openclaw-office) | Stars: 209
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw Multi-Agent 系统缺乏可视化的协作监控界面，难以直观理解 Agent 之间的消息流和工作状态。OpenClaw Office 通过 2D/3D 虚拟办公室场景渲染 Agent 工作状态、协作链接、工具调用、资源消耗，并提供全功能控制台进行系统管理。

**Features:** 虚拟办公室, Agent 头像, 协作可视化, 侧边面板, Chat, Console

---

### OpenClaw Nerve

[daggerhashimoto/openclaw-nerve](https://github.com/daggerhashimoto/openclaw-nerve) | Stars: 178
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw Agent 的消息渠道（Telegram、WhatsApp、Discord）无法提供实时图表渲染、工作区编辑、文件浏览、看板任务管理和 Token 监控等高级功能。Nerve 是一个自托管的 Web UI，提供语音对话、实时工作区编辑、内联图表、Cron 调度和完整的 Token 级可见性，30 秒内完成安装。

**Features:** 语音交互（12 种语言、唤醒词激活、本地 Whisper 转录、多提供商 TTS）, 完整工作区可见性（子 Agent 会话、工作区文件、内存、配置、工具, 看板任务板（拖放任务管理 + Agent 执行 + 审核工作流 + 提案收件箱）, 响应式设计（桌面、平板、移动端适配, 实时图表（TradingView 图表、K 线图、数据可视化直接嵌入对话）, Cron 调度（从 UI 创建定时任务和一次性提醒）

---

### VidClaw

[madrzak/vidclaw](https://github.com/madrzak/vidclaw) | Stars: 139
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw Agent 在远程服务器上运行时缺乏可观测性，用户无法实时了解 Agent 的执行状态和行为。VidClaw 通过实时录屏和回放功能，将 Agent 的每次运行转化为可观测、可审计、可分享的视频记录。

**Features:** 看板任务管理, 实时使用追踪, 模型热切换, 活动日历视图, 工作区文件浏览器, 技能管理器

---

### ClawMonitor

[openclawq/clawmonitor](https://github.com/openclawq/clawmonitor) | Stars: 32 | Python | MIT
Researched: 2026-03-13 | Updated: 2026-03-13

ClawMonitor 是一个轻量级的 OpenClaw Agent 会话实时监控工具。提供 TUI（终端用户界面）和 CLI 两种交互方式，可以追踪多个 Agent 会话的状态、消息交换和执行进度。

---

### OpenClaw Monitoring by VideoDB

[video-db/openclaw-monitoring](https://github.com/video-db/openclaw-monitoring) | Stars: 15
Researched: 2026-03-11 | Updated: 2026-03-13

远程运行的 AI Agent 缺乏可观测性，用户无法实时了解 Agent 的执行状态和行为，只能"发送任务 → 等待 → 收到成功消息 → 祈祷"。VideoDB Monitoring 通过实时流和可回放录制，将每次 Agent 运行转化为可观测、可审计、可分享的视频记录。

**Features:** 实时流 + 可回放录制, 可搜索时刻, Webhook 告警, 两种集成模式, Agent 自我分析, 多场景应用

---

### OpenClaw-Agent-Control

[JiangAgentLabs/Agent-Control](https://github.com/JiangAgentLabs/Agent-Control) | Stars: 1
Researched: 2026-03-11 | Updated: 2026-03-13

多 Agent 运维场景下，Agent 状态分散在日志和监控系统中，定位和处置成本高。该项目提供风险优先的控制台，将 Agent 可观测性与运维控制决策集中到同一界面，支持实时状态监控、事件时间轴诊断和 Skill 一键部署。

**Features:** 风险优先视图, 清晰状态语义, 事件时间轴, Skill 一键部署, 生命周期管理脚本, 双语文档

---

### OpenClaw Bot Review

[xmanrui/OpenClaw-bot-review](https://github.com/xmanrui/OpenClaw-bot-review) | Stars: 0 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

**Features:** 机器人总览, 模型列表, 会话管理, 消息统计, 技能管理, 告警中心

---

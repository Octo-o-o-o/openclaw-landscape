# mudrii/openclaw-dashboard (261 stars)

> 调研时间：2026-03-13（更新）
> 定位：零依赖本地命令中心，汇总 OpenClaw Agent 的 Gateway 健康、成本、cron 状态、会话、Sub-Agent、模型使用、Git 日志

## 问题与解决方案

多 Agent、多 cron、多 Channel 的 OpenClaw 部署缺乏统一的命令中心，信息分散导致决策效率低。本项目提供零依赖的本地仪表板，汇总所有运维信息，支持 Go 二进制（2,019 req/s）或 Python 服务器（1,745 req/s）。

## 关键特性

- **12 个仪表板面板** — Top Metrics Bar（CPU/RAM/swap/disk + Gateway 状态）、Alerts Banner（智能告警）、System Health、Cost Cards（今日/总计/月预估）、Cron Jobs、Active Sessions、Token Usage（7d/30d/all-time 切换）、Sub-Agent Activity、Charts & Trends（成本曲线 + 模型分布柱状图）、Models/Skills/Git Log、AI Chat
- **Go 二进制部署** — 单文件 9.5–10 MB，HTML/CSS/JS 嵌入二进制，无运行时依赖
- **双服务器架构** — Go（生产，stale-while-revalidate）+ Python（开发），API 完全一致
- **前端架构** — 7 个松耦合 JS 模块（State / DataLayer / DirtyChecker / Renderer / Theme / Chat / App），纯 SVG 图表
- **DirtyChecker** — 13 个布尔脏标记，仅重渲染变化的区域
- **Immutable State Snapshot** — 不可变状态快照，防止 fetch/render 竞态
- **Stale-While-Revalidate** — Go 服务器立即返回缓存数据，后台异步刷新
- **AI Chat** — 通过 OpenClaw Gateway 对成本、会话、cron、配置进行自然语言查询
- **6 种主题** — 3 深 + 3 浅，Glass Morphism UI，19 个 CSS 变量定义每个主题
- **智能告警横幅** — 高成本、cron 失败、高 context 使用率、Gateway 离线
- **5 级模型解析链** — overrides → parent → fallback → defaults，确保准确的模型归属

## 技术实现亮点

| 技术点 | Python (server.py) | Go (openclaw-dashboard) |
|--------|-------------------|------------------------|
| HTML 服务 | 从磁盘读取 | 嵌入二进制（embed.FS） |
| `/api/refresh` | 阻塞式 | Stale-while-revalidate |
| `/api/chat` | 每次请求读取 | mtime 缓存 |
| `/api/system` | TTL 缓存 | RWMutex 缓存 |
| 速率限制 | 10 req/min | 10 req/min |
| 测试 | 122 (pytest) | 87 (go test -race) |
| 吞吐量 | 1,745 req/s | 2,019 req/s |

# Mission Control (2,069 stars)

## 问题与解决方案
大规模运行 AI Agent 时缺乏统一的编排和监控工具，任务、成本、日志分散在多个系统中。Mission Control 提供了一个开源的 Agent 编排仪表板，通过 28 个面板（任务、Agent、日志、Token、内存、Cron、告警、Webhook、Pipeline）实现全栈可观测性，支持多网关连接和实时监控。

## 关键特性
- 28 个监控面板，覆盖任务、Agent、成本、日志、内存、Cron、告警、Webhook、Pipeline
- 实时推送（WebSocket + SSE），智能轮询在用户离开时暂停
- 零外部依赖（SQLite + 单命令启动，无需 Redis/Postgres/Docker）
- 基于角色的访问控制（Viewer/Operator/Admin）+ Session + API Key 认证
- 质量门禁系统，任务完成前需审核签字
- 多网关支持（OpenClaw 及更多即将支持）

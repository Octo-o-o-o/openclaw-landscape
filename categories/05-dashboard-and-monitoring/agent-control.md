# OpenClaw-Agent-Control (1 star)

## 问题与解决方案

多 Agent 运维场景下，Agent 状态分散在日志和监控系统中，定位和处置成本高。该项目提供风险优先的控制台，将 Agent 可观测性与运维控制决策集中到同一界面，支持实时状态监控、事件时间轴诊断和 Skill 一键部署。

## 关键特性

- **风险优先视图** — 核心展示区优先显示卡住（stalled）、异常（blocked）、活跃（executing）状态，降低 MTTD
- **清晰状态语义** — 定义 5 种标准状态（idle、executing、waiting、stalled、blocked），避免状态歧义
- **事件时间轴** — 可视化 Agent 和 Sub-agent 的状态演化，支持回溯和根因分析
- **Skill 一键部署** — 提供 `deploy_with_skill.sh` 脚本，自动完成后端（FastAPI）和前端（Next.js）的启动
- **生命周期管理脚本** — 封装启动、停止、重启、状态查询、日志查看等运维操作
- **双语文档** — 提供中英文文档和教程，降低国际团队接入成本

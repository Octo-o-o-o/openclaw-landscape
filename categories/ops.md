# Ops Tools

> Backup, health monitoring, runbook automation, and operational tooling.
> 备份、健康监控、运维手册自动化及运维工具。

**3 projects** | [Back to overview](../README.md)

---

### OpenClaw Guardian

[LeoYeAI/openclaw-guardian](https://github.com/LeoYeAI/openclaw-guardian) | Stars: 938 | Bash Shell Script（单文件 `guardian.sh`，约 150 行） | MIT
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw Gateway 在生产环境中面临的稳定性挑战：

**Features:** 所有参数都有合理的默认值, 无需修改代码即可直接运行, 通过环境变量灵活调整行为

---

### openclaw-backup

[LeoYeAI/openclaw-backup](https://github.com/LeoYeAI/openclaw-backup) | Stars: 917
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 实例的迁移和备份缺乏标准化方案，用户需要手动备份配置、凭证、会话历史等数据。该项目提供一键备份和恢复功能，将 workspace、memory、skills、credentials、bot tokens、API keys、agent session history 打包为单个归档文件，支持零重新配对迁移到新实例。

**Features:** 一键备份, 一键恢复, 浏览器 UI, 服务器迁移, 安全措施, 由 MyClaw.ai 提供支持

---

### openclaw-runbook

[digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook) | Stars: 894
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 用户在生产环境中面临成本失控、内存泄漏、配额耗尽等问题。该项目提供实战 Runbook，涵盖 coordinator vs worker 模型、成本控制、内存边界、安全加固等最佳实践，帮助用户构建稳定、可预测、低成本的 OpenClaw 部署。

**Features:** 实战指南, 示例模板, Showcases, 配置参考, VPS 部署和安全加固指南, 社区资源

---

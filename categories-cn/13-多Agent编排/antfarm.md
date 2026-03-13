> https://github.com/snarktank/antfarm

# Antfarm (2,104 stars)

## 问题与解决方案
Antfarm 解决了 OpenClaw Agent 团队协作的复杂性问题。传统方式需要手动编排多个 Agent、管理上下文传递和状态追踪，而 Antfarm 提供了一键安装的多 Agent 工作流框架，通过 YAML 定义确定性流程，让专业化 Agent 团队自动协作完成复杂任务。

## 核心架构
- **Ralph 循环模式** — 每个 Agent 在独立 session 中运行，通过 git history 和 progress files 持久化记忆，避免上下文窗口膨胀
- **SQLite + Cron 编排** — 无需 Redis/Kafka/容器编排，Agent 通过 cron 轮询任务队列，claim step 后执行并传递上下文
- **YAML 工作流定义** — 声明式定义 Agent 角色、工作空间、验证标准和步骤依赖关系
- **自动重试与升级机制** — 失败步骤自动重试，重试耗尽后升级给人工介入

## 关键特性
- **3 个预置工作流** — feature-dev (7 agents)、security-audit (7 agents)、bug-fix (6 agents)
- **Agent 互相验证** — developer 不自己验收，由独立 verifier 检查 acceptance criteria
- **一键安装** — `curl | bash` 安装，自动配置 Agent 工作空间、cron 任务和权限
- **Web Dashboard** — 实时监控运行状态、步骤进度和 Agent 输出
- **安全审查机制** — 仅从官方 repo 安装工作流，所有社区贡献经过 prompt injection 审查

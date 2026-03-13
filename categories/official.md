# Official

> Projects maintained by the OpenClaw organization.
> OpenClaw 官方组织维护的项目。

**6 projects** | [Back to overview](../README.md)

---

### openclaw/openclaw — OpenClaw 主项目

[openclaw/openclaw](https://github.com/openclaw/openclaw) | Stars: 299,704 | TypeScript (ESM)，严格类型检查 | MIT
Researched: 2026-03-11 | Updated: 2026-03-13

**Features:** 单一控制平面管理会话、频道、工具和事件, WebSocket 协议, 内置 Control UI 和 WebChat

---

### openclaw/clawhub

[openclaw/clawhub](https://github.com/openclaw/clawhub) | Stars: 5,292 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 生态系统面临的核心问题是 Agent 技能（Skills）的分发、版本管理和发现。随着 AI Agent 能力的扩展，需要一个标准化的方式来：

**Features:** 上传流程, 版本控制, 每次上传创建新 `SkillVersion`, `latest` 标签自动指向最新版本（除非用户重新标记）, 支持回滚

---

### openclaw/skills

[openclaw/skills](https://github.com/openclaw/skills) | Stars: 2,524 | Python
Researched: 2026-03-11 | Updated: 2026-03-13

openclaw/skills 仓库解决的是 技能注册中心的持久化备份和历史存档 问题：

**Features:** 所有版本保留, 软删除版本, 变更追踪

---

### openclaw/lobster

[openclaw/lobster](https://github.com/openclaw/lobster) | Stars: 795 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

1. Token 浪费: AI Agent 在执行多步骤任务时需要反复重新规划每一步，消耗大量 token 2. 确定性不足: 纯 LLM 驱动的任务执行缺乏可预测性和可重复性 3. 可恢复性差: 任务中断后难以从断点恢复，需要重新开始 4. 文本管道局限: 传统 Unix 管道基于文本流，无法高效传递结构化数据（JSON/对象）

**Features:** JSON-first, 结构化数据, 类型安全

---

### openclaw/acpx

[openclaw/acpx](https://github.com/openclaw/acpx) | Stars: 719 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

1. PTY 抓取的脆弱性: AI Agent 编排器通过伪终端（PTY）与编码 Agent 交互，需要解析 ANSI 转义序列和文本输出，容易出错且难以维护 2. 缺乏结构化协议: 传统 CLI 工具输出非结构化文本，Agent 难以可靠地提取工具调用、思考过程、文件变更等信息 3. 会话管理混乱: 多个 Agent 任务并行时，会话状态难以隔离和恢复 4. 权限控制缺失: 无法细粒度控制 Agent 的文件读写和命令执行权限 5. 跨 Agent 平台碎片化: 不同编码 Agent（OpenClaw、Codex、Claude Code 等）有各自的 CLI 接口，编排器需要适配多套协议

**Features:** 多轮对话, 历史记录, 崩溃恢复

---

### openclaw/openclaw-ansible

[openclaw/openclaw-ansible](https://github.com/openclaw/openclaw-ansible) | Stars: 481 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

1. 部署复杂度: OpenClaw 依赖多个组件（Node.js、pnpm、Docker、Tailscale、防火墙、systemd），手动安装容易出错且耗时 2. 安全风险: 默认配置可能暴露不必要的端口，缺乏防火墙和入侵防护 3. 环境一致性: 不同服务器的系统配置差异导致部署结果不一致 4. 权限管理: OpenClaw 需要特定的用户权限和 systemd 服务配置 5. 远程访问: 需要安全的远程访问方式，避免直接暴露服务端口 6. 自动更新: 缺乏自动安全补丁机制，增加维护负担

**Features:** 零配置, 快速, 幂等

---

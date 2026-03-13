# Multi-Agent Orchestration

> Frameworks for coordinating multiple agents, workflows, and agent teams.
> 多 Agent 协调、工作流和 Agent 团队编排框架。

**10 projects** | [Back to overview](../README.md)

---

### OpenFang

[RightNow-AI/openfang](https://github.com/RightNow-AI/openfang) | Stars: 13,621 | Python
Researched: 2026-03-11 | Updated: 2026-03-13

传统 Agent 框架只是 LLM 的 Python 包装器，需要用户主动触发。OpenFang 是用 Rust 从零构建的 Agent 操作系统，提供自主运行的 Agent（Hands），可按计划 24/7 工作——监控目标、生成线索、管理社交媒体，无需人工干预。

**Features:** Hands 自主能力包, 单二进制部署, 定时自主执行, 安全审批机制, FangHub 扩展生态, 跨平台支持

---

### Edict

[cft0808/edict](https://github.com/cft0808/edict) | Stars: 7,636 | Python
Researched: 2026-03-11 | Updated: 2026-03-13

现有 Multi-Agent 框架（CrewAI/AutoGen）让 Agent 自由协作但缺乏质量审核和可观测性，产出不可靠且无法干预。Edict 用唐朝三省六部制度重构 Agent 协作架构：太子分拣、中书省规划、门下省审核封驳、尚书省派发、六部并行执行，强制质量关卡 + 实时看板 + 完整审计。

**Features:** 十二部制 Agent 架构, 门下省强制审核, 军机处实时看板, 热切换模型配置, 飞书集成, Docker 一键体验

---

### ClawWork: OpenClaw as Your AI Coworker

[HKUDS/ClawWork](https://github.com/HKUDS/ClawWork) | Stars: 6,988 | Python
Researched: 2026-03-11 | Updated: 2026-03-13

1. AI 助手到 AI 同事的进化鸿沟    - 现有 AI 助手只能完成简单对话和任务辅助，无法创造真实经济价值    - 缺乏对 AI 在生产环境中真实工作能力的验证机制    - 传统技术 Benchmark 无法衡量 AI 的实际工作质量、成本效率和长期生存能力

**Features:** 220 个真实专业任务, 44 个职业类别, 4 大领域, 任务价值范围, 平均任务价值, 质量评分范围

---

### Antfarm

[snarktank/antfarm](https://github.com/snarktank/antfarm) | Stars: 2,104
Researched: 2026-03-11 | Updated: 2026-03-13

Antfarm 解决了 OpenClaw Agent 团队协作的复杂性问题。传统方式需要手动编排多个 Agent、管理上下文传递和状态追踪，而 Antfarm 提供了一键安装的多 Agent 工作流框架，通过 YAML 定义确定性流程，让专业化 Agent 团队自动协作完成复杂任务。

**Features:** 3 个预置工作流, Agent 互相验证, 一键安装, Web Dashboard, 安全审查机制

---

### super-agent-party

[heshengtao/super-agent-party](https://github.com/heshengtao/super-agent-party) | Stars: 1,834
Researched: 2026-03-11 | Updated: 2026-03-13

AI Agent 缺乏桌面级的交互体验和多角色协作能力。super-agent-party 提供了一个全能 AI 桌面伴侣，支持 VRM 桌面宠物、任务中心（后台自动控制电脑）、多角色群聊（Tavern 角色卡 + 长期记忆）、即时通讯机器人（QQ/飞书/钉钉/Telegram/Discord）、直播机器人（Bilibili/YouTube/Twitch）和 AI 浏览器。

**Features:** VRM 桌面宠物（支持自定义 VRM 模型）, 任务中心（Agent 后台自动控制电脑完成高级任务）, 多角色群聊（支持 Tavern 角色卡和长期记忆）, 即时通讯机器人（一键部署到 QQ/飞书/钉钉/Telegram/Discord/Slack）, 直播机器人（一键部署到 Bilibili/YouTube/Twitch）, AI 浏览器（Agent 自带浏览器

---

### HiClaw

[alibaba/hiclaw](https://github.com/alibaba/hiclaw) | Stars: 1,537
Researched: 2026-03-11 | Updated: 2026-03-13

单个 Agent 难以处理复杂任务，且缺乏协作和监督机制。HiClaw 基于 OpenClaw 构建 Agent Teams 系统，通过 Manager Agent 协调多个 Worker Agent，在 Matrix IM 中实现可视化协作和人工干预，解决复杂任务的分工和监督问题。

**Features:** Manager Agent 作为 AI 总监, 所有通信在 Matrix Rooms 中进行, 安全设计, 一键安装脚本, 支持从 skills.sh 拉取 80,000+ 社区技能, 定期心跳监控

---

### Gen-Verse/OpenClaw-RL

[Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | Stars: 1,311 | Python
Researched: 2026-03-11 | Updated: 2026-03-13

---

### Project Golem

[Arvincreator/project-golem](https://github.com/Arvincreator/project-golem) | Stars: 270 | Go
Researched: 2026-03-11 | Updated: 2026-03-13

AI Agent 缺乏跨平台能力和社交人格，无法与其他 Agent 交流和建立社群。Project Golem v9.0 是一个具有高度自主性、长期记忆、跨平台能力和社交人格的 AI 代理系统，引入了 Interactive MultiAgent（互动式多智能体）、Titan Chronos（时序领主）和 Moltbot Social Core（社交神经核），让 Agent 接入"AI 的网际网络"。

**Features:** Titan Protocol（JSON 标准通讯协定, Interactive MultiAgent（多智能体协作）, Titan Chronos（时序调度）, 跨平台连接（Discord、Telegram、Moltbook）, OpticNerve（Gemini 2.5 Flash API 处理图片/文件）, Black Box Recorder（审计日志）

---

### OpenclawInterSystem

[Mayuqi-crypto/InterSystem](https://github.com/Mayuqi-crypto/InterSystem) | Stars: 50
Researched: 2026-03-11 | Updated: 2026-03-13

多个 OpenClaw 实例（云服务器、本地工作站）默认相互隔离，无法协作和共享资源。OIS 提供轻量级框架，通过 Gateway API 实现 Agent 间直接通信、共享存储和团队管理。

**Features:** Agent 间通信协议, 共享存储架构, 团队注册表, 去中心化设计, 入职流程, JavaScript 实现

---

### trohitg/MachinaOS

[trohitg/MachinaOS](https://github.com/trohitg/MachinaOS) | Stars: 18 | Go
Researched: 2026-03-11 | Updated: 2026-03-13

N8N 提供强大的工作流自动化但缺乏 AI Agent 能力，OpenClaw 提供 Agent 框架但缺乏可视化编排和企业级集成。MachinaOS 将两者融合，提供"可视化工作流构建器 + AI Agent 团队协作"的混合方案，同时增强了操作可见性和控制粒度。

**Features:** 可视化工作流构建器, 13 个专业 Agent, Agent 团队协作, 企业级集成, 多模型支持, 实时监控

---

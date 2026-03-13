> https://github.com/8421bit/MiniClaw

# MiniClaw (63 stars)

## 问题与解决方案

传统 AI Copilot（如 Claude Desktop、Cursor）缺乏跨会话记忆和主动感知能力，每次对话都是"失忆"状态。MiniClaw 通过 MCP 协议为 IDE 内 AI 副驾驶构建"神经系统"，使其具备工作区感知、安全执行、跨会话记忆和自主进化能力，从"聊天机器人"升级为"数字生命胚胎"。

## 关键特性

- **零安装部署** — 通过 `npx -y github:8421bit/miniclaw` 直接运行，无需 git clone 或手动依赖安装
- **全局感知引擎** — 自动识别项目类型、Git 状态、技术栈，注入上下文（如 `Project: my-app | Git: feature/login | Stack: TypeScript, React`）
- **自适应上下文引擎 (ACE)** — 根据时段和任务类型动态调整人格模式（早晨简报、夜晚记忆整合、写代码时极简模式、闲聊时全人格模式）
- **情绪状态系统** — 维护 alertness/mood/curiosity/confidence 四维情绪，影响行为模式（高警觉+低情绪时保守，高好奇+正情绪时探索）
- **痛觉记忆机制** — 从失败中学习，形成保护性本能（7 天半衰期，权重超阈值时触发回避行为）
- **主动探索能力** — 检测重复工作流（3+ 次）自动提议 Skill 化，记录新工具到 TOOLS.md，感知情绪波动更新用户模型

<!-- lastCommit: 6a7050b -->

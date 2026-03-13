# OpenClaw Mini (555 stars)

## 问题与解决方案

OpenClaw Mini 解决了"OpenClaw 架构学习门槛高"的痛点。通过从 43 万行代码中提炼核心设计，提供最小化实现（核心层 + 扩展层 + 工程层三层分离），帮助开发者理解生产级 Agent 的系统级设计：双层循环 + EventStream 事件流、会话持久化（JSONL）、上下文管理（裁剪 + 摘要压缩）、长期记忆、技能系统、主动唤醒、多 Provider 适配（22+ 提供商）等，而非简单的 Agent Loop。

## 关键特性

- **三层架构分离** — 核心层（Agent Loop/EventStream/Session/Context/Tools/Provider，任何 Agent 必需）、扩展层（Memory/Skills/Heartbeat，OpenClaw 特有）、工程层（Session Key/Tool Policy/Command Queue，生产级防护）
- **双层循环 + EventStream** — Outer loop（follow-up 循环，处理 end_turn/tool_use 继续）+ Inner loop（工具执行 + steering injection），返回 EventStream（18 种类型化事件，异步推拉）
- **会话持久化（JSONL）** — Session 模块管理 JSONL 历史，支持加载、追加、裁剪
- **上下文管理三件套** — Loader（按需加载 AGENTS.md 等 bootstrap 文件）、Pruning（三层递进裁剪：tool_result → assistant → 保留最近）、Compaction（自适应分块摘要压缩）
- **长期记忆 + 技能系统 + 主动唤醒** — Memory（关键词检索 + 时间衰减）、Skills（SKILL.md frontmatter + 触发词匹配）、Heartbeat（wake 请求合并 + runner 调度）
- **多 Provider 适配** — 基于 pi-ai，支持 Anthropic/OpenAI/Google/Groq 等 22+ 提供商
- **工程层防护** — Session Key（多 agent 会话键规范化）、Tool Policy（三级访问控制）、Command Queue（并发 lane 控制）、Tool Result Guard（自动补齐缺失 tool_result）、Context Window Guard（上下文窗口溢出保护）

# 记忆系统

| # | 项目 | Stars | 简介 | 调研 |
|---|------|-------|------|------|
| 1 | memU | 12,811 | 解决了 24/7 长时运行 Agent 的两大核心问题：上下文窗口膨胀导致的 token 成本爆炸，以及被动响应模式无法主动理解用户意图。 | [memU.md](memU.md) |
| 2 | EverMemOS | 2,520 | EverMemOS 解决了 AI Agent 的长期记忆问题。 | [evermemos.md](evermemos.md) |
| 3 | memory-lancedb-pro | 2,030 | AI Agent 缺乏持久化的长期记忆能力，跨会话信息丢失严重。 | [memory-lancedb-pro.md](memory-lancedb-pro.md) |
| 4 | OpenClaw Supermemory | 579 | OpenClaw Supermemory 解决了 Agent"短期记忆限制"的痛点。 | [supermemory.md](supermemory.md) |
| 5 | PowerMem | 489 | AI 应用需要持久化记忆历史对话、用户偏好和上下文信息，但全上下文方案成本高、响应慢。 | [powermem.md](powermem.md) |
| 6 | openclaw-memory-fusion | 106 | OpenClaw 的记忆能力依赖模型自觉写入，聪明模型会主动记忆但多数模型不稳定，会话 compaction 后关键上下文易丢失。 | [memory-fusion.md](memory-fusion.md) |
| 7 | openclaw-memory-final | 94 | 生产环境的 AI 记忆系统需要处理增量更新、去重、稳定性监控和成本控制等工程问题，单纯的 LLM 记忆提取不足以支撑 7x24 运行。 | [memory-final.md](memory-final.md) |
| 8 | openclaw_memory_supersystem-v1.0 | 64 | OpenClaw 的 MEMORY.md 机制存在"乱棍打死老师傅"问题：对话变长后检索出大量相关度 80% 但无用的信息，导致 Token 消耗 300... | [memory-supersystem.md](memory-supersystem.md) |
| 9 | memu-engine-for-OpenClaw | 46 | OpenClaw 的单一 `memu.db` 存储导致多 Agent 记忆混杂、跨 Agent 检索规则模糊、共享文档与私有记忆无法隔离。 | [memu-engine.md](memu-engine.md) |
| 10 | openclaw-memory-architecture | 31 | AI Agent 的记忆系统通常只依赖单一的向量搜索，导致精确查询（如"我女儿的生日"）和模糊查询（如"上周关于部署的讨论"）都使用同一套机制，效率低下。 | [12layer-memory.md](12layer-memory.md) |
| 11 | openclaw-memory-management | 29 | AI Agent 记忆越多反而越"笨"，上下文 Token 消耗过大导致响应变慢且成本高昂。 | [memory-management.md](memory-management.md) |

> https://github.com/ktao732084/memory-supersystem

# openclaw_memory_supersystem-v1.0 (64 stars)

## 问题与解决方案

OpenClaw 的 MEMORY.md 机制存在"乱棍打死老师傅"问题：对话变长后检索出大量相关度 80% 但无用的信息，导致 Token 消耗 3000-8000 且精准度仅 60%。该项目受神经科学启发，构建三层记忆架构（工作记忆/长期记忆/事件日志）+ 7 阶段 Consolidation + Fact/Belief/Summary 分类，将 Token 消耗降至 <2000（↓60-75%），检索精准度提升至 90%（↑50%）。

## 关键特性

- **三层存储架构** — 工作记忆（SQLite 热存储）、长期记忆（JSONL 冷存储）、事件日志（原始对话），模拟人脑短期/长期记忆分离
- **7 阶段记忆整合** — 废话过滤 → 实体识别 → 冲突检测 → 记忆操作 (ADD/UPDATE/DELETE/NOOP) → 置信度标注 → 分类 (Fact/Belief/Summary) → 自动衰减
- **混合检索引擎** — 关键词 (BM25) + 向量 (GGUF 本地模型) + 分片索引 + 多级缓存，支持时序查询（"用户上周提到的 X"）
- **Memory Operator** — 92.9% 准确率的 CRUD 操作器，支持冲突消解协议（柔性降权而非硬删除）和虚假记忆过滤
- **时序引擎** — TemporalQueryEngine + FactEvolutionTracker + EvidenceTracker，追踪事实演变和证据链
- **QMD 语义搜索集成** — 支持 `qmd_search` + `router_search` 混合检索，Mini-Consolidate 白天轻量检查 + pending.jsonl 缓冲区

<!-- lastCommit: 6a7050b -->

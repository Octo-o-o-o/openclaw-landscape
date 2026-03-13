# Memory Systems

> Memory management, persistence, and retrieval systems for AI agents.
> AI Agent 的记忆管理、持久化和检索系统。

**11 projects** | [Back to overview](../README.md)

---

### memU

[NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) | Stars: 12,811
Researched: 2026-03-11 | Updated: 2026-03-13

解决了 24/7 长时运行 Agent 的两大核心问题：上下文窗口膨胀导致的 token 成本爆炸，以及被动响应模式无法主动理解用户意图。memU 通过文件系统式记忆架构和主动意图捕获，让 Agent 能够持续在线、低成本运行，并在用户未发出指令时就能预判需求并主动行动。

**Features:** 主动意图捕获, 主动任务执行, memU Bot, 记忆即文件系统, 可移植性

---

### EverMemOS

[EverMind-AI/EverMemOS](https://github.com/EverMind-AI/EverMemOS) | Stars: 2,520
Researched: 2026-03-11 | Updated: 2026-03-13

EverMemOS 解决了 AI Agent 的长期记忆问题。传统 Agent（包括 OpenClaw）的记忆局限于单次会话或短期上下文，无法跨会话、跨平台、跨 LLM 持久化和演化。EverMemOS 提供操作系统级的记忆层，支持 24/7 运行的 Agent 持续学习、记忆共享、跨平台迁移，已集成 OpenClaw、Live2D 角色、TEN Framework 等场景。

**Features:** 跨平台记忆, 持续学习, 记忆演化, 多存储后端, OpenClaw 集成, Memory Genesis Competition 2026

---

### memory-lancedb-pro

[CortexReach/memory-lancedb-pro](https://github.com/CortexReach/memory-lancedb-pro) | Stars: 2,030
Researched: 2026-03-11 | Updated: 2026-03-13

AI Agent 缺乏持久化的长期记忆能力，跨会话信息丢失严重。memory-lancedb-pro 为 OpenClaw 提供生产级长期记忆插件，通过混合检索（Vector + BM25）、交叉编码器重排序、Weibull 衰减和三层晋升机制，实现智能记忆提取、生命周期管理和多作用域隔离。

**Features:** 混合检索（Vector + BM25 全文搜索 + Cross-Encoder 重排序）, LLM 驱动的 6 类记忆自动提取（无需手动 `memory_store`）, Weibull 衰减 + 三层晋升机制（重要记忆浮现, 多作用域隔离（per-agent、per-user、per-project 记忆边界）, 支持任意 Embedding 提供商（OpenAI、Jina、Gemini、Ollama）, 完整运维工具（CLI、备份、迁移、升级、导入导出）

---

### OpenClaw Supermemory

[supermemoryai/openclaw-supermemory](https://github.com/supermemoryai/openclaw-supermemory) | Stars: 579
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw Supermemory 解决了 Agent"短期记忆限制"的痛点。通过 Supermemory 云服务（需 Pro 及以上订阅），为 OpenClaw Agent 提供长期记忆能力：自动记忆对话、召回相关上下文、构建持久化用户档案，无需本地基础设施。Auto-Recall（每轮 AI 前查询相关记忆并注入上下文）+ Auto-Capture（每轮 AI 后发送对话到云端提取和去重）+ 自定义容器标签（work/personal/bookmarks 等，AI 自动路由）实现全自动记忆管理。

**Features:** 云端长期记忆, Auto-Recall 自动召回, Auto-Capture 自动捕获, 自定义容器标签, Slash 命令 + AI 工具, CLI 管理

---

### PowerMem

[oceanbase/powermem](https://github.com/oceanbase/powermem) | Stars: 489
Researched: 2026-03-11 | Updated: 2026-03-13

AI 应用需要持久化记忆历史对话、用户偏好和上下文信息，但全上下文方案成本高、响应慢。PowerMem 结合向量检索、全文搜索、图数据库的混合架构，引入 Ebbinghaus 遗忘曲线理论，在 LOCOMO 基准测试中实现 48.77% 准确率提升、91.83% 延迟降低、96.53% Token 成本削减。

**Features:** 混合检索架构, Ebbinghaus 遗忘曲线, 智能记忆提取, 多 Agent 支持, 多模态支持, Sub Stores 分区

---

### openclaw-memory-fusion

[dztabel-happy/openclaw-memory-fusion](https://github.com/dztabel-happy/openclaw-memory-fusion) | Stars: 106
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 的记忆能力依赖模型自觉写入，聪明模型会主动记忆但多数模型不稳定，会话 compaction 后关键上下文易丢失。memory-fusion 用三层 cron（hourly/daily/weekly）做系统级自动提取/蒸馏/巩固，将"重要对话 → 可检索知识"变成可运维流程，实现"永不失忆"。

**Features:** 三层 cron 架构, 增量游标机制, 防套娃硬约束, 高信噪比输入, A′ 滚动区, 可运维设计

---

### openclaw-memory-final

[codesfly/openclaw-memory-final](https://github.com/codesfly/openclaw-memory-final) | Stars: 94
Researched: 2026-03-11 | Updated: 2026-03-13

生产环境的 AI 记忆系统需要处理增量更新、去重、稳定性监控和成本控制等工程问题，单纯的 LLM 记忆提取不足以支撑 7x24 运行。memory-final 提供面向生产的记忆架构：日增量蒸馏 + 周精炼 + 幂等去重 + watchdog 守护 + QMD 索引 + 上下文预算控制，确保记忆系统的可靠性和成本可控性。

**Features:** 分层记忆管道, 子 Agent 任务卡索引, 幂等捕获, 低噪声告警, 成本感知索引, 上下文预算控制

---

### openclaw_memory_supersystem-v1.0

[ktao732084/memory-supersystem](https://github.com/ktao732084/memory-supersystem) | Stars: 64
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 的 MEMORY.md 机制存在"乱棍打死老师傅"问题：对话变长后检索出大量相关度 80% 但无用的信息，导致 Token 消耗 3000-8000 且精准度仅 60%。该项目受神经科学启发，构建三层记忆架构（工作记忆/长期记忆/事件日志）+ 7 阶段 Consolidation + Fact/Belief/Summary 分类，将 Token 消耗降至 <2000（↓60-75%），检索精准度提升至 90%（↑50%）。

**Features:** 三层存储架构, 7 阶段记忆整合, 混合检索引擎, Memory Operator, 时序引擎, QMD 语义搜索集成

---

### memu-engine-for-OpenClaw

[duxiaoxiong/memu-engine](https://github.com/duxiaoxiong/memu-engine) | Stars: 46
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 的单一 `memu.db` 存储导致多 Agent 记忆混杂、跨 Agent 检索规则模糊、共享文档与私有记忆无法隔离。v0.3.1 通过 per-agent 内存布局（每个 Agent 独立 DB）+ 显式共享存储（`memory/shared/memu.db`）+ 可配置检索策略（`searchableStores`），实现记忆隔离、共享文档分离、跨 Agent 检索显式控制。

**Features:** Per-Agent 内存布局, 显式共享存储, 统一运行时布局, 自动升级迁移, MemU 提取管道, 零依赖启动

---

### openclaw-memory-architecture

[coolmanns/12layer-memory](https://github.com/coolmanns/12layer-memory) | Stars: 31
Researched: 2026-03-11 | Updated: 2026-03-13

AI Agent 的记忆系统通常只依赖单一的向量搜索，导致精确查询（如"我女儿的生日"）和模糊查询（如"上周关于部署的讨论"）都使用同一套机制，效率低下。该项目提出 12 层记忆架构，结合结构化存储、语义搜索、知识图谱和认知模式，为不同类型的记忆召回选择最优策略。

**Features:** 12 层分层架构, 统一搜索接口, 知识图谱集成, 语义搜索优化, 激活衰减系统, LightRAG 领域知识库

---

### openclaw-memory-management

[jzOcb/memory-management](https://github.com/jzOcb/memory-management) | Stars: 29
Researched: 2026-03-11 | Updated: 2026-03-13

AI Agent 记忆越多反而越"笨"，上下文 Token 消耗过大导致响应变慢且成本高昂。该项目基于 @ohxiyu 的 P0/P1/P2 优先级体系，通过自动归档和分层记忆管理，将 Token 使用量降低 78%（从 6,618 降至 1,488），同时保持记忆的准确性和可访问性。

**Features:** 三层优先级体系, 自动归档机制, 结构化 Lessons 存储, 核心原则精简, 干运行模式, 多集成方式

---

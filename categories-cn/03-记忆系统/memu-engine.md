# memu-engine-for-OpenClaw (46 stars)

## 问题与解决方案

OpenClaw 的单一 `memu.db` 存储导致多 Agent 记忆混杂、跨 Agent 检索规则模糊、共享文档与私有记忆无法隔离。v0.3.1 通过 per-agent 内存布局（每个 Agent 独立 DB）+ 显式共享存储（`memory/shared/memu.db`）+ 可配置检索策略（`searchableStores`），实现记忆隔离、共享文档分离、跨 Agent 检索显式控制。

## 关键特性

- **Per-Agent 内存布局** — 每个 Agent 写入独立 DB（`memory/<agent>/memu.db`），默认记忆隔离，避免跨 Agent 污染
- **显式共享存储** — 共享文档存储在 `memory/shared/memu.db`，通过 `agentSettings.searchableStores` 控制跨 Agent 检索权限
- **统一运行时布局** — 所有数据集中在 `~/.openclaw/memUdata/`（conversations/resources/memory/state），便于备份、迁移、清理
- **自动升级迁移** — 从 v0.2.6 单 DB 布局自动迁移到 v0.3.1 per-agent 布局，备份优先（backup-first behavior）
- **MemU 提取管道** — 基于 MemU 上游项目，从对话日志和 Markdown 文档提取 profiles/events/knowledge/skills/behavior signals
- **零依赖启动** — 通过 `uv sync` 自动引导隔离 Python 环境（`python/.venv`），从 `python/uv.lock` 安装锁定依赖

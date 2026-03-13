> https://github.com/supermemoryai/openclaw-supermemory

# OpenClaw Supermemory (579 stars)

## 问题与解决方案

OpenClaw Supermemory 解决了 Agent"短期记忆限制"的痛点。通过 Supermemory 云服务（需 Pro 及以上订阅），为 OpenClaw Agent 提供长期记忆能力：自动记忆对话、召回相关上下文、构建持久化用户档案，无需本地基础设施。Auto-Recall（每轮 AI 前查询相关记忆并注入上下文）+ Auto-Capture（每轮 AI 后发送对话到云端提取和去重）+ 自定义容器标签（work/personal/bookmarks 等，AI 自动路由）实现全自动记忆管理。

## 关键特性

- **云端长期记忆** — 基于 Supermemory 云服务，自动提取、去重、构建用户档案，无需本地部署
- **Auto-Recall 自动召回** — 每轮 AI 前查询语义相似的历史对话和用户档案，注入为上下文（默认最多 10 条）
- **Auto-Capture 自动捕获** — 每轮 AI 后发送对话到云端，提取关键信息并长期存储（支持 `all` 过滤短文本或 `everything` 全捕获）
- **自定义容器标签** — 定义 work/personal/bookmarks 等容器，AI 根据指令自动选择容器（如"存储工作任务到 work"）
- **Slash 命令 + AI 工具** — `/remember <text>` 手动保存、`/recall <query>` 搜索记忆，AI 自主使用 `supermemory_store`/`search`/`forget`/`profile` 工具
- **CLI 管理** — `openclaw supermemory setup` 配置 API Key、`status` 查看配置、`search <query>` 搜索记忆、`profile` 查看用户档案、`wipe` 删除所有记忆
- **灵活配置** — 支持环境变量（`SUPERMEMORY_OPENCLAW_API_KEY`）或 `~/.openclaw/openclaw.json` 配置，可调整召回数量、档案注入频率、捕获模式等

<!-- lastCommit: 6a7050b -->

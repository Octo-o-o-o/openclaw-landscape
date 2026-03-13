> https://github.com/jzOcb/memory-management

# openclaw-memory-management (29 stars)

## 问题与解决方案

AI Agent 记忆越多反而越"笨"，上下文 Token 消耗过大导致响应变慢且成本高昂。该项目基于 @ohxiyu 的 P0/P1/P2 优先级体系，通过自动归档和分层记忆管理，将 Token 使用量降低 78%（从 6,618 降至 1,488），同时保持记忆的准确性和可访问性。

## 关键特性

- **三层优先级体系** — P0（核心身份，永不过期）、P1（活跃项目，90 天 TTL）、P2（临时记忆，30 天 TTL）
- **自动归档机制** — 通过 cron 定时任务自动将过期记忆迁移至 archive 目录，保持热记忆文件精简（≤200 行）
- **结构化 Lessons 存储** — 将经验教训以 JSONL 格式存储，支持语义搜索而非全量加载
- **核心原则精简** — 将 17 条分散规则压缩为 5 条核心原则（AGENTS.md），其余存入可检索的 lessons 库
- **干运行模式** — 提供 `--dry-run` 和 `--stats` 参数，支持预览归档操作和统计分析
- **多集成方式** — 支持 OpenClaw Skill、Claude Code 规则文件等多种集成方式

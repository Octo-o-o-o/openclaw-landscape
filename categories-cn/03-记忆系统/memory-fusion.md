# openclaw-memory-fusion (106 stars)

## 问题与解决方案

OpenClaw 的记忆能力依赖模型自觉写入，聪明模型会主动记忆但多数模型不稳定，会话 compaction 后关键上下文易丢失。memory-fusion 用三层 cron（hourly/daily/weekly）做系统级自动提取/蒸馏/巩固，将"重要对话 → 可检索知识"变成可运维流程，实现"永不失忆"。

## 关键特性

- **三层 cron 架构** — L1 hourly（微同步，5 次/天）、L2 daily（23:30 canonical + A′ 滚动 7 天）、L3 weekly（00:20 gate，分类治理 + 晋升）
- **增量游标机制** — 按 byte offset 读取 `~/.openclaw/agents/<agent>/sessions/*.jsonl`，不丢不重，容忍半行 JSON
- **防套娃硬约束** — cron prompt 以 `[cron:` 开头，扫描器忽略 cron 会话和通知文本，验证方式：重复跑 hourly 应收敛到 `events: 0`
- **高信噪比输入** — 仅提取 `role=user`（意图/决策/偏好）和 `role=assistant`（最终结论），跳过 tool-call 和工具回显
- **A′ 滚动区** — daily 维护 `MEMORY.md#近期重要更新（滚动 7 天）`（<= 30 条），weekly 晋升长期有效内容到正式分类
- **可运维设计** — 锁机制（避免并发覆盖）+ weekly gate（每周至少成功一次）+ Telegram 通知面板（统一 `events/updated/coverage` 格式）

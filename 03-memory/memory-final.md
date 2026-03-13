# openclaw-memory-final (94 stars)

## 问题与解决方案

生产环境的 AI 记忆系统需要处理增量更新、去重、稳定性监控和成本控制等工程问题，单纯的 LLM 记忆提取不足以支撑 7x24 运行。memory-final 提供面向生产的记忆架构：日增量蒸馏 + 周精炼 + 幂等去重 + watchdog 守护 + QMD 索引 + 上下文预算控制，确保记忆系统的可靠性和成本可控性。

## 关键特性

- **分层记忆管道** — 短期工作台（CURRENT_STATE）+ 日增量蒸馏（memory/YYYY-MM-DD.md）+ 周精炼（MEMORY.md + 周报归档）
- **子 Agent 任务卡索引** — 隔离会话的执行结果以任务卡形式写入 `memory/tasks/YYYY-MM-DD.md`，先查任务卡再做语义检索
- **幂等捕获** — 消息指纹游标（`processed-sessions.json`），避免重复处理
- **低噪声告警** — 仅在连续 2 次异常后告警，过滤偶发故障
- **成本感知索引** — daily 仅 `qmd update`（BM25），weekly 才 `qmd update && qmd embed`（向量化）
- **上下文预算控制** — 硬性限制单文件和总注入记忆字符数，防止 token 超限
- **动态 profile 注入** — 根据 profile（main/ops/btc/quant）加载最小上下文包
- **冲突检测** — 持久化记忆变更前扫描路由/规则漂移
- **检索 watchdog + 夜间维护** — 30 分钟健康检查 + 每日 03:20 `qmd update`/条件 `embed`

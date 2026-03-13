> https://github.com/zscole/model-hierarchy-skill

# model-hierarchy-skill (329 stars)

## 问题与解决方案

AI Agent 默认将所有任务路由到昂贵模型（如 Claude Opus $15-75/M tokens），但 80% 的任务是常规操作（文件读取、状态检查、格式化），用廉价模型（$0.14/M tokens）即可完成。model-hierarchy-skill 通过任务复杂度分类实现成本优化路由，在保持质量的前提下降低约 10 倍成本。

## 关键特性

- **三层模型分级** — ROUTINE（80%，$0.14-0.50/M）、MODERATE（15%，$1-5/M）、COMPLEX（5%，$10-75/M）
- **任务分类规则** — 文件操作/查询/格式化 → 廉价模型；代码生成/摘要 → 中档模型；调试/架构设计 → 高级模型
- **跨平台适配** — 提供 OpenClaw SKILL.md、Claude Code/Codex 项目指令、通用 Agent 系统集成示例
- **成本测算工具** — 基于 100K tokens/天的月度成本对比（纯 Opus $225 vs 分层 $19）
- **pytest 测试套件** — `tests/test_classification.py` + `scenarios.json` 验证分类准确性
- **子 Agent 默认策略** — 建议子 Agent 默认使用廉价模型，仅在任务失败时升级

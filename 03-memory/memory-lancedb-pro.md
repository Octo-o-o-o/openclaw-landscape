# memory-lancedb-pro (2,030 stars)

## 问题与解决方案
AI Agent 缺乏持久化的长期记忆能力，跨会话信息丢失严重。memory-lancedb-pro 为 OpenClaw 提供生产级长期记忆插件，通过混合检索（Vector + BM25）、交叉编码器重排序、Weibull 衰减和三层晋升机制，实现智能记忆提取、生命周期管理和多作用域隔离。

## 关键特性
- 混合检索（Vector + BM25 全文搜索 + Cross-Encoder 重排序）
- LLM 驱动的 6 类记忆自动提取（无需手动 `memory_store`）
- Weibull 衰减 + 三层晋升机制（重要记忆浮现，陈旧记忆淡化）
- 多作用域隔离（per-agent、per-user、per-project 记忆边界）
- 支持任意 Embedding 提供商（OpenAI、Jina、Gemini、Ollama）
- 完整运维工具（CLI、备份、迁移、升级、导入导出）

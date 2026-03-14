> https://github.com/stellarlinkco/myclaw

# stellarlinkco/myclaw (236 stars)

## 问题与解决方案

完整的 OpenClaw 部署过于复杂，用户需要轻量级的"个人 Agent 助手"快速上手。MyClaw 提供最小化的 clawbot 实现，专注于核心 Agent 能力（对话、工具调用、记忆），去除企业级功能（多租户、权限管理），适合个人开发者和小团队。

## 关键特性

- **轻量级架构** — 单文件或最小依赖部署，无需 Docker Compose 或复杂配置，5 分钟内启动
- **核心 Agent 能力** — 支持多轮对话、工具调用（文件操作、网络请求、代码执行）、短期/长期记忆
- **模型灵活性** — 支持 OpenAI、Claude、Gemini、本地 LLM（Ollama），通过环境变量切换
- **技能系统** — 兼容 OpenClaw SKILL.md 格式，可直接复用社区技能（如 awesome-openclaw-skills）
- **本地优先** — 数据存储在本地 SQLite/JSON，无需外部数据库或云服务
- **开发者友好** — 提供 Python API 和 CLI 两种使用方式，易于集成到现有工作流

<!-- lastCommit: 6901071 -->

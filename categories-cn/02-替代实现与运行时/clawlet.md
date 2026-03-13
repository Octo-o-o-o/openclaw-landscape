# clawlet (657 stars)

## 问题与解决方案

传统 AI 助手依赖复杂运行时（Node.js/Python）和外部数据库，部署繁琐且资源占用高。clawlet 用 Go 编译为单一静态二进制（无 CGO、无运行时依赖），内嵌 SQLite + sqlite-vec，实现开箱即用的混合语义记忆搜索，一个文件即可在任意机器上运行。

## 关键特性

- **零依赖部署** — 单一静态二进制，内嵌 SQLite + sqlite-vec，无需安装数据库或运行时
- **多 LLM 提供商** — 支持 OpenAI/OpenRouter/Anthropic/Gemini/Ollama/vLLM，统一配置接口
- **OAuth 无密钥登录** — OpenAI Codex 支持设备码流程（`--device-code`），适合 SSH/容器环境
- **混合语义搜索** — BM25 + 向量检索内置，记忆查询无需外部服务
- **灵活配置** — JSON 配置文件（`~/.clawlet/config.json`），支持环境变量和模型默认参数覆盖
- **本地模型优先** — Ollama/vLLM 路由统一为 `ollama/<model>` 前缀，自动适配 OpenAI 兼容端点

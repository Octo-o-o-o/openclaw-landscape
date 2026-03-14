> https://github.com/nearai/ironclaw

# IronClaw (9,108 stars)

## 问题与解决方案
现有 AI 助手数据处理不透明、与企业利益绑定、存在隐私泄露风险。IronClaw 用 Rust 重写 OpenClaw 核心，强调隐私优先（本地存储 + 加密）、透明可审计（开源 + 无遥测）、自扩展能力（动态构建工具）、多层安全防护（WASM 沙箱 + prompt injection 防御）。

## 核心架构
- **WASM 沙箱**：不可信工具运行在隔离的 WebAssembly 容器，基于能力的权限模型（HTTP / secrets / tool invocation 显式授权）
- **Credential 保护**：secrets 在宿主边界注入，WASM 代码不可见，请求/响应双向泄漏检测
- **Docker 沙箱**：隔离容器执行，per-job token，orchestrator/worker 模式
- **混合搜索**：全文 + 向量搜索 + Reciprocal Rank Fusion，workspace 文件系统，identity files
- **多通道**：REPL / HTTP webhooks / WASM channels (Telegram / Slack) / Web Gateway (SSE/WebSocket 流式)
- **Routines**：Cron 调度 / 事件触发 / webhook 处理，后台自动化
- **Self-repair**：自动检测和恢复卡住的操作

## 关键特性
- Rust 实现：内存安全、高性能、并发友好
- 安全优先：WASM 沙箱 + endpoint allowlist + leak detection + prompt injection 防御 + rate limiting
- 动态工具构建：描述需求，IronClaw 自动构建 WASM 工具
- MCP 协议支持：连接 Model Context Protocol 服务器
- 多 LLM 后端：NEAR AI（默认）/ OpenRouter / Together AI / Fireworks AI / Ollama / vLLM / LiteLLM
- 持久化内存：PostgreSQL + pgvector，混合搜索
- 并行任务：多请求并发处理，隔离上下文

<!-- lastCommit: f9b880c -->

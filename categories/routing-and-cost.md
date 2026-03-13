# LLM Routing & Cost Optimization

> Smart model routing, token optimization, and cost management.
> 智能模型路由、Token 优化和成本管理。

**6 projects** | [Back to overview](../README.md)

---

### ClawRouter

[BlockRunAI/ClawRouter](https://github.com/BlockRunAI/ClawRouter) | Stars: 5,352
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 将所有请求发送到同一模型，小任务也调用大模型导致成本浪费。ClawRouter 是 Agent 原生的 LLM 路由器，通过 15 维度评分算法在 <1ms 内将请求路由到最合适的模型，支持 41+ 模型，使用 x402 协议的 USDC 非托管支付（Base/Solana），节省 74-100% 成本。

**Features:** 本地路由引擎, 四种路由策略, 41+ 模型支持, 图像生成集成, x402 非托管支付, OpenClaw 插件

---

### Manifest

[mnfst/manifest](https://github.com/mnfst/manifest) | Stars: 3,733
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 将所有请求发送到同一模型，小任务也调用大模型导致成本浪费。Manifest 是 OpenClaw 插件，通过 23 维度评分算法在 <2ms 内将请求路由到最合适的模型，节省高达 70% 成本。提供 Cloud 和 Local 两种部署模式，Local 模式所有数据留在本地，Cloud 模式仅传输 OpenTelemetry 元数据（不含消息内容）。

**Features:** 23 维度路由算法, Cloud/Local 双模式, OTLP 原生支持, 零编码安装, 隐私优先架构, 匿名产品分析

---

### Antigravity-Claude-Proxy

[badrisnarayanan/antigravity](https://github.com/badrisnarayanan/antigravity) | Stars: 3,107 | Go
Researched: 2026-03-11 | Updated: 2026-03-13

Antigravity-Claude-Proxy 解决了 Claude/Gemini 模型在 OpenClaw/Claude Code 中的接入成本问题。通过代理 Antigravity Cloud Code 的免费 Claude/Gemini 配额，将 Google Generative AI 格式转换为 Anthropic Messages API 格式，使 OpenClaw 用户无需付费 API Key 即可使用 Claude/Gemini 模型。但存在 Google ToS 违规风险，部分用户账号被封禁。

**Features:** Anthropic API 兼容, 双模型支持, 多账号管理, Web Dashboard, 后台运行, ToS 风险警告

---

### openclaw-zero-token

[linuxhsj/zero-token](https://github.com/linuxhsj/zero-token) | Stars: 1,450
Researched: 2026-03-11 | Updated: 2026-03-13

使用 AI 模型需要购买 API Token，存在成本和信用卡绑定门槛。该项目通过浏览器自动化捕获会话凭证，实现免费访问 ChatGPT、Claude、Gemini、DeepSeek、Qwen、Doubao、Kimi、GLM、Grok、Manus 等主流 AI 平台，消除 API Token 成本。

**Features:** 通过 Playwright 浏览器自动化捕获会话凭证, 所有模型支持本地工具调用（exec、read_file、list_dir、browser、apply_patch）, AskOnce 功能, 凭证本地存储, 提供一键安装脚本和完整文档

---

### Tokscale

[junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) | Stars: 1,090 | Rust
Researched: 2026-03-11 | Updated: 2026-03-13

Tokscale 解决了 AI 辅助开发时代"Token 消耗不可见"的痛点。通过统一解析 15+ AI 编码工具（OpenCode/Claude Code/OpenClaw/Cursor/Codex/Gemini/Amp/Droid/Pi/Kimi 等）的本地会话数据（`~/.openclaw/agents/`、`~/.claude/projects/` 等），结合 LiteLLM 实时定价数据（支持分层定价和缓存折扣），提供跨平台 Token 使用追踪、成本计算、可视化仪表板和全球排行榜。

**Features:** 15+ AI 工具统一追踪, 原生 Rust TUI + 跨平台, 实时定价计算, 3D 贡献图 + Wrapped 2025, 全球排行榜 + 公开档案, 按平台/日期过滤

---

### model-hierarchy-skill

[zscole/model-hierarchy-skill](https://github.com/zscole/model-hierarchy-skill) | Stars: 329
Researched: 2026-03-11 | Updated: 2026-03-13

AI Agent 默认将所有任务路由到昂贵模型（如 Claude Opus $15-75/M tokens），但 80% 的任务是常规操作（文件读取、状态检查、格式化），用廉价模型（$0.14/M tokens）即可完成。model-hierarchy-skill 通过任务复杂度分类实现成本优化路由，在保持质量的前提下降低约 10 倍成本。

**Features:** 三层模型分级, 任务分类规则, 跨平台适配, 成本测算工具, pytest 测试套件, 子 Agent 默认策略

---

> https://github.com/HKUDS/nanobot

# nanobot (32,038 stars)

## 问题与解决方案
OpenClaw 功能强大但代码复杂（数万行），难以理解、修改和扩展。nanobot 用 ~4,000 行核心代码实现 OpenClaw 核心功能（99% 代码量减少），专注轻量化、研究友好、快速迭代。

## 核心架构
- **Provider 层**：统一 LLM 接口（OpenRouter / OpenAI / Claude / DeepSeek / Qwen / Moonshot / vLLM / Azure / VolcEngine），2 步添加新 provider
- **Channel 层**：多平台接入（Telegram / Discord / Slack / Feishu / DingTalk / QQ / Email / WhatsApp / Matrix / CLI）
- **MCP 协议**：Model Context Protocol 支持，连接外部工具和数据源
- **Memory 系统**：混合搜索（全文 + 向量 + Reciprocal Rank Fusion），workspace 文件系统，identity files
- **Heartbeat 机制**：虚拟 tool-call 心跳，防止长时间静默导致超时
- **Cron 调度**：自然语言任务调度，支持定时提醒和自动化

## 关键特性
- 超轻量：核心 agent 代码 ~4,000 行（可运行 `bash core_agent_lines.sh` 实时验证）
- 快速启动：`uv tool install nanobot-ai` + `nanobot onboard` + `nanobot agent` 三步启动
- 多模态支持：跨 channel 的文件/图片/语音接收和发送
- Prompt caching：Anthropic prompt cache 优化，降低 token 消耗
- 安全加固：session 隔离、输入验证、路径遍历防护、配置加密
- 研究友好：代码清晰可读，易于理解和修改

<!-- lastCommit: 6a7050b -->

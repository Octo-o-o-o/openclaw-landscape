> https://github.com/destinyfrancis/knowledge-distiller

# openclaw-knowledge-distiller (43 stars)

## 问题与解决方案

研究者和学生需要快速消化大量视频内容（YouTube/Bilibili/Facebook），但手动观看耗时且难以结构化。该项目通过本地 ASR（Qwen3-ASR MLX）+ AI 摘要（Gemini/OpenAI/Anthropic），将视频秒速转化为结构化知识文章，支持 8 种摘要风格（学术笔记、投资分析、播客摘要等），完全本地运行且免费。

## 关键特性

- **智能字幕检测** — 优先提取现有字幕（跳过 ASR 加速处理），无字幕时自动下载音频并本地转录（Qwen3-ASR MLX，Apple Silicon 优化）
- **零 API 密钥模式** — `--no-summary` 参数实现纯本地转录，无需外部服务（模型 1-2 GB 首次自动下载）
- **8 种摘要风格** — Standard/Academic/Action List/News Brief/Investment Analysis/Podcast Digest/ELI5/Bullet Notes，通过 `--style` 参数切换
- **多语言支持** — 粤语/普通话/英语/日语/韩语等 50+ 语言，支持方言提示（如 `--asr-prompt "這是粵語口語對話，請保留懶音"`）
- **MCP Server 集成** — 可从 Claude Code、OpenClaw 或任何 MCP 兼容 Agent 调用，实现视频处理自动化
- **多 AI 提供商** — 支持 Google Gemini（默认）、OpenAI、Anthropic，通过 `--provider` 和 `--model` 参数切换

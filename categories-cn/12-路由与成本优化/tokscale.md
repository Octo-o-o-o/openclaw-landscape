> https://github.com/junhoyeo/tokscale

# Tokscale (1,090 stars)

## 问题与解决方案

Tokscale 解决了 AI 辅助开发时代"Token 消耗不可见"的痛点。通过统一解析 15+ AI 编码工具（OpenCode/Claude Code/OpenClaw/Cursor/Codex/Gemini/Amp/Droid/Pi/Kimi 等）的本地会话数据（`~/.openclaw/agents/`、`~/.claude/projects/` 等），结合 LiteLLM 实时定价数据（支持分层定价和缓存折扣），提供跨平台 Token 使用追踪、成本计算、可视化仪表板和全球排行榜。

## 关键特性

- **15+ AI 工具统一追踪** — 支持 OpenCode/Claude Code/OpenClaw/Cursor/Codex/Gemini/Amp/Droid/Pi/Kimi/Qwen/Roo Code/Kilo/Mux/Synthetic，自动解析本地会话数据（JSONL/SQLite/JSON）
- **原生 Rust TUI + 跨平台** — 高性能终端界面（Overview/Models/Daily Summary/Stats 四视图），支持 macOS/Linux/Windows（含 WSL2）
- **实时定价计算** — 基于 LiteLLM 定价数据，支持分层定价模型和缓存 Token 折扣，精确到模型版本
- **3D 贡献图 + Wrapped 2025** — Web 前端可视化（类似 GitHub 贡献图），年度总结报告（按 Agent/模型/日期维度统计）
- **全球排行榜 + 公开档案** — `bunx tokscale@latest submit` 提交数据到排行榜，生成公开个人档案（类似 Kardashev 文明等级）
- **按平台/日期过滤** — `tokscale --platform openclaw --since 2025-01-01 --until 2025-03-11` 灵活筛选
- **Cursor IDE 专项支持** — API 同步缓存（`~/.config/tokscale/cursor-cache/`），`tokscale cursor sync` 命令

<!-- lastCommit: b1d8585 -->

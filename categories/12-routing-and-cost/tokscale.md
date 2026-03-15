> https://github.com/junhoyeo/tokscale

# Tokscale (1,090 stars)

## Problem & Solution

Tokscale addresses the pain point of "invisible token consumption" in the AI-assisted development era. By uniformly parsing local session data from 15+ AI coding tools (OpenCode/Claude Code/OpenClaw/Cursor/Codex/Gemini/Amp/Droid/Pi/Kimi, etc.) located in directories like `~/.openclaw/agents/` and `~/.claude/projects/`, combined with LiteLLM real-time pricing data (supporting tiered pricing and cache discounts), it provides cross-platform token usage tracking, cost calculation, visualization dashboards, and global leaderboards.

## Key Features

- **15+ AI Tool Unified Tracking** — Supports OpenCode/Claude Code/OpenClaw/Cursor/Codex/Gemini/Amp/Droid/Pi/Kimi/Qwen/Roo Code/Kilo/Mux/Synthetic, auto-parsing local session data (JSONL/SQLite/JSON)
- **Native Rust TUI + Cross-Platform** — High-performance terminal interface (Overview/Models/Daily Summary/Stats four views), supports macOS/Linux/Windows (including WSL2)
- **Real-Time Pricing Calculation** — Based on LiteLLM pricing data, supports tiered pricing models and cached token discounts, precise to model version
- **3D Contribution Graph + Wrapped 2025** — Web frontend visualization (similar to GitHub contribution graph), annual summary report (statistics by Agent/model/date dimensions)
- **Global Leaderboard + Public Profiles** — `bunx tokscale@latest submit` to submit data to leaderboard, generates public profiles (similar to Kardashev civilization scale)
- **Platform/Date Filtering** — `tokscale --platform openclaw --since 2025-01-01 --until 2025-03-11` for flexible filtering
- **Cursor IDE Dedicated Support** — API sync cache (`~/.config/tokscale/cursor-cache/`), `tokscale cursor sync` command

<!-- lastCommit: a680fc081cbb637e62211b1ea44740de4ec9bb69 -->

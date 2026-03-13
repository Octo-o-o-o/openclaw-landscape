> https://github.com/destinyfrancis/knowledge-distiller

# openclaw-knowledge-distiller (43 stars)

## Problem & Solution

Researchers and students need to quickly digest large volumes of video content (YouTube/Bilibili/Facebook), but manual viewing is time-consuming and hard to structure. This project uses local ASR (Qwen3-ASR MLX) + AI summarization (Gemini/OpenAI/Anthropic) to convert videos into structured knowledge articles in seconds, supporting 8 summary styles (academic notes, investment analysis, podcast digest, etc.), running entirely locally and for free.

## Key Features

- **Smart subtitle detection** — Prioritizes extracting existing subtitles (skipping ASR to speed up processing); when no subtitles are available, automatically downloads audio and transcribes locally (Qwen3-ASR MLX, optimized for Apple Silicon)
- **Zero API key mode** — The `--no-summary` parameter enables pure local transcription without any external services (model is 1-2 GB, auto-downloaded on first run)
- **8 summary styles** — Standard/Academic/Action List/News Brief/Investment Analysis/Podcast Digest/ELI5/Bullet Notes, switchable via the `--style` parameter
- **Multilingual support** — Cantonese/Mandarin/English/Japanese/Korean and 50+ languages, with dialect prompting support (e.g., `--asr-prompt "This is Cantonese colloquial conversation, please preserve lazy pronunciation"`)
- **MCP Server integration** — Can be invoked from Claude Code, OpenClaw, or any MCP-compatible Agent for automated video processing
- **Multiple AI providers** — Supports Google Gemini (default), OpenAI, and Anthropic, switchable via `--provider` and `--model` parameters

<!-- lastCommit: 6a7050b -->

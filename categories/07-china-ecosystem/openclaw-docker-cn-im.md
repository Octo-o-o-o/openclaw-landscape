> https://github.com/justlovemaki/docker-cn-im

# OpenClaw-Docker-CN-IM (3,126 stars)

## Problem & Solution
OpenClaw natively does not support China's mainstream IM platforms (Feishu/Lark, DingTalk, QQ, WeCom), and deployment configuration is complex. This project provides a Docker image with pre-installed Chinese IM plugins, ready to use out of the box. Platform credentials are configured via environment variables, with data persistence support, built-in OpenCode AI / Playwright / Chinese TTS.

## Core Architecture
- **Docker image**: Based on the official OpenClaw image, pre-installed with Feishu (Lark)/DingTalk/QQ/WeCom plugins
- **Environment variable configuration**: Unified configuration of AI models and IM platform credentials through a `.env` file
- **Configuration sync script**: Automatically syncs environment variables to OpenClaw configuration files on startup
- **Data persistence**: Mounts `~/.openclaw` directory to preserve configuration and workspace
- **Multi-protocol support**: Both OpenAI protocol and Claude protocol API formats
- **Feishu (Lark) official plugin**: Integrates the Feishu official team plugin CLI tool (`feishu-plugin-onboard`), supporting Calendar/Tasks/Bitable and other OAPI capabilities

## Key Features
- Ready out of the box: `docker-compose up -d` for one-click startup
- Full coverage of Chinese IM: Feishu/Lark (official plugin + legacy built-in) / DingTalk / QQ / WeCom
- Flexible configuration: Minimum configuration requires only `MODEL_ID` / `BASE_URL` / `API_KEY` three parameters
- Multi-account support: WeCom supports multi-account configuration; Feishu (Lark) supports automatic migration from `accounts.main` to `default`
- Recommended companion: AIClient-2-API, which converts AI clients to standard APIs for unlimited Token invocation
- Recommended model: `gemini-3-flash-preview` (1M tokens context, fast response, high cost-effectiveness)

<!-- lastCommit: 6a7050b -->

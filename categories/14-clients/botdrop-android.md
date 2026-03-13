> https://github.com/zhixianio/botdrop-android

# BotDrop Android (303 stars)

## Problem & Solution

Running an AI Agent on an Android phone requires installing Termux, configuring Node.js, and manually executing CLI commands, creating a high technical barrier. BotDrop wraps OpenClaw into a user-friendly Android app with a 4-step guided installation (Auth -> Agent -> Install -> Channel), requiring no terminal or CLI, with background Gateway auto-restart support.

## Key Features

- **4-Step Guided Installation** — Auth (configure AI provider credentials) -> Agent (create Agent) -> Install (install dependencies) -> Channel (configure Telegram/Discord)
- **Multi-Provider Support** — Anthropic, OpenAI, Google Gemini, OpenRouter, etc.
- **Telegram & Discord Integration** — Chat with your Agent through IM apps
- **Background Gateway** — Keeps the Agent running with automatic restart
- **No Terminal Required** — All operations completed through GUI
- **Termux-Based** — Provides a Linux environment for running Node.js AI Agents
- **Crashlytics Integration** — Firebase Crashlytics crash reporting (optional, configured at build time)

<!-- lastCommit: 6a7050b -->

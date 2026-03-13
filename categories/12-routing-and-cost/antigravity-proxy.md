> https://github.com/badrisnarayanan/antigravity

# Antigravity-Claude-Proxy (3,107 stars)

## Problem & Solution

Antigravity-Claude-Proxy addresses the cost of accessing Claude/Gemini models in OpenClaw/Claude Code. By proxying Antigravity Cloud Code's free Claude/Gemini quota and converting Google Generative AI format to Anthropic Messages API format, it allows OpenClaw users to use Claude/Gemini models without a paid API Key. However, there is a risk of Google ToS violation, and some user accounts have been banned.

## Key Features

- **Anthropic API Compatible** — Provides an Anthropic Messages API format proxy server, seamlessly integrating with Claude Code CLI and OpenClaw
- **Dual Model Support** — Supports both Claude (Anthropic) and Gemini (Google) models via the Antigravity Cloud Code backend
- **Multi-Account Management** — Supports single-account mode (reads Antigravity local database) and multi-account mode (OAuth authorization for multiple Google accounts)
- **Web Dashboard** — Provides a Web UI for managing accounts, viewing health status, and manual authorization (supports headless servers)
- **Background Running** — Runs as a background process with start/stop/restart/status commands, default port 8080
- **ToS Risk Warning** — Explicitly warns about Google ToS violation risks, recommends using secondary accounts rather than primary accounts

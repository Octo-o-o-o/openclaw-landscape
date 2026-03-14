> https://github.com/xmanrui/OpenClaw-bot-review

# OpenClaw Bot Review (Dashboard)

| Field | Value |
|-------|-------|
| Repository | [xmanrui/OpenClaw-bot-review](https://github.com/xmanrui/OpenClaw-bot-review) |
| Stars | 548 |
| Language | TypeScript (Next.js) |
| License | — |
| Last Active | 2026-03 |

## Introduction

A lightweight web dashboard for viewing all OpenClaw Bot/Agent/model/session statuses at a glance. Reads directly from the local `~/.openclaw/openclaw.json` configuration file and session data, requiring no database.

## Core Features

- **Bot Overview** — Card wall displaying all Agents' names, emojis, models, platform bindings, session statistics, and Gateway health status
- **Model List** — View all configured Providers and models, including context window, max output, reasoning support, and single-model testing
- **Session Management** — Browse all sessions by Agent, with type identification (DM, group chat, scheduled task), Token usage, and connectivity testing
- **Message Statistics** — Token consumption and average response time trends, viewable by day/week/month, with SVG chart display
- **Skill Management** — View all installed skills (built-in, extension, custom), with search and filtering support
- **Alert Center** — Configure alert rules (model unavailable, bot unresponsive), with Feishu notification delivery
- **Gateway Health Detection** — Real-time Gateway status indicator with 10-second auto-polling; click to navigate to the OpenClaw web page
- **Platform Connectivity Testing** — One-click testing of all Feishu/Discord bindings and DM Session connectivity
- **Auto Refresh** — Configurable refresh intervals (manual, 10s, 30s, 1min, 5min, 10min)
- **Internationalization** — Chinese/English interface toggle
- **Theme Toggle** — Dark/light theme support
- **Pixel Office** — Pixel-art animated office where Agents appear as pixel characters, walking, sitting, and interacting with furniture in real time

## Tech Stack

- Next.js + TypeScript
- Tailwind CSS
- No database — reads directly from local configuration files

## Requirements

- Node.js 18+
- OpenClaw installed with configuration file at `~/.openclaw/openclaw.json`
- Docker deployment supported

<!-- lastCommit: 6e5e862 -->

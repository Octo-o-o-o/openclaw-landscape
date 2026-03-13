> https://github.com/mudrii/dashboard

# mudrii/openclaw-dashboard (261 stars)

> Research date: 2026-03-13 (updated)
> Positioning: Zero-dependency local command center aggregating Gateway health, costs, cron status, sessions, Sub-Agents, model usage, and Git logs for OpenClaw Agents

## Problem & Solution

Multi-Agent, multi-cron, multi-channel OpenClaw deployments lack a unified command center, with scattered information leading to low decision-making efficiency. This project provides a zero-dependency local dashboard that aggregates all operational information, supporting Go binary (2,019 req/s) or Python server (1,745 req/s).

## Key Features

- **12 Dashboard Panels** — Top Metrics Bar (CPU/RAM/swap/disk + Gateway status), Alerts Banner (smart alerts), System Health, Cost Cards (today/total/monthly forecast), Cron Jobs, Active Sessions, Token Usage (7d/30d/all-time toggle), Sub-Agent Activity, Charts & Trends (cost curve + model distribution bar chart), Models/Skills/Git Log, AI Chat
- **Go Binary Deployment** — Single file 9.5-10 MB, HTML/CSS/JS embedded in binary, zero runtime dependencies
- **Dual Server Architecture** — Go (production, stale-while-revalidate) + Python (development), fully consistent API
- **Frontend Architecture** — 7 loosely coupled JS modules (State / DataLayer / DirtyChecker / Renderer / Theme / Chat / App), pure SVG charts
- **DirtyChecker** — 13 boolean dirty flags, only re-renders changed regions
- **Immutable State Snapshot** — Immutable state snapshots prevent fetch/render race conditions
- **Stale-While-Revalidate** — Go server immediately returns cached data while asynchronously refreshing in the background
- **AI Chat** — Natural language queries about costs, sessions, cron, and configuration via OpenClaw Gateway
- **6 Themes** — 3 dark + 3 light, Glass Morphism UI, 19 CSS variables defining each theme
- **Smart Alert Banner** — High cost, cron failures, high context usage, Gateway offline
- **5-Level Model Resolution Chain** — overrides -> parent -> fallback -> defaults, ensuring accurate model attribution

## Technical Implementation Highlights

| Technical Detail | Python (server.py) | Go (openclaw-dashboard) |
|-----------------|-------------------|------------------------|
| HTML Serving | Read from disk | Embedded in binary (embed.FS) |
| `/api/refresh` | Blocking | Stale-while-revalidate |
| `/api/chat` | Read per request | mtime cache |
| `/api/system` | TTL cache | RWMutex cache |
| Rate Limiting | 10 req/min | 10 req/min |
| Tests | 122 (pytest) | 87 (go test -race) |
| Throughput | 1,745 req/s | 2,019 req/s |

<!-- lastCommit: 6a7050b -->

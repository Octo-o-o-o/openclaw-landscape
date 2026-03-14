> https://github.com/crabwise-ai/crabwalk

# Crabwalk (859 stars)

## Problem & Solution

Crabwalk addresses the pain point of OpenClaw Agent runtime being a "black box with no observability." By connecting to the OpenClaw Gateway via WebSocket (`ws://127.0.0.1:18789`), it subscribes to the Agent session event stream in real time, visualizing thinking states, tool calls, and response chains as ReactFlow node graphs. It supports simultaneous monitoring across WhatsApp/Telegram/Discord/Slack, providing session filtering, action tracking, and workspace file browsing as a real-time companion monitor.

## Key Features

- **Real-Time Node Graph Visualization** — ReactFlow renders Agent sessions and action chains; expanding nodes reveals tool parameters and payloads
- **Unified Multi-Platform Monitoring** — Simultaneously monitors Agent activity across WhatsApp/Telegram/Discord/Slack, aggregated in a single interface
- **WebSocket Event Stream Subscription** — Connects to OpenClaw Gateway (default `ws://127.0.0.1:18789`), receiving session events in real time (thinking/tool calls/responses)
- **Session Filtering & Search** — Filter by platform, search by recipient, quickly locate target sessions
- **Workspace File Browsing** — Mounts `~/.openclaw/workspace` into the container for real-time viewing of files operated on by Agents
- **CLI + Docker Dual Mode** — Native CLI (`crabwalk start --daemon`) or Docker deployment (`docker run -p 3000:3000`), auto-detects Gateway token (`~/.openclaw/openclaw.json`)
- **QR Code Quick Access** — Displays a QR code on startup; scan with your phone to open the monitoring interface (requires `qrencode`)

<!-- lastCommit: ea99ca9 -->

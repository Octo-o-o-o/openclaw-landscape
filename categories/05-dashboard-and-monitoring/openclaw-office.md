> https://github.com/WW-AI-Lab/openclaw-office

# OpenClaw Office (210 stars)

## Problem & Solution

OpenClaw Multi-Agent systems lack a visual collaborative monitoring interface, making it difficult to intuitively understand the message flow and working status between Agents. OpenClaw Office renders Agent working states, collaboration links, tool calls, and resource consumption through 2D/3D virtual office scenes, and provides a full-featured console for system management.

## Key Features

- **Virtual Office** — 2D SVG isometric office + 3D React Three Fiber scene; Agent = digital employee, Office = Agent runtime, Desk = Session, Meeting Pod = collaboration context
- **Agent Avatars** — Deterministically generated SVG avatars from Agent IDs, with real-time status animations (idle, working, speaking, tool calling, error)
- **Collaboration Visualization** — Collaboration lines show message flow between Agents, speech bubbles stream Markdown text and tool calls in real time
- **Side Panel** — Agent details, Token line charts, cost pie charts, activity heatmaps, SubAgent relationship graphs, event timelines
- **Chat** — Bottom-docked chat bar for real-time conversations with Agents, Agent selector, streaming message display, Markdown rendering, chat history drawer
- **Console** — Full-featured system management interface including Dashboard, Agents, Channels, Skills, Cron, and Settings pages
- **Remote Gateway Support** — Supports remote OpenClaw Gateway access through `/gateway-ws` proxy flow (Alibaba Cloud, Tencent Cloud, and other hosted environments)
- **i18n** — Chinese and English bilingual support with runtime language switching
- **Mock Mode** — Development without requiring a Gateway connection

<!-- lastCommit: 801528c -->

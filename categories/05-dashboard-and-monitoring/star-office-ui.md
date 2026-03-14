> https://github.com/ringhyacinth/Star-Office-UI

# Star Office UI (4,092 stars)

## Problem & Solution

AI Agent working states are invisible -- users cannot intuitively understand "what the Agent is doing right now, what it did yesterday, or whether it is online." Star Office UI is a pixel-art AI office dashboard that visualizes Agent status in real time as office scenes, supporting multi-Agent collaboration, Chinese/English/Japanese trilingual support, AI-generated image decoration, and desktop pet mode.

## Key Features

- **Six Status Visualizations** — idle/writing/researching/executing/syncing/error automatically mapped to different office areas, with pixel characters walking in real time + speech bubbles
- **Yesterday's Notes** — Automatically reads the most recent day's work records from `memory/*.md`, displays them as cards after sanitization, providing an Agent work history snapshot
- **Multi-Agent Collaboration** — Invite other Agents to join the office via join key, view multi-person status in real time, suitable for team collaboration scenarios
- **Art Asset Management** — Sidebar for managing character/scene/decoration assets, supports dynamic frame synchronization to avoid flickering, can connect to Gemini API for AI-generated backgrounds
- **Security Hardening** — Sidebar password protection, weak password blocking in production environments, Session Cookie hardening to prevent unauthorized access
- **Flexible Deployment** — Python 3.10+ backend (Flask), 30-second manual deployment or Docker one-click startup, Cloudflare Tunnel recommended for public access

<!-- lastCommit: f29c107 -->

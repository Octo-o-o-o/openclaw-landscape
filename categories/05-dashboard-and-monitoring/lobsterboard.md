> https://github.com/Curbob/LobsterBoard

# Curbob/LobsterBoard

## Basic Information

- **Stars**: 815
- **URL**: https://github.com/Curbob/LobsterBoard
- **License**: Business Source License 1.1 (BSL-1.1)
- **Author**: Curbob

## Problem & Solution

### Core Problem

LobsterBoard addresses the visual monitoring and control needs of OpenClaw users:

1. **Lack of unified visual interface**: OpenClaw itself is a command-line tool without an intuitive dashboard
2. **Difficulty monitoring multiple servers**: Need to simultaneously monitor OpenClaw instances across multiple VPS
3. **Inconvenient AI usage quota tracking**: Quotas for Claude Code, Copilot, Cursor, and other AI services are scattered
4. **Missing system status monitoring**: CPU, memory, disk, and Docker container status require manual querying
5. **Scattered configuration management**: OpenClaw configuration, Cron tasks, and log viewing require operating in multiple places

### Solution

LobsterBoard is a **self-hosted drag-and-drop dashboard builder**, providing:

- **60+ Widgets**: System monitoring, weather, calendar, RSS, smart home, finance, AI/LLM tracking, and more
- **Template Gallery**: Export/import/share dashboard layouts with automatic screenshot previews
- **Custom Pages**: Extend the dashboard with full custom pages (notes, kanban, etc.)
- **Remote Server Monitoring**: Monitor multiple servers via lobsterboard-agent
- **Zero Cloud Dependency**: Runs entirely locally, data never leaves your machine

## Core Architecture

### Tech Stack

```
LobsterBoard
├── Frontend: Pure JavaScript (no framework)
│   ├── builder.js      # Editor: drag, resize, config I/O
│   ├── widgets.js      # 60+ widget definitions
│   └── templates.js    # Template gallery & export system
├── Backend: Node.js single-file server
│   └── server.cjs      # Express server, SSE streaming data
├── Data Storage: JSON files
│   └── config.json     # User-saved layouts
└── Extension System: Custom pages
    └── pages/          # Auto-discovered custom pages
```

### Architecture Characteristics

1. **No Build Step**: Run `node server.cjs` directly, no webpack/vite needed
2. **Single Server Architecture**: One Node.js process handles all requests
3. **SSE Streaming Data**: System stats pushed in real time via Server-Sent Events
4. **Auto-Discovery Mechanism**: Custom pages placed in the `pages/` directory are automatically loaded

### Widget System Architecture

```javascript
// Widget definition structure
{
  id: "cpu-memory",
  name: "CPU / Memory",
  category: "system",
  defaultSize: { w: 4, h: 3 },
  properties: {
    server: { type: "select", options: ["local", "remote-1"] },
    refreshInterval: { type: "number", default: 2000 }
  },
  render: (container, config) => {
    // Render logic
  },
  update: (container, data) => {
    // Update logic
  }
}
```

## Key Features

### 1. Drag-and-Drop Editor

- **20px Grid Snapping**: Precise layout alignment
- **Resize Handles**: Drag to resize widgets
- **Properties Panel**: Right-side panel for configuring widget properties
- **Canvas Size Presets**: 1920x1080, 2560x1440, etc.

### 2. Remote Server Monitoring

**Architecture**:

```
┌─────────────────────────────────────────────┐
│  LobsterBoard (Control Host)                │
│  http://localhost:8080                      │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  Uptime Monitor Widget               │  │
│  │  Server: remote-vps-1                │  │
│  │  ├─ CPU: 45%                         │  │
│  │  ├─ Memory: 2.1GB / 8GB              │  │
│  │  └─ Uptime: 15 days                  │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
                    ↓ HTTP API
┌─────────────────────────────────────────────┐
│  Remote VPS                                 │
│  http://vps-ip:9090                         │
│                                             │
│  lobsterboard-agent                         │
│  ├─ API Key Authentication                  │
│  ├─ System Metrics Collection               │
│  └─ Docker Container Status                 │
└─────────────────────────────────────────────┘
```

**Supported Remote Widgets**:
- Uptime Monitor (system uptime, CPU, memory)
- CPU / Memory (CPU usage + RAM usage)
- Disk Usage (disk space, ring chart)
- Network Speed (upload/download throughput)
- Docker Containers (container list and status)

### 3. AI/LLM Usage Tracking

**Supported AI Services** (14):

| Service | Tracked Content | Configuration |
|---------|----------------|---------------|
| Claude Code | Session, weekly, Opus limits | Run `claude` once |
| Codex CLI | Session, weekly, code reviews | Run `codex` once |
| GitHub Copilot | Premium, chat, completions | Run `gh auth login` |
| Cursor | Credits, usage breakdown | Use Cursor IDE |
| Gemini CLI | Pro, flash models | Run `gemini` once |
| Amp | Free tier, credits | Run `amp` once |
| Factory / Droid | Standard, premium tokens | Run `factory` once |
| Kimi Code | Session, weekly | Run `kimi` once |
| JetBrains AI | Quota tracking | IDE login |
| Antigravity | Gemini 3, Claude via Google | Run `antigravity-usage login` |
| MiniMax | Coding plan session | Set `MINIMAX_API_KEY` |
| Z.ai | Session, weekly | Set `ZAI_API_KEY` |
| AI Cost Tracker | Monthly cost breakdown | — |
| API Status | Provider availability | — |

**Implementation Principle**:
- Reads local cache files from various AI CLI tools (e.g., `~/.claude/usage.json`)
- Queries usage via API (requires API Key)
- Displays remaining quota and usage trends in real time

### 4. Template System

**Features**:
- **Export**: Export current dashboard as a template (with automatic screenshot preview)
- **Browse**: Template gallery for discovering pre-built layouts
- **Import**: Two modes
  - **Replace**: Replace the entire dashboard
  - **Merge**: Append template widgets below the existing layout

**Storage Structure**:

```
templates/
├── templates.json          # Template index
└── my-template/
    ├── config.json         # Widget configuration
    └── preview.png         # Automatic screenshot
```

### 5. Custom Pages System

**Structure**:

```
pages/
└── my-page/
    ├── page.json       # Metadata (title, icon, order)
    ├── index.html      # Page UI
    └── api.cjs         # Optional: server-side API routes
```

**Auto-Discovery**:
- Scans the `pages/` directory on startup
- Automatically registers routes at `/pages/my-page`
- Navigation bar automatically displays entry points

### 6. Five Themes

| Theme | Style | Characteristics |
|-------|-------|-----------------|
| Default | Dark | Emoji icons, classic look |
| Terminal | CRT Green | Scanline effect, Phosphor icons |
| Paper | Beige/Sepia | Serif fonts, vintage feel |
| Feminine | Pink/Lavender | Soft glow |
| Feminine Dark | Pink-Purple | Dark background, pink-purple accents |

## Summary

While LobsterBoard is a general-purpose dashboard tool, its design concepts -- **drag-and-drop layouts**, **remote monitoring architecture**, **AI quota tracking**, and **custom pages system** -- are highly applicable. The **multi-instance monitoring** and **visual customization** aspects in particular offer valuable architectural references for building flexible monitoring and management interfaces.

<!-- lastCommit: 05c0c77f1c1c7d2f43e1087e619245cfa6fe1342 -->

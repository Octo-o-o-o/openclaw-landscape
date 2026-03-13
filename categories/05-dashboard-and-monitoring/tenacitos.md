> https://github.com/carlosazaustre/tenacitOS

# carlosazaustre/tenacitOS

## Basic Information

- **Stars**: 689
- **URL**: https://github.com/carlosazaustre/tenacitOS
- **License**: MIT
- **Tech Stack**: Next.js 15 + React 19 + Tailwind CSS v4
- **Author**: Carlos Azaustre

## Problem & Solution

### Core Problem

OpenClaw users need a **real-time dashboard and control center** to manage AI Agent instances, but face the following difficulties:

1. **Lack of visual monitoring**: OpenClaw itself is a command-line tool without an intuitive monitoring interface
2. **Difficult multi-Agent management**: Need to simultaneously manage multiple Agents (main, studio, infra, etc.)
3. **Inconvenient cost tracking**: Token usage and costs are scattered across individual Agent logs
4. **Complex cron task management**: Requires manual crontab file editing
5. **Inconvenient memory file viewing**: MEMORY.md, SOUL.md, and other files require opening in an editor
6. **Scattered activity logs**: Agent operation logs are spread across multiple files

### Solution

TenacitOS is a **real-time dashboard and control center** that reads directly from OpenClaw's configuration and data:

- **System Monitoring**: Real-time VPS metrics (CPU, RAM, disk, network) + PM2/Docker status
- **Agent Dashboard**: All Agents, sessions, Token usage, models, activity status
- **Cost Tracking**: Real cost analysis read from OpenClaw sessions (SQLite)
- **Cron Manager**: Visual Cron manager with weekly timeline, run history, and manual triggering
- **Activity Stream**: Real-time Agent operation logs with heatmaps and charts
- **Memory Browser**: Explore, search, and edit Agent memory files
- **File Browser**: Navigate workspace files with preview and in-browser editing
- **Global Search**: Full-text search across memory and workspace files
- **Notifications**: Real-time notification center with unread badges
- **Office 3D**: Interactive 3D office with one desk per Agent (React Three Fiber)
- **Terminal**: Read-only terminal for safe status commands
- **Authentication**: Password protection with rate limiting and secure cookies

## Core Architecture

### Tech Stack

```
TenacitOS
├── Frontend: Next.js 15 (App Router) + React 19
│   ├── Tailwind CSS v4
│   ├── React Three Fiber (3D Office)
│   ├── Recharts (Charts)
│   └── Lucide React (Icons)
├── Backend: Next.js API Routes
│   ├── Filesystem reads (OpenClaw config and data)
│   ├── SQLite queries (Cost tracking)
│   └── System metrics collection (CPU, memory, disk)
├── Data Storage: JSON files + SQLite
│   ├── data/cron-jobs.json
│   ├── data/activities.json
│   ├── data/notifications.json
│   └── OpenClaw SQLite database
└── Authentication: Next.js Middleware + Cookie
```

### Architecture Characteristics

**Zero Additional Backend**: TenacitOS reads directly from OpenClaw's files and database, requiring no additional database or backend service.

```
/root/.openclaw/              ← OPENCLAW_DIR (configurable)
├── openclaw.json             ← Agent list, channels, model configuration
├── workspace/                ← Main Agent workspace (MEMORY.md, SOUL.md, etc.)
├── workspace-studio/         ← Sub-Agent workspace
├── workspace-infra/
├── ...
└── workspace/mission-control/ ← TenacitOS installs here
```

### Data Flow

```
┌─────────────────────────────────────────────┐
│  TenacitOS (Next.js App)                    │
│  http://localhost:3000                      │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  Dashboard Page                      │  │
│  │  ├─ Agent status cards               │  │
│  │  ├─ Cost charts                      │  │
│  │  └─ Activity stream                  │  │
│  └──────────────────────────────────────┘  │
│                    ↓                        │
│  ┌──────────────────────────────────────┐  │
│  │  API Routes                          │  │
│  │  ├─ /api/agents                      │  │
│  │  ├─ /api/sessions                    │  │
│  │  ├─ /api/costs                       │  │
│  │  └─ /api/system                      │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  OpenClaw Data Sources                      │
│  ├─ openclaw.json (Agent configuration)     │
│  ├─ workspace/MEMORY.md (Memory files)      │
│  ├─ workspace/.sessions/*.db (Session DB)   │
│  └─ /proc/* (System metrics)                │
└─────────────────────────────────────────────┘
```

## Key Features

### 1. Agent Auto-Discovery

**Implementation**:

```typescript
// src/app/api/agents/route.ts
import { readFileSync } from 'fs';
import { join } from 'path';

export async function GET() {
  const openclawDir = process.env.OPENCLAW_DIR || '/root/.openclaw';
  const configPath = join(openclawDir, 'openclaw.json');
  const config = JSON.parse(readFileSync(configPath, 'utf-8'));

  const agents = config.agents.list.map(agent => ({
    id: agent.id,
    name: agent.name,
    workspace: agent.workspace,
    model: agent.model,
    ui: agent.ui || { emoji: '🤖', color: '#FFCC00' }
  }));

  return Response.json({ agents });
}
```

**Characteristics**:
- **Zero configuration**: Automatically reads Agent list from `openclaw.json`
- **Custom appearance**: Each Agent can define its own emoji and color
- **Real-time updates**: Changes to `openclaw.json` are visible after page refresh

### 2. Cost Tracking

**Data Source**: OpenClaw's SQLite database

```typescript
// scripts/collect-usage.ts
import Database from 'better-sqlite3';
import { join } from 'path';

const openclawDir = process.env.OPENCLAW_DIR || '/root/.openclaw';
const dbPath = join(openclawDir, 'workspace/.sessions/sessions.db');
const db = new Database(dbPath, { readonly: true });

const sessions = db.prepare(`
  SELECT
    agent_id,
    model,
    input_tokens,
    output_tokens,
    cache_read_tokens,
    cache_write_tokens,
    created_at
  FROM sessions
  WHERE created_at >= datetime('now', '-30 days')
`).all();

// Calculate costs
const costs = sessions.map(session => {
  const pricing = getPricing(session.model);
  return {
    agent_id: session.agent_id,
    date: session.created_at.split('T')[0],
    cost: (
      session.input_tokens * pricing.input +
      session.output_tokens * pricing.output +
      session.cache_read_tokens * pricing.cacheRead +
      session.cache_write_tokens * pricing.cacheWrite
    ) / 1_000_000
  };
});

// Save to JSON
writeFileSync('data/costs.json', JSON.stringify(costs, null, 2));
```

**Automatic Collection**:

```bash
# Collect once per hour
./scripts/setup-cron.sh
# Adds cron job: 0 * * * * cd /path/to/mission-control && npx tsx scripts/collect-usage.ts
```

**Visualization**:

- **Daily cost trend chart**: Recharts line chart
- **Grouped by Agent**: Cost proportion per Agent
- **Grouped by model**: Cost proportion per model

### 3. Cron Manager

**Features**:
- **Visual Timeline**: Week view showing each Cron task's execution time
- **Run History**: Last 10 run records
- **Manual Trigger**: Click button to manually run Cron tasks
- **Enable/Disable**: Toggle Cron task enabled status

**Data Structure**:

```json
// data/cron-jobs.json
{
  "jobs": [
    {
      "id": "daily-report",
      "name": "Daily Report",
      "schedule": "0 9 * * *",
      "command": "openclaw run daily-report",
      "enabled": true,
      "lastRun": "2026-03-10T09:00:00Z",
      "nextRun": "2026-03-11T09:00:00Z",
      "history": [
        { "timestamp": "2026-03-10T09:00:00Z", "status": "success", "duration": 1234 },
        { "timestamp": "2026-03-09T09:00:00Z", "status": "success", "duration": 1456 }
      ]
    }
  ]
}
```

### 4. Office 3D

**Technology**: React Three Fiber + Drei

**Features**:
- **Interactive 3D office**: One desk per Agent
- **Custom positions**: Configure in `src/components/Office3D/agentsConfig.ts`
- **3D avatars**: Supports Ready Player Me GLB format
- **Fallback mechanism**: Displays colored spheres if no GLB file is available

**Configuration**:

```typescript
// src/components/Office3D/agentsConfig.ts
export const AGENTS: AgentConfig[] = [
  {
    id: "main",
    name: "Main Agent",
    emoji: "🤖",
    position: [0, 0, 0],
    color: "#FFCC00",
    role: "Main Agent",
  },
  {
    id: "studio",
    name: "Studio Agent",
    emoji: "🎬",
    position: [3, 0, 0],
    color: "#E91E63",
    role: "Creative Agent",
  },
  // Supports up to 6 Agents
];
```

**3D Avatars**:

```
public/models/
├── main.glb        ← Main Agent avatar
├── studio.glb      ← workspace-studio Agent
└── infra.glb       ← workspace-infra Agent
```

### 5. Memory Browser

**Features**:
- **File List**: Display all memory files (MEMORY.md, SOUL.md, PLAN.md, etc.)
- **Search**: Full-text search across memory file contents
- **Preview**: Markdown rendering preview
- **Edit**: In-browser editing, saved to the filesystem

**Implementation**:

```typescript
// src/app/api/memory/route.ts
import { readdirSync, readFileSync, writeFileSync } from 'fs';
import { join } from 'path';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const agentId = searchParams.get('agent') || 'main';

  const workspaceDir = join(
    process.env.OPENCLAW_DIR || '/root/.openclaw',
    agentId === 'main' ? 'workspace' : `workspace-${agentId}`
  );

  const files = readdirSync(workspaceDir)
    .filter(f => f.endsWith('.md'))
    .map(f => ({
      name: f,
      path: join(workspaceDir, f),
      content: readFileSync(join(workspaceDir, f), 'utf-8'),
      size: statSync(join(workspaceDir, f)).size,
      modified: statSync(join(workspaceDir, f)).mtime
    }));

  return Response.json({ files });
}

export async function POST(request: Request) {
  const { path, content } = await request.json();
  writeFileSync(path, content, 'utf-8');
  return Response.json({ success: true });
}
```

### 6. System Monitoring

**Metrics**:
- **CPU Usage**: Read from `/proc/stat`
- **Memory Usage**: Read from `/proc/meminfo`
- **Disk Usage**: Read from `df` command
- **Network Traffic**: Read from `/proc/net/dev`
- **PM2 Status**: Read from `pm2 jlist`
- **Docker Status**: Read from `docker ps`

**Implementation**:

```typescript
// src/lib/system-metrics.ts
import { execSync } from 'child_process';

export function getCpuUsage(): number {
  const stat = readFileSync('/proc/stat', 'utf-8');
  const cpuLine = stat.split('\n')[0];
  const [, user, nice, system, idle] = cpuLine.split(/\s+/).map(Number);
  const total = user + nice + system + idle;
  return ((total - idle) / total) * 100;
}

export function getMemoryUsage(): { used: number; total: number } {
  const meminfo = readFileSync('/proc/meminfo', 'utf-8');
  const total = parseInt(meminfo.match(/MemTotal:\s+(\d+)/)?.[1] || '0') * 1024;
  const available = parseInt(meminfo.match(/MemAvailable:\s+(\d+)/)?.[1] || '0') * 1024;
  return { used: total - available, total };
}

export function getDiskUsage(): { used: number; total: number } {
  const df = execSync('df -B1 /').toString();
  const [, , total, used] = df.split('\n')[1].split(/\s+/);
  return { used: parseInt(used), total: parseInt(total) };
}
```

## Summary

carlosazaustre/tenacitOS is a **complete OpenClaw control center**, with value in:

1. **Zero additional backend**: Reads directly from OpenClaw's configuration and data
2. **Agent auto-discovery**: No manual configuration needed
3. **Cost tracking**: Reads real cost data from SQLite
4. **Cron manager**: Visual Cron task management
5. **Office 3D**: 3D visualization of Agent status
6. **Memory browser**: Search, preview, and edit memory files

<!-- lastCommit: 6a7050b -->

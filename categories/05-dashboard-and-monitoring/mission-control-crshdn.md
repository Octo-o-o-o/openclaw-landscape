> https://github.com/crshdn/mission-control

# crshdn/mission-control (Autensa)

## Basic Information

- **GitHub Stars**: 1,319
- **Project URL**: https://github.com/crshdn/mission-control
- **Live Demo**: https://missioncontrol.ghray.com
- **Latest Version**: v1.5.0
- **License**: MIT
- **Tech Stack**: Next.js 14, TypeScript 5, SQLite 3, OpenClaw Gateway

## Problem & Solution

### Core Problem
Traditional AI Agent systems lack a unified task orchestration and visual management interface, making it difficult for users to:
1. Intuitively create and track AI task execution progress
2. Engage in interactive task planning conversations with AI
3. Monitor the working status of multiple Agents in real time
4. Manage the complete task lifecycle (from planning to delivery)

### Solution
Mission Control (now rebranded as Autensa) provides a complete AI Agent orchestration dashboard:

**Task Management Layer**
- Kanban board interface with drag-and-drop support, 7 status columns (PLANNING -> INBOX -> ASSIGNED -> IN PROGRESS -> TESTING -> REVIEW -> DONE)
- Task image attachment support (new in v1.5.0), allowing AI Agents to see reference images (UI prototypes, screenshots, etc.)
- Interactive AI planning flow: AI proactively asks clarifying questions rather than executing blindly

**Agent Orchestration Layer**
- Automatically creates specialized Agents and assigns tasks
- Real-time progress tracking and status synchronization
- Gateway Agent Discovery: one-click import of existing Agents from OpenClaw Gateway, no need to recreate
- Supports Sub-Agent registration and activity log recording

**Real-Time Monitoring Layer**
- Live Feed real-time event stream showing Agent activities, task updates, and system events
- WebSocket connection to OpenClaw Gateway for AI Agent orchestration
- Complete deliverable tracking system

## Core Architecture

### System Architecture Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                       YOUR MACHINE                           │
│                                                              │
│  ┌─────────────────┐          ┌──────────────────────────┐  │
│  │ Mission Control  │◄────────►│    OpenClaw Gateway      │  │
│  │   (Next.js)      │   WS     │  (AI Agent Runtime)      │  │
│  │   Port 4000      │          │  Port 18789              │  │
│  └────────┬─────────┘          └───────────┬──────────────┘  │
│           │                                │                  │
│           ▼                                ▼                  │
│  ┌─────────────────┐          ┌──────────────────────────┐  │
│  │     SQLite       │          │     AI Provider          │  │
│  │    Database      │          │  (Anthropic / OpenAI)    │  │
│  └─────────────────┘          └──────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### Technical Architecture

**Frontend Layer (Next.js 14 App Router)**
```
src/
├── app/
│   ├── api/                    # API Routes
│   │   ├── tasks/              # Task CRUD + planning + scheduling
│   │   ├── agents/             # Agent management
│   │   ├── openclaw/           # Gateway proxy endpoints
│   │   └── webhooks/           # Agent completion callbacks
│   ├── settings/               # Settings page
│   └── workspace/[slug]/       # Workspace dashboard
├── components/
│   ├── MissionQueue.tsx        # Kanban board
│   ├── PlanningTab.tsx         # AI planning interface
│   ├── AgentsSidebar.tsx       # Agent panel
│   ├── LiveFeed.tsx            # Real-time event stream
│   └── TaskModal.tsx           # Task creation/editing
└── lib/
    ├── db/                     # SQLite + migrations
    ├── openclaw/               # Gateway client + device identity
    ├── validation.ts           # Zod schema validation
    └── types.ts                # TypeScript types
```

**Data Layer**
- SQLite database (`mission-control.db`)
- Workspace filesystem (`~/Documents/Shared/projects`)
- In-memory state management (no persistence)

**Integration Layer**
- OpenClaw Gateway WebSocket connection
- Bearer Token authentication
- HMAC Webhook signature verification

### Task Lifecycle

```
 CREATE          PLAN            ASSIGN          EXECUTE         DELIVER
┌────────┐    ┌────────┐    ┌────────────┐    ┌──────────┐    ┌────────┐
│  New   │───►│  AI    │───►│   Agent    │───►│  Agent   │───►│  Done  │
│  Task  │    │  Q&A   │    │  Created   │    │  Works   │    │  ✓     │
└────────┘    └────────┘    └────────────┘    └──────────┘    └────────┘
```

**Status Flow**:
```
PLANNING → INBOX → ASSIGNED → IN PROGRESS → TESTING → REVIEW → DONE
```

- **PLANNING**: Interactive AI Q&A phase
- **INBOX**: New tasks waiting to be processed
- **ASSIGNED**: Assigned to an Agent, ready to start
- **IN PROGRESS**: Agent is executing
- **TESTING**: Automated quality gates (browser tests, CSS validation, resource checks)
- **REVIEW**: Passed automated tests, awaiting human approval
- **DONE**: Task completed and approved

### API Orchestration Protocol

**1. Register Sub-Agent**
```bash
POST /api/tasks/{TASK_ID}/subagent
{
  "openclaw_session_id": "unique-session-id",
  "agent_name": "Designer"
}
```

**2. Record Activity Log**
```bash
POST /api/tasks/{TASK_ID}/activities
{
  "activity_type": "updated",  # spawned/updated/completed/file_created/status_changed
  "message": "Started working on design mockups",
  "agent_id": "optional-agent-uuid"
}
```

**3. Register Deliverable**
```bash
POST /api/tasks/{TASK_ID}/deliverables
{
  "deliverable_type": "file",
  "title": "Homepage Design",
  "path": "$PROJECTS_PATH/homepage/index.html",
  "description": "Main homepage with responsive layout"
}
```

## Key Features

### 1. Interactive AI Planning
- AI proactively asks clarifying questions rather than blindly executing
- Multi-turn conversational planning flow
- Automatically creates specialized Agents based on user answers

### 2. Task Image Attachments (v1.5.0)
- Upload reference images to tasks
- AI Agents can view images during scheduling
- Suitable for UI prototypes, screenshots, visual specifications

### 3. Gateway Agent Discovery
- One-click import of existing Agents from OpenClaw Gateway
- No need to recreate Agents in Mission Control
- Automatic synchronization of Agent configuration and status

### 4. Real-Time Event Stream
- WebSocket real-time push
- Displays Agent activities, task updates, and system events
- Supports SSE (Server-Sent Events) streaming

### 5. Multi-Machine Deployment Support
- Dashboard and AI Agents can run on different machines
- Supports Tailscale remote connections
- Configuration example:
```env
OPENCLAW_GATEWAY_URL=wss://your-machine.tailnet-name.ts.net
OPENCLAW_GATEWAY_TOKEN=your-shared-token
```

### 6. Security Features
- Bearer Token authentication (`MC_API_TOKEN`)
- HMAC Webhook signature verification (`WEBHOOK_SECRET`)
- Zod schema validation
- Path traversal protection
- Security response headers

### 7. Privacy-First Design
- Open source and self-hosted
- No built-in analytics trackers
- No centralized user data collection
- Data stays on local deployment

### 8. Docker Production Ready
- Optimized Dockerfile
- docker-compose orchestration
- Named volume persistence (`mission-control-data`, `mission-control-workspace`)
- Supports `host.docker.internal` for connecting to local OpenClaw

### 9. Automated Testing Gates
- TESTING status automatically runs quality checks
- Browser testing
- CSS validation
- Resource integrity checks

## Summary

Mission Control provides a complete AI Agent orchestration reference implementation, with core value in:

1. **Visual Orchestration**: Kanban + real-time event stream for an intuitive UI
2. **Interactive Planning**: AI proactively asks clarifying questions during requirement gathering
3. **Hierarchical Management**: Clear Task -> Agent -> Sub-Agent -> Deliverable hierarchy
4. **Production Ready**: Security, privacy, multi-machine deployment, Docker support
5. **Open Integration**: Standardized interfaces based on OpenClaw Gateway

<!-- lastCommit: 6a7050b -->

> https://github.com/grp06/openclaw-studio

# OpenClaw Studio

## Basic Information

- **GitHub**: https://github.com/grp06/openclaw-studio
- **Stars**: 1,549
- **Language**: TypeScript
- **Created**: 2026-01-28
- **Last Updated**: 2026-03-11
- **Description**: A clean web dashboard for OpenClaw. Connect your Gateway, manage agents, and ship faster.

## Problem & Solution

### Core Problem

OpenClaw's native architecture has the following pain points:

1. **Deployment complexity**: Single-process architecture, Agent creation requires manual configuration + restart
2. **Insufficient visibility**: Lack of a unified visual interface, making it difficult to monitor Agent status and task execution
3. **Difficult mobile access**: Depends on specific Channel configuration, not usable out of the box
4. **Inconvenient human intervention**: Lacks an intuitive approval workflow and permission management interface
5. **Difficult multi-Agent collaboration**: No unified control panel for managing multiple Agent instances

### Solution

OpenClaw Studio provides a modern Web Dashboard that addresses the above issues through:

1. **Zero-Configuration Connection**: Connects to OpenClaw Gateway via WebSocket, no Gateway configuration changes needed
2. **Unified Control Panel**: Single interface for managing all Agents, sessions, tasks, and approvals
3. **Real-Time Monitoring**: SSE streaming of runtime events, showing Agent thinking processes, tool calls, and execution results in real time
4. **Visual Approval Workflow**: Graphical interface for handling exec command approvals, supporting "Allow Once", "Always Allow", and "Deny"
5. **Mobile-Friendly**: Responsive design, accessible via mobile browsers
6. **Cron Task Management**: Visual creation and management of scheduled tasks
7. **Fine-Grained Permission Control**: Graphical configuration of Agent tool policies, sandbox modes, and workspace access permissions

## Core Architecture

### System Architecture

OpenClaw Studio adopts a **Server-Owned Control Plane** architecture, completely eschewing the browser-direct-to-Gateway pattern:

```
┌─────────────────────────────────────────────────────────────┐
│                    OpenClaw Studio                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Browser                                                    │
│    │                                                        │
│    ├─→ HTTP + SSE (/api/runtime/*, /api/intents/*)        │
│    │                                                        │
│  Studio Server (Next.js)                                   │
│    │                                                        │
│    ├─→ Control Plane Runtime (src/lib/controlplane/)      │
│    │   ├─ openclaw-adapter.ts (upstream WebSocket)        │
│    │   ├─ runtime.ts (singleton, subscription fanout)     │
│    │   └─ projection-store.ts (SQLite: runtime.db)        │
│    │                                                        │
│    └─→ WebSocket (server-owned)                           │
│                                                             │
│  OpenClaw Gateway                                          │
│    └─ ws://localhost:18789 (or remote)                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Design Decisions

1. **Server-Side WebSocket Adapter**: Studio server maintains a single WebSocket connection to the Gateway; browsers communicate with Studio via HTTP API and SSE
2. **SQLite Persistence**: Runtime event projections and replay queues stored in `runtime.db`, ensuring state consistency across page refreshes and process restarts
3. **SSE Streaming**: `/api/runtime/stream` provides a real-time event stream, supporting `Last-Event-ID` replay mechanism
4. **Intent-Based Write Operations**: All mutation operations go through `/api/intents/*` routes, following a semantic API design
5. **Server-Side Gateway Token Hosting**: Tokens stored on the server in `settings.json`, automatically redacted in API responses

### Core Modules

#### 1. Control Plane Runtime

**Location**: `src/lib/controlplane/`

- **openclaw-adapter.ts**: Upstream WebSocket lifecycle management, handshake, request allowlisting, reconnection strategy
- **runtime.ts**: Process-level singleton runtime, subscription fanout, Gateway call boundary
- **projection-store.ts**: SQLite projection store + event queue (`runtime.db`)

#### 2. Runtime Read Routes

**Location**: `src/app/api/runtime/`

- `/summary`: Runtime summary
- `/fleet`: Agent fleet status
- `/agents/[agentId]/history`: Agent history (supports pagination and cursors)
- `/stream`: SSE event stream (supports `Last-Event-ID` replay)
- `/config`, `/models`, `/sessions`, `/chat-history`, `/cron`, `/skills/status`, `/agent-file`, `/agent-state`, `/media`: Various resource queries

#### 3. Intent Routes

**Location**: `src/app/api/intents/`

**Chat-Related**:
- `/chat-send`: Send message
- `/chat-abort`: Abort conversation
- `/sessions-reset`: Reset session

**Agent Management**:
- `/agent-create`: Create Agent
- `/agent-rename`: Rename Agent
- `/agent-delete`: Delete Agent
- `/agent-wait`: Wait for Agent readiness
- `/agent-permissions-update`: Update permissions
- `/agent-skills-allowlist`: Skills allowlist
- `/agent-file-set`: Set Agent file

**Approval Management**:
- `/exec-approval-resolve`: Resolve individual approval
- `/exec-approvals-set`: Batch set approval policies

**Cron Tasks**:
- `/cron-add`, `/cron-run`, `/cron-remove`, `/cron-remove-agent`, `/cron-restore`

**Skill Management**:
- `/skills-install`, `/skills-update`, `/skills-remove`

#### 4. Settings Boundary

**Location**: `src/app/api/studio/route.ts`

- Persistent file: `~/.openclaw/openclaw-studio/settings.json`
- Gateway token hosted server-side, automatically redacted in API responses
- Gateway URL/Token changes trigger deterministic reconnection: `runtime.reconnectForGatewaySettingsChange()`

### Runtime Persistence Model

**SQLite Database Path**: `${resolveStateDir()}/openclaw-studio/runtime.db`

**Projection Store Responsibilities**:
- Idempotent application of domain events
- Persistent ordered event queue
- Provides replay/history window queries

**SSE Replay Behavior**:
- With `Last-Event-ID`: Replays forward from that ID
- Without `Last-Event-ID`: Replays the most recent tail window from the queue head

### History Model

**Route**: `/api/runtime/agents/[agentId]/history`

**Query Parameters**:
- `limit`: Limit the number of returned entries
- `beforeOutboxId`: Exclusive cursor (pagination)

**Response**:
- `entries`: Array of history entries
- `hasMore`: Whether more data is available
- `nextBeforeOutboxId`: Next page cursor

**Client Integration**: `useRuntimeSyncController` injects fetched queue rows into the same event pipeline as SSE, deduplicating via outbox id/time key.

## Key Features

### 1. Zero-Configuration Deployment

```bash
npx -y openclaw-studio@latest
cd openclaw-studio
npm run dev
```

One command to start, auto-detects local OpenClaw Gateway or manually configure a remote Gateway.

### 2. Multi-Scenario Deployment Support

#### A. Gateway Local + Studio Local (Same Machine)

```bash
# Studio configuration
Upstream URL: ws://localhost:18789
Upstream Token: <gateway token>
```

#### B. Gateway Cloud + Studio Local (Laptop)

**Recommended (Tailscale Serve)**:

```bash
# On the Gateway host
tailscale serve --yes --bg --https 443 http://127.0.0.1:18789

# Studio configuration
Upstream URL: wss://<gateway-host>.ts.net
Upstream Token: <gateway token>
```

**Alternative (SSH Tunnel)**:

```bash
# On the laptop
ssh -L 18789:127.0.0.1:18789 user@<gateway-host>

# Studio configuration
Upstream URL: ws://localhost:18789
```

#### C. Studio Cloud + Gateway Cloud

```bash
# Run Studio on VPS
npm run dev

# If OpenClaw is on the same VPS
Upstream URL: ws://localhost:18789

# Expose Studio via Tailscale
tailscale serve --yes --bg --https 443 http://127.0.0.1:3000

# Browser access
https://<studio-host>.ts.net
```

### 3. Permission & Sandbox Management

Studio provides a graphical interface for configuring Agent permissions, with configurations flowing to the Gateway for runtime enforcement:

#### Tool Policy

- **Commands**: `Off` / `Ask` / `Auto`
- **Web Access**: `On` / `Off`
- **File Tools**: `On` / `Off`

Maps to OpenClaw tool groups:
- `group:runtime` -> Runtime execution tools (`exec`, `process`)
- `group:web` -> Browser automation tools
- `group:file` -> File read/write tools

#### Sandbox Mode

- **off**: No sandbox
- **all**: All sessions sandboxed
- **non-main**: All except main session sandboxed

#### Workspace Access

- **none**: Sandbox cannot access Agent workspace
- **ro**: Read-only mount
- **rw**: Read-write mount

#### Exec Approval Policy

- **Security**: `strict` / `moderate` / `permissive`
- **Ask**: List of command patterns requiring approval
- **Allowlist**: Allowlisted commands (auto-approved)

### 4. Real-Time Event Stream

**SSE Endpoint**: `/api/runtime/stream`

**Event Types**:
- `agent.created`, `agent.deleted`, `agent.renamed`
- `session.started`, `session.ended`
- `chat.message`, `chat.thinking`, `chat.tool_call`
- `exec.approval_requested`, `exec.approval_resolved`
- `cron.job_added`, `cron.job_executed`

**Replay Mechanism**:
- Client sends `Last-Event-ID` to request replay
- Server queries SQLite queue and replays missed events
- Ensures state consistency after page refresh

### 5. Cron Task Management

Visual creation and management of scheduled tasks:

- **Task Types**: Scheduled messages, scheduled commands
- **Cron Expressions**: Standard cron syntax
- **Target Agent**: Select the Agent to execute the task
- **Task History**: View execution records and results

### 6. Skill Management

- **Skill Installation**: Install community skills from skills.sh
- **Skill Updates**: Update installed skills
- **Skill Removal**: Uninstall unneeded skills
- **Agent Skill Allowlist**: Control which skills each Agent can use

### 7. Approval Workflow

Graphical handling of exec command approvals:

- **Real-Time Notifications**: Approval requests pushed to browser via SSE
- **Three Actions**: Allow Once / Always Allow / Deny
- **Approval History**: View all approval records
- **Policy Updates**: Approval decisions automatically update Agent approval policies

### 8. Mobile Support

- Responsive design adapting to mobile browsers
- Touch operation support
- Mobile-optimized UI layout

### 9. Security Features

- **Server-Side Token Hosting**: Gateway tokens stored server-side, inaccessible to browsers
- **Access Token Protection**: Enforces `STUDIO_ACCESS_TOKEN` when bound to non-loopback addresses
- **API Redaction**: Sensitive information automatically redacted in API responses
- **CORS Protection**: Strict cross-origin policies

### 10. Developer-Friendly

- **Full-Stack TypeScript**: Type safety
- **Hot Reload**: Automatic reload in development mode
- **Error Handling**: Detailed error codes and diagnostic information
- **Logging System**: Structured logs for easy debugging
- **Test Coverage**: Playwright E2E tests

## Summary

OpenClaw Studio provides the following core value:

1. **Architecture Pattern**: Server-side control plane + SSE event stream + SQLite persistence
2. **API Design**: Intent-based semantic API, clearly expressing business intent
3. **Permission Management**: Fine-grained tool policies + sandbox modes + approval workflows
4. **Real-Time Sync**: SSE + replay mechanism ensuring state consistency
5. **Multi-Scenario Deployment**: Local/cloud/hybrid deployment adapting to different user needs
6. **Security Practices**: Server-side token hosting + API redaction + audit logs
7. **Developer Experience**: TypeScript type safety + detailed error codes + comprehensive testing

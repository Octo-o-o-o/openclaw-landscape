> https://github.com/qwibitai/nanoclaw

# NanoClaw

## Basic Info

- **GitHub**: https://github.com/qwibitai/nanoclaw
- **Stars**: 21,451
- **Author**: qwibitai
- **Tech Stack**: Node.js 20+, TypeScript, Claude Agent SDK 0.2.29, SQLite, Docker/Apple Container
- **License**: MIT

## Problem & Solution

### Core Problems

OpenClaw is powerful but suffers from serious understandability and security issues:
- **Excessive code complexity**: Nearly 500K lines of code, 53 configuration files, 70+ dependencies
- **Weak security model**: Application-layer permission controls (allowlist, pairing codes) rather than true OS-level isolation
- **Single-process shared memory**: All functionality runs in a single Node process with no isolation boundaries
- **Configuration bloat**: Features stacked through configuration files, leading to system bloat

### NanoClaw's Solution

**1. Minimalist, Understandable Architecture**
- Single process + a small number of source files, no microservices
- Core code small enough for Claude Code to explain the entire codebase
- Philosophy: Small enough to understand

**2. Container-level Security Isolation**
- Agents run in Linux containers (Apple Container on macOS, Docker on Linux)
- Filesystem isolation: can only access explicitly mounted directories
- Bash commands execute inside the container, not on the host
- Non-root user execution (uid 1000)
- Ephemeral containers (`--rm` flag)

**3. Credential Proxy Mechanism**
- Real API credentials never enter the container
- Host machine runs an HTTP credential proxy (port 3001)
- Container receives placeholder API keys, proxy injects real credentials
- Agent cannot discover real credentials from environment variables, files, or `/proc`

**4. Skills System Replaces Feature Stacking**
- Instead of adding features to core code, uses Skills to transform the user's fork
- Users run skill commands like `/add-telegram`, and Claude Code modifies the code
- Each user gets customized clean code, not a bloated generic system
- Skills are committed as git branches, users apply them via merge

## Core Architecture

### System Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                    Host Process (Node.js)                         │
├──────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐              ┌────────────────┐                │
│  │ Channel      │─────────────▶│  SQLite DB     │                │
│  │ System       │◀─────────────│  (messages.db) │                │
│  │ (self-reg)   │              └────────┬───────┘                │
│  └──────────────┘                       │                         │
│                                         │                         │
│  ┌──────────────┐    ┌──────────────┐  │  ┌──────────────┐      │
│  │ Message Poll │    │ Scheduler    │  │  │ IPC Listener │      │
│  │ Loop         │    │ Loop         │  │  └──────────────┘      │
│  └──────┬───────┘    └──────┬───────┘  │                         │
│         │                   │          │                         │
│         └───────────┬───────┘          │                         │
│                     │ Spawn Container  │                         │
│                     ▼                  │                         │
├──────────────────────────────────────────────────────────────────┤
│                   Container (Linux VM)                            │
├──────────────────────────────────────────────────────────────────┤
│  Working Dir: /workspace/group (mounted from host)               │
│  Volume Mounts:                                                  │
│    • groups/{name}/ → /workspace/group                           │
│    • groups/global/ → /workspace/global/ (non-main groups)       │
│    • data/sessions/{group}/.claude/ → /home/node/.claude/        │
│  Tools: Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch│
│        agent-browser, mcp__nanoclaw__* (via IPC)                 │
└──────────────────────────────────────────────────────────────────┘
```

### Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Channel System | Channel Registry (`src/channels/registry.ts`) | Self-registration on startup |
| Message Storage | SQLite (better-sqlite3) | Stores messages for polling |
| Container Runtime | Docker / Apple Container | Isolated environment for Agent execution |
| Agent | @anthropic-ai/claude-agent-sdk | Runs Claude with tools and MCP servers |
| Browser Automation | agent-browser + Chromium | Web interaction and screenshots |
| Runtime | Node.js 20+ | Host process for routing and scheduling |

### Channel System Architecture

**Self-registration Pattern**:
1. Each channel skill adds a file in `src/channels/` (e.g., `whatsapp.ts`)
2. Module calls `registerChannel()` on load
3. Barrel file `src/channels/index.ts` imports all channel modules, triggering registration
4. On startup, the orchestrator connects all channels with credentials; channels missing credentials emit a WARN log and are skipped

**Channel Interface**:
```typescript
interface Channel {
  name: string;
  connect(): Promise<void>;
  sendMessage(jid: string, text: string): Promise<void>;
  isConnected(): boolean;
  ownsJid(jid: string): boolean;
  disconnect(): Promise<void>;
  setTyping?(jid: string, isTyping: boolean): Promise<void>;
  syncGroups?(force: boolean): Promise<void>;
}
```

### Message Flow

```
Channel --> SQLite --> Poll Loop --> Container (Claude Agent SDK) --> Response
```

- Single Node.js process
- Channels added via skills and self-registered on startup
- Agent executes in isolated Linux containers with filesystem isolation
- Only mounted directories are accessible
- Per-group message queue with concurrency control
- IPC via filesystem

### Key Files

- `src/index.ts` - Orchestrator: state, message loop, agent invocation
- `src/channels/registry.ts` - Channel registry (self-registration on startup)
- `src/ipc.ts` - IPC listener and task handling
- `src/router.ts` - Message formatting and outbound routing
- `src/group-queue.ts` - Per-group queue with global concurrency limit
- `src/container-runner.ts` - Spawns streaming agent containers
- `src/task-scheduler.ts` - Runs scheduled tasks
- `src/db.ts` - SQLite operations (messages, groups, sessions, state)
- `groups/*/CLAUDE.md` - Per-group memory

## Key Features

### 1. Multi-channel Messaging Support

- Chat with the assistant from WhatsApp, Telegram, Discord, Slack, or Gmail
- Add channels via skills (e.g., `/add-whatsapp`, `/add-telegram`)
- Can run one or more channels simultaneously

### 2. Isolated Group Contexts

- Each group has its own `CLAUDE.md` memory
- Isolated filesystem
- Runs in its own container sandbox with only that filesystem mounted

### 3. Main Channel

- Private channel (self-chat) for admin control
- Each group fully isolated

### 4. Scheduled Tasks

- Periodic jobs that run Claude and can reply to messages

### 5. Web Access

- Search and fetch web content

### 6. Container Isolation

- Agents sandboxed in Apple Container (macOS) or Docker (macOS/Linux)

### 7. Agent Swarms

- Launch specialized agent teams to collaborate on complex tasks
- NanoClaw is the first personal AI assistant to support agent swarms

### 8. Optional Integrations

- Add Gmail (`/add-gmail`) and more via skills

### 9. Skills System Architecture

**Three-layer Resolution Model**:
1. **Git Layer** - Deterministic, programmatic. `git merge-file` merging, `git rerere` replays cached resolutions. No AI involved. Handles the vast majority of cases.
2. **Claude Code Layer** - Reads `SKILL.md`, `.intent.md`, migration guides, and `state.yaml` to understand context. Resolves conflicts that git cannot handle programmatically. Caches resolutions via `git rerere`.
3. **User Layer** - Asks the user when Claude Code lacks context or intent. Only occurs when two features truly conflict at the application level.

**Skill Package Structure**:
```
skills/
  add-whatsapp/
    SKILL.md                    # Context, intent, feature description
    manifest.yaml               # Metadata, dependencies, env vars, post-apply steps
    tests/                      # Integration tests
      whatsapp.test.ts
    add/                        # New files - copied directly
      src/channels/whatsapp.ts
    modify/                     # Modified code files - merged via git merge-file
      src/server.ts             # Full file: clean core + whatsapp changes
      src/server.ts.intent.md   # Intent description
```

**Structured Operations**:
- `package.json`, `docker-compose.yml`, `.env.example`, etc. are not text-merged
- Skills declare structured requirements in the manifest, applied programmatically by the system
- Batch processing: merge all dependency declarations, write to `package.json` once, run `npm install` once at the end

### 10. Security Model

**Trust Model**:
| Entity | Trust Level | Rationale |
|--------|------------|-----------|
| Main Group | Trusted | Private self-chat, admin control |
| Non-main Groups | Untrusted | Other users may be malicious |
| Container Agent | Sandboxed | Isolated execution environment |
| WhatsApp Messages | User Input | Potential prompt injection |

**Security Boundaries**:

1. **Container Isolation (Primary Boundary)**
   - Process isolation - container processes cannot affect the host
   - Filesystem isolation - only explicitly mounted directories are visible
   - Non-root execution - runs as unprivileged `node` user (uid 1000)
   - Ephemeral containers - each invocation is a fresh environment (`--rm`)

2. **Mount Security**
   - External allowlist - mount permissions stored in `~/.config/nanoclaw/mount-allowlist.json`
   - Outside the project root, never mounted into containers; agent cannot modify
   - Default block patterns: `.ssh`, `.gnupg`, `.aws`, `.azure`, `.gcloud`, `.kube`, `.docker`, `credentials`, `.env`, `.netrc`, `.npmrc`, `id_rsa`, `id_ed25519`, `private_key`, `.secret`
   - Symlinks resolved before validation (prevents traversal attacks)
   - Container path validation (rejects `..` and absolute paths)
   - `nonMainReadOnly` option forces read-only for non-main groups

3. **Read-only Project Root**
   - Main group's project root mounted as read-only
   - Writable paths the agent needs (group folders, IPC, `.claude/`) mounted separately
   - Prevents agent from modifying host application code (`src/`, `dist/`, `package.json`, etc.)

4. **Session Isolation**
   - Each group has isolated Claude sessions in `data/sessions/{group}/.claude/`
   - Groups cannot see other groups' conversation history
   - Prevents cross-group information leakage

5. **IPC Authorization**
   - Message and task operations verified against group identity

6. **Credential Isolation (Credential Proxy)**
   - Real API credentials never enter the container
   - Host machine runs an HTTP credential proxy
   - Container receives placeholder credentials, proxy injects real credentials
   - Agent cannot discover real credentials

## Summary

NanoClaw is a lightweight alternative to OpenClaw, with core value in:
1. **Understandability**: Codebase small enough to fully comprehend
2. **Security**: Container-level isolation + credential proxy
3. **Customizability**: Skills system + AI-assisted modifications
4. **AI-native**: Claude Code-driven setup, debugging, and operations

<!-- lastCommit: c090287 -->

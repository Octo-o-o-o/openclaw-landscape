> https://github.com/abhi1693/openclaw-mission-control

# OpenClaw Mission Control — Agent Orchestration & Governance Control Plane

## Basic Information

- **GitHub**: https://github.com/abhi1693/openclaw-mission-control
- **Stars**: 1,957
- **Author**: abhi1693
- **Positioning**: A centralized operations and governance platform for OpenClaw, providing unified work orchestration, Agent management, approval controls, and Gateway integration
- **Core Value**: Provides unified visibility, approval controls, and Gateway-aware orchestration capabilities for running OpenClaw across teams and organizations

## Problem & Solution

### Core Pain Points

1. **Complex Multi-Agent Operations** — Enterprise environments running multiple OpenClaw Agents lack a unified management interface, requiring switching between multiple tools
2. **Lack of Approval & Governance** — Sensitive operations (e.g., deleting data, executing high-privilege commands) lack human approval workflows, posing security risks
3. **Difficult Distributed Environment Management** — Multiple Gateway environments (dev, staging, production) lack unified orchestration and monitoring
4. **Opaque Workflows** — No unified activity logs or audit trails, making it difficult to troubleshoot issues and trace operations
5. **Low Team Collaboration Efficiency** — Lack of task assignment, Board management, and tagging system tools for collaboration
6. **Missing API Automation** — Operations depend on manual execution, lacking API support for automation

### Solution

OpenClaw Mission Control addresses the above issues through:

1. **Unified Control Plane** — Provides Web UI and HTTP API for unified management of Organizations, Board Groups, Boards, Tasks, Agents, and Gateways
2. **Approval-Driven Governance** — Sensitive operations require approval workflows, preserving decision trails
3. **Gateway-Aware Orchestration** — Connects and operates remote execution environments without changing operational workflows
4. **Activity History & Audit** — Records all system operations, supporting quick troubleshooting and accountability
5. **API-First Design** — Web UI and automation clients use the same API, supporting CI/CD integration
6. **Team-Level Structure** — Organizations, Board Groups, Boards, Tasks, Tags, and Users managed in a single system

## Core Architecture

### Tech Stack

- **Backend**: FastAPI + Python 3.12 + SQLAlchemy 2 (async) + Alembic
- **Frontend**: Next.js (App Router) + TypeScript + Tailwind CSS
- **Database**: PostgreSQL
- **Testing**: pytest (backend) + vitest + Testing Library (frontend)
- **CI/CD**: GitHub Actions (lint / typecheck / test / coverage / build)
- **Deployment**: Docker Compose + one-click install script

### Project Structure

```
openclaw-mission-control/
├── backend/
│   ├── app/
│   │   ├── api/              # 25 API routes
│   │   │   ├── activity.py
│   │   │   ├── agents.py
│   │   │   ├── approvals.py
│   │   │   ├── boards.py
│   │   │   ├── board_groups.py
│   │   │   ├── gateways.py
│   │   │   ├── organizations.py
│   │   │   ├── tasks.py
│   │   │   ├── tags.py
│   │   │   └── ...
│   │   ├── models/           # 20+ SQLAlchemy models
│   │   │   ├── base.py
│   │   │   ├── agents.py
│   │   │   ├── approvals.py
│   │   │   ├── boards.py
│   │   │   ├── tasks.py
│   │   │   ├── gateways.py
│   │   │   └── ...
│   │   ├── services/         # Business logic services
│   │   │   ├── openclaw/     # OpenClaw integration
│   │   │   │   ├── gateway_dispatch.py
│   │   │   │   ├── gateway_rpc.py
│   │   │   │   ├── lifecycle_orchestrator.py
│   │   │   │   ├── provisioning.py
│   │   │   │   └── ...
│   │   │   ├── activity_log.py
│   │   │   ├── approval_task_links.py
│   │   │   ├── board_lifecycle.py
│   │   │   └── ...
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── core/             # Core utilities (logging, time, config)
│   │   └── db/               # Database sessions, pagination, query managers
│   ├── migrations/           # Alembic migrations
│   ├── tests/                # pytest test suite
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/              # Next.js App Router
│   │   │   ├── activity/
│   │   │   ├── agents/
│   │   │   ├── approvals/
│   │   │   ├── boards/
│   │   │   ├── board-groups/
│   │   │   ├── gateways/
│   │   │   ├── organization/
│   │   │   ├── settings/
│   │   │   └── ...
│   │   ├── components/       # React components
│   │   ├── lib/              # Utility functions
│   │   └── api/generated/    # Auto-generated API client
│   ├── cypress/              # E2E tests
│   └── Dockerfile
├── docs/                     # Documentation
│   ├── architecture/
│   ├── deployment/
│   ├── development/
│   ├── getting-started/
│   ├── operations/
│   ├── reference/
│   └── testing/
├── scripts/                  # Utility scripts
├── compose.yml               # Docker Compose configuration
├── install.sh                # One-click install script
└── Makefile                  # Development commands
```

### Data Model

**Core Entities**:

1. **Organization** — Organization (tenant isolation)
2. **Board Group** — Board grouping (e.g., "Q1 Goals", "Engineering")
3. **Board** — Work board (corresponds to a goal or project)
4. **Task** — Task (work item within a Board)
5. **Agent** — OpenClaw Agent (executes tasks)
6. **Gateway** — OpenClaw Gateway (connects to remote environments)
7. **Approval** — Approval (sensitive operations require approval)
8. **Tag** — Tag (for categorization and filtering)
9. **User** — User (operator)
10. **Activity Event** — Activity log (audit trail)

**Relationship Diagram**:
```
Organization
  ├── Board Groups
  │   └── Boards
  │       ├── Tasks
  │       ├── Agents
  │       └── Approvals
  ├── Gateways
  ├── Tags
  └── Users
```

**Board Model**:
```python
class Board(TenantScoped, table=True):
    id: UUID
    organization_id: UUID
    name: str
    slug: str
    description: str
    gateway_id: UUID | None              # Associated Gateway
    board_group_id: UUID | None          # Parent Board Group
    board_type: str = "goal"             # Board type
    objective: str | None                # Objective description
    success_metrics: dict | None         # Success metrics
    target_date: datetime | None         # Target date
    goal_confirmed: bool = False         # Whether objective is confirmed
    require_approval_for_done: bool = True  # Require approval for task completion
    require_review_before_done: bool = False  # Require review before completion
    block_status_changes_with_pending_approval: bool = False  # Block status changes when approvals are pending
    only_lead_can_change_status: bool = False  # Only Lead can change status
    max_agents: int = 1                  # Maximum number of Agents
    created_at: datetime
    updated_at: datetime
```

**Task Model**:
```python
class Task(TenantScoped, table=True):
    id: UUID
    board_id: UUID | None
    title: str
    description: str | None
    status: str = "inbox"                # inbox / in_progress / done / blocked
    priority: str = "medium"             # low / medium / high / urgent
    due_at: datetime | None
    in_progress_at: datetime | None
    previous_in_progress_at: datetime | None
    created_by_user_id: UUID | None
    assigned_agent_id: UUID | None       # Which Agent is assigned
    auto_created: bool = False           # Whether auto-created
    auto_reason: str | None              # Reason for auto-creation
    created_at: datetime
    updated_at: datetime
```

**Approval Model**:
```python
class Approval:
    id: UUID
    board_id: UUID
    task_id: UUID | None                 # Associated task (optional)
    status: str = "pending"              # pending / approved / rejected
    action_type: str                     # Action type (e.g., "delete_task")
    action_context: dict | None          # Action context
    requested_by_agent_id: UUID | None
    requested_by_user_id: UUID | None
    resolved_by_user_id: UUID | None
    resolved_at: datetime | None
    created_at: datetime
```

### OpenClaw Integration Architecture

**Gateway Integration**:
- **Gateway Dispatch** — Dispatches tasks to remote Gateways for execution
- **Gateway RPC** — Communicates with Gateways via WebSocket
- **Lifecycle Orchestrator** — Manages Agent lifecycle (start, stop, restart)
- **Provisioning** — Automatically configures Agents (generates config files, injects environment variables)

**Agent Management**:
- **Agent Registration** — Registers OpenClaw Agents with Mission Control
- **Agent Status Sync** — Real-time Agent status synchronization (running, idle, error)
- **Agent Assignment** — Assigns tasks to specific Agents
- **Agent Approval** — Triggers approval workflows when Agents execute sensitive operations

## Key Features

### 1. Work Orchestration

**Organizations**:
- Multi-tenant isolation
- Organization-level permission control
- Organization invitations and member management

**Board Groups**:
- Grouping by quarter, department, or project
- Supports nested structures
- Batch operations (e.g., "archive all Q1 Boards")

**Boards**:
- Objective-driven work boards (Objective, Success Metrics, Target Date)
- Approval policy configuration (require approval for task completion, only Lead can change status)
- Gateway binding (Board associated with a specific Gateway environment)
- Board snapshots (records Board configuration change history)

**Tasks**:
- Status management (inbox / in_progress / done / blocked)
- Priority (low / medium / high / urgent)
- Task dependencies
- Custom fields
- Task assignment (assign to User or Agent)
- Auto-creation (Agents auto-create tasks)

**Tags**:
- Cross-Board tagging system
- Supports colors and icons
- Tag filtering and search

### 2. Agent Operations

**Agent Lifecycle Management**:
- Create Agent (auto-generates config files)
- Start / Stop / Restart Agent
- Agent status monitoring (running, idle, error)
- Agent log viewing

**Agent Configuration**:
- SOUL.md editing (Agent persona definition)
- IDENTITY.md editing (Agent identity information)
- Environment variable injection
- Skill installation and management

**Agent Assignment**:
- Assign tasks to specific Agents
- Agent load balancing (auto-assign tasks to idle Agents)
- Agent permission control (Agents can only access tasks assigned to them)

### 3. Governance and Approvals

**Approval Workflow**:
- Sensitive operations trigger approvals (e.g., deleting tasks, executing high-privilege commands)
- Approval requests include action context (who requested, what operation, why)
- Approval decision records (who approved/rejected, when, reason)
- Approval history tracking

**Approval Policies**:
- Board-level approval policy (`require_approval_for_done`)
- Task-level approval policy (`block_status_changes_with_pending_approval`)
- Custom approval rules (e.g., "task deletion requires 2-person approval")

**Approval-Task Association**:
- An approval can be associated with multiple tasks (batch operations)
- Automatic check for pending approvals when task status changes
- Operations execute automatically after approval

### 4. Gateway Management

**Gateway Registration**:
- Connect to remote OpenClaw Gateways
- Gateway authentication (Token-based)
- Gateway health checks

**Gateway Orchestration**:
- Bind Boards to specific Gateways
- Tasks auto-dispatched to corresponding Gateways for execution
- Gateway failover (switch to backup Gateway when primary fails)

**Gateway Communication**:
- WebSocket real-time communication
- RPC calls (start Agent, execute commands, query status)
- Message queue (async task dispatch)

### 5. Activity Visibility

**Activity Log**:
- Records all system operations (create, update, delete, approve)
- Includes operator, timestamp, operation type, and operation context
- Supports filtering and search (by time, operator, operation type)

**Audit Trail**:
- Reconstruct operation history ("who did what and when")
- Troubleshooting ("why did the task status change to blocked")
- Compliance audit ("what sensitive operations occurred in the past 30 days")

**Activity Timeline**:
- Board-level activity timeline (shows all operations within a Board)
- Task-level activity timeline (shows all changes to a task)
- Agent-level activity timeline (shows all Agent operations)

### 6. API-First Model

**Unified API**:
- Web UI and automation clients use the same API
- RESTful API (25 routes)
- OpenAPI specification (auto-generated API documentation)

**Auto-Generated Client**:
- Uses Orval to auto-generate TypeScript client (`frontend/src/api/generated/`)
- Type-safe API calls
- Automatic authentication and error handling

**CI/CD Integration**:
- Auto-create tasks via API
- Trigger Agent execution via API
- Query task status via API

### 7. Authentication & Authorization

**Dual Authentication Modes**:
- **Local Mode** — Shared Bearer Token (suitable for self-hosting)
- **Clerk Mode** — Clerk JWT authentication (suitable for SaaS)

**Agent Authentication**:
- Agents authenticate via `X-Agent-Token` header
- Agent permission isolation (can only access assigned tasks)
- Agent rate limiting (20 requests / 60 seconds / IP)

**User Permissions**:
- Organization-level permissions (Owner / Admin / Member)
- Board-level permissions (Lead / Contributor / Viewer)
- Operation-level permissions (e.g., "only Lead can delete tasks")

### 8. One-Click Installation & Deployment

**Install Script** (`install.sh`):
- Interactive installation wizard
- Auto-detects system dependencies (Docker, Docker Compose, Node.js)
- Auto-installs missing dependencies (macOS via Homebrew)
- Generates configuration files (`.env`)
- Starts services (Docker Compose or local mode)

**Deployment Modes**:
- **Docker Mode** — One-click full stack startup (recommended)
- **Local Mode** — Local development (backend + frontend separated)

**Supported Platforms**:
- Linux (Ubuntu, Debian, CentOS, Fedora)
- macOS (Intel + Apple Silicon)
- Windows WSL2

## Summary

OpenClaw Mission Control is an excellent **Agent orchestration and governance control plane**. Through its unified Web UI and API, approval-driven governance, Gateway-aware orchestration, and activity history with audit trails, it provides a complete operations solution for enterprise-grade OpenClaw deployments.

<!-- lastCommit: 010bac00050a8fa041474a89574d7961ba8f334c -->

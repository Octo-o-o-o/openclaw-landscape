# OpenClaw Mission Control — Agent 编排与治理控制平面

## 基本信息

- **GitHub**: https://github.com/abhi1693/openclaw-mission-control
- **Stars**: 1,957
- **作者**: abhi1693
- **定位**: OpenClaw 的集中式运维与治理平台，提供统一的工作编排、Agent 管理、审批控制、Gateway 集成
- **核心价值**: 为跨团队、跨组织运行 OpenClaw 提供统一的可见性、审批控制、Gateway 感知的编排能力

## 问题与解决方案

### 核心痛点

1. **多 Agent 运维复杂** — 企业环境中运行多个 OpenClaw Agent，缺乏统一的管理界面，需要在多个工具间切换
2. **缺乏审批与治理** — 敏感操作（如删除数据、执行高权限命令）缺乏人工审批流程，存在安全风险
3. **分布式环境管理困难** — 多个 Gateway 环境（开发、测试、生产）缺乏统一的编排和监控
4. **工作流程不透明** — 缺乏统一的活动日志和审计追踪，难以排查问题和追溯操作
5. **团队协作效率低** — 缺乏任务分配、Board 管理、标签系统等协作工具
6. **API 自动化缺失** — 运维操作依赖手动执行，缺乏 API 支持自动化

### 解决方案

OpenClaw Mission Control 通过以下方式解决上述问题：

1. **统一控制平面** — 提供 Web UI 和 HTTP API，统一管理 Organizations、Board Groups、Boards、Tasks、Agents、Gateways
2. **审批驱动的治理** — 敏感操作需要通过审批流程，保留决策轨迹
3. **Gateway 感知的编排** — 连接和操作远程执行环境，无需改变运维工作流
4. **活动历史与审计** — 记录所有系统操作，支持快速排查和问责
5. **API 优先设计** — Web UI 和自动化客户端使用相同的 API，支持 CI/CD 集成
6. **团队级结构** — Organizations、Board Groups、Boards、Tasks、Tags、Users 在一个系统中统一管理

## 核心架构

### 技术栈

- **后端**: FastAPI + Python 3.12 + SQLAlchemy 2 (async) + Alembic
- **前端**: Next.js (App Router) + TypeScript + Tailwind CSS
- **数据库**: PostgreSQL
- **测试**: pytest (后端) + vitest + Testing Library (前端)
- **CI/CD**: GitHub Actions (lint / typecheck / test / coverage / build)
- **部署**: Docker Compose + 一键安装脚本

### 项目结构

```
openclaw-mission-control/
├── backend/
│   ├── app/
│   │   ├── api/              # 25 个 API 路由
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
│   │   ├── models/           # 20+ SQLAlchemy 模型
│   │   │   ├── base.py
│   │   │   ├── agents.py
│   │   │   ├── approvals.py
│   │   │   ├── boards.py
│   │   │   ├── tasks.py
│   │   │   ├── gateways.py
│   │   │   └── ...
│   │   ├── services/         # 业务逻辑服务
│   │   │   ├── openclaw/     # OpenClaw 集成
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
│   │   ├── core/             # 核心工具（logging、time、config）
│   │   └── db/               # 数据库会话、分页、查询管理器
│   ├── migrations/           # Alembic 迁移
│   ├── tests/                # pytest 测试套件
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
│   │   ├── components/       # React 组件
│   │   ├── lib/              # 工具函数
│   │   └── api/generated/    # 自动生成的 API 客户端
│   ├── cypress/              # E2E 测试
│   └── Dockerfile
├── docs/                     # 文档
│   ├── architecture/
│   ├── deployment/
│   ├── development/
│   ├── getting-started/
│   ├── operations/
│   ├── reference/
│   └── testing/
├── scripts/                  # 工具脚本
├── compose.yml               # Docker Compose 配置
├── install.sh                # 一键安装脚本
└── Makefile                  # 开发命令
```

### 数据模型

**核心实体**:

1. **Organization** — 组织（租户隔离）
2. **Board Group** — Board 分组（如 "Q1 Goals"、"Engineering"）
3. **Board** — 工作板（对应一个目标或项目）
4. **Task** — 任务（Board 中的工作项）
5. **Agent** — OpenClaw Agent（执行任务）
6. **Gateway** — OpenClaw Gateway（连接远程环境）
7. **Approval** — 审批（敏感操作需要审批）
8. **Tag** — 标签（用于分类和筛选）
9. **User** — 用户（操作者）
10. **Activity Event** — 活动日志（审计追踪）

**关系图**:
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

**Board 模型**:
```python
class Board(TenantScoped, table=True):
    id: UUID
    organization_id: UUID
    name: str
    slug: str
    description: str
    gateway_id: UUID | None              # 关联的 Gateway
    board_group_id: UUID | None          # 所属 Board Group
    board_type: str = "goal"             # Board 类型
    objective: str | None                # 目标描述
    success_metrics: dict | None         # 成功指标
    target_date: datetime | None         # 目标日期
    goal_confirmed: bool = False         # 目标是否确认
    require_approval_for_done: bool = True  # 完成任务需要审批
    require_review_before_done: bool = False  # 完成前需要审查
    block_status_changes_with_pending_approval: bool = False  # 有待审批时阻止状态变更
    only_lead_can_change_status: bool = False  # 仅 Lead 可以变更状态
    max_agents: int = 1                  # 最大 Agent 数量
    created_at: datetime
    updated_at: datetime
```

**Task 模型**:
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
    assigned_agent_id: UUID | None       # 分配给哪个 Agent
    auto_created: bool = False           # 是否自动创建
    auto_reason: str | None              # 自动创建原因
    created_at: datetime
    updated_at: datetime
```

**Approval 模型**:
```python
class Approval:
    id: UUID
    board_id: UUID
    task_id: UUID | None                 # 关联的任务（可选）
    status: str = "pending"              # pending / approved / rejected
    action_type: str                     # 操作类型（如 "delete_task"）
    action_context: dict | None          # 操作上下文
    requested_by_agent_id: UUID | None
    requested_by_user_id: UUID | None
    resolved_by_user_id: UUID | None
    resolved_at: datetime | None
    created_at: datetime
```

### OpenClaw 集成架构

**Gateway 集成**:
- **Gateway Dispatch** — 将任务分发到远程 Gateway 执行
- **Gateway RPC** — 通过 WebSocket 与 Gateway 通信
- **Lifecycle Orchestrator** — 管理 Agent 生命周期（启动、停止、重启）
- **Provisioning** — 自动配置 Agent（生成配置文件、注入环境变量）

**Agent 管理**:
- **Agent 注册** — 将 OpenClaw Agent 注册到 Mission Control
- **Agent 状态同步** — 实时同步 Agent 状态（运行中、空闲、错误）
- **Agent 分配** — 将任务分配给特定 Agent
- **Agent 审批** — Agent 执行敏感操作时触发审批流程

## 关键特性

### 1. 工作编排（Work Orchestration）

**Organizations**:
- 多租户隔离
- 组织级权限控制
- 组织邀请与成员管理

**Board Groups**:
- 按季度、部门、项目分组
- 支持嵌套结构
- 批量操作（如 "归档 Q1 所有 Boards"）

**Boards**:
- 目标驱动的工作板（Objective、Success Metrics、Target Date）
- 审批策略配置（完成任务需要审批、仅 Lead 可以变更状态）
- Gateway 绑定（Board 关联特定 Gateway 环境）
- Board 快照（记录 Board 配置变更历史）

**Tasks**:
- 状态管理（inbox / in_progress / done / blocked）
- 优先级（low / medium / high / urgent）
- 任务依赖（Task Dependencies）
- 自定义字段（Custom Fields）
- 任务分配（分配给 User 或 Agent）
- 自动创建（Agent 自动创建任务）

**Tags**:
- 跨 Board 的标签系统
- 支持颜色和图标
- 标签筛选和搜索

### 2. Agent 运维（Agent Operations）

**Agent 生命周期管理**:
- 创建 Agent（自动生成配置文件）
- 启动 / 停止 / 重启 Agent
- Agent 状态监控（运行中、空闲、错误）
- Agent 日志查看

**Agent 配置**:
- SOUL.md 编辑（Agent 人格定义）
- IDENTITY.md 编辑（Agent 身份信息）
- 环境变量注入
- 技能安装与管理

**Agent 分配**:
- 将任务分配给特定 Agent
- Agent 负载均衡（自动分配任务到空闲 Agent）
- Agent 权限控制（Agent 只能访问分配给它的任务）

### 3. 审批与治理（Governance and Approvals）

**审批流程**:
- 敏感操作触发审批（如删除任务、执行高权限命令）
- 审批请求包含操作上下文（谁请求、什么操作、为什么）
- 审批决策记录（谁批准/拒绝、何时、原因）
- 审批历史追踪

**审批策略**:
- Board 级审批策略（`require_approval_for_done`）
- 任务级审批策略（`block_status_changes_with_pending_approval`）
- 自定义审批规则（如 "删除任务需要 2 人审批"）

**审批与任务关联**:
- 一个审批可以关联多个任务（批量操作）
- 任务状态变更时自动检查是否有待审批
- 审批通过后自动执行操作

### 4. Gateway 管理（Gateway Management）

**Gateway 注册**:
- 连接远程 OpenClaw Gateway
- Gateway 认证（Token-based）
- Gateway 健康检查

**Gateway 编排**:
- 将 Board 绑定到特定 Gateway
- 任务自动分发到对应 Gateway 执行
- Gateway 故障转移（主 Gateway 失败时切换到备用 Gateway）

**Gateway 通信**:
- WebSocket 实时通信
- RPC 调用（启动 Agent、执行命令、查询状态）
- 消息队列（异步任务分发）

### 5. 活动历史与审计（Activity Visibility）

**活动日志**:
- 记录所有系统操作（创建、更新、删除、审批）
- 包含操作者、时间戳、操作类型、操作上下文
- 支持筛选和搜索（按时间、操作者、操作类型）

**审计追踪**:
- 重建操作历史（"谁在何时做了什么"）
- 故障排查（"为什么任务状态变成了 blocked"）
- 合规审计（"过去 30 天内有哪些敏感操作"）

**活动时间线**:
- Board 级活动时间线（显示 Board 内所有操作）
- Task 级活动时间线（显示任务的所有变更）
- Agent 级活动时间线（显示 Agent 的所有操作）

### 6. API 优先设计（API-First Model）

**统一 API**:
- Web UI 和自动化客户端使用相同的 API
- RESTful API（25 个路由）
- OpenAPI 规范（自动生成 API 文档）

**自动生成的客户端**:
- 使用 Orval 自动生成 TypeScript 客户端（`frontend/src/api/generated/`）
- 类型安全的 API 调用
- 自动处理认证和错误

**CI/CD 集成**:
- 通过 API 自动创建任务
- 通过 API 触发 Agent 执行
- 通过 API 查询任务状态

### 7. 认证与授权（Authentication & Authorization）

**双认证模式**:
- **Local Mode** — 共享 Bearer Token（适合自托管）
- **Clerk Mode** — Clerk JWT 认证（适合 SaaS）

**Agent 认证**:
- Agent 通过 `X-Agent-Token` 头认证
- Agent 权限隔离（只能访问分配给它的任务）
- Agent 速率限制（20 请求 / 60 秒 / IP）

**用户权限**:
- Organization 级权限（Owner / Admin / Member）
- Board 级权限（Lead / Contributor / Viewer）
- 操作级权限（如 "只有 Lead 可以删除任务"）

### 8. 一键安装与部署

**安装脚本** (`install.sh`):
- 交互式安装向导
- 自动检测系统依赖（Docker、Docker Compose、Node.js）
- 自动安装缺失依赖（macOS 通过 Homebrew）
- 生成配置文件（`.env`）
- 启动服务（Docker Compose 或本地模式）

**部署模式**:
- **Docker 模式** — 一键启动完整栈（推荐）
- **本地模式** — 本地开发（后端 + 前端分离）

**支持平台**:
- Linux（Ubuntu、Debian、CentOS、Fedora）
- macOS（Intel + Apple Silicon）
- Windows WSL2
## 总结

OpenClaw Mission Control 是一个优秀的 **Agent 编排与治理控制平面**，通过统一的 Web UI 和 API、审批驱动的治理、Gateway 感知的编排、活动历史与审计追踪，为企业级 OpenClaw 部署提供了完整的运维解决方案。ClawButler 可以借鉴其思路，完善 **Dashboard**、**审批流程**、**Gateway 编排**、**活动时间线**、**Board 与 Task 管理**、**一键安装脚本**、**API 自动生成客户端**、**测试覆盖率策略**，提升企业级运维能力和用户体验。

# OpenClaw Studio

## 基本信息

- **GitHub**: https://github.com/grp06/openclaw-studio
- **Stars**: 1,549
- **语言**: TypeScript
- **创建时间**: 2026-01-28
- **最后更新**: 2026-03-11
- **描述**: A clean web dashboard for OpenClaw. Connect your Gateway, manage agents, and ship faster.

## 问题与解决方案

### 核心问题

OpenClaw 原生架构存在以下痛点：

1. **部署复杂性**：单进程架构，Agent 创建需要手动配置 + 重启
2. **可见性不足**：缺乏统一的可视化界面，难以监控 Agent 状态和任务执行
3. **移动端访问困难**：依赖特定 Channel 配置，无法开箱即用
4. **人工干预不便**：缺少直观的审批流程和权限管理界面
5. **多 Agent 协作困难**：没有统一的控制面板管理多个 Agent 实例

### 解决方案

OpenClaw Studio 提供了一个现代化的 Web Dashboard，通过以下方式解决上述问题：

1. **零配置连接**：通过 WebSocket 连接到 OpenClaw Gateway，无需修改 Gateway 配置
2. **统一控制面板**：单一界面管理所有 Agent、会话、任务和审批
3. **实时监控**：SSE 流式传输运行时事件，实时展示 Agent 思考过程、工具调用和执行结果
4. **可视化审批流程**：图形化界面处理 exec 命令审批，支持"允许一次"、"总是允许"、"拒绝"
5. **移动端友好**：响应式设计，支持移动浏览器访问
6. **Cron 任务管理**：可视化创建和管理定时任务
7. **权限精细控制**：图形化配置 Agent 工具策略、沙箱模式、工作空间访问权限

## 核心架构

### 系统架构

OpenClaw Studio 采用**服务端控制平面架构**（Server-Owned Control Plane），完全摒弃了浏览器直连 Gateway 的模式：

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

### 关键设计决策

1. **服务端 WebSocket 适配器**：Studio 服务端维护一个到 Gateway 的 WebSocket 连接，浏览器通过 HTTP API 和 SSE 与 Studio 通信
2. **SQLite 持久化**：运行时事件投影和重放队列存储在 `runtime.db`，确保页面刷新和进程重启后的状态一致性
3. **SSE 流式传输**：`/api/runtime/stream` 提供实时事件流，支持 `Last-Event-ID` 重放机制
4. **Intent-based 写操作**：所有变更操作通过 `/api/intents/*` 路由，语义化 API 设计
5. **Gateway 令牌服务端托管**：令牌存储在服务端 `settings.json`，API 响应中自动脱敏

### 核心模块

#### 1. Control Plane Runtime

**位置**: `src/lib/controlplane/`

- **openclaw-adapter.ts**: 上游 WebSocket 生命周期管理、握手、请求白名单、重连策略
- **runtime.ts**: 进程级单例运行时、订阅扇出、Gateway 调用边界
- **projection-store.ts**: SQLite 投影存储 + 事件队列（`runtime.db`）

#### 2. Runtime Read Routes

**位置**: `src/app/api/runtime/`

- `/summary`: 运行时摘要
- `/fleet`: Agent 舰队状态
- `/agents/[agentId]/history`: Agent 历史记录（支持分页和游标）
- `/stream`: SSE 事件流（支持 `Last-Event-ID` 重放）
- `/config`, `/models`, `/sessions`, `/chat-history`, `/cron`, `/skills/status`, `/agent-file`, `/agent-state`, `/media`: 各类资源查询

#### 3. Intent Routes

**位置**: `src/app/api/intents/`

**聊天相关**:
- `/chat-send`: 发送消息
- `/chat-abort`: 中止对话
- `/sessions-reset`: 重置会话

**Agent 管理**:
- `/agent-create`: 创建 Agent
- `/agent-rename`: 重命名 Agent
- `/agent-delete`: 删除 Agent
- `/agent-wait`: 等待 Agent 就绪
- `/agent-permissions-update`: 更新权限
- `/agent-skills-allowlist`: 技能白名单
- `/agent-file-set`: 设置 Agent 文件

**审批管理**:
- `/exec-approval-resolve`: 解决单个审批
- `/exec-approvals-set`: 批量设置审批策略

**Cron 任务**:
- `/cron-add`, `/cron-run`, `/cron-remove`, `/cron-remove-agent`, `/cron-restore`

**技能管理**:
- `/skills-install`, `/skills-update`, `/skills-remove`

#### 4. Settings Boundary

**位置**: `src/app/api/studio/route.ts`

- 持久化文件: `~/.openclaw/openclaw-studio/settings.json`
- Gateway 令牌服务端托管，API 响应自动脱敏
- Gateway URL/Token 变更触发确定性重连：`runtime.reconnectForGatewaySettingsChange()`

### 运行时持久化模型

**SQLite 数据库路径**: `${resolveStateDir()}/openclaw-studio/runtime.db`

**Projection Store 职责**:
- 幂等应用领域事件
- 持久化有序事件队列
- 提供重放/历史窗口查询

**SSE 重放行为**:
- 携带 `Last-Event-ID`: 从该 ID 向前重放
- 不携带 `Last-Event-ID`: 从队列头部重放最近的尾部窗口

### 历史记录模型

**路由**: `/api/runtime/agents/[agentId]/history`

**查询参数**:
- `limit`: 限制返回条数
- `beforeOutboxId`: 排他性游标（分页）

**响应**:
- `entries`: 历史条目数组
- `hasMore`: 是否有更多数据
- `nextBeforeOutboxId`: 下一页游标

**客户端集成**: `useRuntimeSyncController` 将获取的队列行注入与 SSE 相同的事件管道，通过 outbox id/time key 去重。

## 关键特性

### 1. 零配置部署

```bash
npx -y openclaw-studio@latest
cd openclaw-studio
npm run dev
```

一行命令启动，自动检测本地 OpenClaw Gateway 或手动配置远程 Gateway。

### 2. 多场景部署支持

#### A. Gateway 本地 + Studio 本地（同一台机器）

```bash
# Studio 配置
Upstream URL: ws://localhost:18789
Upstream Token: <gateway token>
```

#### B. Gateway 云端 + Studio 本地（笔记本）

**推荐方式（Tailscale Serve）**:

```bash
# Gateway 主机上
tailscale serve --yes --bg --https 443 http://127.0.0.1:18789

# Studio 配置
Upstream URL: wss://<gateway-host>.ts.net
Upstream Token: <gateway token>
```

**备选方式（SSH 隧道）**:

```bash
# 笔记本上
ssh -L 18789:127.0.0.1:18789 user@<gateway-host>

# Studio 配置
Upstream URL: ws://localhost:18789
```

#### C. Studio 云端 + Gateway 云端

```bash
# VPS 上运行 Studio
npm run dev

# 如果 OpenClaw 在同一 VPS
Upstream URL: ws://localhost:18789

# 通过 Tailscale 暴露 Studio
tailscale serve --yes --bg --https 443 http://127.0.0.1:3000

# 浏览器访问
https://<studio-host>.ts.net
```

### 3. 权限与沙箱管理

Studio 提供图形化界面配置 Agent 权限，配置流向 Gateway 并在运行时强制执行：

#### 工具策略（Tool Policy）

- **Commands**: `Off` / `Ask` / `Auto`
- **Web Access**: `On` / `Off`
- **File Tools**: `On` / `Off`

映射到 OpenClaw 工具组：
- `group:runtime` → 运行时执行工具（`exec`, `process`）
- `group:web` → 浏览器自动化工具
- `group:file` → 文件读写工具

#### 沙箱模式（Sandbox Mode）

- **off**: 不使用沙箱
- **all**: 所有会话都沙箱化
- **non-main**: 除主会话外都沙箱化

#### 工作空间访问（Workspace Access）

- **none**: 沙箱无法访问 Agent 工作空间
- **ro**: 只读挂载
- **rw**: 读写挂载

#### Exec 审批策略

- **Security**: `strict` / `moderate` / `permissive`
- **Ask**: 需要审批的命令模式列表
- **Allowlist**: 白名单命令（自动通过）

### 4. 实时事件流

**SSE 端点**: `/api/runtime/stream`

**事件类型**:
- `agent.created`, `agent.deleted`, `agent.renamed`
- `session.started`, `session.ended`
- `chat.message`, `chat.thinking`, `chat.tool_call`
- `exec.approval_requested`, `exec.approval_resolved`
- `cron.job_added`, `cron.job_executed`

**重放机制**:
- 客户端发送 `Last-Event-ID` 请求重放
- 服务端从 SQLite 队列查询并重放缺失事件
- 确保页面刷新后状态一致

### 5. Cron 任务管理

可视化创建和管理定时任务：

- **任务类型**: 定时消息、定时命令
- **Cron 表达式**: 标准 cron 语法
- **目标 Agent**: 选择执行任务的 Agent
- **任务历史**: 查看执行记录和结果

### 6. 技能管理

- **技能安装**: 从 skills.sh 安装社区技能
- **技能更新**: 更新已安装技能
- **技能移除**: 卸载不需要的技能
- **Agent 技能白名单**: 控制每个 Agent 可用的技能

### 7. 审批工作流

图形化处理 exec 命令审批：

- **实时通知**: 审批请求通过 SSE 推送到浏览器
- **三种操作**: 允许一次 / 总是允许 / 拒绝
- **审批历史**: 查看所有审批记录
- **策略更新**: 审批后自动更新 Agent 审批策略

### 8. 移动端支持

- 响应式设计，适配移动浏览器
- 支持触摸操作
- 移动端优化的 UI 布局

### 9. 安全特性

- **令牌服务端托管**: Gateway 令牌存储在服务端，浏览器无法访问
- **访问令牌保护**: 非 loopback 绑定时强制 `STUDIO_ACCESS_TOKEN`
- **API 脱敏**: 敏感信息在 API 响应中自动脱敏
- **CORS 保护**: 严格的跨域策略

### 10. 开发者友好

- **TypeScript 全栈**: 类型安全
- **热重载**: 开发模式下自动重载
- **错误处理**: 详细的错误码和诊断信息
- **日志系统**: 结构化日志，便于调试
- **测试覆盖**: Playwright E2E 测试
# ClawButler API 架构
apps/api/
├── routers/
│   ├── runtime/          # 运行时查询路由（类似 Studio 的 /api/runtime/*）
│   │   ├── summary.py
│   │   ├── fleet.py
│   │   ├── stream.py     # SSE 事件流
│   │   └── history.py
│   └── intents/          # 意图操作路由（类似 Studio 的 /api/intents/*）
│       ├── agent_create.py
│       ├── task_assign.py
│       └── approval_resolve.py
├── services/
│   ├── controlplane/     # 控制平面服务
│   │   ├── openclaw_adapter.py
│   │   ├── dify_adapter.py
│   │   ├── langgraph_adapter.py
│   │   └── runtime.py    # 统一运行时抽象
│   └── projection/       # 事件投影存储
│       └── store.py      # PostgreSQL 或 SQLite
```

### 2. 实时事件流与重放机制

**借鉴点**: SSE + SQLite 队列的重放机制解决了分布式 Agent 系统的状态同步难题。

**应用场景**:
- ClawButler 需要聚合来自多个平台的 Agent 事件
- 用户刷新页面或重连时需要恢复完整状态
- 审计日志需要完整的事件历史

**技术实现**:
```python
# ClawButler 事件流架构
class EventProjectionStore:
    """事件投影存储（PostgreSQL）"""

    async def append_event(self, event: AgentEvent) -> int:
        """追加事件到队列，返回 outbox_id"""

    async def replay_from(self, last_event_id: int, limit: int) -> List[AgentEvent]:
        """从指定 ID 重放事件"""

    async def get_agent_history(
        self,
        agent_id: str,
        before_outbox_id: Optional[int] = None,
        limit: int = 50
    ) -> Tuple[List[AgentEvent], bool, Optional[int]]:
        """分页查询 Agent 历史"""

# SSE 端点
@router.get("/v1/runtime/stream")
async def stream_events(
    request: Request,
    last_event_id: Optional[str] = Header(None)
):
    """SSE 事件流，支持重放"""
    if last_event_id:
        # 重放缺失事件
        events = await projection_store.replay_from(int(last_event_id))
        for event in events:
            yield f"id: {event.outbox_id}\ndata: {event.json()}\n\n"

    # 订阅实时事件
    async for event in runtime.subscribe():
        yield f"id: {event.outbox_id}\ndata: {event.json()}\n\n"
```

### 3. 权限与审批工作流

**借鉴点**: Studio 的权限管理和审批流程提供了细粒度的 Agent 控制能力。

**应用场景**:
- ClawButler 需要统一管理跨平台 Agent 的权限
- 敏感操作（如 exec 命令、API 调用）需要人工审批
- 不同组织/团队需要不同的权限策略

**技术实现**:
```python
# ClawButler 权限模型
class AgentPermissions(BaseModel):
    """Agent 权限配置"""
    agent_id: str
    tool_policy: ToolPolicy  # allow/deny 工具列表
    sandbox_mode: SandboxMode  # off/all/non-main
    workspace_access: WorkspaceAccess  # none/ro/rw
    exec_approval_policy: ExecApprovalPolicy

class ExecApprovalPolicy(BaseModel):
    """Exec 审批策略"""
    security: Literal["strict", "moderate", "permissive"]
    ask: List[str]  # 需要审批的命令模式
    allowlist: List[str]  # 白名单命令

# 审批工作流
class ApprovalWorkflow:
    async def request_approval(
        self,
        agent_id: str,
        command: str,
        context: Dict
    ) -> ApprovalRequest:
        """创建审批请求"""

    async def resolve_approval(
        self,
        request_id: str,
        action: Literal["allow_once", "allow_always", "deny"]
    ) -> None:
        """解决审批请求"""

    async def update_policy(
        self,
        agent_id: str,
        command_pattern: str,
        action: str
    ) -> None:
        """更新审批策略"""
```

### 4. 多场景部署模式

**借鉴点**: Studio 支持本地/云端/混合部署，适配不同用户场景。

**应用场景**:
- ClawButler 需要支持本地开发、私有云部署、公有云 SaaS 等多种场景
- 用户可能在笔记本上开发，在云端运行生产环境
- 需要支持 Tailscale、SSH 隧道等多种网络接入方式

**技术实现**:
```yaml
# ClawButler 部署配置
# 场景 A: 全本地部署
CLAWBUTLER_API_URL: http://localhost:8000
CLAWBUTLER_WEB_URL: http://localhost:3000

# 场景 B: API 云端 + Web 本地
CLAWBUTLER_API_URL: https://api.clawbutler.cc
CLAWBUTLER_WEB_URL: http://localhost:3000

# 场景 C: 全云端部署 + Tailscale
CLAWBUTLER_API_URL: https://api-host.ts.net
CLAWBUTLER_WEB_URL: https://web-host.ts.net
```

### 5. Intent-based API 设计

**借鉴点**: Studio 的 Intent Routes 提供了语义化的 API 设计，清晰表达操作意图。

**应用场景**:
- ClawButler 的 API 应该表达业务意图，而非底层技术细节
- 便于前端开发者理解和使用
- 便于生成 API 文档和 SDK

**技术实现**:
```python
# ClawButler Intent-based API
# ❌ 不好的设计（暴露实现细节）
POST /v1/agents/{agent_id}/config
POST /v1/agents/{agent_id}/permissions
POST /v1/agents/{agent_id}/sandbox

# ✅ 好的设计（表达意图）
POST /v1/intents/agent-create
POST /v1/intents/agent-permissions-update
POST /v1/intents/task-assign
POST /v1/intents/approval-resolve
```

### 6. 错误处理与诊断

**借鉴点**: Studio 提供了详细的错误码和诊断信息，便于排查问题。

**应用场景**:
- ClawButler 需要统一的错误处理机制
- 跨平台错误需要标准化映射
- 用户需要清晰的错误提示和解决方案

**技术实现**:
```python
# ClawButler 错误码体系
class ErrorCode(str, Enum):
    # Gateway 相关
    GATEWAY_UNAVAILABLE = "gateway.unavailable"
    GATEWAY_TIMEOUT = "gateway.timeout"
    GATEWAY_AUTH_FAILED = "gateway.auth_failed"

    # Agent 相关
    AGENT_NOT_FOUND = "agent.not_found"
    AGENT_CREATE_FAILED = "agent.create_failed"
    AGENT_PERMISSION_DENIED = "agent.permission_denied"

    # 平台相关
    PLATFORM_UNSUPPORTED = "platform.unsupported"
    PLATFORM_API_ERROR = "platform.api_error"

class ClawButlerError(Exception):
    def __init__(
        self,
        code: ErrorCode,
        message: str,
        details: Optional[Dict] = None
    ):
        self.code = code
        self.message = message
        self.details = details or {}
```

### 7. 配置管理与热重载

**借鉴点**: Studio 的配置变更触发确定性重连机制，确保配置更新生效。

**应用场景**:
- ClawButler 需要支持运行时配置更新
- 配置变更不应导致服务中断
- 需要通知所有连接的客户端配置已更新

**技术实现**:
```python
# ClawButler 配置热重载
class ConfigManager:
    async def update_config(self, config: Config) -> None:
        """更新配置并触发重连"""
        await self.save_config(config)
        await self.runtime.reconnect_for_config_change()
        await self.broadcast_config_updated()

class Runtime:
    async def reconnect_for_config_change(self) -> None:
        """配置变更后重连所有适配器"""
        for adapter in self.adapters.values():
            await adapter.reconnect()
```

### 8. 移动端优先设计

**借鉴点**: Studio 的响应式设计和移动端优化。

**应用场景**:
- ClawButler Web 需要支持移动端访问
- 管理员可能在移动设备上处理审批
- 移动端查看 Agent 状态和日志

**技术实现**:
- 使用 Tailwind CSS 响应式设计
- 移动端优化的 UI 组件
- 触摸友好的交互设计
- PWA 支持（离线访问、推送通知）

### 9. 开发者体验

**借鉴点**: Studio 的开发者友好特性。

**应用场景**:
- ClawButler 需要良好的开发者体验
- 便于社区贡献和扩展
- 降低学习曲线

**技术实现**:
- TypeScript 类型安全（前端）
- Pydantic 类型验证（后端）
- 详细的 API 文档（OpenAPI）
- 完善的测试覆盖
- 清晰的错误提示
- 结构化日志

### 10. 安全最佳实践

**借鉴点**: Studio 的安全设计。

**应用场景**:
- ClawButler 需要保护敏感信息（API 密钥、凭证）
- 防止未授权访问
- 审计日志

**技术实现**:
```python
# ClawButler 安全实践
# 1. 令牌服务端托管
class CredentialStore:
    """凭证存储（加密）"""
    async def store_credential(self, key: str, value: str) -> None:
        encrypted = encrypt(value)
        await db.execute("INSERT INTO credentials ...")

    async def get_credential(self, key: str) -> str:
        encrypted = await db.fetchval("SELECT value FROM credentials ...")
        return decrypt(encrypted)

# 2. API 响应脱敏
class AgentResponse(BaseModel):
    agent_id: str
    name: str
    api_key: Optional[str] = Field(None, exclude=True)  # 自动排除

# 3. 访问令牌保护
@router.get("/v1/runtime/stream")
async def stream_events(
    request: Request,
    token: str = Depends(verify_access_token)
):
    """需要访问令牌"""

# 4. 审计日志
class AuditLog:
    async def log_action(
        self,
        user_id: str,
        action: str,
        resource: str,
        details: Dict
    ) -> None:
        """记录审计日志"""
```

## 总结

OpenClaw Studio 为 ClawButler 提供了以下核心借鉴价值：

1. **架构模式**：服务端控制平面 + SSE 事件流 + SQLite 持久化
2. **API 设计**：Intent-based 语义化 API，清晰表达业务意图
3. **权限管理**：细粒度工具策略 + 沙箱模式 + 审批工作流
4. **实时同步**：SSE + 重放机制，确保状态一致性
5. **多场景部署**：本地/云端/混合部署，适配不同用户需求
6. **安全实践**：令牌服务端托管 + API 脱敏 + 审计日志
7. **开发者体验**：TypeScript 类型安全 + 详细错误码 + 完善测试

这些设计理念和技术实现可以直接应用到 ClawButler 的架构设计中，帮助构建一个统一、安全、易用的 Agent 控制平面。

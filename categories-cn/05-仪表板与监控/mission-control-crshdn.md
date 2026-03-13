> https://github.com/crshdn/mission-control

# crshdn/mission-control (Autensa)

## 基本信息

- **GitHub Stars**: 1,319
- **项目地址**: https://github.com/crshdn/mission-control
- **在线演示**: https://missioncontrol.ghray.com
- **最新版本**: v1.5.0
- **开源协议**: MIT
- **技术栈**: Next.js 14, TypeScript 5, SQLite 3, OpenClaw Gateway

## 问题与解决方案

### 核心问题
传统 AI Agent 系统缺乏统一的任务编排和可视化管理界面，用户难以：
1. 直观地创建和跟踪 AI 任务执行进度
2. 与 AI 进行交互式的任务规划对话
3. 实时监控多个 Agent 的工作状态
4. 管理任务的完整生命周期（从规划到交付）

### 解决方案
Mission Control（现更名为 Autensa）提供了一个完整的 AI Agent 编排仪表板：

**任务管理层**
- Kanban 看板界面，支持拖拽操作，7 个状态列（PLANNING → INBOX → ASSIGNED → IN PROGRESS → TESTING → REVIEW → DONE）
- 任务图片附件支持（v1.5.0 新增），AI Agent 可以看到参考图片（UI 原型、截图等）
- 交互式 AI 规划流程：AI 主动提问澄清需求，而非直接执行

**Agent 编排层**
- 自动创建专业化 Agent 并分配任务
- 实时进度追踪和状态同步
- Gateway Agent Discovery：一键从 OpenClaw Gateway 导入现有 Agent，无需重复创建
- 支持 Sub-Agent 注册和活动日志记录

**实时监控层**
- Live Feed 实时事件流，展示 Agent 活动、任务更新和系统事件
- WebSocket 连接到 OpenClaw Gateway 进行 AI Agent 编排
- 完整的交付物追踪系统

## 核心架构

### 系统架构图

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

### 技术架构

**前端层 (Next.js 14 App Router)**
```
src/
├── app/
│   ├── api/                    # API Routes
│   │   ├── tasks/              # 任务 CRUD + 规划 + 调度
│   │   ├── agents/             # Agent 管理
│   │   ├── openclaw/           # Gateway 代理端点
│   │   └── webhooks/           # Agent 完成回调
│   ├── settings/               # 设置页面
│   └── workspace/[slug]/       # 工作区仪表板
├── components/
│   ├── MissionQueue.tsx        # Kanban 看板
│   ├── PlanningTab.tsx         # AI 规划界面
│   ├── AgentsSidebar.tsx       # Agent 面板
│   ├── LiveFeed.tsx            # 实时事件流
│   └── TaskModal.tsx           # 任务创建/编辑
└── lib/
    ├── db/                     # SQLite + 迁移
    ├── openclaw/               # Gateway 客户端 + 设备身份
    ├── validation.ts           # Zod 模式验证
    └── types.ts                # TypeScript 类型
```

**数据层**
- SQLite 数据库（`mission-control.db`）
- 工作区文件系统（`~/Documents/Shared/projects`）
- 内存级状态管理（无持久化）

**集成层**
- OpenClaw Gateway WebSocket 连接
- Bearer Token 认证
- HMAC Webhook 签名验证

### 任务生命周期

```
 CREATE          PLAN            ASSIGN          EXECUTE         DELIVER
┌────────┐    ┌────────┐    ┌────────────┐    ┌──────────┐    ┌────────┐
│  New   │───►│  AI    │───►│   Agent    │───►│  Agent   │───►│  Done  │
│  Task  │    │  Q&A   │    │  Created   │    │  Works   │    │  ✓     │
└────────┘    └────────┘    └────────────┘    └──────────┘    └────────┘
```

**状态流转**:
```
PLANNING → INBOX → ASSIGNED → IN PROGRESS → TESTING → REVIEW → DONE
```

- **PLANNING**: AI 交互式提问阶段
- **INBOX**: 等待处理的新任务
- **ASSIGNED**: 已分配给 Agent，准备开始
- **IN PROGRESS**: Agent 正在执行
- **TESTING**: 自动化质量门（浏览器测试、CSS 验证、资源检查）
- **REVIEW**: 通过自动化测试，等待人工审批
- **DONE**: 任务完成并批准

### API 编排协议

**1. 注册 Sub-Agent**
```bash
POST /api/tasks/{TASK_ID}/subagent
{
  "openclaw_session_id": "unique-session-id",
  "agent_name": "Designer"
}
```

**2. 记录活动日志**
```bash
POST /api/tasks/{TASK_ID}/activities
{
  "activity_type": "updated",  # spawned/updated/completed/file_created/status_changed
  "message": "Started working on design mockups",
  "agent_id": "optional-agent-uuid"
}
```

**3. 注册交付物**
```bash
POST /api/tasks/{TASK_ID}/deliverables
{
  "deliverable_type": "file",
  "title": "Homepage Design",
  "path": "$PROJECTS_PATH/homepage/index.html",
  "description": "Main homepage with responsive layout"
}
```

## 关键特性

### 1. 交互式 AI 规划
- AI 主动提问澄清需求，而非盲目执行
- 多轮对话式规划流程
- 基于用户回答自动创建专业化 Agent

### 2. 任务图片附件（v1.5.0）
- 上传参考图片到任务
- AI Agent 在调度时可见图片
- 适用于 UI 原型、截图、视觉规范

### 3. Gateway Agent Discovery
- 一键从 OpenClaw Gateway 导入现有 Agent
- 无需在 Mission Control 中重复创建
- 自动同步 Agent 配置和状态

### 4. 实时事件流
- WebSocket 实时推送
- 展示 Agent 活动、任务更新、系统事件
- 支持 SSE（Server-Sent Events）流式传输

### 5. 多机部署支持
- Dashboard 和 AI Agent 可运行在不同机器
- 支持 Tailscale 远程连接
- 配置示例：
```env
OPENCLAW_GATEWAY_URL=wss://your-machine.tailnet-name.ts.net
OPENCLAW_GATEWAY_TOKEN=your-shared-token
```

### 6. 安全特性
- Bearer Token 认证（`MC_API_TOKEN`）
- HMAC Webhook 签名验证（`WEBHOOK_SECRET`）
- Zod 模式验证
- 路径遍历保护
- 安全响应头

### 7. 隐私优先设计
- 开源自托管
- 无内置分析追踪器
- 无集中式用户数据收集
- 数据保留在本地部署

### 8. Docker 生产就绪
- 优化的 Dockerfile
- docker-compose 编排
- 命名卷持久化（`mission-control-data`, `mission-control-workspace`）
- 支持 `host.docker.internal` 连接本地 OpenClaw

### 9. 自动化测试门
- TESTING 状态自动运行质量检查
- 浏览器测试
- CSS 验证
- 资源完整性检查
# apps/api/routers/runbook_execution.py
@router.get("/runbooks/{runbook_id}/executions/{execution_id}/timeline")
async def get_execution_timeline(execution_id: str):
    """类似 Mission Control 的 Live Feed，返回执行时间线"""
    return {
        "events": [
            {"type": "agent_spawned", "timestamp": "...", "agent": "..."},
            {"type": "step_completed", "timestamp": "...", "step": "..."},
            {"type": "deliverable_created", "timestamp": "...", "path": "..."}
        ]
    }
```

### 2. 交互式规划流程
**借鉴点**: AI 主动提问澄清需求的规划模式

**应用场景**:
- Verified Templates 部署前的参数收集
- Runbook 创建向导
- Agent 配置优化建议

**实现建议**:
```python
# apps/api/services/template_planning.py
class TemplatePlanningService:
    async def start_planning(self, template_id: str) -> PlanningSession:
        """启动交互式规划会话"""
        questions = await self._generate_clarifying_questions(template_id)
        return PlanningSession(questions=questions)

    async def process_answer(self, session_id: str, answer: dict) -> NextStep:
        """处理用户回答，返回下一步（继续提问或开始部署）"""
        pass
```

### 3. Sub-Agent 注册和追踪
**借鉴点**: 分层 Agent 管理和活动日志记录

**应用场景**:
- ClawButler Federation 中的 Peer Agent 追踪
- A2A 调用链路可视化
- 多 Agent 协作审计

**实现建议**:
```python
# apps/api/models/agent_activity.py
class AgentActivity(Base):
    __tablename__ = "agent_activities"

    id = Column(UUID, primary_key=True)
    parent_agent_id = Column(UUID, ForeignKey("agents.id"))  # 父 Agent
    sub_agent_id = Column(UUID, ForeignKey("agents.id"))     # 子 Agent
    activity_type = Column(Enum("spawned", "updated", "completed", "a2a_call"))
    message = Column(Text)
    timestamp = Column(DateTime)

    # 类似 Mission Control 的活动日志
```

### 4. Gateway Discovery 模式
**借鉴点**: 一键导入现有 Agent 的发现机制

**应用场景**:
- ClawButler 从 OpenClaw Gateway 导入 Agent
- 从 Dify 平台同步 Agent 配置
- LangGraph Agent 自动注册

**实现建议**:
```python
# apps/api/services/agent_discovery.py
class AgentDiscoveryService:
    async def discover_from_openclaw(self, gateway_url: str) -> List[AgentConfig]:
        """从 OpenClaw Gateway 发现 Agent"""
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{gateway_url}/api/agents")
            return [self._convert_to_clawbutler_config(a) for a in resp.json()]

    async def import_agent(self, agent_config: AgentConfig, workspace_id: str):
        """导入 Agent 到 ClawButler"""
        pass
```

### 5. 交付物追踪系统
**借鉴点**: 文件级交付物注册和验证

**应用场景**:
- Runbook 执行结果追踪
- Config Safety 快照文件管理
- Template 部署产物记录

**实现建议**:
```python
# apps/api/models/deliverable.py
class Deliverable(Base):
    __tablename__ = "deliverables"

    id = Column(UUID, primary_key=True)
    runbook_execution_id = Column(UUID, ForeignKey("runbook_executions.id"))
    deliverable_type = Column(Enum("file", "config", "snapshot"))
    title = Column(String)
    path = Column(String)  # 相对于 workspace 的路径
    description = Column(Text)
    file_exists = Column(Boolean)  # Mission Control 的验证机制
    created_at = Column(DateTime)
```

### 6. 多机部署架构
**借鉴点**: Dashboard 和 Agent Runtime 分离部署

**应用场景**:
- ClawButler Control Plane（Web + API）与 Edge Agent 分离
- Federation 跨机器 Peer 连接
- 混合云部署（Control Plane 在云端，Agent 在本地）

**实现建议**:
```yaml
# docker-compose.federation.yml
services:
  clawbutler-control-plane:
    image: clawbutler/control-plane
    environment:
      - EDGE_AGENT_DISCOVERY_URL=wss://edge.tailnet.ts.net

  clawbutler-edge-agent:
    image: clawbutler/edge-agent
    environment:
      - CONTROL_PLANE_URL=wss://control.clawbutler.cc
      - FEDERATION_TOKEN=${FEDERATION_TOKEN}
```

### 7. 安全和隐私设计
**借鉴点**:
- Bearer Token + HMAC Webhook 双重认证
- 隐私优先（无追踪器、本地数据）
- 路径遍历保护

**应用场景**:
- ClawButler API 认证中间件增强
- Webhook 回调签名验证（已有 `idempotency.py`，可扩展 HMAC）
- 工作区文件访问控制

**实现建议**:
```python
# apps/api/middleware/webhook_auth.py
import hmac
import hashlib

def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool:
    """类似 Mission Control 的 HMAC 验证"""
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)

# apps/api/middleware/path_security.py
def validate_workspace_path(path: str, workspace_base: str) -> bool:
    """防止路径遍历攻击"""
    resolved = Path(path).resolve()
    base = Path(workspace_base).resolve()
    return resolved.is_relative_to(base)
```

### 8. 实时通信层
**借鉴点**: WebSocket + SSE 双协议支持

**应用场景**:
- ClawButler Web 实时事件推送
- Runbook 执行进度流式更新
- Agent 状态变更通知

**实现建议**:
```python
# apps/api/routers/sse.py
from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

router = APIRouter()

@router.get("/events/stream")
async def event_stream(workspace_id: str):
    """类似 Mission Control 的 Live Feed SSE"""
    async def event_generator():
        async for event in event_bus.subscribe(workspace_id):
            yield {
                "event": event.type,
                "data": event.to_json()
            }
    return EventSourceResponse(event_generator())
```

### 9. 自动化质量门
**借鉴点**: TESTING 状态的自动化检查

**应用场景**:
- Config Safety 部署前验证
- Template 兼容性检查
- Runbook 执行后置检查

**实现建议**:
```python
# apps/api/services/quality_gate.py
class QualityGateService:
    async def run_deployment_checks(self, deployment_id: str) -> QualityReport:
        """类似 Mission Control 的 TESTING 阶段"""
        checks = [
            self._check_config_syntax(),
            self._check_dependency_compatibility(),
            self._check_resource_availability(),
            self._check_security_vulnerabilities()
        ]
        results = await asyncio.gather(*checks)
        return QualityReport(
            passed=all(r.success for r in results),
            checks=results
        )
```

### 10. 贡献者协作模式
**借鉴点**: Mission Control 的贡献者展示和归属

**应用场景**:
- ClawButler 社区贡献追踪
- Template 作者归属
- Agent 配置来源标记

**实现建议**:
```python
# apps/api/models/contribution.py
class Contribution(Base):
    __tablename__ = "contributions"

    id = Column(UUID, primary_key=True)
    contributor_id = Column(UUID, ForeignKey("users.id"))
    resource_type = Column(Enum("template", "agent_config", "runbook"))
    resource_id = Column(UUID)
    contribution_type = Column(Enum("created", "improved", "reviewed"))
    description = Column(String)  # e.g., "Device Identity", "Port Configuration"
    created_at = Column(DateTime)
```

## 总结

Mission Control 提供了一个完整的 AI Agent 编排参考实现，其核心价值在于：

1. **可视化编排**: Kanban + 实时事件流的直观 UI
2. **交互式规划**: AI 主动提问的需求澄清流程
3. **分层管理**: Task → Agent → Sub-Agent → Deliverable 的清晰层次
4. **生产就绪**: 安全、隐私、多机部署、Docker 化
5. **开放集成**: 基于 OpenClaw Gateway 的标准化接口

对 ClawButler 而言，可以借鉴其编排 UI 范式、交互式规划流程、Sub-Agent 追踪机制，并结合 ClawButler 的 Federation 和 Config Safety 特性，构建更强大的跨平台 Agent 控制平面。

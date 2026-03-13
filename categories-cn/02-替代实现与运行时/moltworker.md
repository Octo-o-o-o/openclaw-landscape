> https://github.com/cloudflare/moltworker

# cloudflare/moltworker

## 基本信息

- **GitHub**: https://github.com/cloudflare/moltworker
- **Stars**: 9,558
- **语言**: TypeScript
- **创建时间**: 2026-01-27
- **最后更新**: 2026-03-11
- **描述**: 在 Cloudflare Workers 上运行 OpenClaw（原 Moltbot/Clawdbot）个人 AI 助手

## 问题与解决方案

### 核心问题

1. **自托管门槛高**：传统 AI 助手需要用户自行维护服务器、处理运维问题（进程管理、日志、备份、安全更新）
2. **成本不可控**：24/7 运行的 VPS 或云主机成本高昂，且资源利用率低
3. **冷启动慢**：容器化部署的冷启动时间长（1-2 分钟），影响用户体验
4. **数据持久化难**：无状态容器环境下，如何保存对话历史、配置、已配对设备等状态

### 解决方案

**Serverless 容器化部署**：将 OpenClaw 打包为 Docker 镜像，运行在 Cloudflare Sandbox 容器中，利用 Cloudflare Workers 的全球边缘网络实现：

1. **零运维部署**：一键部署到 Cloudflare Workers，无需管理服务器
2. **按需计费**：容器可配置空闲后休眠（`SANDBOX_SLEEP_AFTER`），降低成本至 ~$5-6/月（仅运行 4 小时/天）
3. **全球加速**：利用 Cloudflare 的 CDN 网络，全球低延迟访问
4. **R2 持久化**：通过 R2 对象存储实现配置、对话历史的跨容器重启持久化（每 5 分钟自动备份）
5. **多层认证**：Cloudflare Access（管理员认证）+ Gateway Token（Control UI 访问）+ Device Pairing（设备配对）三层安全防护

## 核心架构

### 技术栈

```
┌─────────────────────────────────────────────────────────────┐
│                    Cloudflare Workers                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Hono Web Framework                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐     │   │
│  │  │ Admin UI   │  │  API       │  │  Debug     │     │   │
│  │  │ (/_admin/) │  │  (/api/*)  │  │  (/debug/*) │     │   │
│  │  └────────────┘  └────────────┘  └────────────┘     │   │
│  │                                                      │   │
│  │  ┌────────────────────────────────────────────────┐ │   │
│  │  │     Cloudflare Access JWT Middleware          │ │   │
│  │  └────────────────────────────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Cloudflare Sandbox Container                 │   │
│  │  ┌────────────────────────────────────────────────┐  │   │
│  │  │  OpenClaw Gateway (Node.js 22 + pnpm)         │  │   │
│  │  │  - WebSocket Server (ws://localhost:18789)    │  │   │
│  │  │  - HTTP API                                    │  │   │
│  │  │  - Device Pairing                              │  │   │
│  │  │  - Multi-channel Support                       │  │   │
│  │  └────────────────────────────────────────────────┘  │   │
│  │                                                        │   │
│  │  ┌────────────────────────────────────────────────┐  │   │
│  │  │  Skills (Browser Automation, Custom Tools)     │  │   │
│  │  └────────────────────────────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              R2 Object Storage                       │   │
│  │  - Config Backup (every 5 min)                      │   │
│  │  - Conversation History                             │   │
│  │  - Paired Devices                                   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         Browser Rendering (CDP Shim)                 │   │
│  │  - Headless Chrome for Web Automation               │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  Anthropic / OpenAI    │
              │  (via AI Gateway)      │
              └────────────────────────┘
```

### 关键组件

1. **Worker 层（TypeScript + Hono）**
   - `src/index.ts`：主应用入口，路由挂载
   - `src/auth/`：Cloudflare Access JWT 认证（JWKS 验证、中间件）
   - `src/gateway/`：OpenClaw 进程管理（启动、环境变量、R2 挂载、备份同步）
   - `src/routes/`：API 路由（设备管理、网关控制、调试端点）
   - `src/client/`：React 管理界面（设备配对、R2 状态、网关重启）

2. **容器层（Docker + OpenClaw）**
   - 基础镜像：`cloudflare/sandbox:0.7.0`
   - Node.js 22 + pnpm + OpenClaw 2026.2.3
   - 启动脚本：`start-openclaw.sh`（R2 恢复 → 启动网关 → 定时备份）
   - 预装技能：`skills/cloudflare-browser`（CDP 客户端、截图、视频录制）

3. **持久化层（R2 + rclone）**
   - 启动时从 R2 恢复配置到 `/root/.openclaw`
   - 运行时每 5 分钟自动同步到 R2
   - 管理界面提供"立即备份"按钮

4. **认证层（三层防护）**
   - **Cloudflare Access**：保护 `/_admin/`、`/api/*`、`/debug/*` 路由，基于 JWT 验证
   - **Gateway Token**：访问 Control UI 需提供 `?token=` 查询参数
   - **Device Pairing**：新设备必须通过管理界面显式批准才能使用

### 部署流程

```bash
# 1. 安装依赖
npm install

# 2. 配置 AI 提供商（二选一）
npx wrangler secret put ANTHROPIC_API_KEY
# 或使用 Cloudflare AI Gateway
npx wrangler secret put CLOUDFLARE_AI_GATEWAY_API_KEY
npx wrangler secret put CF_AI_GATEWAY_ACCOUNT_ID
npx wrangler secret put CF_AI_GATEWAY_GATEWAY_ID

# 3. 生成并设置 Gateway Token
export MOLTBOT_GATEWAY_TOKEN=$(openssl rand -hex 32)
echo "$MOLTBOT_GATEWAY_TOKEN" | npx wrangler secret put MOLTBOT_GATEWAY_TOKEN

# 4. 部署
npm run deploy

# 5. 配置 Cloudflare Access（保护管理界面）
# 在 Workers & Pages 仪表板中启用 Cloudflare Access
npx wrangler secret put CF_ACCESS_TEAM_DOMAIN
npx wrangler secret put CF_ACCESS_AUD

# 6. 配置 R2 持久化（可选但推荐）
npx wrangler secret put R2_ACCESS_KEY_ID
npx wrangler secret put R2_SECRET_ACCESS_KEY
npx wrangler secret put CF_ACCOUNT_ID
```

## 关键特性

### 1. Serverless 容器编排

- **Durable Objects**：每个 Worker 绑定一个 Sandbox Durable Object，确保单实例运行
- **容器生命周期管理**：
  - 默认 `SANDBOX_SLEEP_AFTER=never`（永不休眠，推荐用于生产）
  - 可配置空闲超时（如 `10m`、`1h`）以降低成本
  - 冷启动时间 1-2 分钟，后续请求快速响应
- **进程监控**：通过 `sandbox.startProcess()` 启动 OpenClaw，自动重启失败进程

### 2. R2 持久化方案

**备份/恢复模式**（简化设计，无需修改 OpenClaw 代码）：

```bash
# 启动时恢复
if [ -d /mnt/r2/.openclaw ]; then
  cp -r /mnt/r2/.openclaw /root/
fi

# 运行时定时备份（每 5 分钟）
while true; do
  sleep 300
  rclone sync /root/.openclaw r2:moltbot-data/.openclaw
done
```

**优势**：
- 对话历史、配对设备、配置文件跨容器重启持久化
- 管理界面显示最后备份时间，支持手动触发备份
- 无 R2 凭证时仍可运行（使用临时存储）

### 3. 多层认证体系

| 层级 | 保护范围 | 认证方式 | 用途 |
|------|---------|---------|------|
| Cloudflare Access | `/_admin/*`, `/api/*`, `/debug/*` | JWT（JWKS 验证） | 管理员身份验证 |
| Gateway Token | Control UI (`/?token=`) | 查询参数 | 防止未授权访问 |
| Device Pairing | 所有设备（浏览器、CLI、聊天平台） | 配对码 + 管理员批准 | 设备级访问控制 |

**本地开发模式**：设置 `DEV_MODE=true` 跳过 Cloudflare Access 认证并启用 `allowInsecureAuth`（绕过设备配对）

### 4. 浏览器自动化（CDP Shim）

利用 Cloudflare Browser Rendering 提供 Chrome DevTools Protocol 端点：

```typescript
// 端点
GET  /cdp/json/version          // 浏览器版本信息
GET  /cdp/json/list             // 可用目标列表
GET  /cdp/json/new              // 创建新目标
WS   /cdp/devtools/browser/{id} // CDP WebSocket 连接

// 认证：所有端点需 ?secret=<CDP_SECRET>
```

**预装技能**：
- `cloudflare-browser/scripts/screenshot.js`：网页截图
- `cloudflare-browser/scripts/video.js`：多页面录制视频
- `cloudflare-browser/scripts/cdp-client.js`：可复用 CDP 客户端库

### 5. AI Gateway 集成

**原生支持 Cloudflare AI Gateway**（缓存、限流、分析、成本追踪）：

```bash
# 配置 AI Gateway（优先级高于直接 API 密钥）
npx wrangler secret put CLOUDFLARE_AI_GATEWAY_API_KEY  # 上游提供商 API 密钥
npx wrangler secret put CF_AI_GATEWAY_ACCOUNT_ID
npx wrangler secret put CF_AI_GATEWAY_GATEWAY_ID

# 可选：覆盖默认模型（默认 Claude Sonnet 4.5）
npx wrangler secret put CF_AI_GATEWAY_MODEL
# 示例：workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast
```

**支持的提供商**：
- Workers AI（Unified Billing，无需单独 API 密钥）
- Anthropic、OpenAI、Groq 等（通过网关转发 API 密钥）

### 6. 管理界面功能

访问 `/_admin/`（需 Cloudflare Access 认证）：

- **R2 存储状态**：显示是否配置 R2、最后备份时间、"立即备份"按钮
- **网关控制**：重启 OpenClaw 网关进程
- **设备配对**：
  - 查看待批准设备列表
  - 单个批准或批量批准
  - 查看已配对设备

### 7. 调试端点

启用 `DEBUG_ROUTES=true` 后可访问（需 Cloudflare Access）：

```
GET /debug/processes              # 列出容器内所有进程
GET /debug/logs?id=<process_id>   # 获取特定进程日志
GET /debug/version                # 容器和 OpenClaw 版本信息
```

### 8. 成本优化

**标准配置成本估算**（`standard-1` 实例：1/2 vCPU, 4 GiB 内存, 8 GB 磁盘）：

| 资源 | 月度用量（24/7） | 免费额度 | 超额 | 约成本 |
|------|----------------|---------|------|--------|
| 内存 | 2,920 GiB-hrs | 25 GiB-hrs | 2,895 GiB-hrs | ~$26/月 |
| CPU（10% 利用率） | ~2,190 vCPU-min | 375 vCPU-min | ~1,815 vCPU-min | ~$2/月 |
| 磁盘 | 5,840 GB-hrs | 200 GB-hrs | 5,640 GB-hrs | ~$1.50/月 |
| Workers Paid 计划 | - | - | - | $5/月 |
| **总计** | - | - | - | **~$34.50/月** |

**优化策略**：
- 配置 `SANDBOX_SLEEP_AFTER=10m`，空闲后休眠
- 仅运行 4 小时/天可降至 ~$5-6/月（加上 $5 计划费）
- 选择更小实例（`lite`：256 MiB/$0.50/月）或更大实例（`standard-4`：12 GiB）
# apps/api/services/config_backup.py
async def backup_to_r2(snapshot_id: uuid.UUID):
    """每 5 分钟自动备份配置快照到 R2"""
    snapshot = await get_snapshot(snapshot_id)
    await r2_client.put_object(
        Bucket="clawbutler-backups",
        Key=f"snapshots/{snapshot_id}.json",
        Body=snapshot.to_json()
    )

async def restore_from_r2(snapshot_id: uuid.UUID):
    """从 R2 恢复配置快照"""
    obj = await r2_client.get_object(
        Bucket="clawbutler-backups",
        Key=f"snapshots/{snapshot_id}.json"
    )
    return ConfigSnapshot.from_json(obj["Body"].read())
```

### 5. AI Gateway 成本追踪

**借鉴点**：Cloudflare AI Gateway 的统一计费和分析功能与 ClawButler 的成本追踪需求高度契合

**集成方案**：
- 在 ClawButler 的 LLM 调用层添加 AI Gateway 代理选项
- 从 AI Gateway API 拉取成本数据，写入 `billing_usage` 表
- 支持多提供商成本聚合（Anthropic、OpenAI、Workers AI）

**数据流**：
```
ClawButler Agent → AI Gateway → Anthropic/OpenAI
                       ↓
                  Analytics API
                       ↓
            ClawButler Billing Service
                       ↓
              PostgreSQL (billing_usage)
```

**优势**：
- 统一的成本追踪接口（无需对接每个 LLM 提供商的计费 API）
- 缓存和限流功能降低 API 成本
- 实时成本告警（超过配额时触发 Webhook）

### 6. 调试端点设计

**借鉴点**：moltworker 的 `/debug/*` 端点设计可用于 ClawButler 的运维工具

**新增端点**：
```python
# apps/api/routers/debug.py
@router.get("/debug/agents")
async def list_agents():
    """列出所有 Agent 进程状态"""
    return {"agents": await agent_manager.list_all()}

@router.get("/debug/agents/{agent_id}/logs")
async def get_agent_logs(agent_id: str):
    """获取特定 Agent 的日志"""
    return await log_service.get_logs(agent_id, limit=1000)

@router.get("/debug/federation/peers")
async def list_federation_peers():
    """列出所有 Federation Peer 连接状态"""
    return await federation_service.get_peer_status()

@router.post("/debug/agents/{agent_id}/restart")
async def restart_agent(agent_id: str):
    """重启特定 Agent"""
    await agent_manager.restart(agent_id)
    return {"status": "restarted"}
```

**安全控制**：
- 通过 `DEBUG_MODE` 环境变量启用（生产环境默认禁用）
- 需要 Admin 角色权限（Auth.js session 验证）
- 审计日志记录所有调试操作

### 7. 一键部署脚本

**借鉴点**：moltworker 的 `npm run deploy` 简化部署流程，ClawButler 可优化现有 `deploy/deploy.sh`

**改进方向**：
- 添加交互式配置向导（类似 `npx wrangler secret put`）
- 自动检测缺失的环境变量并提示用户输入
- 支持多环境部署（dev/staging/production）
- 集成健康检查（部署后自动验证服务可用性）

**示例**：
```bash
# 当前方式（需手动编辑 .env）
cp deploy/.env.production .env
nano .env
bash deploy/deploy.sh

# 改进后（交互式配置）
bash deploy/deploy.sh --interactive
# 提示：Enter DATABASE_URL: postgresql://...
# 提示：Enter ANTHROPIC_API_KEY: sk-ant-...
# 自动生成 SECRET_KEY、验证配置、部署、运行健康检查
```

### 8. 成本优化策略

**借鉴点**：moltworker 的容器休眠机制可用于 ClawButler 的多 Agent 场景

**应用场景**：
- 企业部署了 50 个 Agent，但大部分时间只有 5-10 个活跃
- 闲置 Agent 自动休眠，收到请求时唤醒（类似 AWS Lambda）

**实施方案**：
```python
# apps/api/services/agent_scheduler.py
class AgentScheduler:
    async def check_idle_agents(self):
        """每 5 分钟检查闲置 Agent"""
        idle_agents = await self.get_idle_agents(idle_threshold=600)  # 10 分钟无活动
        for agent in idle_agents:
            await self.sleep_agent(agent.id)
            logger.info(f"Agent {agent.id} hibernated due to inactivity")

    async def wake_agent(self, agent_id: str):
        """收到请求时唤醒 Agent"""
        if await self.is_sleeping(agent_id):
            await self.start_agent_container(agent_id)
            logger.info(f"Agent {agent_id} woken up")
```

**成本节省**：
- 假设 50 个 Agent，平均活跃率 20%，可节省 80% 的计算资源成本
- 配合 Kubernetes HPA（Horizontal Pod Autoscaler）实现自动扩缩容

### 总结

moltworker 为 ClawButler 提供了以下关键启示：

1. **Serverless 优先**：提供 Cloudflare Workers 部署选项，降低中小团队运维负担
2. **多层认证**：强化 Federation 场景的安全防护（配对码 + 审批流程）
3. **容器编排**：实现 Agent 级别的资源隔离和生命周期管理
4. **对象存储**：利用 R2/S3 实现配置快照的跨实例持久化
5. **成本追踪**：集成 AI Gateway 统一计费接口
6. **运维工具**：添加调试端点和交互式部署脚本
7. **资源优化**：实现 Agent 休眠/唤醒机制，降低多 Agent 场景成本

这些改进将使 ClawButler 在保持企业级功能的同时，提供更灵活的部署选项和更低的运营成本。

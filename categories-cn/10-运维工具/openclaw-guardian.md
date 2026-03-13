> https://github.com/LeoYeAI/openclaw-guardian

# OpenClaw Guardian

## 基本信息

- **项目名称**: OpenClaw Guardian
- **GitHub**: https://github.com/LeoYeAI/openclaw-guardian
- **Stars**: 938
- **作者**: LeoYeAI (MyClaw.ai 团队)
- **许可证**: MIT
- **定位**: OpenClaw Gateway 的生产级守护进程（watchdog）

## 问题与解决方案

### 核心问题

OpenClaw Gateway 在生产环境中面临的稳定性挑战：

1. **Gateway 进程意外崩溃** — 由于内存泄漏、未捕获异常、依赖服务故障等原因，Gateway 进程可能在运行中突然停止
2. **配置错误导致启动失败** — 用户修改 workspace 中的技能、配置文件或依赖后，可能引入语法错误或逻辑错误，导致 Gateway 无法正常启动
3. **无人值守场景下的服务中断** — MyClaw.ai 平台运行数千个 AI Agent 实例，需要 24/7 自动恢复能力，人工干预成本过高
4. **缺乏历史回滚机制** — 当 workspace 被破坏时，缺少自动回退到上一个稳定状态的能力
5. **故障通知不及时** — 运维团队无法第一时间感知 Gateway 异常

### 解决方案

Guardian 提供三层自动恢复机制 + 通知系统：

**第一层：自动健康检查**
- 每 30 秒（可配置）检测 Gateway 进程是否存活（通过 `pgrep -f "openclaw-gateway"`）
- 轻量级、低开销的监控循环

**第二层：`openclaw doctor --fix` 自动修复**
- 检测到 Gateway 停止后，自动执行 OpenClaw 官方的诊断修复工具
- 最多尝试 3 次（可配置），每次间隔 10 秒
- 修复成功后立即恢复监控，无需人工介入

**第三层：Git 回滚 + 强制重启**
- 当 `doctor --fix` 连续失败后，触发 workspace 的 git 回滚
- 自动识别最近的稳定 commit（排除 `rollback`、`daily-backup`、`auto-backup`、`guardian-auto` 等自动提交）
- 执行 `git reset --hard <stable-commit>` 回退到稳定版本
- 强制杀死旧进程并重启 Gateway
- 创建回滚记录 commit，便于事后审计

**第四层：冷却期 + 持续监控**
- 如果回滚后仍然失败，进入 300 秒（可配置）冷却期，避免无限循环
- 冷却期结束后自动恢复监控

**附加功能：每日自动快照**
- 每天自动执行 `git add -A && git commit -m "daily-backup: auto snapshot YYYY-MM-DD"`
- 为回滚机制提供稳定的历史版本基础

**可选通知：Discord Webhook**
- 支持通过 `DISCORD_WEBHOOK_URL` 环境变量配置 Discord 通知
- 关键事件（启动、故障、修复成功、回滚）实时推送到运维频道

## 核心架构

### 技术栈

- **语言**: Bash Shell Script（单文件 `guardian.sh`，约 150 行）
- **依赖工具**:
  - `git` — workspace 回滚和快照
  - `pgrep` / `pkill` — 进程检测和管理
  - `curl` — Discord 通知（可选）
  - `openclaw` CLI — 官方诊断工具

### 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                    Guardian 主循环                           │
│  while true; do                                             │
│    daily_backup()      # 每日快照                           │
│    if ! is_gateway_running; then                            │
│      repair_gateway()  # 三层修复流程                       │
│    fi                                                       │
│    sleep $CHECK_INTERVAL                                    │
│  done                                                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              repair_gateway() 修复流程                       │
├─────────────────────────────────────────────────────────────┤
│  1. notify("Gateway 异常，开始修复...")                     │
│  2. for i in 1..MAX_REPAIR_ATTEMPTS:                        │
│       try_doctor_fix()                                      │
│       if success: return 0                                  │
│  3. notify("doctor --fix 失败，尝试 git 回滚...")          │
│  4. do_rollback()                                           │
│       - get_stable_commit()  # 查找稳定版本                │
│       - git reset --hard <commit>                           │
│       - pkill + restart gateway                             │
│       - if success: return 0                                │
│  5. notify("所有修复手段均失败，冷却期...")                │
│  6. sleep $COOLDOWN_PERIOD                                  │
└─────────────────────────────────────────────────────────────┘
```

### 配置参数

| 环境变量 | 默认值 | 说明 |
|---------|--------|------|
| `GUARDIAN_WORKSPACE` | `$HOME/.openclaw/workspace` | Workspace 路径（必须是 git 仓库） |
| `GUARDIAN_LOG` | `/tmp/openclaw-guardian.log` | 日志文件路径 |
| `GUARDIAN_CHECK_INTERVAL` | `30` | 健康检查间隔（秒） |
| `GUARDIAN_MAX_REPAIR` | `3` | `doctor --fix` 最大尝试次数 |
| `GUARDIAN_COOLDOWN` | `300` | 失败后冷却期（秒） |
| `OPENCLAW_CMD` | `openclaw` | OpenClaw CLI 命令 |
| `DISCORD_WEBHOOK_URL` | _(未设置)_ | Discord 通知 Webhook（可选） |

### 部署方式

**1. 手动部署**
```bash
# 初始化 workspace git 仓库（必需）
cd ~/.openclaw/workspace
git init && git add -A && git commit -m "initial"

# 安装 Guardian
cp scripts/guardian.sh ~/.openclaw/guardian.sh
chmod +x ~/.openclaw/guardian.sh

# 后台启动
nohup ~/.openclaw/guardian.sh >> /tmp/openclaw-guardian.log 2>&1 &
```

**2. AI Agent 自动安装**
用户只需对 OpenClaw Agent 说：
> "Help me install openclaw-guardian to harden my gateway"

Agent 会自动完成 git 初始化、脚本安装和启动。

**3. 容器重启自动启动**
在 `~/.openclaw/start-gateway.sh` 中添加：
```bash
pkill -f "guardian.sh" 2>/dev/null || true
nohup /home/ubuntu/.openclaw/guardian.sh >> /tmp/openclaw-guardian.log 2>&1 &
```

**4. 作为 OpenClaw Skill 安装**
```bash
clawhub install myclaw-guardian
```

## 关键特性

### 1. 零配置开箱即用

- 所有参数都有合理的默认值
- 无需修改代码即可直接运行
- 通过环境变量灵活调整行为

### 2. 渐进式修复策略

- 优先使用官方 `doctor --fix` 工具（最小侵入）
- 仅在必要时才执行 git 回滚（保留用户修改）
- 避免过度激进的恢复操作

### 3. 智能稳定版本识别

`get_stable_commit()` 函数通过正则表达式排除自动提交：
```bash
git log --all --oneline -50 | \
  grep -v -E "rollback|daily-backup|auto-backup|guardian-auto" | \
  sed -n '2p' | awk '{print $1}'
```
- 跳过最近的 commit（可能是导致故障的版本）
- 选择倒数第二个人工提交作为回滚目标

### 4. 防止无限循环

- 修复失败后强制进入冷却期（默认 5 分钟）
- 避免在无法恢复的情况下持续消耗系统资源
- 为人工介入留出时间窗口

### 5. 与 gw-watchdog 互补

| 特性 | gw-watchdog | Guardian |
|------|-------------|----------|
| 检查间隔 | 15 秒 | 30 秒 |
| 修复动作 | 快速重启 | `doctor --fix` → git 回滚 |
| Git 回滚 | ❌ | ✅ |
| Discord 通知 | ❌ | ✅ |
| 每日备份 | ❌ | ✅ |

两者可以同时运行：
- `gw-watchdog` 处理瞬时崩溃（快速重启）
- `Guardian` 处理配置错误和持久性故障（深度修复）

### 6. 生产级日志和通知

**日志格式**：
```
[2026-03-11 14:32:15] 🚀 Guardian 守护进程启动 (check=30s, max_repair=3)
[2026-03-11 14:35:42] Gateway 异常，开始修复流程...
[2026-03-11 14:35:43] 修复尝试 1/3
[2026-03-11 14:35:53] doctor --fix 修复成功，Gateway 已恢复
```

**Discord 通知示例**：
```
🚨 **OpenClaw Guardian**: Gateway 异常，开始修复流程...
🚨 **OpenClaw Guardian**: ✅ doctor --fix 修复成功（第 1 次尝试）
```

### 7. 安全性考虑

- 脚本使用 `set -euo pipefail` 严格模式
- 回滚前记录当前 commit SHA，便于事后恢复
- 所有 git 操作都在 workspace 目录内执行，不影响其他仓库
- Discord Webhook URL 通过环境变量传递，不硬编码在脚本中
# apps/api/services/config_safety_v2.py

class ConfigHealthMonitor:
    """配置健康监控器（类似 Guardian 的健康检查循环）"""

    async def check_agent_health(self, agent_id: str) -> HealthStatus:
        """检查 Agent 是否正常运行"""
        # 1. 检查 Agent 进程状态（通过 MCP 连接）
        # 2. 检查最近错误日志
        # 3. 检查工具调用成功率
        pass

    async def auto_rollback_on_failure(
        self,
        agent_id: str,
        max_attempts: int = 3
    ):
        """检测到故障后自动回滚配置"""
        # 1. 尝试重启 Agent（类似 doctor --fix）
        # 2. 如果失败，回滚到最近的稳定快照
        # 3. 记录回滚事件到 audit_logs
        # 4. 发送通知到 Slack/Discord/Email
        pass
```

**B. 配置快照的"稳定性标记"**
```python
# apps/api/models/config_snapshot.py

class ConfigSnapshot(Base):
    # 现有字段...
    is_stable = Column(Boolean, default=False)  # 标记为稳定版本
    stability_score = Column(Float)  # 稳定性评分（基于运行时长、错误率）
    last_verified_at = Column(DateTime)  # 最后验证时间
```

借鉴 Guardian 的 `get_stable_commit()` 逻辑，自动识别稳定快照：
- 运行超过 24 小时无故障 → 标记为 stable
- 回滚时优先选择 `is_stable=True` 的快照

**C. 渐进式回滚策略**
```python
# apps/api/services/config_safety_v2.py

async def progressive_rollback(self, agent_id: str):
    """渐进式回滚（类似 Guardian 的三层修复）"""
    # 第一层：重启 Agent（最小侵入）
    if await self.restart_agent(agent_id):
        return RollbackResult.RESTART_SUCCESS

    # 第二层：回滚到上一个快照（保留大部分修改）
    last_snapshot = await self.get_last_snapshot(agent_id)
    if await self.rollback_to_snapshot(agent_id, last_snapshot.id):
        return RollbackResult.SNAPSHOT_ROLLBACK_SUCCESS

    # 第三层：回滚到最近的稳定快照（深度恢复）
    stable_snapshot = await self.get_last_stable_snapshot(agent_id)
    if await self.rollback_to_snapshot(agent_id, stable_snapshot.id):
        return RollbackResult.STABLE_ROLLBACK_SUCCESS

    # 第四层：进入冷却期，通知管理员
    await self.enter_cooldown(agent_id, duration=300)
    await self.notify_admin(agent_id, "All rollback attempts failed")
    return RollbackResult.MANUAL_INTERVENTION_REQUIRED
```

### 2. Runbooks 模块增强

**当前 ClawButler 能力**：
- Runbook 自动化注册（versioned definitions）
- 多后端调度器（mock / openclaw_native / openprose）
- 执行时间线（event timeline）
- 触发类型（manual / schedule / webhook / event）

**Guardian 启发的改进方向**：

**A. 内置"健康检查 Runbook"模板**
```python
# apps/api/services/runbook_templates.py

HEALTH_CHECK_RUNBOOK = {
    "name": "agent-health-monitor",
    "description": "Periodic health check for Agent instances (inspired by OpenClaw Guardian)",
    "schedule": {"kind": "cron", "expr": "*/5 * * * *"},  # 每 5 分钟
    "steps": [
        {
            "name": "check_mcp_connection",
            "action": "mcp.ping",
            "timeout": 10,
            "on_failure": "continue"
        },
        {
            "name": "check_error_rate",
            "action": "metrics.query",
            "params": {"metric": "agent.error_rate", "window": "5m"},
            "threshold": {"max": 0.1},  # 错误率 > 10% 触发告警
            "on_failure": "trigger_rollback"
        },
        {
            "name": "auto_rollback",
            "action": "config.rollback_to_stable",
            "condition": "previous_step_failed",
            "notify": ["slack", "email"]
        }
    ]
}
```

**B. Runbook 执行失败自动回滚**
```python
# apps/api/services/runbook_executor.py

class RunbookExecutor:
    async def execute_with_rollback(self, runbook_id: str):
        """执行 Runbook，失败时自动回滚"""
        snapshot = await self.create_pre_execution_snapshot()

        try:
            result = await self.execute(runbook_id)
            if result.status == "failed":
                await self.rollback_to_snapshot(snapshot.id)
                await self.notify("Runbook failed, rolled back to pre-execution state")
        except Exception as e:
            await self.rollback_to_snapshot(snapshot.id)
            raise
```

### 3. 新增"Agent Watchdog"功能模块

借鉴 Guardian 的完整设计，为 ClawButler 添加专门的 Agent 守护功能：

**数据库模型**：
```python
# apps/api/models/agent_watchdog.py

class AgentWatchdogConfig(Base):
    __tablename__ = "agent_watchdog_configs"

    id = Column(UUID, primary_key=True)
    agent_id = Column(UUID, ForeignKey("agents.id"))

    # 监控配置
    check_interval = Column(Integer, default=30)  # 秒
    max_repair_attempts = Column(Integer, default=3)
    cooldown_period = Column(Integer, default=300)  # 秒

    # 通知配置
    discord_webhook_url = Column(String, nullable=True)
    slack_webhook_url = Column(String, nullable=True)
    email_recipients = Column(ARRAY(String), default=[])

    # 回滚策略
    auto_rollback_enabled = Column(Boolean, default=True)
    rollback_to_stable_only = Column(Boolean, default=True)

    # 状态
    is_active = Column(Boolean, default=False)
    last_check_at = Column(DateTime)
    last_failure_at = Column(DateTime)
    consecutive_failures = Column(Integer, default=0)

class AgentWatchdogEvent(Base):
    __tablename__ = "agent_watchdog_events"

    id = Column(UUID, primary_key=True)
    agent_id = Column(UUID, ForeignKey("agents.id"))
    event_type = Column(Enum("health_check", "repair_attempt", "rollback", "cooldown"))
    status = Column(Enum("success", "failure"))
    details = Column(JSONB)
    created_at = Column(DateTime, default=datetime.utcnow)
```

**API 路由**：
```python
# apps/api/routers/agent_watchdog.py

@router.post("/agents/{agent_id}/watchdog/enable")
async def enable_watchdog(agent_id: UUID, config: WatchdogConfigCreate):
    """启用 Agent 守护进程"""
    pass

@router.get("/agents/{agent_id}/watchdog/status")
async def get_watchdog_status(agent_id: UUID):
    """获取守护进程状态和最近事件"""
    pass

@router.post("/agents/{agent_id}/watchdog/test")
async def test_watchdog(agent_id: UUID):
    """手动触发一次健康检查（用于测试）"""
    pass
```

**后台任务**：
```python
# apps/api/tasks/agent_watchdog.py

async def watchdog_loop():
    """全局守护循环（类似 Guardian 的 while true 循环）"""
    while True:
        active_configs = await get_active_watchdog_configs()

        for config in active_configs:
            if should_check(config):
                await check_and_repair(config)

        await asyncio.sleep(10)  # 全局循环间隔
```

### 4. Federation 模块增强

**Guardian 启发的跨节点健康监控**：

```python
# apps/api/services/federation_health.py

class FederationHealthMonitor:
    """监控 Federation 对等节点的健康状态"""

    async def check_peer_health(self, peer_id: str):
        """检查远程 Peer 是否可达"""
        # 1. 发送 A2A health check 请求
        # 2. 检查响应时间和错误率
        # 3. 如果连续失败，标记为 unhealthy
        pass

    async def auto_failover(self, peer_id: str):
        """自动故障转移（类似 Guardian 的回滚）"""
        # 1. 将流量路由到备用 Peer
        # 2. 通知管理员
        # 3. 定期重试连接故障 Peer
        pass
```

### 5. 运维工具增强

**A. 一键部署 Watchdog**
```bash
# scripts/enable-watchdog.sh

#!/bin/bash
# 为所有 Agent 启用守护进程

curl -X POST "https://clawbutler.cc/api/v1/agents/bulk/watchdog/enable" \
  -H "Authorization: Bearer $API_TOKEN" \
  -d '{
    "check_interval": 30,
    "max_repair_attempts": 3,
    "auto_rollback_enabled": true,
    "discord_webhook_url": "$DISCORD_WEBHOOK"
  }'
```

**B. 守护进程仪表板**
在 Web UI 中添加专门的 Watchdog 监控页面：
- 实时显示所有 Agent 的健康状态
- 最近的修复事件时间线
- 回滚历史和成功率统计
- 一键启用/禁用守护功能

### 6. 成本优化

Guardian 的轻量级设计（单个 Bash 脚本，30 秒检查间隔）对 ClawButler 的启示：

**A. 分层监控策略**
- **轻量级健康检查**（每 30 秒）：仅检查 MCP 连接和进程状态
- **深度健康检查**（每 5 分钟）：检查错误日志、工具调用成功率、内存使用
- **完整诊断**（仅在故障时）：执行完整的配置验证和依赖检查

**B. 避免过度监控**
- 不为每个 Agent 启动独立的守护进程（资源浪费）
- 使用单个全局守护循环 + 数据库驱动的配置
- 仅在用户明确启用时才激活 Watchdog

### 7. 文档和用户教育

Guardian 的文档策略值得借鉴：
- **一键安装命令**：`clawhub install myclaw-guardian`
- **AI Agent 自助安装**：用户只需说"帮我安装 guardian"
- **清晰的配置说明**：所有环境变量都有默认值和说明
- **与现有工具的对比表**：明确 Guardian 与 gw-watchdog 的差异

ClawButler 可以提供类似的体验：
```bash
# 一键启用所有 Agent 的守护功能
clawbutlerctl watchdog enable --all

# 查看守护状态
clawbutlerctl watchdog status

# 查看最近的修复事件
clawbutlerctl watchdog events --last 24h
```

## 总结

OpenClaw Guardian 是一个**生产级、零配置、渐进式修复**的 Agent 守护方案，核心价值在于：

1. **自动化运维**：无需人工干预即可处理 90% 的常见故障
2. **渐进式修复**：从最小侵入（重启）到深度恢复（git 回滚），避免过度激进
3. **智能回滚**：自动识别稳定版本，避免回滚到同样有问题的配置
4. **轻量级设计**：单个 Bash 脚本，无额外依赖，资源占用极低
5. **生产验证**：MyClaw.ai 平台运行数千个实例的实战经验

对 ClawButler 的最大启示是：**配置管理不仅要支持手动回滚，更要支持自动健康监控和故障自愈**。通过将 Guardian 的设计理念融入 Config Safety V2、Runbooks 和新增的 Agent Watchdog 模块，ClawButler 可以从"配置版本管理工具"升级为"自愈式 Agent 控制平面"。

<!-- lastCommit: 137e138 -->

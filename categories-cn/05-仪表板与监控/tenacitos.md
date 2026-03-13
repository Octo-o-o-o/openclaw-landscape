> https://github.com/carlosazaustre/tenacitOS

# carlosazaustre/tenacitOS

## 基本信息

- **Stars**: 689
- **URL**: https://github.com/carlosazaustre/tenacitOS
- **License**: MIT
- **技术栈**: Next.js 15 + React 19 + Tailwind CSS v4
- **作者**: Carlos Azaustre

## 问题与解决方案

### 核心问题

OpenClaw 用户需要一个**实时仪表板和控制中心**来管理 AI Agent 实例，但面临以下困难：

1. **缺乏可视化监控**：OpenClaw 本身是命令行工具，缺少直观的监控界面
2. **多 Agent 管理困难**：需要同时管理多个 Agent（main、studio、infra 等）
3. **成本追踪不便**：Token 使用和成本分散在各个 Agent 的日志中
4. **Cron 任务管理复杂**：需要手动编辑 crontab 文件
5. **记忆文件查看不便**：MEMORY.md、SOUL.md 等文件需要用编辑器打开
6. **活动日志分散**：Agent 的操作日志分散在多个文件中

### 解决方案

TenacitOS 是一个**实时仪表板和控制中心**，直接读取 OpenClaw 的配置和数据：

- **📊 系统监控**：实时 VPS 指标（CPU、RAM、磁盘、网络）+ PM2/Docker 状态
- **🤖 Agent 仪表板**：所有 Agent、会话、Token 使用、模型、活动状态
- **💰 成本追踪**：从 OpenClaw 会话（SQLite）读取真实成本分析
- **⏰ Cron 管理器**：可视化 Cron 管理器，带周时间线、运行历史、手动触发
- **📋 活动流**：实时 Agent 操作日志，带热力图和图表
- **🧠 记忆浏览器**：探索、搜索、编辑 Agent 记忆文件
- **📁 文件浏览器**：导航工作区文件，带预览和浏览器内编辑
- **🔎 全局搜索**：跨记忆和工作区文件的全文搜索
- **🔔 通知**：实时通知中心，带未读徽章
- **🏢 Office 3D**：交互式 3D 办公室，每个 Agent 一张桌子（React Three Fiber）
- **📺 终端**：只读终端，用于安全状态命令
- **🔐 认证**：密码保护，带速率限制和安全 Cookie

## 核心架构

### 技术栈

```
TenacitOS
├── 前端：Next.js 15 (App Router) + React 19
│   ├── Tailwind CSS v4
│   ├── React Three Fiber (3D Office)
│   ├── Recharts (图表)
│   └── Lucide React (图标)
├── 后端：Next.js API Routes
│   ├── 文件系统读取（OpenClaw 配置和数据）
│   ├── SQLite 查询（成本追踪）
│   └── 系统指标采集（CPU、内存、磁盘）
├── 数据存储：JSON 文件 + SQLite
│   ├── data/cron-jobs.json
│   ├── data/activities.json
│   ├── data/notifications.json
│   └── OpenClaw SQLite 数据库
└── 认证：Next.js Middleware + Cookie
```

### 架构特点

**零额外后端**：TenacitOS 直接读取 OpenClaw 的文件和数据库，无需额外的数据库或后端服务。

```
/root/.openclaw/              ← OPENCLAW_DIR (可配置)
├── openclaw.json             ← Agent 列表、通道、模型配置
├── workspace/                ← 主 Agent 工作区（MEMORY.md, SOUL.md 等）
├── workspace-studio/         ← 子 Agent 工作区
├── workspace-infra/
├── ...
└── workspace/mission-control/ ← TenacitOS 安装在这里
```

### 数据流

```
┌─────────────────────────────────────────────┐
│  TenacitOS (Next.js App)                    │
│  http://localhost:3000                      │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  Dashboard Page                      │  │
│  │  ├─ Agent 状态卡片                   │  │
│  │  ├─ 成本图表                         │  │
│  │  └─ 活动流                           │  │
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
│  OpenClaw 数据源                             │
│  ├─ openclaw.json (Agent 配置)              │
│  ├─ workspace/MEMORY.md (记忆文件)          │
│  ├─ workspace/.sessions/*.db (会话数据库)   │
│  └─ /proc/* (系统指标)                      │
└─────────────────────────────────────────────┘
```

## 关键特性

### 1. Agent 自动发现

**实现原理**：

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

**特点**：
- **零配置**：从 `openclaw.json` 自动读取 Agent 列表
- **自定义外观**：每个 Agent 可以定义自己的 emoji 和颜色
- **实时更新**：修改 `openclaw.json` 后刷新页面即可看到变化

### 2. 成本追踪

**数据源**：OpenClaw 的 SQLite 数据库

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

// 计算成本
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

// 保存到 JSON
writeFileSync('data/costs.json', JSON.stringify(costs, null, 2));
```

**自动收集**：

```bash
# 每小时收集一次
./scripts/setup-cron.sh
# 添加 cron 任务：0 * * * * cd /path/to/mission-control && npx tsx scripts/collect-usage.ts
```

**可视化**：

- **日成本趋势图**：Recharts 折线图
- **按 Agent 分组**：每个 Agent 的成本占比
- **按模型分组**：每个模型的成本占比

### 3. Cron 管理器

**功能**：
- **可视化时间线**：周视图，显示每个 Cron 任务的执行时间
- **运行历史**：最近 10 次运行记录
- **手动触发**：点击按钮手动运行 Cron 任务
- **启用/禁用**：切换 Cron 任务的启用状态

**数据结构**：

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

**技术**：React Three Fiber + Drei

**功能**：
- **交互式 3D gent 一张桌子
- **自定义位置**：在 `src/components/Office3D/agentsConfig.ts` 中配置
- **3D 头像**：支持 Ready Player Me GLB 格式
- **回退机制**：如果没有 GLB 文件，显示彩色球体

**配置**：

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
  // 最多支持 6 个 Agent
];
```

**3D 头像**：

```
public/models/
├── main.glb        ← 主 Agent 头像
├── studio.glb      ← workspace-studio Agent
└── infra.glb       ← workspace-infra Agent
```

### 5. 记忆浏览器

**功能**：
- **文件列表**：显示所有记忆文件（MEMORY.md、SOUL.md、PLAN.md 等）
- **搜索**：全文搜索记忆文件内容
- **预览**：Markdown 渲染预览
- **编辑**：浏览器内编辑，保存到文件系统

**实现**：

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

### 6. 系统监控

**指标**：
- **CPU 使用率**：从 `/proc/stat` 读取
- **内存使用**：从 `/proc/meminfo` 读取
- **磁盘使用**：从 `df` 命令读取
- **网络流量**：从 `/proc/net/dev` 读取
- **PM2 状态**：从 `pm2 jlist` 读取
- **Docker 状态**：从 `docker ps` 读取

**实现**：

```typescript
// src/lib/system-metrics.ts
im{ execSync } from 'child_process';

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
  const available = parseInt(meminfo.match(/MemAvailable:\s+(\d+)/)?.[1] || '0') * 10rn { used: total - available, total };
}

export function getDiskUsage(): { used: number; total: number } {
  const df = execSync('df -B1 /').toString();
  const [, , total, used] = df.split('\n')[1].split(/\s+/);
  return { used: parseInt(used), total: parseInt(total) };
}
```
## 总结

carlosazaustre/tenacitOS 是一个**完整的 OpenClaw 控制中心**，其价值在于：

1. **零额外后端**：直接读取 OpenClaw 的配置和数据
2. **Agent 自动发现**：无需手动配置
3. **成本追踪**：从 SQLite 读取真实成本数据
4. **Cron 管理器**：可视化 Cron 任务管理
5. **Office 3D**：3D 可视化 Agent 状态
6. **记忆浏览器**：搜索、预览、编辑记忆文件

ClawButler 可以借鉴其**零额外后端架构**、**Agent 自动发现**、**成本追踪**、**Cron 管理器**等设计，为用户提供一个**统一的控制中心**，管理和监控整个 Agent 集群。

<!-- lastCommit: 137e138 -->

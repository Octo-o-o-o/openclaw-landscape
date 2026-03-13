> https://github.com/Curbob/LobsterBoard

# Curbob/LobsterBoard

## 基本信息

- **Stars**: 815
- **URL**: https://github.com/Curbob/LobsterBoard
- **License**: Business Source License 1.1 (BSL-1.1)
- **作者**: Curbob

## 问题与解决方案

### 核心问题

LobsterBoard 解决了 OpenClaw 用户的可视化监控和控制需求：

1. **缺乏统一的可视化界面**：OpenClaw 本身是命令行工具，缺少直观的仪表板
2. **多服务器监控困难**：需要同时监控多台 VPS 上的 OpenClaw 实例
3. **AI 使用额度追踪不便**：Claude Code、Copilot、Cursor 等多个 AI 服务的额度分散
4. **系统状态监控缺失**：CPU、内存、磁盘、Docker 容器状态需要手动查询
5. **配置管理分散**：OpenClaw 配置、Cron 任务、日志查看需要在多个地方操作

### 解决方案

LobsterBoard 是一个**自托管的拖拽式仪表板构建器**，提供：

- **60+ 小部件**：系统监控、天气、日历、RSS、智能家居、金融、AI/LLM 追踪等
- **模板画廊**：导出/导入/分享仪表板布局，自动截图预览
- **自定义页面**：扩展仪表板，支持完整的自定义页面（笔记、看板等）
- **远程服务器监控**：通过 lobsterboard-agent 监控多台服务器
- **零云依赖**：完全本地运行，数据不离开本地

## 核心架构

### 技术栈

```
LobsterBoard
├── 前端：纯 JavaScript（无框架）
│   ├── builder.js      # 编辑器：拖拽、缩放、配置 I/O
│   ├── widgets.js      # 60+ 小部件定义
│   └── templates.js    # 模板画廊 & 导出系统
├── 后端：Node.js 单文件服务器
│   └── server.cjs      # Express 服务器，SSE 流式数据
├── 数据存储：JSON 文件
│   └── config.json     # 用户保存的布局
└── 扩展系统：自定义页面
    └── pages/          # 自动发现的自定义页面
```

### 架构特点

1. **无构建步骤**：直接运行 `node server.cjs`，无需 webpack/vite
2. **单服务器架构**：一个 Node.js 进程处理所有请求
3. **SSE 流式数据**：系统统计通过 Server-Sent Events 实时推送
4. **自动发现机制**：自定义页面放入 `pages/` 目录自动加载

### 小部件系统架构

```javascript
// 小部件定义结构
{
  id: "cpu-memory",
  name: "CPU / Memory",
  category: "system",
  defaultSize: { w: 4, h: 3 },
  properties: {
    server: { type: "select", options: ["local", "remote-1"] },
    refreshInterval: { type: "number", default: 2000 }
  },
  render: (container, config) => {
    // 渲染逻辑
  },
  update: (container, data) => {
    // 更新逻辑
  }
}
```

## 关键特性

### 1. 拖拽式编辑器

- **20px 网格对齐**：精确布局
- **调整大小手柄**：拖拽调整小部件尺寸
- **属性面板**：右侧面板配置小部件属性
- **画布尺寸预设**：1920×1080、2560×1440 等

### 2. 远程服务器监控

**架构**：

```
┌─────────────────────────────────────────────┐
│  LobsterBoard (主控端)                       │
│  http://localhost:8080                      │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  Uptime Monitor Widget               │  │
│  │  Server: remote-vps-1                │  │
│  │  ├─ CPU: 45%                         │  │
│  │  ├─ Memory: 2.1GB / 8GB              │  │
│  │  └─ Uptime: 15 days                  │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
                    ↓ HTTP API
┌─────────────────────────────────────────────┐
│  Remote VPS                                 │
│  http://vps-ip:9090                         │
│                                             │
│  lobsterboard-agent                         │
│  ├─ API Key 验证                            │
│  ├─ 系统指标采集                            │
│  └─ Docker 容器状态                         │
└─────────────────────────────────────────────┘
```

**支持的远程小部件**：
- Uptime Monitor（系统运行时间、CPU、内存）
- CPU / Memory（CPU 使用率 + RAM 使用率）
- Disk Usage（磁盘空间，环形图）
- Network Speed（上传/下载吞吐量）
- Docker Containers（容器列表和状态）

### 3. AI/LLM 使用追踪

**支持的 AI 服务**（14 个）：

| 服务 | 追踪内容 | 配置方式 |
|------|---------|---------|
| Claude Code | Session, weekly, Opus limits | 运行 `claude` 一次 |
| Codex CLI | Session, weekly, code reviews | 运行 `codex` 一次 |
| GitHub Copilot | Premium, chat, completions | 运行 `gh auth login` |
| Cursor | Credits, usage breakdown | 使用 Cursor IDE |
| Gemini CLI | Pro, flash models | 运行 `gemini` 一次 |
| Amp | Free tier, credits | 运行 `amp` 一次 |
| Factory / Droid | Standard, premium tokens | 运行 `factory` 一次 |
| Kimi Code | Session, weekly | 运行 `kimi` 一次 |
| JetBrains AI | Quota tracking | IDE 登录 |
| Antigravity | Gemini 3, Claude via Google | 运行 `antigravity-usage login` |
| MiniMax | Coding plan session | 设置 `MINIMAX_API_KEY` |
| Z.ai | Session, weekly | 设置 `ZAI_API_KEY` |
| AI Cost Tracker | Monthly cost breakdown | — |
| API Status | Provider availability | — |

**实现原理**：
- 读取各 AI CLI 工具的本地缓存文件（如 `~/.claude/usage.json`）
- 通过 API 查询使用情况（需要 API Key）
- 实时显示剩余额度和使用趋势

### 4. 模板系统

**功能**：
- **导出**：当前仪表板导出为模板（自动截图预览）
- **浏览**：模板画廊发现预构建布局
- **导入**：两种模式
  - **Replace**：替换整个仪表板
  - **Merge**：将模板小部件追加到现有布局下方

**存储结构**：

```
templates/
├── templates.json          # 模板索引
└── my-template/
    ├── config.json         # 小部件配置
    └── preview.png         # 自动截图
```

### 5. 自定义页面系统

**结构**：

```
pages/
└── my-page/
    ├── page.json       # 元数据（title, icon, order）
    ├── index.html      # 页面 UI
    └── api.cjs         # 可选：服务端 API 路由
```

**自动发现**：
- 启动时扫描 `pages/` 目录
- 自动注册路由 `/pages/my-page`
- 导航栏自动显示入口

### 6. 五种主题

| 主题 | 风格 | 特点 |
|------|------|------|
| Default | 深色 | Emoji 图标，经典外观 |
| Terminal | CRT 绿色 | 扫描线效果，Phosphor 图标 |
| Paper | 米色/棕褐色 | 衬线字体，复古感 |
| Feminine | 粉色/薰衣草 | 柔和光晕 |
| Feminine Dark | 粉紫色 | 深色背景，粉紫色强调 |
## 总结

LobsterBoard 虽然是通用仪表板工具，但其**拖拽式布局**、**远程监控架构**、**AI 额度追踪**、**自定义页面系统**等设计理念非常适合 ClawButler。特别是在**多实例监控**和**可视化定制**方面，可以直接借鉴其架构，为 ClawButler 用户提供更灵活的监控和管理界面。

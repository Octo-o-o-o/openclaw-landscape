# SamurAIGPT/awesome-openclaw

## 基本信息

- **Stars**: 778
- **URL**: https://github.com/SamurAIGPT/awesome-openclaw
- **License**: CC0 1.0 (Public Domain)
- **类型**: 资源列表（Awesome List）
- **作者**: Anil Chandra Naidu Matcha (@matchaman11)

## 问题与解决方案

### 核心问题

OpenClaw 生态快速发展，社区项目、工具、教程、文章分散在各处，用户面临以下困难：

1. **资源分散**：社区项目、技能、教程、文章分散在 GitHub、Medium、YouTube 等平台
2. **信息过载**：每天有大量新项目和文章发布，难以筛选优质资源
3. **缺少分类**：资源没有系统分类，难以快速找到需要的内容
4. **更新不及时**：官方文档更新较慢，社区资源更新更快
5. **新手友好度不足**：缺少从入门到精通的完整学习路径

### 解决方案

awesome-openclaw 是一个**精选的 OpenClaw 资源列表**，提供：

- **700+ 社区技能**：ClawHub 官方技能商店
- **12+ 消息平台集成**：WhatsApp、Telegram、Discord、Slack 等
- **50+ 外部服务集成**：GitHub、Gmail、Spotify、Obsidian 等
- **13,000+ MCP 服务器**：Model Context Protocol 生态
- **社区项目分类**：Web 客户端、部署工具、记忆系统、企业解决方案等
- **教程和文章**：从入门到高级的完整学习路径
- **安全资源**：最佳实践、安全工具、已知风险

## 核心架构

### 资源分类体系

```
awesome-openclaw/
├── 官方资源
│   ├── OpenClaw 官网
│   ├── GitHub 仓库（150k+ stars）
│   ├── 官方文档
│   ├── ClawHub（技能商店）
│   └── 发布日志
├── 快速开始
│   ├── 安装指南
│   ├── 首次配置
│   └── Web 仪表板
├── 安装指南
│   ├── 官方指南
│   ├── 平台指南（macOS/Linux/Windows/Docker/云）
│   └── 托管服务（OctoClaw、SlackClaw）
├── 技能和插件
│   ├── 技能注册表（ClawHub、AgentFund、ClawdTalk 等）
│   ├── 热门技能（LinkedIn、X/Twitter 等）
│   ├── 技能分类（生产力、开发、智能家居等）
│   └── 插件开发
├── 集成
│   ├── 消息平台（12+）
│   └── 外部服务（50+）
├── MCP 支持
│   ├── MCP 资源
│   └── MCP 服务器列表
├── 教程和指南
│   ├── 入门教程
│   └── 高级教程
├── 文章和新闻
│   ├── 起源和历史
│   ├── 行业报道
│   └── 安全分析
├── 社区
│   ├── 官方频道
│   ├── 活动（ClawCon）
│   └── 创建者
├── 社区项目
│   ├── Web 客户端和 UI
│   ├── 部署和基础设施
│   ├── 记忆和存储
│   ├── 企业解决方案
│   ├── 中国 IM 集成
│   ├── 监控和工具
│   ├── 交易和金融
│   ├── 开发工作流
│   ├── 内容和发布
│   ├── 市场
│   └── 其他
├── 替代方案和对比
│   ├── 替代方案列表
│   └── 对比资源
├── 安全
│   ├── 最佳实践
│   ├── 安全工具
│   ├── 安全资源
│   └── 已知风险
└── FAQ
```

### 数据结构

**表格式资源列表**：

```markdown
| Project | Stars | Description |
|---------|-------|-------------|
| [clawterm](https://github.com/nicholaschen/clawterm) | - | Terminal-based OpenClaw client |
| [MobileClaw](https://github.com/wende/mobileclaw) | NEW | Mobile-first PWA client for OpenClaw |
```

**分类列表**：

```markdown
### Beginner

| Tutorial | Source | Description |
|----------|--------|-------------|
| [What is OpenClaw?](https://medium.com/@gemQueenx/...) | Medium | Setup + Features guide |
```

## 关键特性

### 1. 社区项目分类（200+ 项目）

#### Web 客户端和 UI（7 个）

| 项目 | Stars | 描述 |
|------|-------|------|
| **MobileClaw** | NEW | 移动优先 PWA 客户端，实时工具调用，内联差异，子 Agent 活动流 |
| **Nerve** | NEW | 自托管 Web 驾驶舱，实时流式，推理块，语音 I/O，子 Agent 会话监控 |
| **SwarmClaw** | NEW | 自托管 AI Agent 编排仪表板，多提供商支持，任务调度 |
| **PinchChat** | - | 开源 Webchat UI，ChatGPT 风格界面，实时工具调用可视化 |
| **webclaw** | 155+ | 快速、极简的 OpenClaw Web 客户端 |

#### 部署和基础设施（10 个）

| 项目 | Stars | 描述 |
|------|-------|------|
| **moltworker** | 7.9k | 在 Cloudflare Workers 上运行 OpenClaw |
| **OpenClaw Easy** | NEW | 零配置 OpenClaw 桌面应用（macOS/Windows），无需终端 |
| **OpenClawInstaller** | 1.3k | OpenClaw 一键部署工具 |
| **OpenClaw Kit (TurboStarter)** | NEW | 固执己见的 OpenClaw 包装器启动套件，带基础设施、认证、计费 |
| **MimiClaw** | NEW | 在 $5 ESP32-S3 芯片上运行 OpenClaw，无需 Linux 或 Node.js |
| **openclaw-self-healing** | NEW | 4 层自主自愈系统，Claude Code 作为紧急医生 |
| **OctoClaw** | NEW | 完全托管的 OpenClaw 托管（德国 Hetzner），GDPR 合规 |
| **SlackClaw** | NEW | 专为 Slack 工作区设计的托管 OpenClaw 部署 |
| **PhoneClaw** | NEW | 自动化所有 Android 手机应用 |
| **LightClaw** | NEW | 轻量级 OpenClaw 启发的 Python Agent 核心 |

#### 记忆和存储（4 个）

| 项目 | Stars | 描述 |
|------|-------|------|
| **memU** | 8k | 主动 Agent 的持久记忆层 |
| **Agent Second Brain** | 152 | 完整的第二大脑系统：语音笔记 → Telegram → Obsidian 保险库 + Todoist 任务 |
| **clawmem** | - | OpenClaw 的基于向量的记忆 |
| **soul-upload.com** | - | OpenClaw 工作区工件的加密备份存储（SOUL.md、MEMORY.md 等） |

#### 企业解决方案（3 个）

| 项目 | Stars | 描述 |
|------|-------|------|
| **archestra** | 2.8k | 带 RBAC 的企业级 OpenClaw |
| **openclaw-saml** | - | OpenClaw 的 SAML 认证 |
| **claw-audit** | - | 审计日志和合规工具 |

#### 中国 IM 集成（5 个）

| 项目 | Stars | 描述 |
|------|-------|------|
| **openclaw-dingtalk** | 500+ | 钉钉集成 |
| **openclaw-feishu** | 400+ | 飞书/Lark 集成 |
| **openclaw-wechat** | 600+ | 微信集成 |
| **openclaw-qq** | 300+ | QQ 集成 |
| **openclaw-wework** | 200+ | 企业微信集成 |

#### 监控和工具（6 个）

| 项目 | Stars | 描述 |
|------|-------|------|
| **Manifest** | 3.3k | OpenClaw Agent 的实时成本可观测性 |
| **crabwalk** | 683 | OpenClaw 的实时伴侣监控器 |
| **opik-openclaw** | 50 | Opik 中的跟踪级可观测性 OpenClaw 插件 |
| **AgentPulse** | NEW | 实时 LLM 成本追踪和可观测性 |
| **WatchClaw** | NEW | OpenClaw 部署的自主安全/运维加固层 |

### 2. MCP 支持（13,000+ 服务器）

**MCP 资源**：

- **MCP 适配器插件**：将 MCP 工具暴露为原生 Agent 工具
- **原生 MCP 支持问题**：功能讨论
- **MCP 服务器 PR**：服务器支持实现

**精选 MCP 服务器**：

| 服务器 | 描述 |
|--------|------|
| `https://api.anchorbrowser.io/mcp` | AI Agent 的云浏览器平台 |
| **AI Image Generator & Editor** | 通过统一接口生成专业 AI 图像，1,300+ 精选提示 |
| **ecap-security-auditor** | 漏洞扫描 |
| **glin-profanity-mcp** | 亵渎检测 |
| **AnChain.AI Data MCP** | AML 合规 |
| **skillsync-mcp** | Claude Code 的安全门控技能管理器 |
| **meyhem-search** | Agent 原生搜索，带反馈驱动排名 |
| **wavestreamer** | AI 预测平台 |
| **defi-mcp** | DeFi MCP 服务器，12 个工具 |
| **x-twitter-scraper** | X API 和 Twitter 爬虫技能，40+ 工具 |

### 3. 教程和指南

#### 入门教程（4 个）

| 教程 | 来源 | 描述 |
|------|------|------|
| [What is OpenClaw?](https://medium.com/@gemQueenx/...) | Medium | 设置 + 功能指南 |
| [OpenClaw for Developers](https://dev.to/mechcloud_academy/...) | DEV.to | 开发者指南 |
| [What is OpenClaw?](https://www.digitalocean.com/...) | DigitalOcean | 综合解释器 |
| [Complete Installation Guide](https://www.aifreeapi.com/...) | AI Free API | WhatsApp、Telegram、Discord 设置 |

#### 高级教程（3 个）

| 教程 | 来源 | 描述 |
|------|------|------|
| [GitHub PR Review Automation](https://zenvanriel.nl/...) | Blog | 自动化代码审查 |
| [Creating AI Agent Workforce](https://o-mega.ai/...) | o-mega | 终极劳动力指南 |
| [Pre-Launch Checklist](https://habr.com/...) | Habr | 安全和配置检查清单 |

### 4. 安全资源

#### 最佳实践

- 在沙盒环境中运行 OpenClaw 以限制爆炸半径
- 限制文件系统访问仅限必要目录
- 将 API 密钥存储在环境变量中 — 永远不要硬编码
- 保持 OpenClaw 更新到最新版本
- 在从第三方来源安装技能之前审查
- 永远不要将 OpenClaw 实例暴露到公共互联网

#### 安全工具

| 项目 | 描述 |
|------|------|
| **aquaman** | 凭证隔离代理 — API 密钥永远不会进入 Agent 进程 |
| **APort Agent Guardrails** | OpenClaw 的预操作授权 |
| **leashed** | AI Agent 的策略引擎、审计日志和紧急停止开关 |

#### 已知风险

- 暴露的实例可能被对手劫持
- 通过摄取数据中的恶意内容进行提示注入
- 配置错误的设置可能泄漏敏感数据或 API 密钥

### 5. 替代方案和对比

| Agent | 类型 | 最适合 |
|-------|------|---------|
| **OpenClaw** | 开源 | 个人 AI 助手，聊天驱动，12+ 消息平台 |
| **Manus AI** | 专有 | 通用 Agent 框架 |
| **OpenManus** | 开源 | 开源 Manus AI 替代方案 |
| **AutoGPT** | 开源 | 自主任务执行 |
| **Open Interpreter** | 开源 | 基于终端的代码执行 |
| **Claude Code** | 专有 | 开发者编码辅助 |
| **Jan.ai** | 开源 | 注重隐私，完全离线 |
| **Agent Zero** | 开源 | 完全本地自主 Agent |
| **Khoj** | 开源 | 开源个人 AI |
| **eesel AI** | SaaS | 商业客户服务 |
## 总结

SamurAIGPT/awesome-openclaw 是一个**社区资源的集大成者**，其价值在于：

1. **系统分类**：200+ 项目按功能分类
2. **持续更新**：标注 NEW 项目，保持列表新鲜
3. **多维度**：项目、教程、文章、安全、对比
4. **社区驱动**：接受社区贡献，共同维护

ClawButler 可以借鉴其**分类体系**、**表格展示**、**安全资源**、**FAQ**等设计，创建 `docs/awesome-clawbutler.md`，汇聚 ClawButler 生态的所有资源，降低用户发现成本，促进社区发展。

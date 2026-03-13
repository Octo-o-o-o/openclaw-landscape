# VoltAgent/awesome-openclaw-skills

## 基本信息

- **GitHub Stars**: 34,650
- **项目地址**: https://github.com/VoltAgent/awesome-openclaw-skills
- **项目定位**: OpenClaw 技能生态的精选目录，从官方 ClawHub 技能注册表中筛选并分类了 5,490+ 个社区构建的技能
- **维护方**: VoltAgent 团队

## 问题与解决方案

### 核心问题

1. **技能发现困难** — OpenClaw 官方技能注册表（ClawHub）包含数千个技能，但缺乏有效的分类和筛选机制，用户难以找到符合需求的技能
2. **生态碎片化** — 社区贡献的技能质量参差不齐，缺乏统一的展示和评估标准
3. **使用场景不明确** — 用户不清楚 OpenClaw 可以应用于哪些具体场景，缺乏灵感来源

### 解决方案

**awesome-openclaw-skills 提供了一个精选的技能目录系统**：

1. **分类体系** — 将 5,490+ 技能按照 30+ 个功能类别组织：
   - AI & LLMs (197 个技能)
   - Browser & Automation
   - Coding Agents & IDEs
   - DevOps & Cloud
   - Git & GitHub
   - Communication (Slack, Discord, Email 等)
   - Data & Analytics
   - Marketing & Sales
   - Health & Fitness
   - Gaming
   - 等等

2. **快速安装** — 提供两种安装方式：
   ```bash
   # ClawHub CLI 一键安装
   clawhub install <skill-slug>

   # 手动安装（复制到技能目录）
   ~/.openclaw/skills/  # 全局
   ~/workspace/.openclaw/skills/  # 工作区级别
   ```

3. **技能元数据展示** — 每个技能条目包含：
   - 技能名称和 slug
   - 简短描述
   - GitHub 链接（指向官方技能仓库）
   - 作者信息

4. **灵感库** — 通过展示真实的社区用例，帮助用户理解 OpenClaw 的应用场景

## 核心架构

### 目录结构

```
awesome-openclaw-skills/
├── README.md                    # 主入口，包含目录和安装说明
├── categories/                  # 分类目录
│   ├── ai-and-llms.md          # AI 和 LLM 相关技能
│   ├── browser-and-automation.md
│   ├── coding-agents-and-ides.md
│   ├── communication.md
│   ├── devops-and-cloud.md
│   ├── git-and-github.md
│   ├── data-and-analytics.md
│   ├── marketing-and-sales.md
│   ├── health-and-fitness.md
│   ├── gaming.md
│   └── ... (30+ 个分类文件)
├── CONTRIBUTING.md              # 贡献指南
└── LICENSE
```

### 技能分类逻辑

**30+ 个功能类别**，覆盖 OpenClaw 生态的主要应用场景：

1. **开发者工具类**：
   - Coding Agents & IDEs
   - Git & GitHub
   - DevOps & Cloud
   - CLI Utilities

2. **生产力工具类**：
   - Browser & Automation
   - Notes & PKM (个人知识管理)
   - Calendar & Scheduling
   - PDF & Documents

3. **通信协作类**：
   - Communication (Slack, Discord, Telegram, Email)
   - Social Media

4. **AI 能力扩展类**：
   - AI & LLMs (197 个技能)
   - Image & Video Generation
   - Voice & Audio

5. **垂直领域类**：
   - Marketing & Sales
   - Health & Fitness
   - Gaming
   - Finance & Crypto

6. **平台集成类**：
   - Apple Apps & Services
   - iOS & macOS Development
   - Media & Streaming

### 技能条目格式

每个技能条目遵循统一格式：

```markdown
- [skill-slug](https://github.com/openclaw/skills/tree/main/skills/author/skill-slug/SKILL.md) - 技能描述
```

示例（AI & LLMs 类别）：

```markdown
- [agent-memory](https://github.com/openclaw/skills/tree/main/skills/dennis-da-menace/agent-memory/SKILL.md) - Persistent memory system for AI agents.
- [agent-orchestrator](https://github.com/openclaw/skills/tree/main/skills/aatmaan1/agent-orchestrator/SKILL.md) - Meta-agent skill for orchestrating complex tasks.
- [claude-usage-checker](https://github.com/openclaw/skills/tree/main/skills/aligurelli/claude-usage-checker/SKILL.md) - Check Claude Code / Claude Max usage limits.
```

## 关键特性

### 1. 精选策略

- **来源可信** — 所有技能均来自 OpenClaw 官方技能注册表（ClawHub），经过社区验证
- **持续更新** — 通过 GitHub Actions 自动同步 ClawHub 的最新技能
- **质量筛选** — 虽然包含 5,490+ 技能，但通过分类和描述帮助用户快速判断质量

### 2. 分类体系

**30+ 个功能类别**，每个类别包含数十到数百个技能：

- **AI & LLMs** (197 个) — Agent 编排、多模型切换、记忆系统、提示词优化
- **Browser & Automation** — 网页自动化、数据抓取、表单填充
- **Coding Agents & IDEs** — 代码生成、重构、测试、文档生成
- **Communication** — Slack、Discord、Telegram、Email、WhatsApp 集成
- **DevOps & Cloud** — Docker、Kubernetes、AWS、GCP、Azure 管理
- **Git & GitHub** — PR 审查、Issue 管理、代码提交自动化

### 3. 安装便利性

**ClawHub CLI 一键安装**：

```bash
clawhub install <skill-slug>
```

**手动安装**（支持全局和工作区级别）：

| 位置 | 路径 |
|------|------|
| 全局 | `~/.openclaw/skills/` |
| 工作区 | `~/workspace/.openclaw/skills/` |

### 4. 社区驱动

- **开放贡献** — 提供 CONTRIBUTING.md 指导社区贡献新技能
- **Discord 社区** — 1,361,559,153,780,195,478 成员的活跃社区
- **持续维护** — 最近更新显示项目保持活跃

### 5. 技能示例（AI & LLMs 类别）

**Agent 编排与协作**：
- `agent-orchestrator` — 元 Agent 技能，用于编排复杂任务
- `agent-registry` — Agent 发现系统，支持 token 高效的 Agent 协作
- `agent-autonomy-kit` — 让 Agent 停止等待提示，实现自主运行

**记忆与上下文管理**：
- `agent-memory` — 持久化记忆系统
- `context-gatekeeper` — 通过总结最近对话保持 token 友好

**多模型支持**：
- `communicate` — 直接从聊天启动本地或 Hugging Face 模型
- `bunni-persona` — 多人格和模型切换工具包

**安全与监控**：
- `agent-sentinel` — Agent 的操作断路器
- `claude-usage-checker` — 检查 Claude Code / Claude Max 使用限额
## 总结

VoltAgent/awesome-openclaw-skills 是 OpenClaw 生态的重要基础设施，通过精选和分类 5,490+ 技能，解决了技能发现和生态碎片化问题。对 ClawButler 而言，其核心价值在于：

1. **模板库设计参考** — 分类体系、元数据标准、安装机制
2. **生态建设策略** — 开放社区、贡献工作流、质量验证
3. **能力映射基础** — 跨平台技能映射、能力路由
4. **成本与审计** — 技能成本追踪、权限管理、沙箱测试
5. **自动化场景** — Runbook 模板、工作流编排

ClawButler 可以借鉴其设计理念，构建跨平台的"Agent Capability Marketplace"，成为异构 Agent 生态的统一能力层。

> https://github.com/hesamsheikh/awesome-openclaw-usecases

# Awesome OpenClaw Use Cases

## 基本信息

- **GitHub**: https://github.com/hesamsheikh/awesome-openclaw-usecases
- **Stars**: 23,013
- **维护者**: Hesam Sheikh (@Hesamation)
- **社区**: Discord (Open Source AI Builders)
- **用例数量**: 36+
- **分类**: 社交媒体、创意与构建、基础设施与 DevOps、生产力、研究与学习、金融与交易

## 问题与解决方案

### 核心问题

**OpenClaw 适配瓶颈**: 用户不缺技能 (skills)，缺的是 **发现 OpenClaw 如何改善生活的具体方式**。

- 官方文档侧重技术实现，缺少场景化用例
- 用户不知道 OpenClaw 能解决哪些实际问题
- 社区最佳实践分散在 Discord / Reddit / X，难以检索
- 新用户学习曲线陡峭，缺少可复制的模板

### 解决方案

**社区驱动的用例库**: 收集真实用户的 OpenClaw 使用场景，提供可复制的配置模板和实现指南。

- **真实性**: 仅接受已验证至少运行一天的用例
- **可操作性**: 每个用例包含痛点、实现方式、配置示例、所需技能
- **安全警告**: 明确标注第三方技能和依赖的安全风险
- **分类清晰**: 按应用场景分为 6 大类，便于检索

## 核心架构

### 用例分类体系

```
awesome-openclaw-usecases/
├── usecases/
│   ├── 社交媒体 (4 个)
│   │   ├── daily-reddit-digest.md
│   │   ├── daily-youtube-digest.md
│   │   ├── x-account-analysis.md
│   │   └── multi-source-tech-news-digest.md
│   │
│   ├── 创意与构建 (5 个)
│   │   ├── overnight-mini-app-builder.md
│   │   ├── youtube-content-pipeline.md
│   │   ├── content-factory.md
│   │   ├── autonomous-game-dev-pipeline.md
│   │   └── podcast-production-pipeline.md
│   │
│   ├── 基础设施与 DevOps (2 个)
│   │   ├── n8n-workflow-orchestration.md
│   │   └── self-healing-home-server.md
│   │
│   ├── 生产力 (18 个)
│   │   ├── autonomous-project-management.md
│   │   ├── multi-channel-customer-service.md
│   │   ├── phone-based-personal-assistant.md
│   │   ├── inbox-declutter.md
│   │   ├── personal-crm.md
│   │   ├── health-symptom-tracker.md
│   │   ├── multi-channel-assistant.md
│   │   ├── project-state-management.md
│   │   ├── dynamic-dashboard.md
│   │   ├── todoist-task-manager.md
│   │   ├── family-calendar-household-assistant.md
│   │   ├── multi-agent-team.md
│   │   ├── aionui-cowork-desktop.md
│   │   ├── custom-morning-brief.md
│   │   ├── meeting-notes-action-items.md
│   │   ├── habit-tracker-accountability-coach.md
│   │   ├── second-brain.md
│   │   └── event-guest-confirmation.md
│   │
│   ├── 研究与学习 (5 个)
│   │   ├── earnings-tracker.md
│   │   ├── knowledge-base-rag.md
│   │   ├── market-research-product-factory.md
│   │   ├── pre-build-idea-validator.md
│   │   └── semantic-memory-search.md
│   │
│   └── 金融与交易 (1 个)
│       └── polymarket-autopilot.md
│
├── README.md (英文)
├── README_CN.md (中文)
├── README_KR.md (韩文)
└── CONTRIBUTING.md
```

### 用例文档结构

每个用例遵循统一模板:

```markdown
# [用例名称]

## Pain Point (痛点)
描述用户面临的具体问题

## What It Does (功能)
解决方案的核心能力列表

## How It Works (实现方式)
1. 步骤 1
2. 步骤 2
3. ...

## Skills You Need (所需技能)
- skill_name_1
- skill_name_2

## Setup (配置)
### AGENTS.md / SOUL.md / config.toml 示例
```toml
[配置内容]
```

## Example Output (示例输出)
实际运行结果截图或文本

## Tips & Gotchas (注意事项)
- 常见问题
- 最佳实践
```

## 关键特性

### 1. 社交媒体自动化

#### Daily Reddit Digest (每日 Reddit 摘要)
- **痛点**: 订阅多个 subreddit，信息过载，无法筛选高质量内容
- **方案**: 基于用户偏好 (关键词、最小点赞数、排除模式) 自动抓取并总结
- **技能**: `reddit_search`, `memory_save`, `schedule`
- **输出**: 每日摘要邮件或 Telegram 消息

#### Daily YouTube Digest (每日 YouTube 摘要)
- **痛点**: 订阅频道过多，错过重要视频
- **方案**: 抓取订阅频道新视频，生成摘要 (标题、时长、关键点)
- **技能**: `youtube_search`, `youtube_transcript`, `schedule`

#### Multi-Source Tech News Digest (多源科技新闻聚合)
- **痛点**: 科技新闻分散在 RSS、Twitter/X、GitHub、HN，手动聚合耗时
- **方案**: 从 109+ 源自动聚合，质量评分，自然语言查询
- **技能**: `rss_fetch`, `twitter_search`, `github_trending`, `web_search`
- **特色**: 支持自然语言过滤 ("Show me AI infra news from last 7 days")

### 2. 创意与构建

#### Overnight Mini-App Builder (目标驱动的自主任务)
- **痛点**: 想法多但执行少，缺少自动化的任务分解和执行
- **方案**: 用户脑暴目标 → Agent 自动生成、调度、完成每日任务 (包括构建惊喜小应用)
- **技能**: `sessions_spawn`, `file_write`, `shell_execute`, `git_commit`
- **示例**: 用户说 "Build a habit tracker"，Agent 隔夜生成 MVP 并部署

#### Autonomous Game Dev Pipeline (自主游戏开发流水线)
- **痛点**: 教育游戏开发周期长，需要协调 backlog、实现、测试、文档、Git 提交
- **方案**: 全生命周期管理，从 backlog 选择到实现、注册、文档、Git 提交，强制 "Bugs First" 策略
- **技能**: `file_read`, `file_write`, `shell_execute`, `git_commit`, `sessions_spawn`
- **特色**: 多 Agent 并行工作 (开发 Agent、测试 Agent、文档 Agent)

#### Podcast Production Pipeline (播客制作流水线)
- **痛点**: 播客制作需要嘉宾调研、大纲撰写、节目笔记、社交媒体推广，手动操作耗时
- **方案**: 自动化全流程 (主题 → 嘉宾调研 → 大纲 → 节目笔记 → 社交媒体素材)
- **技能**: `web_search`, `file_write`, `memory_save`

### 3. 基础设施与 DevOps

#### n8n Workflow Orchestration (n8n 工作流编排)
- **痛点**: Agent 直接调用 API 需要管理凭证，安全风险高
- **方案**: Agent 通过 Webhook 委托给 n8n 工作流，凭证由 n8n 管理，Agent 永不接触
- **技能**: `http_request` (调用 n8n webhook)
- **优势**: 可视化工作流、凭证隔离、可锁定集成

#### Self-Healing Home Server (自愈家庭服务器)
- **痛点**: 家庭服务器 (NAS、Pi-hole、Home Assistant) 故障需要手动 SSH 修复
- **方案**: 常驻基础设施 Agent，SSH 访问，自动化 cron 任务，自愈能力
- **技能**: `shell_execute`, `ssh_execute`, `schedule`, `memory_recall`
- **示例**: 检测到 Docker 容器停止 → 自动重启 → 记录日志 → Telegram 通知

### 4. 生产力

#### Autonomous Project Management (自主项目管理)
- **痛点**: 传统编排模式 (orchestrator) 成为瓶颈，主 Agent 成为交通警察
- **方案**: 去中心化协调，子 Agent 通过共享 `STATE.yaml` 文件自主工作
- **核心模式**:
  ```yaml
  # STATE.yaml
  tasks:
    - id: homepage-hero
      status: in_progress
      owner: pm-frontend
    - id: api-auth
      status: done
      owner: pm-backend
    - id: content-migration
      status: blocked
      blocked_by: api-auth
  ```
- **技能**: `sessions_spawn`, `sessions_send`, `file_read`, `file_write`, `git_commit`
- **优势**: 并行执行、无编排开销、自文档化

#### Multi-Agent Specialized Team (多 Agent 专业团队)
- **痛点**: 单个 Agent 上下文窗口有限，无法同时处理策略、开发、营销、业务分析
- **方案**: 多个专业 Agent (Milo 策略、Josh 业务、Marketing 营销、Dev 开发)，共享内存，单一 Telegram 群组控制
- **配置示例**:
  ```text
  ## SOUL.md — Milo (Strategy Lead)
  Model: Claude Opus
  Channel: Telegram (responds to @milo)
  Daily tasks:
  - 8:00 AM: Review overnight agent activity
  - 6:00 PM: End-of-day recap
  ```
- **技能**: `memory_save`, `memory_recall`, `schedule`, `telegram_send`

#### Phone-Based Personal Assistant (电话个人助理)
- **痛点**: 开车、做饭时无法使用键盘，需要免提语音助理
- **方案**: 通过电话呼叫访问 OpenClaw，语音查询日历、Jira、网页搜索
- **技能**: `voice_call`, `calendar_read`, `jira_search`, `web_search`
- **实现**: Twilio / Vonage + OpenClaw webhook

#### Second Brain (第二大脑)
- **痛点**: 想法、笔记、链接分散在多个工具，难以检索
- **方案**: 发送任何内容到 Bot 自动保存，通过自定义 Next.js 仪表板搜索所有记忆
- **技能**: `memory_save`, `memory_recall`, `semantic_search`
- **特色**: 向量搜索 + 关键词搜索混合检索

#### Event Guest Confirmation (活动嘉宾确认)
- **痛点**: 手动逐个电话确认活动嘉宾出席，耗时且容易遗漏
- **方案**: AI 语音电话逐个呼叫嘉宾列表，确认出席，收集备注，生成汇总报告
- **技能**: `voice_call`, `memory_save`, `file_write`
- **实现**: Bland.ai / Vapi.ai + OpenClaw

### 5. 研究与学习

#### Personal Knowledge Base (RAG) (个人知识库)
- **痛点**: 收藏的文章、推文、URL 无法语义检索
- **方案**: 拖拽 URL / 推文到聊天，自动构建可搜索知识库
- **技能**: `web_scrape`, `memory_save`, `semantic_search`
- **技术**: RAG (Retrieval-Augmented Generation)

#### Market Research & Product Factory (市场调研与产品工厂)
- **痛点**: 不知道用户真实痛点，盲目开发产品
- **方案**: 使用 "Last 30 Days" 技能挖掘 Reddit 和 X 的真实痛点，OpenClaw 构建 MVP
- **技能**: `reddit_search`, `twitter_search`, `file_write`, `shell_execute`
- **流程**: 痛点挖掘 → 需求验证 → MVP 开发 → 用户测试

#### Pre-Build Idea Validator (构建前创意验证)
- **痛点**: 开发前不知道市场是否已饱和
- **方案**: 自动扫描 GitHub、HN、npm、PyPI、Product Hunt，拥挤则停止，空白则继续
- **技能**: `github_search`, `npm_search`, `pypi_search`, `web_search`
- **输出**: 竞品分析报告 + 建议 (继续 / 停止 / 差异化)

#### Semantic Memory Search (语义内存搜索)
- **痛点**: OpenClaw 的 Markdown 内存文件只能关键词搜索
- **方案**: 为内存文件增加向量驱动的语义搜索，混合检索，自动同步
- **技能**: `memory_recall`, `semantic_search`, `embedding_generate`
- **技术**: 向量数据库 (Pinecone / Weaviate / Qdrant) + 混合检索

### 6. 金融与交易

#### Polymarket Autopilot (预测市场自动交易)
- **痛点**: 手动交易预测市场耗时，缺少回测和策略分析
- **方案**: 自动化纸面交易，回测，策略分析，每日绩效报告
- **技能**: `http_request` (Polymarket API), `memory_save`, `schedule`
- **注意**: 仅纸面交易，不接受加密货币相关用例
# ClawButler Runbook 状态文件
runbook_id: deploy-v2.5
status: in_progress
steps:
  - id: build-api
    status: done
    owner: runbook-backend
    output: "docker.io/clawbutler/api:v2.5"
  - id: run-migrations
    status: in_progress
    owner: runbook-db
  - id: deploy-web
    status: blocked
    blocked_by: run-migrations
```

**ClawButler 实现**:
- Runbook 执行器增加 `state_backend` 配置 (file / redis / postgres)
- 支持多 Runbook 并行执行，通过状态文件协调
- Web UI 实时展示状态文件 (类似 GitHub Actions 的 workflow 视图)

### 5. 自愈基础设施

**Self-Healing Home Server 模式**:
- **核心**: 常驻 Agent + SSH 访问 + 自动化 cron 任务 + 自愈能力
- **ClawButler 应用**:
  - Runbook 增加 **Self-Healing** 触发类型 (除了 manual / schedule / webhook / event)
  - 配置示例:
    ```yaml
    trigger:
      type: self_healing
      check_interval: 5m
      condition: "docker ps | grep api | wc -l == 0"
      action: "docker compose up -d api"
    ```
  - 应用场景:
    - API 容器停止 → 自动重启
    - 数据库连接池耗尽 → 自动重启 PgBouncer
    - 磁盘空间不足 → 自动清理日志

### 6. 多渠道集成

**Phone-Based Personal Assistant 模式**:
- **核心**: 通过电话呼叫访问 Agent
- **ClawButler 应用**:
  - 增加 **Voice Channel** (Twilio / Vonage)
  - 用户通过电话查询 Agent 状态、触发 Runbook、查看成本报告
  - 应用场景: 运维人员在通勤时通过电话触发紧急部署

**Multi-Channel Customer Service 模式**:
- **核心**: 统一 WhatsApp、Instagram、Email、Google Reviews 到单一 AI 收件箱
- **ClawButler 应用**:
  - Federation 增加 **Customer Service Router**
  - 自动将客户消息路由到合适的 Agent (技术支持 Agent、销售 Agent、投诉处理 Agent)
  - 24/7 自动响应 + 人工接管机制

### 7. 知识库与 RAG

**Personal Knowledge Base (RAG) 模式**:
- **核心**: 拖拽 URL / 推文到聊天，自动构建可搜索知识库
- **ClawButler 应用**:
  - 增加 **Knowledge Base** 模块
  - 用户上传文档 (PDF、Markdown、URL) → 自动向量化 → 语义搜索
  - 应用场景:
    - Agent 配置历史搜索 ("Show me all agents using GPT-4")
    - Runbook 执行日志搜索 ("Find all failed deployments last week")
    - 审计日志搜索 ("Who modified the billing config?")

**Semantic Memory Search 模式**:
- **核心**: 向量搜索 + 关键词搜索混合检索
- **ClawButler 实现**:
  - PostgreSQL + pgvector 扩展
  - 混合检索算法: `score = 0.7 * vector_similarity + 0.3 * keyword_match`

### 8. 市场调研与验证

**Pre-Build Idea Validator 模式**:
- **核心**: 构建前自动扫描市场，拥挤则停止，空白则继续
- **ClawButler 应用**:
  - Verified Templates 部署前增加 **Market Validation** 步骤
  - 自动扫描 GitHub / Docker Hub / npm，检查是否已有类似模板
  - 输出: 竞品分析报告 + 差异化建议

### 9. 安全警告机制

**awesome-openclaw-usecases 的安全警告**:
> OpenClaw skills and third-party dependencies referenced here may have critical security vulnerabilities. Many use cases link to community-built skills, plugins, and external repos that have **not been audited by the maintainer of this list**. Always review skill source code, check requested permissions, and avoid hardcoding API keys or credentials. You are solely responsible for your own security.

**ClawButler 应用**:
- Template Gallery 增加 **Security Badge**:
  - ✅ Official (官方审计)
  - ⚠️ Community (社区贡献，未审计)
  - 🚫 Experimental (实验性，高风险)
- 部署前强制显示安全警告弹窗
- 模板审计报告: 依赖包漏洞、敏感信息泄露、权限请求

### 10. 贡献指南

**awesome-openclaw-usecases 的贡献要求**:
> Please only submit usecases you have already worked with and verified that works (at least for a day). We value real ideas that make our lives actually better, not worse!

**ClawButler 应用**:
- Template Gallery 贡献要求:
  - 必须提供演示视频或截图
  - 必须通过安全审计
  - 必须包含完整的配置示例和部署指南
  - 必须至少运行 7 天无故障
- 社区投票机制: 用户可为模板点赞 / 评论 / 报告问题

## 总结

awesome-openclaw-usecases 的核心价值在于 **场景化用例** + **社区驱动** + **可复制模板**。对于 ClawButler (Agent 控制平面) 而言，最有价值的借鉴点包括:

1. **用例驱动的产品设计**: 建立 Use Cases Gallery，按行业 / 角色分类
2. **模板市场**: 社区贡献 + 安全审计 + 官方认证
3. **多 Agent 协作模式**: 去中心化协调 (STATE.yaml) + 专业团队 (共享内存)
4. **状态管理模式**: Runbook 状态文件 + 并行执行 + 实时展示
5. **自愈基础设施**: Self-Healing 触发类型 + 自动化修复
6. **多渠道集成**: Voice Channel + Customer Service Router
7. **知识库与 RAG**: 语义搜索 + 混合检索 + 审计日志搜索
8. **市场调研与验证**: 模板部署前市场扫描 + 竞品分析
9. **安全警告机制**: Security Badge + 审计报告 + 部署前警告
10. **贡献指南**: 演示视频 + 安全审计 + 社区投票

这些特性可显著提升 ClawButler 的 **用户体验**、**社区活跃度** 和 **生态丰富度**，同时降低新用户的学习曲线。

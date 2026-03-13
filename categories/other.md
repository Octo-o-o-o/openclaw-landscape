# Other

> Projects that don't fit neatly into other categories.
> 未归入其他分类的项目。

**9 projects** | [Back to overview](../README.md)

---

### nanobot

[HKUDS/nanobot](https://github.com/HKUDS/nanobot) | Stars: 32,020
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 功能强大但代码复杂（数万行），难以理解、修改和扩展。nanobot 用 ~4,000 行核心代码实现 OpenClaw 核心功能（99% 代码量减少），专注轻量化、研究友好、快速迭代。

**Features:** 快速启动, 多模态支持, Prompt caching, 安全加固, 研究友好

---

### openimsdk/open-im-server

[openimsdk/open-im-server](https://github.com/openimsdk/open-im-server) | Stars: 15,775 | Go
Researched: 2026-03-11 | Updated: 2026-03-13

1. 开发者工具而非终端产品 — 不是直接安装使用的独立聊天应用，而是提供 SDK 和 Server 供开发者集成到自己的应用中 2. 企业级 IM 能力 — 支持海量用户场景（十万级超大群组、千万级用户、百亿级消息） 3. 灵活的业务扩展 — 通过 REST API 和 Webhooks 机制，让业务系统能够深度定制和扩展 IM 功能

---

### OpenViking

[volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Stars: 5,671 | Python
Researched: 2026-03-11 | Updated: 2026-03-13

Agent 开发中上下文管理碎片化（记忆在代码、资源在向量库、技能分散），传统 RAG 平面存储缺乏全局视图且检索效果差。OpenViking 是字节跳动开源的 Agent 专用上下文数据库，用文件系统范式统一管理记忆/资源/技能，支持分层加载、递归检索、可视化轨迹和自动会话压缩。

**Features:** 文件系统范式, 三层上下文加载, 目录递归检索, 自动会话管理, 多语言 SDK, AGFS 核心扩展

---

### secure-openclaw

[ComposioHQ/secure-openclaw](https://github.com/ComposioHQ/secure-openclaw) | Stars: 1,358
Researched: 2026-03-11 | Updated: 2026-03-13

用户需要 24x7 可用的 AI 助手，但缺乏跨平台消息接入、工具访问控制和应用集成能力。Secure OpenClaw 通过 Composio Tool Router 提供安全的工具访问、持久化内存、定时提醒和 500+ 应用集成，在 WhatsApp、Telegram、Signal、iMessage 等平台上运行。

**Features:** 支持 WhatsApp、Telegram、Signal、iMessage 等多消息平台, Composio Tool Router 提供 500+ 应用集成（Gmail、Slack、GitHub 等）, 工具审批机制, 持久化内存系统, 定时提醒和任务调度, 支持 Claude Code 和 Opencode 两种 AI 提供商

---

### nof1.ai

[195440/nof1.ai](https://github.com/195440/nof1.ai) | Stars: 569
Researched: 2026-03-11 | Updated: 2026-03-13

传统量化交易系统依赖硬编码规则，缺乏自主学习和决策能力。nof1.ai 是一个 AI 驱动的加密货币自动交易系统，基于 VoltAgent 框架构建，通过赋予 AI（DeepSeek V3.2/Grok4/Claude）完全的市场分析和交易决策自主权，实现真正的智能化交易，采用最小人工干预的设计理念。

**Features:** 基于 VoltAgent 框架的 Agent 编排与管理, 支持 OpenAI 兼容 API（OpenRouter、OpenAI、DeepSeek 等）, 集成 Gate.io 和 OKX 交易所（测试网 + 正式网）, LibSQL（SQLite）本地数据持久化（账户历史、交易信号、Agent 决策）, AI 自主市场数据分析、仓位管理和交易执行决策, 摒弃硬编码规则

---

### pjasicek/OpenClaw

[pjasicek/OpenClaw](https://github.com/pjasicek/OpenClaw) | Stars: 448 | 未明确标注（开源）
Researched: 2026-03-11 | Updated: 2026-03-13

注意：这个项目与 OpenClaw AI Agent 框架完全无关。这是一个 1997 年经典平台游戏《Captain Claw》的 C++ 重新实现项目。

---

### EQtreader

[kevin-liu-robot/EQtreader](https://github.com/kevin-liu-robot/EQtreader) | Stars: 54 | Python
Researched: 2026-03-11 | Updated: 2026-03-13

量化交易系统需要集成行情数据获取、交易执行、持仓管理等多个模块，手动开发成本高且容易出错。该项目基于 easyquotation、easytrader、easyquant 等开源库，为 OpenClaw 提供量化交易 Skill，支持同花顺客户端自动化交易和多数据源行情获取。

**Features:** 交易客户端集成, 多数据源行情, 32 位 Python 兼容, OCR 识别支持, 远程部署指南, 数据源扩展

---

### market-sentry

[ZiyaZhang/market-sentry](https://github.com/ZiyaZhang/market-sentry) | Stars: 31
Researched: 2026-03-11 | Updated: 2026-03-13

投资者需要同时监控 A 股、美股、加密货币等多资产类别，手动跟踪异动和生成日报耗时且容易遗漏。该 Skill 提供多市场统一监控，支持实时异动检测（价格阈值、Z-score 统计异常、成交量激增）、每日简报生成和飞书推送，并通过 EvidencePack 机制确保数据可审计。

**Features:** 多市场支持, 三层异动检测, 叙事式简报, 飞书双模式推送, EvidencePack 审计, 静默监控模式

---

### openclaw-skill-snowtrace

[chenmuwen0930/snowtrace](https://github.com/chenmuwen0930/snowtrace) | Stars: 27
Researched: 2026-03-11 | Updated: 2026-03-13

投资者需要手动浏览雪球平台关注的 KOL 动态和自选股行情，信息分散且耗时。该 Skill 通过 Playwright + stealth 绕过雪球 WAF，自动抓取大 V 原创动态和自选股实时行情，生成五段式投资分析报告（大 V 观点摘要 → 行情概览 → 关联分析 → 投资建议 → 免责声明）。

**Features:** 反爬虫绕过, 多市场支持, 持仓盈亏计算, 结构化输出, 混合抓取策略, 环境变量配置

---

# China Ecosystem

> Chinese-language resources, IM integrations (Feishu, DingTalk, WeChat), and localized tools.
> 中文资源、IM 集成（飞书、钉钉、企业微信）及本地化工具。

**19 projects** | [Back to overview](../README.md)

---

### Clawdbot-Feishu

[m1heng/clawdbot-feishu](https://github.com/m1heng/clawdbot-feishu) | Stars: 4,189
Researched: 2026-03-11 | Updated: 2026-03-13

Clawdbot-Feishu 解决了 OpenClaw 在企业协作场景的接入问题。通过飞书（Feishu/Lark）插件，将 OpenClaw Agent 能力无缝集成到企业 IM 平台，支持私聊、群聊 @提及、消息订阅、文件上传等企业级交互场景，降低企业用户使用 AI Agent 的门槛。

**Features:** 完整飞书集成, 工具权限体系, 灵活配置, 企业级权限, 中文社区支持, 结构化反馈

---

### OpenClaw-Docker-CN-IM

[justlovemaki/docker-cn-im](https://github.com/justlovemaki/docker-cn-im) | Stars: 3,124
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 原生不支持中国主流 IM 平台（飞书/钉钉/QQ/企业微信），部署配置复杂。本项目提供预装中国 IM 插件的 Docker 镜像，开箱即用，通过环境变量配置各平台凭证，支持数据持久化，内置 OpenCode AI / Playwright / 中文 TTS。

**Features:** 开箱即用, 中国 IM 全覆盖, 灵活配置, 多账号支持, 推荐搭配 AIClient-2-API, 推荐模型

---

### OpenClawChineseTranslation

[1186258278/ChineseTranslation](https://github.com/1186258278/ChineseTranslation) | Stars: 2,934
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 官方版本为英文界面，对中文用户存在使用门槛。该项目通过每小时自动同步官方更新并进行深度汉化，提供 CLI 命令行和 Dashboard 网页控制台的全中文界面，降低中文用户的使用成本。

**Features:** 每小时自动同步官方更新, CLI 和 Dashboard 全中文界面, 提供一键安装脚本（macOS/Linux/Windows WSL2）, 配套生态工具, 完整的安装、配置、故障排查文档, 支持 Docker 部署和守护进程模式

---

### awesome-openclaw-skills-zh

[clawdbot-ai/awesome-skills-zh](https://github.com/clawdbot-ai/awesome-skills-zh) | Stars: 2,902
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 官方技能库为英文，且技能分散难以查找。该项目翻译官方技能库并按场景分类整理（办公自动化、系统工具、开发运维等），支持中文自然语言调用，降低中文用户的技能发现和使用成本。

**Features:** 翻译自 Clawdbot 官方技能库, 按场景分类, 支持中文自然语言调用, 涵盖邮件管理、日历日程、文档处理、CRM、代码开发、CI/CD、数据库管理等 80,000+ 社区技能, 提供每个技能的核心功能说明和官方链接

---

### BytePioneer-AI/openclaw-china

[BytePioneer-AI/openclaw-china](https://github.com/BytePioneer-AI/openclaw-china) | Stars: 2,790 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 原生不支持中国主流即时通讯平台（钉钉、企业微信、QQ、飞书），导致国内用户无法将 AI Agent 接入企业内部沟通工具，限制了 OpenClaw 在中国市场的应用场景。

---

### xianyu110/awesome-openclaw-tutorial

[xianyu110/awesome-tutorial](https://github.com/xianyu110/awesome-tutorial) | Stars: 2,179 | Shell
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 作为强大的 AI Agent 平台，存在以下痛点：

**Features:** Gateway 认证现在要求显式设置 `gateway.auth.mode`, 必须明确选择 `token` 或 `password` 认证方式, 如果从旧版本升级且没有配置认证, 工具权限和聊天能力隔离, 升级后 OpenClaw 只能聊天不能干活（文件管理、命令执行等工具功能全部失效）

---

### OpenClaw 101 — 7天学习路径与资源聚合站

[mengjian-github/openclaw101](https://github.com/mengjian-github/openclaw101) | Stars: 2,011 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

1. 中文资源分散 — OpenClaw 官方文档以英文为主，中文教程散落在阿里云、腾讯云、B站、CSDN、博客园等平台，新手难以系统化学习 2. 学习路径不清晰 — 从认识 OpenClaw 到实际部署、接入平台、开发技能，缺乏结构化的进阶指南 3. 资源质量参差不齐 — 社区教程质量不一，缺少权威筛选和分类 4. 场景化技能推荐缺失 — 用户不知道针对特定场景（如企业协作、个人助理、内容创作）应该安装哪些技能

**Features:** 35+ 优质资源, 多维度筛选, 来源标注, 精选推荐

---

### DingTalk OpenClaw Connector

[DingTalk-Real-AI/connector](https://github.com/DingTalk-Real-AI/connector) | Stars: 1,603
Researched: 2026-03-11 | Updated: 2026-03-13

解决了钉钉企业用户无法直接使用 OpenClaw Gateway 的集成问题。通过 Stream 模式连接钉钉机器人和 DEAP Agent 到 OpenClaw Gateway，支持 AI Card 流式响应、会话持久化和富媒体消息，让企业用户在钉钉内无缝使用 AI Agent 能力。

**Features:** AI Card 流式响应, 富媒体支持, 钉钉文档 API, 异步模式, Markdown 表格转换

---

### Awesome OpenClaw Usecases ZH

[AlexAnys/awesome-usecases-zh](https://github.com/AlexAnys/awesome-usecases-zh) | Stars: 1,553
Researched: 2026-03-11 | Updated: 2026-03-13

解决了 OpenClaw 普及的核心瓶颈：不是技术门槛，而是用户不知道"能用 AI Agent 做什么"。通过 40 个经过验证的真实用例（含国内生态适配），手把手教用户用 AI 自动化工作与生活，降低从"知道 OpenClaw"到"用起来"的认知鸿沟。

**Features:** 40 个真实用例, 新手友好, 可复制 Prompt, 国内适配方案, 安全提醒

---

### openclaw-wechat

[freestylefly/openclaw-wechat](https://github.com/freestylefly/openclaw-wechat) | Stars: 1,345
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 缺乏微信接入能力，无法覆盖中国用户的主要通信平台。该项目通过 WeChat Channel Plugin 实现 OpenClaw 与个人微信的稳定连接，支持私聊、群聊、文本、图片等消息类型，解决中国用户的 AI 助手接入问题。

**Features:** 支持私聊和群聊（@机器人）, 支持文本、图片消息, 二维码登录流程, 多账号支持（工作号、个人号）, Webhook 配置支持云服务器部署, 支持 iPad 和 Mac 设备类型

---

### openclaw-channel-dingtalk

[soimy/channel-dingtalk](https://github.com/soimy/channel-dingtalk) | Stars: 1,267
Researched: 2026-03-11 | Updated: 2026-03-13

企业用户需要在钉钉内使用 AI 助手，但 OpenClaw 缺乏钉钉接入能力。该项目通过 DingTalk Channel Plugin 使用 Stream 模式（无需公网 IP）实现钉钉企业内部机器人接入，支持私聊、群聊、多种消息类型和互动卡片。

**Features:** Stream 模式, 支持私聊和群聊（@机器人）, 支持文本、图片、语音（自带识别）、视频、文件、钉钉文档/钉盘文件卡片, 引用消息支持, Markdown 回复和互动卡片（支持流式更新）, 进程级内存态

---

### xianyu110/clawbot

[xianyu110/clawbot](https://github.com/xianyu110/clawbot) | Stars: 856 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

1. 官方文档英文为主：缺乏系统的中文安装教程 2. 配置复杂度高：多个配置文件、环境变量、认证方式让新手困惑 3. API 中转配置困难：国内用户需要使用中转 API，但配置方式不明确 4. 常见错误频发：环境变量无效、配置格式错误、服务启动失败等问题

---

### yeuxuan/openclaw-docs

[yeuxuan/openclaw-docs](https://github.com/yeuxuan/openclaw-docs) | Stars: 533 | MIT
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 官方文档以英文为主，中文用户面临以下困难：

---

### openclaw-feishu

[AlexAnys/openclaw-feishu](https://github.com/AlexAnys/openclaw-feishu) | Stars: 522
Researched: 2026-03-11 | Updated: 2026-03-13

飞书用户接入 OpenClaw 存在配置复杂、文档分散、国内生态适配不足的痛点。本项目提供保姆级配置指南、常见问题排查清单、以及飞书官方插件与 OpenClaw 内置插件的对比选型建议，降低非技术用户的接入门槛。

**Features:** 三种插件方案对比, 从零配置教程, 常见问题排查, 国内生态适配, 迁移指南, 进阶配置参考

---

### openclaw-plugin-wecom

[sunnoy/wecom-plugin](https://github.com/sunnoy/wecom-plugin) | Stars: 433
Researched: 2026-03-11 | Updated: 2026-03-13

企业微信接入 OpenClaw 需要处理多账号管理、动态 Agent 隔离、配额感知等企业级需求。本插件基于官方 WebSocket 长连接骨架，提供多账号管理、动态 Agent 路由、Agent API/Webhook 增强出站、指令白名单、配额感知等特性，满足企业级部署需求。

**Features:** 多账号管理, 动态 Agent 路由, Agent API 增强出站, Webhook Bot 群通知, 指令白名单, 配额感知

---

### WeCom OpenClaw Plugin

[11haonb/wecom-plugin](https://github.com/11haonb/wecom-plugin) | Stars: 95 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 缺乏与企业微信（WeCom）的原生集成，无法通过企业通讯工具远程控制 Agent。该插件通过 WeCom 应用接口实现双向通信，用户可通过企业微信发送消息控制 PC 浏览器和执行 AI 任务。

**Features:** 双向消息通道, 富媒体支持, 工具调用集成, 回调服务器, TypeScript 实现, 快速配置

---

### awesome-openclaw-skills-CN

[AIPMAndy/awesome-skills-CN](https://github.com/AIPMAndy/awesome-skills-CN) | Stars: 51
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 官方技能注册表（ClawHub）包含 5,705 个技能，但存在大量垃圾内容、重复条目和非中文开发者友好的描述。该项目人工整理 2,868 个高质量技能，按 18 个分类组织，并提供国产大模型接入指南和中文开发者推荐技能列表。

**Features:** 人工筛选质量保证, 国产模型接入指南, 中文生态推荐, 18 个分类体系, 安全提示, 社区共建机制

---

### wemp-operator

[IanShaw027/wemp-operator](https://github.com/IanShaw027/wemp-operator) | Stars: 46
Researched: 2026-03-11 | Updated: 2026-03-13

微信公众号运营需要手动采集热点、分析数据、管理评论，重复劳动多且效率低。wemp-operator 通过 70 个微信公众号 API 集成 + 20+ 数据源（Hacker News/V2EX 等）+ AI 智能回复，实现内容采集、数据分析、互动管理的全流程自动化，支持自然语言交互（如"帮我采集今天的 AI 热点"）。

**Features:** 三大工作流, 70 个 API 集成, 20+ 数据源, 自然语言触发, AI 智能回复, ClawHub 一键安装

---

### dingtalk-ai-table

[aliramw/dingtalk-ai-table](https://github.com/aliramw/dingtalk-ai-table) | Stars: 46
Researched: 2026-03-11 | Updated: 2026-03-13

钉钉 AI 表格（多维表）的 API 操作复杂且文档分散，手动调用效率低。该项目通过 MCP tools 封装 19 个钉钉 AI 表格 API，提供批量字段新增、批量记录导入、安全测试等脚本，支持新版 ID 体系（baseId/tableId/fieldId/recordId），实现 21/21 测试通过的生产级质量。

**Features:** 新版 API 全覆盖, 批量操作脚本, ID 体系迁移, 安全与构造测试, 环境变量配置, 错误码文档

---

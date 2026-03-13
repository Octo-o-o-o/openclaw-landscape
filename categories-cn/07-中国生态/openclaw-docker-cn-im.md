> https://github.com/justlovemaki/docker-cn-im

# OpenClaw-Docker-CN-IM (3,126 stars)

## 问题与解决方案
OpenClaw 原生不支持中国主流 IM 平台（飞书/钉钉/QQ/企业微信），部署配置复杂。本项目提供预装中国 IM 插件的 Docker 镜像，开箱即用，通过环境变量配置各平台凭证，支持数据持久化，内置 OpenCode AI / Playwright / 中文 TTS。

## 核心架构
- **Docker 镜像**：基于 OpenClaw 官方镜像，预装飞书/钉钉/QQ/企业微信插件
- **环境变量配置**：统一通过 `.env` 文件配置 AI 模型和 IM 平台凭证
- **配置同步脚本**：启动时自动将环境变量同步到 OpenClaw 配置文件
- **数据持久化**：挂载 `~/.openclaw` 目录，保存配置和 workspace
- **多协议支持**：OpenAI 协议和 Claude 协议两种 API 格式
- **飞书官方插件**：集成飞书官方团队插件 CLI 工具（`feishu-plugin-onboard`），支持日历/任务/多维表格等 OAPI 能力

## 关键特性
- 开箱即用：`docker-compose up -d` 一键启动
- 中国 IM 全覆盖：飞书（官方插件 + 旧版内置）/ 钉钉 / QQ / 企业微信
- 灵活配置：最小配置仅需 `MODEL_ID` / `BASE_URL` / `API_KEY` 三个参数
- 多账号支持：企业微信支持多账号配置，飞书支持 `accounts.main` 到 `default` 自动迁移
- 推荐搭配 AIClient-2-API：将 AI 客户端转换为标准 API，实现无限 Token 调用
- 推荐模型：`gemini-3-flash-preview`（1M tokens 上下文，快速响应，高性价比）

<!-- lastCommit: 6a7050b -->

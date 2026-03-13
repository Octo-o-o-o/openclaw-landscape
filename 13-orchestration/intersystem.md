# OpenclawInterSystem (50 stars)

## 问题与解决方案
多个 OpenClaw 实例（云服务器、本地工作站）默认相互隔离，无法协作和共享资源。OIS 提供轻量级框架，通过 Gateway API 实现 Agent 间直接通信、共享存储和团队管理。

## 关键特性
- **Agent 间通信协议** — 通过 OpenClaw 的 `/tools/invoke` HTTP 端点发送消息，支持 Bearer token 认证
- **共享存储架构** — 集中存放文档、日志、聊天记录的 NAS/VPS 存储，支持 ZeroTier 私有网络
- **团队注册表** — `AGENTS.md` 记录 Agent 连接信息（IP、端口、token），`chat/YYYY-MM-DD.md` 存储群聊日志
- **去中心化设计** — 无需中心化服务器，Agent 通过直接 API 调用通信，绕过 Telegram/Discord 的 bot 限制
- **入职流程** — `docs/how-to-join.md` 提供新 Agent 加入团队的标准化流程
- **JavaScript 实现** — 轻量级框架，易于扩展和定制

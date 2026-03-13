> https://github.com/sunnoy/wecom-plugin

# openclaw-plugin-wecom (434 stars)

## 问题与解决方案

企业微信接入 OpenClaw 需要处理多账号管理、动态 Agent 隔离、配额感知等企业级需求。本插件基于官方 WebSocket 长连接骨架，提供多账号管理、动态 Agent 路由、Agent API/Webhook 增强出站、指令白名单、配额感知等特性，满足企业级部署需求。

## 关键特性

- **多账号管理** — 多 Bot 独立配置、共享字段继承，支持企业内多部门/多场景的 Agent 部署
- **动态 Agent 路由** — 按用户/群自动隔离会话与工作区，支持 Workspace 模板自动复制引导文件（`AGENTS.md` 等）
- **Agent API 增强出站** — 自建应用主动发送文本/图片/文件，支持部门（`party:`）/标签（`tag:`）寻址
- **Webhook Bot 群通知** — 命名 webhook 映射，支持 markdown/图片/文件格式
- **指令白名单** — 限制普通用户可执行的 slash 命令，管理员绕过白名单和动态 Agent 路由
- **配额感知** — 被动回复 24h 窗口 + 主动发送额度追踪与告警，防止超限
- **Pending Reply 重试** — WebSocket 断连后自动通过 Agent API 补发未送达回复
- **Reasoning 流式节流** — 800ms 节流防止 SDK 队列溢出
- **入站增强** — 图文混排拆解、语音转写、引用消息上下文透传、消息去重（reqId + msgId）

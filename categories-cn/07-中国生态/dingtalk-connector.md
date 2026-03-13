> https://github.com/DingTalk-Real-AI/connector

# DingTalk OpenClaw Connector (1,604 stars)

## 问题与解决方案
解决了钉钉企业用户无法直接使用 OpenClaw Gateway 的集成问题。通过 Stream 模式连接钉钉机器人和 DEAP Agent 到 OpenClaw Gateway，支持 AI Card 流式响应、会话持久化和富媒体消息，让企业用户在钉钉内无缝使用 AI Agent 能力。

## 核心架构
- **Stream WebSocket 连接** — 钉钉消息通过 Stream 模式推送到 Connector，无需公网 IP 和 webhook 配置
- **HTTP SSE 流式转发** — Connector 调用 Gateway `/v1/chat/completions` 接口，将 SSE chunk 实时转换为钉钉 AI Card streaming API
- **会话与记忆隔离** — 按单聊/群聊/群维度分别维护 session 和 memory，支持跨会话记忆共享配置
- **多 Agent 路由** — 一个 Connector 实例可连接多个 Agent，不同钉钉机器人绑定不同 Agent 实现角色分工

## 关键特性
- **AI Card 流式响应** — 打字机效果实时显示 AI 回复，提升用户体验
- **富媒体支持** — 接收 JPEG/PNG 图片、解析 .docx/.pdf/.xlsx 等文件附件、发送音频消息
- **钉钉文档 API** — 支持创建、追加、搜索、列举钉钉文档，实现知识库集成
- **异步模式** — 立即回执用户消息，后台处理任务后主动推送结果，适合耗时任务
- **Markdown 表格转换** — 自动将 Markdown 表格转换为钉钉支持的文本格式

<!-- lastCommit: 6a7050b -->

# Crabwalk (859 stars)

## 问题与解决方案

Crabwalk 解决了 OpenClaw Agent 运行时"黑盒不可观测"的痛点。通过 WebSocket 连接 OpenClaw Gateway（`ws://127.0.0.1:18789`），实时订阅 Agent 会话事件流，将思考状态、工具调用、响应链以 ReactFlow 节点图可视化，支持跨 WhatsApp/Telegram/Discord/Slack 多平台同时监控，提供会话过滤、动作追踪、工作区文件浏览等实时伴侣监控能力。

## 关键特性

- **实时节点图可视化** — ReactFlow 渲染 Agent 会话和动作链，展开节点可查看工具参数和 payload
- **多平台统一监控** — 同时监控 WhatsApp/Telegram/Discord/Slack 上的 Agent 活动，单一界面聚合展示
- **WebSocket 事件流订阅** — 连接 OpenClaw Gateway（默认 `ws://127.0.0.1:18789`），实时接收会话事件（思考/工具调用/响应）
- **会话过滤与搜索** — 按平台筛选、按接收者搜索，快速定位目标会话
- **工作区文件浏览** — 挂载 `~/.openclaw/workspace` 到容器，实时查看 Agent 操作的文件
- **CLI + Docker 双模式** — 原生 CLI（`crabwalk start --daemon`）或 Docker 部署（`docker run -p 3000:3000`），自动检测 Gateway token（`~/.openclaw/openclaw.json`）
- **QR 码快速访问** — 启动时显示 QR 码，手机扫码即可打开监控界面（需 `qrencode`）

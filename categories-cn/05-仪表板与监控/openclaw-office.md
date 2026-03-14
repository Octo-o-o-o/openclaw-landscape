> https://github.com/WW-AI-Lab/openclaw-office

# OpenClaw Office (210 stars)

## 问题与解决方案

OpenClaw Multi-Agent 系统缺乏可视化的协作监控界面，难以直观理解 Agent 之间的消息流和工作状态。OpenClaw Office 通过 2D/3D 虚拟办公室场景渲染 Agent 工作状态、协作链接、工具调用、资源消耗，并提供全功能控制台进行系统管理。

## 关键特性

- **虚拟办公室** — 2D SVG 等距办公室 + 3D React Three Fiber 场景，Agent = 数字员工，Office = Agent 运行时，Desk = Session，Meeting Pod = 协作上下文
- **Agent 头像** — 从 Agent ID 确定性生成 SVG 头像，实时状态动画（idle、working、speaking、tool calling、error）
- **协作可视化** — 协作连线显示 Agent 间消息流，语音气泡实时流式显示 Markdown 文本和工具调用
- **侧边面板** — Agent 详情、Token 折线图、成本饼图、活动热力图、SubAgent 关系图、事件时间线
- **Chat** — 底部停靠聊天栏，实时与 Agent 对话，Agent 选择器、流式消息显示、Markdown 渲染、聊天历史抽屉
- **Console** — 全功能系统管理界面，包含 Dashboard、Agents、Channels、Skills、Cron、Settings 页面
- **远程 Gateway 支持** — 通过 `/gateway-ws` 代理流程支持远程 OpenClaw Gateway 接入（阿里云、腾讯云等托管环境）
- **i18n** — 中英文双语支持，运行时语言切换
- **Mock Mode** — 无需 Gateway 连接即可开发

<!-- lastCommit: 801528c -->

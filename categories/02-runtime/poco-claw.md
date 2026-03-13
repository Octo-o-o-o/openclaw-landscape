# Poco-Claw (1,131 stars)

## 问题与解决方案

Poco-Claw 解决了 OpenClaw 的安全性和易用性问题。传统 OpenClaw 在宿主机执行命令，存在安全风险；CLI 界面对非技术用户门槛高；缺少移动端支持和 IM 集成。Poco 提供更美观的 Web UI、内置沙箱运行时、IM 集成（钉钉/Telegram）、移动端支持、智能记忆（mem0），底层由 Claude Code Agent 驱动。

## 关键特性

- **安全沙箱**：所有任务在隔离容器中运行，安装依赖、修改文件、执行命令不影响宿主环境
- **丰富 UI**：Plan Mode、会话队列、会话终止、项目管理、文件上传、Artifacts 视图（HTML/PDF/Markdown/Xmind/Excalidraw/Drawio）、Playback 视图（命令 I/O/浏览器会话/MCP 工具调用）
- **原生 Claude Code 体验**：Slash Commands、Plan Mode、AskQuestion、MCP & Skills、内置浏览器、GitHub 仓库集成
- **后台执行 + 定时触发**：Agent 可在云端持续运行，即使关闭浏览器，支持定时任务
- **多端交互**：移动端支持、IM 集成（钉钉/Telegram）、推送通知、事件订阅
- **智能记忆（mem0）**：记住用户偏好、项目上下文、历史交互，提供个性化帮助

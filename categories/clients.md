# Desktop & Mobile Clients

> Desktop apps, mobile apps, and terminal clients.
> 桌面应用、移动应用和终端客户端。

**6 projects** | [Back to overview](../README.md)

---

### ClawX

[ValueCell-ai/ClawX](https://github.com/ValueCell-ai/ClawX) | Stars: 3,454
Researched: 2026-03-11 | Updated: 2026-03-13

ClawX 解决了 OpenClaw 的易用性问题。传统 OpenClaw 需要命令行操作、手动配置文件编辑、环境变量管理，对非技术用户门槛极高。ClawX 提供跨平台桌面 GUI（Electron + React），将 CLI 操作转化为可视化界面，内嵌 OpenClaw 运行时，实现"开箱即用"。

**Features:** 零配置门槛, 内嵌 OpenClaw 运行时, 多功能面板, 安全凭证管理, 跨平台支持, 自适应主题

---

### OpenAkita

[openakita/openakita](https://github.com/openakita/openakita) | Stars: 1,114
Researched: 2026-03-11 | Updated: 2026-03-13

OpenAkita 解决了传统 AI 助手"只会聊天不会做事"的痛点。通过多 Agent 协作架构，将复杂任务分解给专业化 Agent 并行执行（编码 Agent 写代码、写作 Agent 写文档、测试 Agent 验证），配合 ReAct 推理引擎（Think → Act → Observe 三阶段循环）和 89+ 工具集成，实现了从对话到实际执行的闭环。

**Features:** 多 Agent 协作系统, Plan Mode 任务分解, ReAct 推理引擎, 零门槛 GUI 配置, 89+ 工具 + 技能市场, 30+ LLM 提供商 + 6 IM 平台

---

### mithun50/openclaw-termux

[mithun50/openclaw-termux](https://github.com/mithun50/openclaw-termux) | Stars: 563 | Go | MIT
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 原本只能在桌面系统（macOS/Linux/Windows）上运行，移动端用户面临以下困难：

**Features:** 启动时自动修补配置, 权限主动请求, WebSocket 通信

---

### PhoneClaw

[rohanarun/phoneclaw](https://github.com/rohanarun/phoneclaw) | Stars: 392
Researched: 2026-03-11 | Updated: 2026-03-13

Android 手机自动化需要 root 权限或复杂的 ADB 配置，普通用户难以使用。PhoneClaw 基于 Android Accessibility Service 实现无 root 自动化，通过 ClawScript（嵌入式 JS 引擎）在运行时生成自动化逻辑，结合视觉辅助 UI 定位（Moondream 视觉模型），实现跨应用的自适应工作流。

**Features:** 无 root 自动化, ClawScript 脚本引擎, 视觉辅助定位, 运行时生成脚本, 跨应用工作流, 验证码自动化

---

### BotDrop Android

[zhixianio/botdrop-android](https://github.com/zhixianio/botdrop-android) | Stars: 303 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

在 Android 手机上运行 AI Agent 需要安装 Termux、配置 Node.js、手动执行 CLI 命令，技术门槛高。BotDrop 将 OpenClaw 封装为用户友好的 Android 应用，提供 4 步引导式安装（Auth → Agent → Install → Channel），无需终端和 CLI，支持后台 Gateway 自动重启。

**Features:** 4 步引导式安装, 多提供商支持, Telegram & Discord 集成, 后台 Gateway, 无需终端, 基于 Termux

---

### OpenClaw on Android

[AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android) | Stars: 0 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

**Features:** 一键安装, 无需 Linux, 分层安装, 8 步安装流程, 进程保活, PC 远程访问

---

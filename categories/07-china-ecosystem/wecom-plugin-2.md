# WeCom OpenClaw Plugin (95 stars)

## 问题与解决方案
OpenClaw 缺乏与企业微信（WeCom）的原生集成，无法通过企业通讯工具远程控制 Agent。该插件通过 WeCom 应用接口实现双向通信，用户可通过企业微信发送消息控制 PC 浏览器和执行 AI 任务。

## 关键特性
- **双向消息通道** — 通过企业微信发送消息，AI 处理后返回响应，支持远程浏览器控制
- **富媒体支持** — 支持图片、语音、视频、文件的发送和接收
- **工具调用集成** — AI 可执行 100+ 内置工具，通过企业微信触发任务
- **回调服务器** — 内置 webhook 服务器处理企业微信消息推送，支持 Token 和 AES 加密验证
- **TypeScript 实现** — Node.js 18+ + TypeScript，完整的类型安全和文档支持
- **快速配置** — 通过 `~/.openclaw/openclaw.json` 配置企业 ID、Secret、Agent ID 等凭证

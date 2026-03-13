# openclaw-feishu (522 stars)

## 问题与解决方案

飞书用户接入 OpenClaw 存在配置复杂、文档分散、国内生态适配不足的痛点。本项目提供保姆级配置指南、常见问题排查清单、以及飞书官方插件与 OpenClaw 内置插件的对比选型建议，降低非技术用户的接入门槛。

## 关键特性

- **三种插件方案对比** — 飞书官方插件（OAuth 用户身份）、OpenClaw 内置插件（机器人身份）、社区早期插件（已停止更新），提供详细选型矩阵
- **从零配置教程** — 4 步引导式安装（Auth → Agent → Install → Channel），覆盖 Anthropic/OpenAI/Gemini 等多模型提供商
- **常见问题排查** — API 配额耗尽根因分析、Lark Webhook 内网穿透方案、版本检查 bug 绕过方法
- **国内生态适配** — 配套 [awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh) 39 个真实用例（含飞书/钉钉/企微/小红书场景）
- **迁移指南** — 从 HTTP 回调模式迁移到 WebSocket 长连接的完整步骤
- **进阶配置参考** — 多维表格、日历日程、任务管理、知识库等高级功能配置示例

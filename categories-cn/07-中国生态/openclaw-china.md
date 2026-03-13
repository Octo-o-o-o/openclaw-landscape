# BytePioneer-AI/openclaw-china

## 基本信息

- **GitHub**: https://github.com/BytePioneer-AI/openclaw-china
- **Stars**: 2,790
- **语言**: TypeScript
- **创建时间**: 2026-01-28
- **最后更新**: 2026-03-11
- **描述**: 面向中国 IM 平台的 OpenClaw 扩展插件集合
- **Topics**: openclaw, openclaw-china, openclaw-dingding, openclaw-feishu, openclaw-qq, openclaw-weixin

## 问题与解决方案

### 核心问题

OpenClaw 原生不支持中国主流即时通讯平台（钉钉、企业微信、QQ、飞书），导致国内用户无法将 AI Agent 接入企业内部沟通工具，限制了 OpenClaw 在中国市场的应用场景。

### 解决方案

openclaw-china 提供了一套完整的中国 IM 平台适配层，通过插件化架构实现：

1. **统一插件包** (`@openclaw-china/channels`)：聚合所有渠道插件，一键安装
2. **单渠道插件**：支持按需安装单个平台（dingtalk / feishu-china / qqbot / wecom / wecom-app）
3. **配置向导** (`openclaw china setup`)：交互式配置流程，降低接入门槛
4. **多账户支持**：同一平台可配置多个机器人账号
5. **全网首发功能**：
   - 钉钉、QQ、企微支持文件接收和发送
   - 钉钉、QQ、飞书支持定时任务
   - 企微智能机器人长连接支持受限主动发送

## 核心架构

### 分层架构

```
OpenClaw 宿主
    ↓
@openclaw-china/channels (统一调度层)
    ↓
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│ dingtalk│ feishu  │  qqbot  │  wecom  │wecom-app│
└─────────┴─────────┴─────────┴─────────┴─────────┘
                    ↓
        @openclaw-china/shared (基础设施层)
```

### 技术栈

- **构建工具**: pnpm workspace + tsup
- **运行时**: Node.js 22+
- **插件系统**: OpenClaw 插件协议（openclaw.plugin.json）
- **连接方式**:
  - 钉钉: Stream API
  - 飞书: WebSocket 长连接
  - QQ: 官方 Bot API
  - 企微智能机器人: WebSocket 长连接（ws 模式，无需公网 IP）
  - 企微自建应用: HTTPS 回调 + 主动发送 API

### 关键设计模式

1. **动态注册机制**: channels 包在启动时动态注册各渠道插件到 OpenClaw
2. **策略模式**: 支持 dmPolicy（私聊策略）和 groupPolicy（群聊策略）配置
   - `open`: 开放所有用户
   - `pairing`: 配对模式
   - `allowlist`: 白名单模式
   - `disabled`: 禁用
3. **适配器模式**: 每个渠道实现统一的消息入站/出站接口
4. **媒体归档**: 入站媒体自动落盘到稳定路径（`~/.openclaw/media/{channel}/inbound/`），避免 `/tmp` 被清理

## 关键特性

### 1. 消息能力矩阵

| 功能 | 钉钉 | 飞书 | QQ | 企微智能机器人 | 企微自建应用 |
|------|:----:|:----:|:--:|:-------------:|:-----------:|
| 文本消息 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Markdown | ✅ | ✅ | ✅ | ✅ | ✅ |
| 流式响应 | ✅ | - | ❌ | ✅ | ❌ |
| 图片/文件 | ✅ | ✅（仅发送） | ✅ | ✅（出站文件受限） | ✅ |
| 语音消息 | ✅ | - | ✅ | ✅ | ✅ |
| 私聊 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 群聊 | ✅ | ✅ | ✅ | ✅ | ❌ |
| @机器人检测 | ✅ | ✅ | ✅ | ❌ | ❌ |
| 多账户 | ✅ | - | ✅ | ✅ | ✅ |
| 主动发送消息 | ✅ | ✅ | ✅ | ✅ | ✅ |

### 2. 企微自建应用高级功能

- **入站媒体归档**: image/voice/file/mixed 自动落盘，消息体写入 `saved:` 稳定路径
- **语音识别**: 接入腾讯云 Flash ASR（录音文件识别极速版）
- **长文本分片**: 自动处理 2048 bytes 限制
- **Stream 占位/刷新**: 5s 规则下缓冲，支持 `/verbose on` 逐段主动发送
- **Access Token 缓存**: 2 小时有效期自动管理
- **专用 Skill**: `wecom-app-ops`（target/replyTo/回发图片/录音/文件、OCR/MCP、排障、媒体保留策略）

### 3. QQ 渠道特性

- **标准 onboarding 适配器**: 支持在渠道配置流程中直接完成凭证接入与禁用
- **已知目标注册表**: 保存到 `~/.openclaw/data/qqbot/known-targets.json`
- **主动发送 helper**: 复用现有文本/媒体出站链路做单目标主动发送
- **长任务通知**: 支持配置延迟时间，提升长耗时任务场景下的交互反馈
- **文件上传**: 支持文件名参数，优化媒体发送链路
- **回退机制**: `msg_id` 失效时回退使用 `event_id`，提升定时与异步回发稳定性

### 4. 钉钉渠道特性

- **多账号支持**: 完善默认账号解析、账号配置管理、监控与出站逻辑
- **长任务通知**: 非 AI 回复切换为直接分发，减少回复链路复杂度
- **AI 卡片**: 可选开启 `enableAICard`（流式响应卡片）

### 5. 企微智能机器人特性

- **长连接 ws 模式**: 无需公网 IP，体验更佳（2026-03-08 全网首发）
- **多账号多 Agent**: 入站路由透传 `accountId`，避免消息错误落到默认 Agent
- **心跳 ACK**: 避免通道在无用户消息期间被错误判定为失活

### 6. 定时任务能力

- **统一采用 sessionTarget="isolated"**: 避免投递串会话
- **固定 delivery.channel/to/accountId**: 提醒类任务不串会话
- **Cron 创建提示词**: 明确要求将执行期约束写入 payload.message（仅纯文本、禁止调用工具、禁止手动发送）
## 总结

openclaw-china 是一个成熟的多平台接入解决方案，其架构设计、功能实现、社区运营都值得 ClawButler 借鉴。特别是：

1. **插件化架构** 可直接应用于 ClawButler 的 Agent 平台接入层
2. **配置向导** 可大幅降低用户接入门槛
3. **多账户与路由策略** 可增强 ClawButler 的访问控制能力
4. **媒体归档** 可解决 Agent 间文件传递和审计日志的痛点
5. **主动发送与定时任务** 可增强 ClawButler 的 Runbook 能力
6. **心跳与健康检查** 可提升 ClawButler 的可靠性
7. **错误处理与排障** 可改善用户体验
8. **社区生态** 可加速 ClawButler 的推广
9. **版本兼容** 可降低升级成本
10. **性能优化** 可支持大规模部署

建议 ClawButler 团队深入研究 openclaw-china 的源码（特别是 `packages/channels` 和 `packages/shared`），并在 V2.5 或 V3.0 中引入类似的平台适配层设计。

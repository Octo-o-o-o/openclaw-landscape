> https://github.com/clawdotnet/openclaw.net

# OpenClaw.NET (84 stars)

## 问题与解决方案
OpenClaw 原生基于 Node.js/TypeScript，在 .NET 生态中缺乏原生支持。OpenClaw.NET 提供完整的 .NET 实现（支持 NativeAOT），包含 Gateway + Agent Runtime，支持 C# 原生工具和 Node.js 插件桥接。

## 关键特性
- **双运行时模式** — `aot` 模式（trim-safe、低内存）和 `jit` 模式（扩展桥接、动态插件），通过 `OpenClaw:Runtime:Mode` 配置
- **分层启动架构** — Bootstrap（配置加载、验证）→ Composition（服务注册）→ Profiles（运行时选择）→ Pipeline（中间件、端点）
- **多客户端支持** — Web UI (`/chat`)、WebSocket (`/ws`)、CLI (`OpenClaw.Cli`)、桌面伴侣 (`OpenClaw.Companion`)
- **Webhook 渠道** — 支持 Telegram、Twilio、WhatsApp、通用 webhook 的入站消息处理
- **18+ 原生工具** — 文件操作、shell 执行、web 搜索等 C# 原生实现，性能优于 Node.js 桥接
- **安全加固配置** — 提供 dev/staging/prod 三级安全配置模板，支持 `--doctor` 模式验证配置

<!-- lastCommit: 36e486c -->

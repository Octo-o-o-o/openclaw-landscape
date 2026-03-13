# Alternative Runtimes

> Alternative implementations and runtimes compatible with the OpenClaw ecosystem.
> 与 OpenClaw 生态兼容的替代实现和运行时。

**18 projects** | [Back to overview](../README.md)

---

### ZeroClaw

[zeroclaw-labs/zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Stars: 25,853 | Rust | MIT OR Apache-2.0
Researched: 2026-03-11 | Updated: 2026-03-13

1. 资源开销过大: OpenClaw (TypeScript) 需要 >1GB RAM + Node.js 运行时 (~390MB)，启动时间在低端硬件上超过 500 秒 2. 部署成本高: OpenClaw 推荐 Mac mini ($599) 或高配 Linux 服务器，边缘设备和低成本硬件无法运行 3. 架构锁定: 现有 Agent 框架通常绑定特定 LLM 提供商、消息渠道或工具生态，迁移成本高 4. 安全性不足: 缺乏沙箱隔离、工作区限制、配对认证等企业级安全机制 5. 冷启动慢: 基于解释型语言的运行时启动延迟高，影响 CLI 和守护进程体验

**Features:** 即时通讯, 企业协作, 传统协议, 新兴协议, 移动端

---

### NanoClaw

[qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw) | Stars: 21,451 | Node.js | MIT
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 虽然功能强大，但存在严重的可理解性和安全性问题： - 代码复杂度过高：近 50 万行代码，53 个配置文件，70+ 依赖项 - 安全模型薄弱：应用层权限控制（allowlist、配对码），而非真正的 OS 级隔离 - 单进程共享内存：所有功能运行在同一个 Node 进程中，缺乏隔离边界 - 配置膨胀：功能通过配置文件堆叠，导致系统臃肿

**Features:** 从 WhatsApp、Telegram、Discord、Slack 或 Gmail 与助手对话, 通过技能添加通道（如 `/add-whatsapp`、`/add-telegram`）, 可同时运行一个或多个通道

---

### cloudflare/moltworker

[cloudflare/moltworker](https://github.com/cloudflare/moltworker) | Stars: 9,558 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

1. 自托管门槛高：传统 AI 助手需要用户自行维护服务器、处理运维问题（进程管理、日志、备份、安全更新） 2. 成本不可控：24/7 运行的 VPS 或云主机成本高昂，且资源利用率低 3. 冷启动慢：容器化部署的冷启动时间长（1-2 分钟），影响用户体验 4. 数据持久化难：无状态容器环境下，如何保存对话历史、配置、已配对设备等状态

**Features:** Durable Objects, 容器生命周期管理, 默认 `SANDBOX_SLEEP_AFTER=never`（永不休眠, 可配置空闲超时（如 `10m`、`1h`）以降低成本, 冷启动时间 1-2 分钟, 进程监控

---

### IronClaw

[nearai/ironclaw](https://github.com/nearai/ironclaw) | Stars: 9,101 | Rust
Researched: 2026-03-11 | Updated: 2026-03-13

现有 AI 助手数据处理不透明、与企业利益绑定、存在隐私泄露风险。IronClaw 用 Rust 重写 OpenClaw 核心，强调隐私优先（本地存储 + 加密）、透明可审计（开源 + 无遥测）、自扩展能力（动态构建工具）、多层安全防护（WASM 沙箱 + prompt injection 防御）。

**Features:** Rust 实现, 安全优先, 动态工具构建, MCP 协议支持, 多 LLM 后端, 持久化内存

---

### MimiClaw

[memovai/mimiclaw](https://github.com/memovai/mimiclaw) | Stars: 4,260 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

MimiClaw 解决了 AI Agent 运行的硬件门槛问题。传统 OpenClaw 需要 Linux/macOS + Node.js + 至少 Mac mini 级别的硬件，而 MimiClaw 将完整的 Agent 运行时压缩到 5 美元的 ESP32-S3 芯片上，无需操作系统，纯 C 实现，功耗仅 0.5W，可 24/7 运行。

**Features:** 极致轻量, 硬件要求, 双模型支持, 本地存储, Telegram 交互, 两层配置系统

---

### Moltis

[moltis-org/moltis](https://github.com/moltis-org/moltis) | Stars: 2,077 | TypeScript
Researched: 2026-03-11 | Updated: 2026-03-13

Moltis 解决了 OpenClaw 的安全性和可审计性问题。传统 OpenClaw（TypeScript + Node.js，~430K LoC）存在供应链攻击风险、内存安全隐患、运行时依赖复杂等问题。Moltis 用 Rust 重写，单二进制部署，零 `unsafe` 代码，沙箱隔离执行，核心代码仅 ~5K LoC（Agent 循环 + 模型层），全栈 ~124K LoC，3,100+ 测试，可独立审计。

**Features:** 内存安全, 沙箱隔离, 单二进制部署, 可审计架构, 全功能内置, 安全设计

---

### zclaw

[tnm/zclaw](https://github.com/tnm/zclaw) | Stars: 1,873
Researched: 2026-03-11 | Updated: 2026-03-13

ESP32 硬件资源极度受限（<= 888 KiB 固件预算），传统 AI 助手无法运行。zclaw 用纯 C 实现超轻量级个人 AI 助手，在 ESP32 上提供完整的调度、GPIO 控制、持久化记忆和自定义工具能力，通过自然语言交互控制物联网设备。

**Features:** 极致轻量, 完整调度系统, GPIO 工具链, 多 LLM 后端, 持久化记忆, USB 本地管理台

---

### Poco-Claw

[poco-ai/poco-claw](https://github.com/poco-ai/poco-claw) | Stars: 1,131
Researched: 2026-03-11 | Updated: 2026-03-13

Poco-Claw 解决了 OpenClaw 的安全性和易用性问题。传统 OpenClaw 在宿主机执行命令，存在安全风险；CLI 界面对非技术用户门槛高；缺少移动端支持和 IM 集成。Poco 提供更美观的 Web UI、内置沙箱运行时、IM 集成（钉钉/Telegram）、移动端支持、智能记忆（mem0），底层由 Claude Code Agent 驱动。

**Features:** 安全沙箱, 丰富 UI, 原生 Claude Code 体验, 后台执行 + 定时触发, 多端交互, 智能记忆（mem0）

---

### clawlet

[mosaxiv/clawlet](https://github.com/mosaxiv/clawlet) | Stars: 657 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

传统 AI 助手依赖复杂运行时（Node.js/Python）和外部数据库，部署繁琐且资源占用高。clawlet 用 Go 编译为单一静态二进制（无 CGO、无运行时依赖），内嵌 SQLite + sqlite-vec，实现开箱即用的混合语义记忆搜索，一个文件即可在任意机器上运行。

**Features:** 零依赖部署, 多 LLM 提供商, OAuth 无密钥登录, 混合语义搜索, 灵活配置, 本地模型优先

---

### openbrowserclaw

[sachaa/openbrowserclaw](https://github.com/sachaa/openbrowserclaw) | Stars: 558
Researched: 2026-03-11 | Updated: 2026-03-13

传统 AI 助手需要服务器基础设施（数据库、文件系统、后台进程），增加部署成本和隐私风险。openbrowserclaw 将整个 Agent 运行时搬进浏览器标签页，利用 IndexedDB/OPFS/Web Worker/WebAssembly 实现零基础设施的个人 AI 助手，数据完全本地化。

**Features:** 纯浏览器架构, 零服务器依赖, 内置工具链, 多渠道支持, PWA 离线能力, Cron 调度器

---

### OpenClaw Mini

[voocel/openclaw-mini](https://github.com/voocel/openclaw-mini) | Stars: 555
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw Mini 解决了"OpenClaw 架构学习门槛高"的痛点。通过从 43 万行代码中提炼核心设计，提供最小化实现（核心层 + 扩展层 + 工程层三层分离），帮助开发者理解生产级 Agent 的系统级设计：双层循环 + EventStream 事件流、会话持久化（JSONL）、上下文管理（裁剪 + 摘要压缩）、长期记忆、技能系统、主动唤醒、多 Provider 适配（22+ 提供商）等，而非简单的 Agent Loop。

**Features:** 三层架构分离, 双层循环 + EventStream, 会话持久化（JSONL）, 上下文管理三件套, 长期记忆 + 技能系统 + 主动唤醒, 多 Provider 适配

---

### stellarlinkco/myclaw

[stellarlinkco/myclaw](https://github.com/stellarlinkco/myclaw) | Stars: 236
Researched: 2026-03-11 | Updated: 2026-03-13

完整的 OpenClaw 部署过于复杂，用户需要轻量级的"个人 Agent 助手"快速上手。MyClaw 提供最小化的 clawbot 实现，专注于核心 Agent 能力（对话、工具调用、记忆），去除企业级功能（多租户、权限管理），适合个人开发者和小团队。

**Features:** 轻量级架构, 核心 Agent 能力, 模型灵活性, 技能系统, 本地优先, 开发者友好

---

### OpenClaw.NET

[clawdotnet/openclaw.net](https://github.com/clawdotnet/openclaw.net) | Stars: 84 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 原生基于 Node.js/TypeScript，在 .NET 生态中缺乏原生支持。OpenClaw.NET 提供完整的 .NET 实现（支持 NativeAOT），包含 Gateway + Agent Runtime，支持 C# 原生工具和 Node.js 插件桥接。

**Features:** 双运行时模式, 分层启动架构, 多客户端支持, Webhook 渠道, 18+ 原生工具, 安全加固配置

---

### OpenCrust

[opencrust-org/opencrust](https://github.com/opencrust-org/opencrust) | Stars: 49 | Node.js
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw（Node.js）存在二进制体积大（~1.2 GB）、内存占用高（~388 MB）、冷启动慢（13.9 秒）、凭证明文存储等问题。OpenCrust 使用 Rust 重写，将二进制压缩至 16 MB、内存降至 13 MB、冷启动缩短至 3 ms，并提供 AES-256-GCM 加密凭证存储和默认启用的 WebSocket 认证。

**Features:** 极致性能, 安全优先, 跨平台预编译, 配置热加载, WASM 插件沙箱, 14 个 LLM 提供商

---

### bastionclaw

[harperaa/bastionclaw](https://github.com/harperaa/bastionclaw) | Stars: 24
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 的 52+ 模块、45+ 依赖、应用级安全（allowlists/pairing codes）导致代码复杂且缺乏 OS 级隔离。bastionclaw 通过 fork NanoClaw 的容器隔离模型，将 Agent 运行在独立 Linux 容器（filesystem isolation），并添加 Telegram-first、Web 控制面板、WhatsApp 发送者白名单、语义记忆（QMD）、Data-to-Wisdom 管道，实现轻量级（8 分钟理解代码）+ 安全加固（CPU/内存限制、secret 清理、per-group IPC namespaces）的个人 AI 助手。

**Features:** 容器隔离模型, Telegram-first 设计, Web 控制面板, WhatsApp 发送者白名单, 语义记忆 + 洞察引擎, Agent Swarm 身份

---

### claw-kernel

[creeper-scr/claw-kernel](https://github.com/creeper-scr/claw-kernel) | Stars: 2 | Rust
Researched: 2026-03-11 | Updated: 2026-03-13

Claw 生态中的每个项目（OpenClaw、ZeroClaw、OpenCrust）都独立实现相同的基础设施（LLM 调用、工具协议、Agent 循环、记忆系统、渠道集成），导致重复开发和碎片化。claw-kernel 将这些原语提取为单一的、经过充分测试的跨平台 Rust 库，作为生态的共享基础设施层。

**Features:** 分层架构, 跨平台抽象层（PAL）, 8 个 LLM 提供商, 双脚本引擎, 670+ 测试覆盖, IPC 守护服务

---

### MicroClaw

[microclaw/microclaw](https://github.com/microclaw/microclaw) | Stars: 0 | Rust
Researched: 2026-03-11 | Updated: 2026-03-13

**Features:** Agentic 工具使用, 会话恢复, 上下文压缩, 子 Agent, 技能系统, 计划与执行

---

### PicoClaw

[sipeed/picoclaw](https://github.com/sipeed/picoclaw) | Stars: 0 | Go
Researched: 2026-03-11 | Updated: 2026-03-13

**Features:** 🪶 超轻量级, 💰 极低成本, ⚡️ 闪电启动, 🌍 真正的可移植性, 🤖 AI 自举开发

---

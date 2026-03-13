> https://github.com/zeroclaw-labs/zeroclaw

# ZeroClaw

## 基本信息

- **GitHub**: https://github.com/zeroclaw-labs/zeroclaw
- **Stars**: 25,853
- **语言**: Rust
- **许可证**: MIT OR Apache-2.0
- **官网**: https://zeroclawlabs.ai
- **社区**: X (@zeroclawlabs), Telegram, Reddit (r/zeroclawlabs), Facebook, 小红书, 微信群

## 问题与解决方案

### 核心问题

1. **资源开销过大**: OpenClaw (TypeScript) 需要 >1GB RAM + Node.js 运行时 (~390MB)，启动时间在低端硬件上超过 500 秒
2. **部署成本高**: OpenClaw 推荐 Mac mini ($599) 或高配 Linux 服务器，边缘设备和低成本硬件无法运行
3. **架构锁定**: 现有 Agent 框架通常绑定特定 LLM 提供商、消息渠道或工具生态，迁移成本高
4. **安全性不足**: 缺乏沙箱隔离、工作区限制、配对认证等企业级安全机制
5. **冷启动慢**: 基于解释型语言的运行时启动延迟高，影响 CLI 和守护进程体验

### ZeroClaw 的解决方案

**极致轻量化**:
- 单二进制文件 (~8.8MB)，无运行时依赖
- 内存占用 <5MB (release 构建)
- 冷启动 <10ms (0.8GHz 核心)
- 可在 $10 硬件上运行 (树莓派 Zero、Orange Pi 等)

**Trait 驱动架构**:
- 所有子系统都是 Trait 接口：Provider、Channel、Memory、Tool、Observer、RuntimeAdapter、SecurityPolicy
- 零代码修改即可切换实现 (配置文件热更新)
- 支持自定义端点 (OpenAI-compatible / Anthropic-compatible)

**安全优先设计**:
- Gateway 配对认证 (一次性 pairing code → bearer token)
- 沙箱运行时 (Docker 隔离 + 资源限制)
- 工作区作用域 (workspace_only 模式 + 路径白名单)
- 命令白名单 / 黑名单
- 加密密钥存储 (本地密钥文件)

**全栈内存系统** (无外部依赖):
- 向量数据库: SQLite BLOB + 余弦相似度搜索
- 关键词搜索: FTS5 虚拟表 + BM25 评分
- 混合检索: 自定义加权合并函数
- 嵌入缓存: LRU 淘汰策略
- 支持 PostgreSQL / Lucid / Markdown / None 后端

## 核心架构

### 系统架构图

```
┌─────────────────────────────────────────────────────────────┐
│                      ZeroClaw Runtime                        │
├─────────────────────────────────────────────────────────────┤
│  Trait Layer (所有子系统都是可插拔接口)                      │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │ Provider │ Channel  │  Memory  │   Tool   │ Observer │  │
│  │  (LLM)   │ (消息)   │ (存储)   │ (能力)   │ (监控)   │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │ Runtime  │ Security │ Identity │  Tunnel  │Heartbeat │  │
│  │ Adapter  │  Policy  │  Config  │          │  Engine  │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘  │
├─────────────────────────────────────────────────────────────┤
│  Core Services                                               │
│  • Agent Loop (单次对话 / 交互模式)                          │
│  • Gateway (Webhook 服务器, 42617 端口)                      │
│  • Daemon (长期运行的自主运行时)                             │
│  • Service Manager (systemd / OpenRC)                        │
├─────────────────────────────────────────────────────────────┤
│  Storage Layer                                               │
│  • SQLite (混合搜索: 向量 + FTS5)                            │
│  • PostgreSQL (远程内存后端)                                 │
│  • Markdown (文件系统持久化)                                 │
│  • Lucid (外部内存桥接)                                      │
└─────────────────────────────────────────────────────────────┘
```

### 关键设计模式

**1. Trait 驱动的可插拔架构**

每个子系统都定义为 Rust Trait，运行时通过配置文件动态选择实现:

```toml
[memory]
backend = "sqlite"  # 可选: sqlite, postgres, lucid, markdown, none

[runtime]
kind = "native"     # 可选: native, docker

[tunnel]
provider = "none"   # 可选: none, cloudflare, tailscale, ngrok, custom
```

**2. 订阅认证 (Subscription Auth)**

支持 OpenAI Codex OAuth 和 Claude Code 订阅令牌:

```bash
# OAuth 设备码流程 (无头服务器)
zeroclaw auth login --provider openai-codex --device-code

# 多账户配置文件
zeroclaw auth use --provider openai-codex --profile work
```

- 存储文件: `~/.zeroclaw/auth-profiles.json` (加密)
- 加密密钥: `~/.zeroclaw/.secret_key`
- Profile ID 格式: `<provider>:<profile_name>`

**3. 混合内存搜索引擎**

完全自研，零外部依赖 (无 Pinecone / Elasticsearch / LangChain):

| 层级 | 实现 |
|------|------|
| 向量数据库 | SQLite BLOB + 余弦相似度 |
| 关键词搜索 | FTS5 虚拟表 + BM25 |
| 混合合并 | 自定义加权函数 (`vector.rs`) |
| 嵌入生成 | `EmbeddingProvider` trait (OpenAI / custom / noop) |
| 分块策略 | 基于行的 Markdown 分块 + 标题保留 |
| 缓存 | SQLite `embedding_cache` 表 + LRU 淘汰 |

**4. 安全沙箱运行时**

```toml
[autonomy]
level = "supervised"  # readonly / supervised / full
workspace_only = true
allowed_commands = ["git", "npm", "cargo", "ls", "cat", "grep"]
forbidden_paths = ["/etc", "/root", "/proc", "/sys", "~/.ssh"]

[runtime.docker]
image = "alpine:3.20"
network = "none"
memory_limit_mb = 512
cpu_limit = 1.0
read_only_rootfs = true
```

**5. Gateway 配对认证**

```
1. 客户端请求配对码: GET /pair
2. 服务端生成一次性码 (6 位数字)
3. 客户端提交配对码: POST /pair (X-Pairing-Code header)
4. 服务端验证并返回 bearer token
5. 后续请求携带 token: Authorization: Bearer <token>
```

## 关键特性

### 1. 多渠道支持 (Channel Trait)

内置 15+ 消息渠道:
- **即时通讯**: Telegram, Discord, Slack, Mattermost, Matrix, Signal, WhatsApp
- **企业协作**: Lark (飞书), DingTalk (钉钉), QQ
- **传统协议**: Email, IRC, Webhook
- **新兴协议**: Nostr, Linq
- **移动端**: iMessage (macOS)

配置示例 (Telegram):

```toml
[channels_config.telegram]
bot_token = "123456:ABC-DEF..."
allowed_chat_ids = [123456789, -1001234567890]
```

### 2. 多模型提供商 (Provider Trait)

支持 20+ LLM 提供商:
- **主流**: OpenAI, Anthropic, Google (Gemini), OpenRouter, Groq
- **本地**: Ollama, llama.cpp server
- **订阅**: OpenAI Codex (ChatGPT), Claude Code
- **自定义**: OpenAI-compatible / Anthropic-compatible 端点

```toml
default_provider = "openrouter"
default_model = "anthropic/claude-sonnet-4-6"

# 自定义端点
# default_provider = "custom:https://your-api.com"
# default_provider = "anthropic-custom:https://your-api.com"
```

### 3. 技能系统 (Skills)

- TOML 清单 + SKILL.md 指令
- 社区技能包 (open-skills, 默认禁用)
- 内置安全审计 (阻止符号链接、脚本文件、不安全 Markdown 链接、高风险 shell payload)

```bash
zeroclaw skills list
zeroclaw skills install <source>
zeroclaw skills audit <source_or_name>
```

### 4. 心跳任务 (Heartbeat)

周期性自主任务执行:

```toml
[heartbeat]
enabled = true
interval_minutes = 30
message = "Check London time"
target = "telegram"
to = "123456789"
```

或使用 `HEARTBEAT.md` 文件定义任务列表。

### 5. 集成生态 (Integrations)

70+ 集成，跨 9 个类别:
- 通信 (Telegram, Discord, Slack, Email, WhatsApp)
- 生产力 (Todoist, Notion, Google Calendar)
- 开发 (GitHub, GitLab, Jira, Linear)
- 数据 (PostgreSQL, Redis, S3)
- 监控 (Prometheus, Grafana)
- 支付 (Stripe, PayPal)
- AI (Composio - 1000+ OAuth 应用, 可选启用)

```bash
zeroclaw integrations info Telegram
```

### 6. AIEOS 身份规范

支持 [AIEOS v1.1](https://aieos.org) (AI Entity Object Specification) 标准化身份:

```toml
[identity]
format = "aieos"
aieos_path = "identity.json"
```

或内联 JSON:

```toml
[identity]
format = "aieos"
aieos_inline = '''
{
  "identity": {"names": {"first": "Nova"}},
  "psychology": {"neural_matrix": {"creativity": 0.9}},
  "linguistics": {"text_style": {"formality_level": 0.2}},
  "motivations": {"core_drive": "Push boundaries"},
  "capabilities": {"skills": [{"name": "Rust engineering"}]}
}
'''
```

### 7. 浏览器工具 (可选启用)

```toml
[browser]
enabled = true
allowed_domains = ["docs.rs"]
backend = "agent_browser"  # agent_browser / rust_native / computer_use / auto
native_headless = true
native_webdriver_url = "http://127.0.0.1:9515"
```

三种后端:
- **agent_browser**: 默认，轻量级
- **rust_native**: 需要 WebDriver (chromedriver / selenium)
- **computer_use**: 外部 sidecar HTTP 端点 (鼠标/键盘控制)

### 8. 迁移工具

从 OpenClaw 迁移内存:

```bash
zeroclaw migrate openclaw --dry-run
zeroclaw migrate openclaw
```

### 9. 服务管理

支持 systemd (用户级) 和 OpenRC (系统级):

```bash
# Linux (systemd, 无需 sudo)
zeroclaw service install
zeroclaw service start

# Alpine (OpenRC, 需要 sudo)
sudo zeroclaw service install
sudo rc-update add zeroclaw default
sudo rc-service zeroclaw start
```

### 10. 一键安装

```bash
# 推荐: 克隆后本地运行
git clone https://github.com/zeroclaw-labs/zeroclaw.git
cd zeroclaw
./install.sh

# 可选: 安装系统依赖 + Rust
./install.sh --install-system-deps --install-rust

# 可选: 优先使用预构建二进制 (低 RAM/磁盘主机)
./install.sh --prefer-prebuilt

# 可选: 仅二进制安装 (无源码构建回退)
./install.sh --prebuilt-only

# 可选: 同时运行 onboarding
./install.sh --onboard --api-key "sk-..." --provider openrouter

# 远程一键安装 (生产环境建议先审查)
curl -fsSL https://raw.githubusercontent.com/zeroclaw-labs/zeroclaw/main/install.sh | bash
```
## 总结

ZeroClaw 的核心价值在于 **极致轻量化** + **Trait 驱动的可插拔架构** + **安全优先设计**。对于 ClawButler (Agent 控制平面) 而言，最有价值的借鉴点包括:

1. **架构层面**: Trait/Protocol 抽象 + 配置热更新
2. **安全机制**: Gateway 配对认证 + 沙箱运行时 + 工作区作用域
3. **多渠道支持**: Channel 抽象层 (优先 Telegram / Slack)
4. **内存系统**: 混合检索 (向量 + 关键词) + 嵌入缓存
5. **订阅认证**: 多账户配置文件 + OAuth 设备码流程
6. **技能系统**: 安全审计 + 社区技能包可选启用
7. **AIEOS 身份规范**: 跨平台 Agent 配置迁移
8. **部署优化**: 单二进制分发 + 预构建二进制

这些特性可显著增强 ClawButler 的 **安全性**、**可扩展性** 和 **跨平台兼容性**，同时降低部署和运维成本。

<!-- lastCommit: 137e138 -->

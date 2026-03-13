> https://github.com/xianyu110/clawbot

# xianyu110/clawbot

## 基本信息

- **Stars**: 856
- **URL**: https://github.com/xianyu110/clawbot
- **状态**: 活跃维护中

## 问题与解决方案

### 核心问题
Clawbot 是 OpenClaw 的完整中文配置指南项目，解决了中文用户在部署和配置 OpenClaw 时遇到的以下痛点：

1. **官方文档英文为主**：缺乏系统的中文安装教程
2. **配置复杂度高**：多个配置文件、环境变量、认证方式让新手困惑
3. **API 中转配置困难**：国内用户需要使用中转 API，但配置方式不明确
4. **常见错误频发**：环境变量无效、配置格式错误、服务启动失败等问题

### 解决方案
提供了一套完整的中文部署指南，包括：

- **分步骤安装教程**：从 Node.js 升级到初始化配置的完整流程
- **多种认证方式对比**：setup-token、Claude Code CLI、API Key 的适用场景
- **API 中转配置方案**：支持多模型中转站和 Claude Code 专用中转
- **踩坑指南**：总结了 6 大常见错误及解决方案
- **常用命令速查**：Gateway 管理、配置管理、日志查看等

## 核心架构

### 文档结构

```
README.md
├── 简介
├── 系统要求
├── 安装步骤
│   ├── 升级 Node.js
│   ├── 选择安装方式（npm/脚本/源码）
│   └── 初始化配置向导
├── 配置自定义中转站
│   ├── 方案一：多模型中转（GPT/Claude/Gemini）
│   └── 方案二：Claude Code 中转（需要 User-Agent）
├── 验证和测试
├── 常见踩坑点（6 个）
├── 常见问题 FAQ（5 个）
└── 常用命令
```

### 配置文件层级

```
~/.clawdbot/
├── clawdbot.json              # 主配置文件
│   ├── models.providers       # 模型提供商配置
│   ├── agents.defaults        # Agent 默认配置
│   ├── gateway                # Gateway 配置
│   └── channels               # 通道配置
├── agents/main/agent/
│   └── auth-profiles.json     # 鉴权配置
└── logs/
    ├── gateway.log            # 主日志
    └── gateway.err.log        # 错误日志
```

## 关键特性

### 1. 多模型中转配置方案

**支持同时配置多个 AI 模型提供商**：

```json
{
  "models": {
    "providers": {
      "api-proxy-gpt": {
        "baseUrl": "https://apipro.maynor1024.live/v1",
        "api": "openai-completions",
        "models": [{"id": "gpt-4o", ...}]
      },
      "api-proxy-claude": {
        "baseUrl": "https://apipro.maynor1024.live",
        "api": "anthropic-messages",
        "models": [{"id": "claude-sonnet-4-5-20250929", ...}]
      },
      "api-proxy-google": {
        "baseUrl": "https://apipro.maynor1024.live/v1beta",
        "api": "google-generative-ai",
        "models": [{"id": "gemini-3-pro-preview", ...}]
      }
    }
  }
}
```

### 2. 认证方式对比表

| 认证方式 | 适用场景 | 优点 | 缺点 |
|---------|---------|------|------|
| setup-token | Claude Max/Pro 订阅用户 | 无需额外付费 | 需要额外步骤生成 token |
| Claude Code CLI | 已配置 Claude Code 的用户 | 自动读取凭证 | 可能找不到凭证文件 |
| API Key | API 按量付费用户 | 最直接 | 需要独立付费 |

### 3. 六大常见踩坑点

1. **环境变量配置无效**：Clawdbot 不支持 `ANTHROPIC_BASE_URL` 环境变量
2. **缺少 models 字段**：配置文件必须包含 `models: []` 字段
3. **Telegram 连接失败**：导致 Gateway 不断重启
4. **Node.js 版本过低**：需要 22.0.0 或更高版本
5. **中转 API 需要特定 User-Agent**：某些中转站要求特定 header
6. **忘记重启 Gateway**：修改配置后必须重启才能生效

### 4. 完整的故障排查流程

```bash
# 1. 检查 Gateway 状态
clawdbot channels status

# 2. 测试 API 端点
curl -s https://code.claude-opus.top/api/v1/messages \
  -H "x-api-key: 你的API密钥" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"claude-sonnet-4-5","max_tokens":100,"messages":[...]}'

# 3. 验证配置文件
cat ~/.clawdbot/clawdbot.json | jq '.models.providers.anthropic'

# 4. 重启 Gateway
clawdbot gateway restart
```
# 使用 jq 验证 JSON 格式
cat ~/.clawdbot/clawdbot.json | jq '.models'

# 验证鉴权配置
cat ~/.clawdbot/agents/main/agent/auth-profiles.json | jq '.'
```

**应用到 ClawButler**：
- 在 `apps/api/routers/config_router.py` 中增加配置验证接口
- 提供 CLI 命令 `clawbutler config validate` 验证配置文件格式
- 启动前自动检查必需字段，给出明确的错误提示

### 4. 中转 API 支持

**可借鉴点**：
- **自定义 baseUrl**：支持用户配置自己的 API 中转站
- **自定义 headers**：支持需要特定 User-Agent 的中转站
- **多层配置优先级**：自定义 JSON → 持久化状态 → 环境变量

**应用到 ClawButler**：
- 在 Federation 模块中支持自定义 API Gateway
- 允许用户为不同的 Agent 配置不同的 API 端点
- 支持 header 注入，兼容各种中转服务

### 5. 用户体验优化

**可借鉴点**：
- **快速参考卡片**：文档末尾提供常用命令速查
- **配置文件位置清单**：列出所有配置文件的路径
- **安全建议**：明确告知用户哪些操作有风险

**应用到 ClawButler**：
- 在 `docs/ops/deploy-guide.md` 中增加"快速参考"章节
- 提供配置文件路径清单和备份命令
- 在 Web UI 的危险操作前增加二次确认

### 6. 社区支持模式

**可借鉴点**：
- **推荐中转服务**：直接推荐可用的 API 中转站
- **购买链接**：提供购买链接，降低用户寻找成本
- **版本信息**：文档末尾标注教程版本和更新日期

**应用到 ClawButler**：
- 在文档中推荐兼容的 MCP Server 和 A2A 服务
- 提供 ClawButler 生态合作伙伴列表
- 文档增加版本标注和最后更新时间

## 总结

xianyu110/clawbot 虽然不是代码项目，但其文档质量和用户体验设计值得 ClawButler 学习。特别是在**多模型配置**、**故障排查流程**、**踩坑指南**等方面，可以直接应用到 ClawButler 的文档体系中，降低用户的部署和配置门槛。

<!-- lastCommit: 137e138 -->

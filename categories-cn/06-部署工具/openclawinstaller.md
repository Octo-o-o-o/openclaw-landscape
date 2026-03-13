> https://github.com/miaoxworld/OpenClawInstaller

# OpenClawInstaller - OpenClaw 一键部署工具

## 基本信息

- **项目名称**: OpenClawInstaller
- **GitHub 地址**: https://github.com/miaoxworld/OpenClawInstaller
- **Stars**: 2,978
- **Forks**: 415
- **主要语言**: Shell
- **创建时间**: 2026-01-29
- **最后更新**: 2026-03-11
- **项目标签**: clawdbot, moltbot, openclaw
- **版本**: v1.0.0

## 问题与解决方案

### 核心问题

OpenClaw 作为一个功能强大的开源个人 AI 助手平台，其部署和配置过程对普通用户存在较高门槛：

1. **环境依赖复杂**: 需要 Node.js >= 22、正确的 npm 配置、系统权限等
2. **配置繁琐**: AI 模型选择、API Key 配置、多渠道接入（Telegram、Discord、WhatsApp 等）需要手动逐项设置
3. **跨平台兼容性**: macOS、Linux、Windows 环境差异导致安装步骤不统一
4. **网络问题**: 国内用户访问 GitHub、npm 官方源速度慢或失败
5. **后续管理困难**: 服务启停、配置修改、版本更新缺乏统一工具

### 解决方案

OpenClawInstaller 通过两个核心脚本提供了完整的自动化部署和管理方案：

**1. 一键安装脚本 (install.sh)**

- **自动环境检测**: 识别操作系统（macOS/Linux/Windows WSL）、检测 Node.js 版本、验证 npm 可用性
- **智能依赖安装**: 自动安装或升级 Node.js 到 v22+，处理不同包管理器（apt/yum/brew）
- **交互式配置向导**:
  - 选择 AI 模型提供商（Anthropic Claude、OpenAI GPT、Google Gemini、OpenRouter、Groq、Mistral AI、Ollama）
  - 支持自定义 API 地址（适配 OneAPI/NewAPI 等中转服务）
  - 配置 API Key 并自动测试连接
  - 设置身份信息（姓名、时区、语言）
- **自动服务启动**: 配置完成后自动启动 OpenClaw Gateway 后台服务
- **配置持久化**: 将配置保存到 `~/.openclaw/env` 和 `~/.openclaw/openclaw.json`

**2. 配置管理菜单 (config-menu.sh)**

提供 TUI（文本用户界面）风格的可视化配置中心，包含：

- **AI 模型配置**: 支持 8+ 主流 AI 服务商，可视化选择和切换
- **消息渠道配置**:
  - Telegram Bot（自动获取 Bot Token 和 User ID）
  - Discord Bot（引导开启 Message Content Intent、获取 Channel ID）
  - WhatsApp（扫码登录，无需 Business API）
  - 飞书（长连接模式，无需公网服务器）
  - Slack、微信、iMessage（仅 macOS）
- **快速测试工具**:
  - API 连接测试
  - 渠道连接验证
  - OpenClaw 诊断工具（`openclaw doctor`）
- **高级设置**:
  - 服务管理（启动/停止/重启/状态查看）
  - 配置备份与恢复
  - 版本更新
  - 完全卸载

## 核心架构

### 技术栈

- **Shell 脚本**: Bash 4.0+，兼容 macOS/Linux/Windows WSL
- **TTY 处理**: 支持 `curl | bash` 管道模式和直接执行模式
- **颜色输出**: ANSI 转义序列实现彩色 TUI
- **配置管理**: JSON 操作（通过 `openclaw config` CLI）+ 环境变量文件

### 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                    用户交互层                                │
│  ┌──────────────┐              ┌──────────────┐            │
│  │ install.sh   │              │config-menu.sh│            │
│  │ 一键安装向导  │              │ 配置管理中心  │            │
│  └──────┬───────┘              └──────┬───────┘            │
└─────────┼──────────────────────────────┼──────────────────┘
          │                              │
          ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    自动化层                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ 环境检测     │  │ 依赖安装     │  │ 配置生成     │     │
│  │ - OS 识别    │  │ - Node.js    │  │ - env 文件   │     │
│  │ - 版本检查   │  │ - npm 包     │  │ - JSON 配置  │     │
│  │ - 权限验证   │  │ - 系统依赖   │  │ - 备份管理   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
          │                              │
          ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  OpenClaw CLI 层                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ openclaw     │  │ openclaw     │  │ openclaw     │     │
│  │ onboard      │  │ config       │  │ gateway      │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│                  配置存储层                                  │
│  ~/.openclaw/                                               │
│  ├── env                    # 环境变量（API Keys）          │
│  ├── openclaw.json          # 核心配置                      │
│  ├── backups/               # 配置备份                      │
│  └── logs/                  # 日志文件                      │
└─────────────────────────────────────────────────────────────┘
```

### 关键实现细节

**1. TTY 输入处理**

```bash
# 检测 stdin 是否为终端
if [ -t 0 ]; then
    TTY_INPUT="/dev/stdin"
else
    # 管道模式，从 /dev/tty 读取
    TTY_INPUT="/dev/tty"
fi

# 统一的读取函数
read_input() {
    local prompt="$1"
    local var_name="$2"
    echo -en "$prompt"
    read $var_name < "$TTY_INPUT"
}
```

这使得脚本既可以 `curl | bash` 运行，也可以直接执行。

**2. 多模型提供商配置**

支持自定义 API 地址的模型配置流程：

```bash
# 1. 询问是否使用自定义 API 地址
read_input "是否使用自定义 API 地址？(y/N): " use_custom

# 2. 如果使用自定义地址，先配置 baseURL
if [ "$use_custom" = "y" ]; then
    read_input "请输入 API 地址: " api_url
    export ANTHROPIC_BASE_URL="$api_url"
fi

# 3. 配置 API Key
read_input "请输入 API Key: " api_key
export ANTHROPIC_API_KEY="$api_key"

# 4. 测试连接
openclaw models test anthropic/claude-sonnet-4-20250514

# 5. 保存到配置文件
echo "export ANTHROPIC_API_KEY=$api_key" >> ~/.openclaw/env
[ -n "$api_url" ] && echo "export ANTHROPIC_BASE_URL=$api_url" >> ~/.openclaw/env
```

**3. 配置备份机制**

```bash
backup_config() {
    local backup_dir="$CONFIG_DIR/backups"
    local timestamp=$(date +%Y%m%d_%H%M%S)

    mkdir -p "$backup_dir"

    [ -f "$OPENCLAW_ENV" ] && cp "$OPENCLAW_ENV" "$backup_dir/env_$timestamp"
    [ -f "$OPENCLAW_JSON" ] && cp "$OPENCLAW_JSON" "$backup_dir/openclaw_$timestamp.json"

    log_info "配置已备份到 $backup_dir"
}
```

**4. 服务管理**

```bash
# 启动后台守护进程
start_service() {
    openclaw gateway start
    log_info "OpenClaw 已在后台启动"
}

# 查看服务状态
check_status() {
    openclaw gateway status
}

# 重启服务
restart_service() {
    openclaw gateway restart
}
```

## 关键特性

### 1. 零配置一键部署

```bash
curl -fsSL https://raw.githubusercontent.com/miaoxworld/OpenClawInstaller/main/install.sh | bash
```

单条命令完成：环境检测 → 依赖安装 → OpenClaw 安装 → 配置向导 → 服务启动。

### 2. 多模型提供商支持

| 提供商 | 模型示例 | 特色功能 |
|--------|---------|---------|
| **Anthropic Claude** | claude-sonnet-4-5, claude-opus-4-5 | 支持自定义 API 地址 |
| **OpenAI GPT** | gpt-4o, gpt-4o-mini | 支持自定义 API 地址，需支持 v1/responses |
| **Google Gemini** | gemini-2.0-flash, gemini-1.5-pro | 官方 API |
| **OpenRouter** | 多模型网关 | 一个 Key 用遍所有模型 |
| **Groq** | llama-3.3-70b-versatile | 超快推理 |
| **Mistral AI** | mistral-large-latest | 欧洲开源模型 |
| **Ollama** | llama3, mistral | 本地部署，无需 API Key |

### 3. 多渠道接入配置

- **Telegram**: 自动引导创建 Bot、获取 Token 和 User ID
- **Discord**: 详细说明开启 Message Content Intent、获取 Channel ID
- **WhatsApp**: 扫码登录，无需 Business API
- **飞书**: 长连接模式，无需 Webhook 地址和公网服务器
- **Slack、微信、iMessage**: 完整配置指南

### 4. 可视化配置中心

`config-menu.sh` 提供类似 `raspi-config` 的 TUI 界面：

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   🦞 OpenClaw 配置中心                                         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

  [1] 🏠 概览仪表板
  [2] 🤖 AI 模型配置
  [3] 📱 消息渠道配置
  [4] 🧪 快速测试
  [5] 📊 服务管理
  [6] 💾 配置备份与恢复
  [7] ⚙️  高级设置
  [0] 🚪 退出

请选择操作 [0-7]:
```

### 5. 智能诊断与测试

- **API 连接测试**: 自动测试 AI 模型 API 连接
- **渠道验证**: 测试 Telegram、Discord 等渠道配置
- **健康检查**: `openclaw doctor` 自动诊断配置问题
- **日志查看**: 实时查看和过滤日志

### 6. 配置备份与恢复

- 自动备份：每次修改配置前自动备份
- 手动备份：通过配置菜单随时备份
- 一键恢复：从备份列表选择恢复点
- 备份管理：查看、删除历史备份

### 7. Docker 支持

提供 `docker-compose.yml` 配置：

```yaml
services:
  openclaw:
    build: .
    image: openclaw:latest
    ports:
      - "18789:18789"
    volumes:
      - ~/.openclaw:/root/.openclaw
    environment:
      - TZ=Asia/Shanghai
    restart: unless-stopped
```

可选集成 Ollama 本地模型服务。
# .env
ANTHROPIC_API_KEY=sk-ant-xxx
```

**改进**：
```bash
# 支持多环境配置
clawbutlerctl config set ai.provider anthropic
clawbutlerctl config set ai.anthropic.apiKey sk-ant-xxx
clawbutlerctl config set ai.anthropic.baseUrl https://custom-proxy.com  # 可选

# 或使用配置文件
clawbutlerctl config import production.yaml
```

### 4. 健康检查和诊断

OpenClawInstaller 的 `openclaw doctor` 自动诊断，ClawButler 可以实现：

```bash
clawbutlerctl doctor

# 输出示例
Checking ClawButler Health...

✓ PostgreSQL connection (latency: 5ms)
✓ Valkey connection (latency: 2ms)
✓ API service (port 8000)
✓ Web service (port 3000)
✗ Claude API (Error: Invalid API key)
⚠ Disk space low (15% remaining)

Recommendations:
1. Update ANTHROPIC_API_KEY in .env
2. Clean up old logs: clawbutlerctl logs clean --older-than 30d
```

### 5. 渠道配置向导

OpenClawInstaller 对 Telegram、Discord、飞书等渠道的配置引导非常详细，ClawButler 可以借鉴到 Federation 配置：

```bash
clawbutlerctl federation add-peer

# 交互式向导
? Peer name: partner-org
? Peer URL: https://partner.clawbutler.cc
? Authentication method:
  ❯ Mutual TLS
    API Key
    OAuth 2.0

? Generate outbound secret? (Y/n): y
Generated: cb_secret_abc123...

? Test connection? (Y/n): y
Testing connection to https://partner.clawbutler.cc... ✓

Peer added successfully!
Next steps:
1. Share this inbound secret with partner: cb_inbound_xyz789
2. Ask partner to add your instance as peer
3. Run: clawbutlerctl federation test partner-org
```

### 6. Docker 部署优化

OpenClawInstaller 的 `docker-compose.yml` 包含健康检查、日志轮转、可选服务（Ollama），ClawButler 可以增强：

**当前 ClawButler docker-compose.yml**：
```yaml
services:
  api:
    build: ./apps/api
    ports:
      - "8000:8000"
  web:
    build: ./apps/web
    ports:
      - "3000:3000"
  postgres:
    image: postgres:17
  valkey:
    image: valkey/valkey:8
```

**改进**：
```yaml
services:
  api:
    build: ./apps/api
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    restart: unless-stopped

  # 可选：本地 AI 模型服务
  ollama:
    image: ollama/ollama:latest
    profiles: ["local-ai"]  # 通过 --profile local-ai 启用
    ports:
      - "11434:11434"
    volumes:
      - ollama-data:/root/.ollama
```

### 7. 配置文件模板

OpenClawInstaller 提供 `examples/config.example.yaml`，ClawButler 可以提供：

```bash
clawbutlerctl config init --template production
# 生成 .env.production 模板，包含所有配置项和注释

clawbutlerctl config init --template development
# 生成 .env.development 模板，使用开发环境默认值
```

### 8. 更新和版本管理

OpenClawInstaller 的配置菜单包含版本更新功能，ClawButler 可以增强 `clawbutlerctl update`：

```bash
clawbutlerctl update

# 输出
Checking for updates...
Current version: v2.5.0
Latest version: v2.6.0

Changelog:
- Config Safety V2.1: Rollback preview
- Verified Templates V2.6: Post-deploy checks
- Runbook: Multi-backend dispatcher

? Update to v2.6.0? (Y/n): y

Backing up current configuration...
Pulling latest code...
Rebuilding containers...
Running migrations...
Restarting services...

Update completed! ✓
```

### 9. 安全配置向导

OpenClawInstaller 在初始化时会提示安全风险，ClawButler 可以增加安全配置检查：

```bash
clawbutlerctl security check

# 输出
Security Audit Report:

⚠ CRITICAL:
- SECRET_KEY is using default value
- Database password is weak (< 12 characters)
- HTTPS not enabled

⚠ WARNING:
- CORS_ALLOWED_ORIGINS set to "*"
- DEBUG mode enabled in production

✓ PASSED:
- API rate limiting enabled
- JWT token expiration configured

Run 'clawbutlerctl security fix' to auto-fix issues.
```

### 10. 国内网络优化

OpenClawInstaller 考虑了国内网络环境（npm 镜像源、GitHub 加速），ClawButler 的安装脚本可以增加：

```bash
# install.sh 检测网络环境
if is_in_china; then
    log_info "检测到国内网络环境，使用加速源..."

    # Docker 镜像使用国内源
    DOCKER_REGISTRY="registry.cn-hangzhou.aliyuncs.com"

    # npm 使用淘宝镜像
    npm config set registry https://registry.npmmirror.com

    # GitHub 使用代理
    git config --global url."https://ghproxy.com/https://github.com/".insteadOf "https://github.com/"
fi
```

### 总结

OpenClawInstaller 最值得 ClawButler 借鉴的三个核心设计：

1. **交互式配置向导**：降低初始化门槛，每步配置后立即测试
2. **TUI 配置中心**：提供 `clawbutlerctl config menu` 可视化管理
3. **健康检查和诊断**：`clawbutlerctl doctor` 自动发现和修复配置问题

这些功能可以显著提升 ClawButler 的用户体验，特别是对于非技术用户和企业部署场景。

<!-- lastCommit: 137e138 -->

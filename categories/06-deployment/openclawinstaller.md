> https://github.com/miaoxworld/OpenClawInstaller

# OpenClawInstaller - OpenClaw One-Click Deployment Tool

## Basic Information

- **Project Name**: OpenClawInstaller
- **GitHub URL**: https://github.com/miaoxworld/OpenClawInstaller
- **Stars**: 2,978
- **Forks**: 415
- **Primary Language**: Shell
- **Created**: 2026-01-29
- **Last Updated**: 2026-03-11
- **Project Tags**: clawdbot, moltbot, openclaw
- **Version**: v1.0.0

## Problem and Solution

### Core Problem

OpenClaw is a powerful open-source personal AI assistant platform, but its deployment and configuration process presents a high barrier for ordinary users:

1. **Complex environment dependencies**: Requires Node.js >= 22, correct npm configuration, system permissions, etc.
2. **Tedious configuration**: AI model selection, API Key setup, multi-channel integration (Telegram, Discord, WhatsApp, etc.) all require manual step-by-step configuration
3. **Cross-platform compatibility**: Differences between macOS, Linux, and Windows environments lead to inconsistent installation steps
4. **Network issues**: Users in China experience slow or failed access to GitHub and the official npm registry
5. **Difficult ongoing management**: Service start/stop, configuration changes, and version updates lack a unified tool

### Solution

OpenClawInstaller provides a complete automated deployment and management solution through two core scripts:

**1. One-Click Installation Script (install.sh)**

- **Automatic environment detection**: Identifies the operating system (macOS/Linux/Windows WSL), checks Node.js version, verifies npm availability
- **Smart dependency installation**: Automatically installs or upgrades Node.js to v22+, handles different package managers (apt/yum/brew)
- **Interactive configuration wizard**:
  - Select AI model provider (Anthropic Claude, OpenAI GPT, Google Gemini, OpenRouter, Groq, Mistral AI, Ollama)
  - Support for custom API endpoints (compatible with OneAPI/NewAPI relay services)
  - Configure API Key with automatic connection testing
  - Set identity information (name, timezone, language)
- **Automatic service startup**: Automatically starts the OpenClaw Gateway background service after configuration
- **Configuration persistence**: Saves configuration to `~/.openclaw/env` and `~/.openclaw/openclaw.json`

**2. Configuration Management Menu (config-menu.sh)**

Provides a TUI (Text User Interface) style visual configuration center, including:

- **AI model configuration**: Supports 8+ mainstream AI providers with visual selection and switching
- **Messaging channel configuration**:
  - Telegram Bot (automatic Bot Token and User ID retrieval)
  - Discord Bot (guides enabling Message Content Intent, obtaining Channel ID)
  - WhatsApp (QR code login, no Business API required)
  - Feishu/Lark (long-connection mode, no public server required)
  - Slack, WeChat, iMessage (macOS only)
- **Quick testing tools**:
  - API connection testing
  - Channel connection verification
  - OpenClaw diagnostic tool (`openclaw doctor`)
- **Advanced settings**:
  - Service management (start/stop/restart/status)
  - Configuration backup and restore
  - Version updates
  - Complete uninstallation

## Core Architecture

### Tech Stack

- **Shell scripts**: Bash 4.0+, compatible with macOS/Linux/Windows WSL
- **TTY handling**: Supports both `curl | bash` piped mode and direct execution mode
- **Color output**: ANSI escape sequences for colorful TUI
- **Configuration management**: JSON operations (via `openclaw config` CLI) + environment variable files

### Architecture Design

```
+-------------------------------------------------------------+
|                    User Interaction Layer                     |
|  +--------------+              +--------------+              |
|  | install.sh   |              |config-menu.sh|              |
|  | One-click    |              | Configuration|              |
|  | Install      |              | Management   |              |
|  +------+-------+              +------+-------+              |
+---------+----------------------------+----------------------+
          |                            |
          v                            v
+-------------------------------------------------------------+
|                    Automation Layer                           |
|  +--------------+  +--------------+  +--------------+       |
|  | Environment  |  | Dependency   |  | Configuration|       |
|  | Detection    |  | Installation |  | Generation   |       |
|  | - OS ID      |  | - Node.js    |  | - env file   |       |
|  | - Version    |  | - npm pkgs   |  | - JSON config|       |
|  | - Permission |  | - System deps|  | - Backup mgmt|       |
|  +--------------+  +--------------+  +--------------+       |
+-------------------------------------------------------------+
          |                            |
          v                            v
+-------------------------------------------------------------+
|                  OpenClaw CLI Layer                           |
|  +--------------+  +--------------+  +--------------+       |
|  | openclaw     |  | openclaw     |  | openclaw     |       |
|  | onboard      |  | config       |  | gateway      |       |
|  +--------------+  +--------------+  +--------------+       |
+-------------------------------------------------------------+
          |
          v
+-------------------------------------------------------------+
|                  Configuration Storage Layer                 |
|  ~/.openclaw/                                               |
|  |- env                    # Environment variables (API Keys)|
|  |- openclaw.json          # Core configuration              |
|  |- backups/               # Configuration backups           |
|  +- logs/                  # Log files                       |
+-------------------------------------------------------------+
```

### Key Implementation Details

**1. TTY Input Handling**

```bash
# Check if stdin is a terminal
if [ -t 0 ]; then
    TTY_INPUT="/dev/stdin"
else
    # Piped mode, read from /dev/tty
    TTY_INPUT="/dev/tty"
fi

# Unified read function
read_input() {
    local prompt="$1"
    local var_name="$2"
    echo -en "$prompt"
    read $var_name < "$TTY_INPUT"
}
```

This allows the script to run both via `curl | bash` and direct execution.

**2. Multi-Model Provider Configuration**

Model configuration flow with custom API endpoint support:

```bash
# 1. Ask whether to use a custom API endpoint
read_input "Use custom API endpoint? (y/N): " use_custom

# 2. If using a custom endpoint, configure baseURL first
if [ "$use_custom" = "y" ]; then
    read_input "Enter API endpoint: " api_url
    export ANTHROPIC_BASE_URL="$api_url"
fi

# 3. Configure API Key
read_input "Enter API Key: " api_key
export ANTHROPIC_API_KEY="$api_key"

# 4. Test connection
openclaw models test anthropic/claude-sonnet-4-20250514

# 5. Save to configuration file
echo "export ANTHROPIC_API_KEY=$api_key" >> ~/.openclaw/env
[ -n "$api_url" ] && echo "export ANTHROPIC_BASE_URL=$api_url" >> ~/.openclaw/env
```

**3. Configuration Backup Mechanism**

```bash
backup_config() {
    local backup_dir="$CONFIG_DIR/backups"
    local timestamp=$(date +%Y%m%d_%H%M%S)

    mkdir -p "$backup_dir"

    [ -f "$OPENCLAW_ENV" ] && cp "$OPENCLAW_ENV" "$backup_dir/env_$timestamp"
    [ -f "$OPENCLAW_JSON" ] && cp "$OPENCLAW_JSON" "$backup_dir/openclaw_$timestamp.json"

    log_info "Configuration backed up to $backup_dir"
}
```

**4. Service Management**

```bash
# Start background daemon
start_service() {
    openclaw gateway start
    log_info "OpenClaw started in background"
}

# Check service status
check_status() {
    openclaw gateway status
}

# Restart service
restart_service() {
    openclaw gateway restart
}
```

## Key Features

### 1. Zero-Configuration One-Click Deployment

```bash
curl -fsSL https://raw.githubusercontent.com/miaoxworld/OpenClawInstaller/main/install.sh | bash
```

A single command completes: environment detection -> dependency installation -> OpenClaw installation -> configuration wizard -> service startup.

### 2. Multi-Model Provider Support

| Provider | Example Models | Special Features |
|----------|---------------|-----------------|
| **Anthropic Claude** | claude-sonnet-4-5, claude-opus-4-5 | Custom API endpoint support |
| **OpenAI GPT** | gpt-4o, gpt-4o-mini | Custom API endpoint support, requires v1/responses support |
| **Google Gemini** | gemini-2.0-flash, gemini-1.5-pro | Official API |
| **OpenRouter** | Multi-model gateway | One key for all models |
| **Groq** | llama-3.3-70b-versatile | Ultra-fast inference |
| **Mistral AI** | mistral-large-latest | European open-source model |
| **Ollama** | llama3, mistral | Local deployment, no API Key required |

### 3. Multi-Channel Integration Configuration

- **Telegram**: Automatically guides Bot creation, Token and User ID retrieval
- **Discord**: Detailed instructions for enabling Message Content Intent and obtaining Channel ID
- **WhatsApp**: QR code login, no Business API required
- **Feishu/Lark**: Long-connection mode, no Webhook URL or public server required
- **Slack, WeChat, iMessage**: Complete configuration guides

### 4. Visual Configuration Center

`config-menu.sh` provides a TUI interface similar to `raspi-config`:

```
+===============================================================+
|                                                               |
|   OpenClaw Configuration Center                               |
|                                                               |
+===============================================================+

  [1] Overview Dashboard
  [2] AI Model Configuration
  [3] Messaging Channel Configuration
  [4] Quick Testing
  [5] Service Management
  [6] Configuration Backup & Restore
  [7] Advanced Settings
  [0] Exit

Select an option [0-7]:
```

### 5. Smart Diagnostics and Testing

- **API connection testing**: Automatically tests AI model API connections
- **Channel verification**: Tests Telegram, Discord, and other channel configurations
- **Health check**: `openclaw doctor` automatically diagnoses configuration issues
- **Log viewing**: Real-time log viewing and filtering

### 6. Configuration Backup and Restore

- Automatic backup: Automatically backs up before each configuration change
- Manual backup: Backup anytime via the configuration menu
- One-click restore: Select a restore point from the backup list
- Backup management: View and delete historical backups

### 7. Docker Support

Provides `docker-compose.yml` configuration:

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

Optional integration with Ollama local model service.

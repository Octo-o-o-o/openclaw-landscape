> https://github.com/xianyu110/clawbot

# xianyu110/clawbot

## Basic Information

- **Stars**: 856
- **URL**: https://github.com/xianyu110/clawbot
- **Status**: Actively maintained

## Problem & Solution

### Core Problem
Clawbot is a comprehensive Chinese configuration guide for OpenClaw, addressing the following pain points Chinese users encounter when deploying and configuring OpenClaw:

1. **Official documentation is primarily in English**: Lacks systematic Chinese installation tutorials
2. **High configuration complexity**: Multiple configuration files, environment variables, and authentication methods confuse beginners
3. **Difficult API proxy configuration**: Chinese users need to use API proxies, but the configuration methods are unclear
4. **Frequent common errors**: Issues like invalid environment variables, configuration format errors, and service startup failures

### Solution
Provides a complete Chinese deployment guide including:

- **Step-by-step installation tutorial**: Complete workflow from Node.js upgrade to initial configuration
- **Authentication method comparison**: Use cases for setup-token, Claude Code CLI, and API Key
- **API proxy configuration**: Support for multi-model proxies and Claude Code dedicated proxies
- **Pitfall guide**: Summarizes 6 major common errors and their solutions
- **Command quick reference**: Gateway management, configuration management, log viewing, etc.

## Core Architecture

### Documentation Structure

```
README.md
├── Introduction
├── System Requirements
├── Installation Steps
│   ├── Upgrade Node.js
│   ├── Choose Installation Method (npm/script/source)
│   └── Initial Configuration Wizard
├── Configure Custom Proxy
│   ├── Option 1: Multi-Model Proxy (GPT/Claude/Gemini)
│   └── Option 2: Claude Code Proxy (requires User-Agent)
├── Verification and Testing
├── Common Pitfalls (6)
├── FAQ (5)
└── Common Commands
```

### Configuration File Hierarchy

```
~/.clawdbot/
├── clawdbot.json              # Main configuration file
│   ├── models.providers       # Model provider configuration
│   ├── agents.defaults        # Agent default configuration
│   ├── gateway                # Gateway configuration
│   └── channels               # Channel configuration
├── agents/main/agent/
│   └── auth-profiles.json     # Authentication configuration
└── logs/
    ├── gateway.log            # Main log
    └── gateway.err.log        # Error log
```

## Key Features

### 1. Multi-Model Proxy Configuration

**Supports configuring multiple AI model providers simultaneously**:

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

### 2. Authentication Method Comparison

| Authentication Method | Use Case | Pros | Cons |
|----------------------|----------|------|------|
| setup-token | Claude Max/Pro subscribers | No additional cost | Requires extra steps to generate token |
| Claude Code CLI | Users with Claude Code configured | Automatically reads credentials | May not find credential files |
| API Key | API pay-per-use users | Most straightforward | Requires separate payment |

### 3. Six Common Pitfalls

1. **Environment variable configuration not working**: Clawdbot does not support the `ANTHROPIC_BASE_URL` environment variable
2. **Missing models field**: Configuration file must include the `models: []` field
3. **Telegram connection failure**: Causes Gateway to restart continuously
4. **Node.js version too low**: Requires version 22.0.0 or higher
5. **Proxy API requires specific User-Agent**: Some proxies require a specific header
6. **Forgetting to restart Gateway**: Must restart after modifying configuration

### 4. Complete Troubleshooting Workflow

```bash
# 1. Check Gateway status
clawdbot channels status

# 2. Test API endpoint
curl -s https://code.claude-opus.top/api/v1/messages \
  -H "x-api-key: your-api-key" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"claude-sonnet-4-5","max_tokens":100,"messages":[...]}'

# 3. Verify configuration file
cat ~/.clawdbot/clawdbot.json | jq '.models.providers.anthropic'

# 4. Restart Gateway
clawdbot gateway restart
```
```bash
# Validate JSON format using jq
cat ~/.clawdbot/clawdbot.json | jq '.models'

# Verify authentication configuration
cat ~/.clawdbot/agents/main/agent/auth-profiles.json | jq '.'
```

# openclaw/acpx

## 基本信息

- **Stars**: 719
- **URL**: https://github.com/openclaw/acpx
- **定位**: Agent Client Protocol (ACP) 的无头 CLI 客户端
- **技术栈**: TypeScript + Node.js + pnpm
- **状态**: Alpha 阶段，API 可能变更
- **协议覆盖**: 参见 [ACP Spec Coverage Roadmap](docs/2026-02-19-acp-coverage-roadmap.md)

## 问题与解决方案

### 核心问题

1. **PTY 抓取的脆弱性**: AI Agent 编排器通过伪终端（PTY）与编码 Agent 交互，需要解析 ANSI 转义序列和文本输出，容易出错且难以维护
2. **缺乏结构化协议**: 传统 CLI 工具输出非结构化文本，Agent 难以可靠地提取工具调用、思考过程、文件变更等信息
3. **会话管理混乱**: 多个 Agent 任务并行时，会话状态难以隔离和恢复
4. **权限控制缺失**: 无法细粒度控制 Agent 的文件读写和命令执行权限
5. **跨 Agent 平台碎片化**: 不同编码 Agent（OpenClaw、Codex、Claude Code 等）有各自的 CLI 接口，编排器需要适配多套协议

### 解决方案

acpx 提供了一个**统一的 ACP 客户端**，让 AI 编排器可以：

- **结构化通信**: 通过 JSON-RPC 2.0 协议与编码 Agent 交互，获取类型化的事件流（thinking、tool_call、diff 等）
- **持久化会话**: 支持多轮对话，会话状态保存在磁盘，可跨进程恢复
- **命名会话**: 同一仓库内并行运行多个独立工作流（如 `-s backend` 和 `-s frontend`）
- **队列机制**: 提示（prompt）排队执行，避免并发冲突
- **协作式取消**: 通过 ACP `session/cancel` 优雅中断任务，而非强制杀进程
- **权限控制**: 细粒度的文件读写和命令执行权限（`--approve-all`、`--approve-reads`、`--deny-all`）
- **统一接口**: 一套命令适配 Pi、OpenClaw、Codex、Claude Code、Gemini、Cursor、Copilot、Kimi、Kiro 等多个 ACP 兼容 Agent

## 核心架构

### 1. 会话管理

#### 会话作用域

- **目录作用域**: 会话绑定到 Git 仓库根目录（或当前目录，如果不在 Git 仓库中）
- **命名会话**: 使用 `-s <name>` 创建并行会话（如 `-s api`、`-s docs`）
- **自动路由**: 提示命令从当前目录向上查找最近的活跃会话

#### 会话生命周期

```bash
# 创建新会话（显式）
acpx codex sessions new
acpx codex sessions new --name api

# 确保会话存在（幂等）
acpx codex sessions ensure
acpx codex sessions ensure --name api

# 发送提示（隐式路由）
acpx codex "fix the tests"
acpx codex -s api "implement token pagination"

# 关闭会话（软关闭，保留历史）
acpx codex sessions close
acpx codex sessions close api

# 查看会话状态
acpx codex sessions list
acpx codex sessions show
acpx codex sessions history --limit 10
acpx codex status
```

#### 会话持久化

- **元数据存储**: `~/.acpx/sessions/`
- **历史记录**: 每次成功的提示追加轻量级历史预览（`role`、`timestamp`、`textPreview`）
- **崩溃恢复**: 如果保存的会话进程已死，acpx 自动重启 Agent 并尝试 `session/load`，失败则回退到 `session/new`

### 2. 队列机制

#### 提示队列

- **串行执行**: 同一会话的提示按提交顺序排队执行
- **队列所有者**: 第一个提示的 acpx 进程成为队列所有者，负责排空队列
- **TTL 机制**: 队列所有者在空闲后保持活跃一段时间（默认 300 秒），等待后续提示
- **无等待模式**: `--no-wait` 提交提示后立即返回，不等待执行完成

```bash
# 提交提示并等待完成
acpx codex "fix the tests"

# 提交提示并立即返回
acpx codex --no-wait "draft test migration plan"

# 取消正在运行的提示
acpx codex cancel
```

#### 队列 IPC

- **进程间通信**: 使用 Unix domain socket 或命名管道
- **命令路由**: `set-mode`、`set`、`cancel` 通过 IPC 发送到队列所有者
- **优雅降级**: 如果队列所有者不存在，直接连接 Agent 进程执行命令

### 3. 权限控制

#### 权限模式

```bash
# 自动批准所有操作
acpx --approve-all codex "apply the patch and run tests"

# 仅批准读操作（默认）
acpx --approve-reads codex "inspect repo structure"

# 拒绝所有操作
acpx --deny-all codex "explain what you can do without tool access"

# 非交互模式下的行为
acpx --non-interactive-permissions fail codex "fail instead of deny in non-TTY"
```

#### 客户端方法

acpx 实现了稳定的 ACP 客户端方法处理器：

- **文件系统**: `fs/read_file`、`fs/write_file`、`fs/list_directory` 等
- **终端**: `terminal/run_command`、`terminal/get_env` 等
- **权限检查**: 基于配置的权限策略，决定批准/拒绝/提示用户
- **cwd 沙箱**: 限制文件操作在会话的工作目录内

### 4. 配置系统

#### 配置文件层级

1. **全局配置**: `~/.acpx/config.json`
2. **项目配置**: `<cwd>/.acpxrc.json`
3. **命令行参数**: 优先级最高

```bash
# 查看合并后的配置
acpx config show

# 创建全局配置模板
acpx config init
```

#### 配置选项

```json
{
  "defaultAgent": "codex",
  "defaultPermissions": "approve-all",
  "nonInteractivePermissions": "deny",
  "authPolicy": "skip",
  "ttl": 300,
  "timeout": null,
  "format": "text",
  "agents": {
    "my-custom": { "command": "./bin/my-acp-server" }
  },
  "auth": {
    "my_auth_method_id": "credential-value"
  }
}
```

### 5. Agent 注册表

#### 内置 Agent

| Agent      | 适配器                                                                 | 底层工具                                                                                                        |
| ---------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `pi`       | [pi-acp](https://github.com/svkozak/pi-acp)                            | [Pi Coding Agent](https://github.com/mariozechner/pi)                                                           |
| `openclaw` | 原生 (`openclaw acp`)                                                  | [OpenClaw ACP bridge](https://github.com/openclaw/openclaw)                                                     |
| `codex`    | [codex-acp](https://github.com/zed-industries/codex-acp)               | [Codex CLI](https://codex.openai.com)                                                                           |
| `claude`   | [claude-agent-acp](https://github.com/zed-industries/claude-agent-acp) | [Claude Code](https://claude.ai/code)                                                                           |
| `gemini`   | 原生 (`gemini --experimental-acp`)                                     | [Gemini CLI](https://github.com/google/gemini-cli)                                                              |
| `cursor`   | 原生 (`cursor-agent acp`)                                              | [Cursor CLI](https://cursor.com/docs/cli/acp)                                                                   |
| `copilot`  | 原生 (`copilot --acp --stdio`)                                         | [GitHub Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-chat/use-copilot-chat-in-the-command-line) |
| `kimi`     | 原生 (`kimi acp`)                                                      | [Kimi CLI](https://github.com/MoonshotAI/kimi-cli)                                                              |
| `opencode` | `npx -y opencode-ai acp`                                               | [OpenCode](https://opencode.ai)                                                                                 |
| `kiro`     | 原生 (`kiro-cli acp`)                                                  | [Kiro CLI](https://kiro.dev)                                                                                    |
| `kilocode` | `npx -y @kilocode/cli acp`                                             | [Kilocode](https://kilocode.ai)                                                                                 |
| `qwen`     | 原生 (`qwen --acp`)                                                    | [Qwen Code](https://github.com/QwenLM/qwen-code)                                                                |

#### 自定义 Agent

```bash
# 命令行指定
acpx --agent ./my-custom-acp-server "do something"

# 配置文件注册
{
  "agents": {
    "my-agent": { "command": "./bin/my-acp-server" }
  }
}

# 使用自定义 Agent
acpx my-agent "review this patch"
```

### 6. 输出格式

#### 文本模式（默认）

```bash
acpx codex "fix the tests"
```

输出人类可读的流式更新：

```
[thinking] Investigating test suite for flaky failures
[tool] Run npm test -- --reporter=verbose (running)
[tool] Run npm test -- --reporter=verbose (completed)
  output: ...
[done] end_turn
```

#### JSON 模式

```bash
acpx --format json codex exec "review this PR"
```

输出 NDJSON 事件流，每行一个 JSON 对象：

```json
{
  "eventVersion": 1,
  "sessionId": "abc123",
  "requestId": "req-42",
  "seq": 7,
  "stream": "prompt",
  "type": "tool_call",
  "status": "completed",
  "title": "Run npm test"
}
```

#### JSON 严格模式

```bash
acpx --format json --json-strict codex exec "review this PR"
```

抑制非 JSON 的 stderr 输出，确保输出可被 `jq` 等工具解析。

#### 安静模式

```bash
acpx --format quiet codex "give me a 3-line summary"
```

仅输出最终的 Assistant 文本，适合脚本集成。

### 7. 一次性执行模式

```bash
# 无状态执行，不保存会话
acpx codex exec "summarize this repo"
acpx exec "what does this repo do?"  # 使用默认 Agent
```

适用场景：
- 快速查询
- 无需上下文的任务
- 自动化脚本

## 关键特性

### 1. 持久化会话

- **多轮对话**: 会话状态跨 acpx 进程调用保持
- **历史记录**: 自动保存对话历史，支持上下文延续
- **崩溃恢复**: Agent 进程崩溃后自动重启并恢复会话

### 2. 命名会话

- **并行工作流**: 同一仓库内运行多个独立任务
- **作用域隔离**: 不同命名会话互不干扰
- **灵活切换**: 使用 `-s <name>` 快速切换工作流

### 3. 队列机制

- **串行执行**: 避免并发冲突
- **提示排队**: 繁忙时自动排队，空闲时立即执行
- **无等待提交**: `--no-wait` 支持异步任务提交

### 4. 协作式取消

- **优雅中断**: 通过 ACP `session/cancel` 请求 Agent 停止
- **状态保留**: 取消后会话状态仍然保存，可继续使用
- **Ctrl+C 支持**: 终端中断信号自动转换为 ACP 取消请求

### 5. 权限控制

- **细粒度策略**: 区分读操作、写操作、命令执行
- **交互式提示**: TTY 环境下可逐个批准操作
- **非交互模式**: 自动批准/拒绝，适合 CI/CD

### 6. 结构化输出

- **类型化事件**: thinking、tool_call、diff、error 等
- **机器可读**: JSON 格式适合自动化处理
- **人类友好**: 文本模式提供清晰的进度反馈

### 7. 统一接口

- **一套命令**: 适配 12+ 个 ACP 兼容 Agent
- **自动下载适配器**: 首次使用时通过 `npx` 自动安装
- **扩展性**: 支持自定义 Agent 注册

### 8. 配置灵活性

- **全局 + 项目**: 支持多层级配置
- **命令行覆盖**: 临时调整参数无需修改配置文件
- **认证集成**: 支持多种认证方法（环境变量、配置文件）

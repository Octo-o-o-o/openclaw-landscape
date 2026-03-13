> https://github.com/openclaw/acpx

# openclaw/acpx

## Basic Information

- **Stars**: 719
- **URL**: https://github.com/openclaw/acpx
- **Purpose**: Headless CLI client for the Agent Client Protocol (ACP)
- **Tech Stack**: TypeScript + Node.js + pnpm
- **Status**: Alpha stage, API subject to change
- **Protocol Coverage**: See [ACP Spec Coverage Roadmap](docs/2026-02-19-acp-coverage-roadmap.md)

## Problem & Solution

### Core Problems

1. **Fragility of PTY scraping**: AI Agent orchestrators interact with coding agents through pseudo-terminals (PTY), requiring parsing of ANSI escape sequences and text output, which is error-prone and hard to maintain
2. **Lack of structured protocol**: Traditional CLI tools produce unstructured text output, making it difficult for agents to reliably extract tool calls, thinking processes, file changes, etc.
3. **Chaotic session management**: When multiple agent tasks run in parallel, session state is difficult to isolate and restore
4. **Missing permission controls**: No fine-grained control over an agent's file read/write and command execution permissions
5. **Cross-agent platform fragmentation**: Different coding agents (OpenClaw, Codex, Claude Code, etc.) each have their own CLI interface, forcing orchestrators to adapt to multiple protocols

### Solution

acpx provides a **unified ACP client** that enables AI orchestrators to:

- **Structured communication**: Interact with coding agents via JSON-RPC 2.0 protocol, receiving typed event streams (thinking, tool_call, diff, etc.)
- **Persistent sessions**: Support multi-turn conversations with session state saved to disk, recoverable across processes
- **Named sessions**: Run multiple independent workflows in parallel within the same repository (e.g., `-s backend` and `-s frontend`)
- **Queue mechanism**: Prompts are queued for serial execution, avoiding concurrency conflicts
- **Cooperative cancellation**: Gracefully interrupt tasks via ACP `session/cancel` instead of force-killing processes
- **Permission control**: Fine-grained file read/write and command execution permissions (`--approve-all`, `--approve-reads`, `--deny-all`)
- **Unified interface**: One set of commands supporting Pi, OpenClaw, Codex, Claude Code, Gemini, Cursor, Copilot, Kimi, Kiro, and other ACP-compatible agents

## Core Architecture

### 1. Session Management

#### Session Scoping

- **Directory scoping**: Sessions are bound to the Git repository root (or the current directory if not in a Git repo)
- **Named sessions**: Use `-s <name>` to create parallel sessions (e.g., `-s api`, `-s docs`)
- **Auto-routing**: Prompt commands search upward from the current directory to find the nearest active session

#### Session Lifecycle

```bash
# Create a new session (explicit)
acpx codex sessions new
acpx codex sessions new --name api

# Ensure a session exists (idempotent)
acpx codex sessions ensure
acpx codex sessions ensure --name api

# Send a prompt (implicit routing)
acpx codex "fix the tests"
acpx codex -s api "implement token pagination"

# Close a session (soft close, preserves history)
acpx codex sessions close
acpx codex sessions close api

# View session status
acpx codex sessions list
acpx codex sessions show
acpx codex sessions history --limit 10
acpx codex status
```

#### Session Persistence

- **Metadata storage**: `~/.acpx/sessions/`
- **History records**: Each successful prompt appends a lightweight history preview (`role`, `timestamp`, `textPreview`)
- **Crash recovery**: If a saved session's process has died, acpx automatically restarts the agent and attempts `session/load`, falling back to `session/new` on failure

### 2. Queue Mechanism

#### Prompt Queue

- **Serial execution**: Prompts within the same session are queued and executed in submission order
- **Queue owner**: The first prompt's acpx process becomes the queue owner, responsible for draining the queue
- **TTL mechanism**: The queue owner remains active for a period after going idle (default 300 seconds), waiting for subsequent prompts
- **No-wait mode**: `--no-wait` submits a prompt and returns immediately without waiting for completion

```bash
# Submit a prompt and wait for completion
acpx codex "fix the tests"

# Submit a prompt and return immediately
acpx codex --no-wait "draft test migration plan"

# Cancel a running prompt
acpx codex cancel
```

#### Queue IPC

- **Inter-process communication**: Uses Unix domain sockets or named pipes
- **Command routing**: `set-mode`, `set`, `cancel` are sent via IPC to the queue owner
- **Graceful degradation**: If the queue owner doesn't exist, commands connect directly to the agent process

### 3. Permission Control

#### Permission Modes

```bash
# Auto-approve all operations
acpx --approve-all codex "apply the patch and run tests"

# Approve reads only (default)
acpx --approve-reads codex "inspect repo structure"

# Deny all operations
acpx --deny-all codex "explain what you can do without tool access"

# Behavior in non-interactive mode
acpx --non-interactive-permissions fail codex "fail instead of deny in non-TTY"
```

#### Client Methods

acpx implements stable ACP client method handlers:

- **Filesystem**: `fs/read_file`, `fs/write_file`, `fs/list_directory`, etc.
- **Terminal**: `terminal/run_command`, `terminal/get_env`, etc.
- **Permission checking**: Approves/denies/prompts the user based on configured permission policies
- **cwd sandboxing**: Restricts file operations to within the session's working directory

### 4. Configuration System

#### Configuration File Hierarchy

1. **Global config**: `~/.acpx/config.json`
2. **Project config**: `<cwd>/.acpxrc.json`
3. **Command-line arguments**: Highest priority

```bash
# View merged configuration
acpx config show

# Create a global config template
acpx config init
```

#### Configuration Options

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

### 5. Agent Registry

#### Built-in Agents

| Agent      | Adapter                                                                 | Underlying Tool                                                                                                 |
| ---------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `pi`       | [pi-acp](https://github.com/svkozak/pi-acp)                            | [Pi Coding Agent](https://github.com/mariozechner/pi)                                                           |
| `openclaw` | Native (`openclaw acp`)                                                 | [OpenClaw ACP bridge](https://github.com/openclaw/openclaw)                                                     |
| `codex`    | [codex-acp](https://github.com/zed-industries/codex-acp)               | [Codex CLI](https://codex.openai.com)                                                                           |
| `claude`   | [claude-agent-acp](https://github.com/zed-industries/claude-agent-acp) | [Claude Code](https://claude.ai/code)                                                                           |
| `gemini`   | Native (`gemini --experimental-acp`)                                    | [Gemini CLI](https://github.com/google/gemini-cli)                                                              |
| `cursor`   | Native (`cursor-agent acp`)                                             | [Cursor CLI](https://cursor.com/docs/cli/acp)                                                                   |
| `copilot`  | Native (`copilot --acp --stdio`)                                        | [GitHub Copilot CLI](https://docs.github.com/copilot/how-tos/copilot-chat/use-copilot-chat-in-the-command-line) |
| `kimi`     | Native (`kimi acp`)                                                     | [Kimi CLI](https://github.com/MoonshotAI/kimi-cli)                                                              |
| `opencode` | `npx -y opencode-ai acp`                                               | [OpenCode](https://opencode.ai)                                                                                 |
| `kiro`     | Native (`kiro-cli acp`)                                                 | [Kiro CLI](https://kiro.dev)                                                                                    |
| `kilocode` | `npx -y @kilocode/cli acp`                                             | [Kilocode](https://kilocode.ai)                                                                                 |
| `qwen`     | Native (`qwen --acp`)                                                   | [Qwen Code](https://github.com/QwenLM/qwen-code)                                                                |

#### Custom Agents

```bash
# Specify via command line
acpx --agent ./my-custom-acp-server "do something"

# Register in config file
{
  "agents": {
    "my-agent": { "command": "./bin/my-acp-server" }
  }
}

# Use the custom agent
acpx my-agent "review this patch"
```

### 6. Output Formats

#### Text Mode (Default)

```bash
acpx codex "fix the tests"
```

Outputs human-readable streaming updates:

```
[thinking] Investigating test suite for flaky failures
[tool] Run npm test -- --reporter=verbose (running)
[tool] Run npm test -- --reporter=verbose (completed)
  output: ...
[done] end_turn
```

#### JSON Mode

```bash
acpx --format json codex exec "review this PR"
```

Outputs an NDJSON event stream, one JSON object per line:

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

#### JSON Strict Mode

```bash
acpx --format json --json-strict codex exec "review this PR"
```

Suppresses non-JSON stderr output, ensuring output is parseable by tools like `jq`.

#### Quiet Mode

```bash
acpx --format quiet codex "give me a 3-line summary"
```

Outputs only the final assistant text, suitable for script integration.

### 7. One-shot Execution Mode

```bash
# Stateless execution, no session saved
acpx codex exec "summarize this repo"
acpx exec "what does this repo do?"  # Uses default agent
```

Use cases:
- Quick queries
- Tasks that don't need context
- Automation scripts

## Key Features

### 1. Persistent Sessions

- **Multi-turn conversations**: Session state persists across acpx process invocations
- **History records**: Automatically saves conversation history, supporting context continuation
- **Crash recovery**: Automatically restarts and recovers sessions after agent process crashes

### 2. Named Sessions

- **Parallel workflows**: Run multiple independent tasks within the same repository
- **Scope isolation**: Different named sessions don't interfere with each other
- **Flexible switching**: Use `-s <name>` to quickly switch workflows

### 3. Queue Mechanism

- **Serial execution**: Avoids concurrency conflicts
- **Prompt queuing**: Automatically queues when busy, executes immediately when idle
- **No-wait submission**: `--no-wait` supports asynchronous task submission

### 4. Cooperative Cancellation

- **Graceful interruption**: Requests the agent to stop via ACP `session/cancel`
- **State preservation**: Session state is still saved after cancellation, allowing continued use
- **Ctrl+C support**: Terminal interrupt signals are automatically converted to ACP cancel requests

### 5. Permission Control

- **Fine-grained policies**: Distinguishes between read operations, write operations, and command execution
- **Interactive prompts**: Allows per-operation approval in TTY environments
- **Non-interactive mode**: Auto-approve/deny, suitable for CI/CD

### 6. Structured Output

- **Typed events**: thinking, tool_call, diff, error, etc.
- **Machine-readable**: JSON format suitable for automated processing
- **Human-friendly**: Text mode provides clear progress feedback

### 7. Unified Interface

- **One set of commands**: Supports 12+ ACP-compatible agents
- **Auto-download adapters**: Automatically installs via `npx` on first use
- **Extensibility**: Supports custom agent registration

### 8. Configuration Flexibility

- **Global + project**: Supports multi-level configuration
- **Command-line overrides**: Temporarily adjust parameters without modifying config files
- **Auth integration**: Supports multiple authentication methods (environment variables, config files)

<!-- lastCommit: 6a7050b -->

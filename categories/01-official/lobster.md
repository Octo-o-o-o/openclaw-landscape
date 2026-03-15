> https://github.com/openclaw/lobster

# openclaw/lobster

## Basic Information

- **Stars**: 795
- **URL**: https://github.com/openclaw/lobster
- **Purpose**: Native workflow shell for OpenClaw
- **Tech Stack**: TypeScript + Node.js + pnpm
- **Status**: Under active development

## Problem & Solution

### Core Problems

1. **Token waste**: AI Agents executing multi-step tasks need to repeatedly re-plan each step, consuming a large number of tokens
2. **Lack of determinism**: Purely LLM-driven task execution lacks predictability and reproducibility
3. **Poor recoverability**: Tasks are difficult to resume from breakpoints after interruption, requiring a full restart
4. **Text pipeline limitations**: Traditional Unix pipes are based on text streams and cannot efficiently pass structured data (JSON/objects)

### Solution

Lobster provides a **typed workflow engine** that allows AI Agents to:

- **Define workflows once**, avoiding LLM calls to re-plan at every step
- **Use JSON pipes** to pass structured data instead of text parsing
- **Support approval gates** for human-agent collaboration
- **Save workflow state** with support for interrupt recovery
- **Execute locally first**, without additional authentication layers or cloud services

## Core Architecture

### 1. Command System

Lobster provides a set of pipeline commands, similar to Unix shell but oriented toward JSON:

```bash
# Execute a shell command and output JSON
lobster "exec --json --shell 'echo [1,2,3]' | where '0>=0' | json"

# Data filtering and transformation
lobster "exec --json --shell 'ls -l' | where 'size > 1000' | pick name,size | table"
```

**Core commands**:
- `exec`: Execute operating system commands
- `exec --stdin raw|json|jsonl`: Pass pipeline input to subprocess stdin
- `where`, `pick`, `head`: Data filtering and selection
- `json`, `table`: Output renderers
- `approve`: Approval gate (TTY prompt or `--emit` for OpenClaw integration)

### 2. Workflow Files

Supports declarative workflow definitions in YAML/JSON format:

```yaml
name: inbox-triage
steps:
  - id: collect
    command: inbox list --json

  - id: categorize
    command: inbox categorize --json
    stdin: $collect.stdout

  - id: approve
    command: inbox apply --approve
    stdin: $categorize.stdout
    approval: required

  - id: execute
    command: inbox apply --execute
    stdin: $categorize.stdout
    condition: $approve.approved
```

**Key features**:
- `stdin: $stepId.stdout`: Data passing between steps (no temporary files needed)
- `approval: required`: Human approval gate
- `condition: $stepId.field`: Conditional execution
- `env`: Environment variable injection

### 3. OpenClaw Tool Call Integration

Lobster provides `openclaw.invoke` and `clawd.invoke` executable shims, allowing workflows to directly call OpenClaw tools:

```yaml
name: hello-world
steps:
  - id: greeting
    command: >
      openclaw.invoke --tool llm-task --action json
      --args-json '{"prompt":"Hello"}'
```

**Prerequisites**:
- Set the `OPENCLAW_URL` environment variable to point to the OpenClaw gateway
- Optionally set `OPENCLAW_TOKEN` for authentication

### 4. Parameter Safety Mechanism

To prevent shell injection attacks, Lobster provides two parameter passing methods:

1. **Direct substitution** (unsafe): `${arg}` is directly substituted into the command string
2. **Environment variables** (recommended):
   - Each parameter is automatically exposed as a `LOBSTER_ARG_<NAME>` environment variable
   - The complete parameter object is exposed as `LOBSTER_ARGS_JSON`

```yaml
args:
  text:
    default: ""
steps:
  - id: safe
    env:
      TEXT: "$LOBSTER_ARG_TEXT"
    command: |
      jq -n --arg text "$TEXT" '{"result": $text}'
```

### 5. GitHub PR Monitoring Example

Lobster includes a built-in GitHub PR monitoring workflow that demonstrates state change detection capabilities:

```bash
node bin/lobster.js "workflows.run --name github.pr.monitor \
  --args-json '{\"repo\":\"openclaw/openclaw\",\"pr\":1152}'"
```

Output includes:
- `changed`: Boolean indicating whether the PR has changes
- `summary.changedFields`: List of changed fields
- `summary.changes`: Detailed from/to change comparisons
- `prSnapshot`: Full current PR snapshot

## Key Features

### 1. Typed Pipelines

- **JSON-first**: Pipelines pass JSON objects/arrays, not text
- **Structured data**: Avoids the fragility and performance overhead of text parsing
- **Type safety**: TypeScript implementation with compile-time type checking

### 2. Local-first

- **No cloud dependency**: All execution happens locally
- **No authentication layer**: Lobster doesn't hold OAuth tokens; it relies on environment variables or external tools
- **Fast execution**: No network round-trip latency

### 3. Composable Macros

- **Single-step invocation**: OpenClaw can execute an entire workflow with one tool call
- **Token savings**: Avoids multi-turn LLM conversations for step planning
- **Determinism**: Workflow logic is fixed, execution results are predictable

### 4. Approval Gates

- **Human-agent collaboration**: Critical steps can require human approval
- **TTY prompts**: Interactive prompts when running locally
- **OpenClaw integration**: `--emit` mode sends approval requests to OpenClaw

### 5. Conditional Execution

- **Dynamic flow**: Decides whether to execute based on preceding step outputs
- **Error handling**: Can skip or retry based on step status

<!-- lastCommit: e196a1ca51446576b32fac524f963f3b1fed3c24 -->

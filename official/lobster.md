# openclaw/lobster

## 基本信息

- **Stars**: 795
- **URL**: https://github.com/openclaw/lobster
- **定位**: OpenClaw 原生工作流 Shell
- **技术栈**: TypeScript + Node.js + pnpm
- **状态**: 活跃开发中

## 问题与解决方案

### 核心问题

1. **Token 浪费**: AI Agent 在执行多步骤任务时需要反复重新规划每一步，消耗大量 token
2. **确定性不足**: 纯 LLM 驱动的任务执行缺乏可预测性和可重复性
3. **可恢复性差**: 任务中断后难以从断点恢复，需要重新开始
4. **文本管道局限**: 传统 Unix 管道基于文本流，无法高效传递结构化数据（JSON/对象）

### 解决方案

Lobster 提供了一个**类型化的工作流引擎**，让 AI Agent 可以：

- **一次性定义工作流**，避免每步都调用 LLM 重新规划
- **使用 JSON 管道**传递结构化数据，而非文本解析
- **支持审批门控**（approval gates），实现人机协作
- **保存工作流状态**，支持中断恢复
- **本地优先执行**，无需额外的认证层或云服务

## 核心架构

### 1. 命令系统

Lobster 提供了一套管道命令，类似 Unix shell 但面向 JSON：

```bash
# 执行 shell 命令并输出 JSON
lobster "exec --json --shell 'echo [1,2,3]' | where '0>=0' | json"

# 数据过滤和转换
lobster "exec --json --shell 'ls -l' | where 'size > 1000' | pick name,size | table"
```

**核心命令**:
- `exec`: 执行操作系统命令
- `exec --stdin raw|json|jsonl`: 将管道输入传递给子进程 stdin
- `where`, `pick`, `head`: 数据过滤和选择
- `json`, `table`: 输出渲染器
- `approve`: 审批门控（TTY 提示或 `--emit` 用于 OpenClaw 集成）

### 2. 工作流文件

支持 YAML/JSON 格式的声明式工作流定义：

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

**关键特性**:
- `stdin: $stepId.stdout`: 步骤间数据传递（无需临时文件）
- `approval: required`: 人工审批门控
- `condition: $stepId.field`: 条件执行
- `env`: 环境变量注入

### 3. OpenClaw 工具调用集成

Lobster 提供了 `openclaw.invoke` 和 `clawd.invoke` 可执行 shim，允许工作流直接调用 OpenClaw 工具：

```yaml
name: hello-world
steps:
  - id: greeting
    command: >
      openclaw.invoke --tool llm-task --action json
      --args-json '{"prompt":"Hello"}'
```

**前置条件**:
- 设置 `OPENCLAW_URL` 环境变量指向 OpenClaw gateway
- 可选设置 `OPENCLAW_TOKEN` 用于认证

### 4. 参数安全机制

为避免 shell 注入攻击，Lobster 提供了两种参数传递方式：

1. **直接替换** (不安全): `${arg}` 直接替换到命令字符串
2. **环境变量** (推荐):
   - 每个参数自动暴露为 `LOBSTER_ARG_<NAME>` 环境变量
   - 完整参数对象暴露为 `LOBSTER_ARGS_JSON`

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

### 5. GitHub PR 监控示例

Lobster 内置了 GitHub PR 监控工作流，展示了状态变更检测能力：

```bash
node bin/lobster.js "workflows.run --name github.pr.monitor \
  --args-json '{\"repo\":\"openclaw/openclaw\",\"pr\":1152}'"
```

输出包含：
- `changed`: 布尔值，表示 PR 是否有变更
- `summary.changedFields`: 变更字段列表
- `summary.changes`: 详细的 from/to 变更对比
- `prSnapshot`: 当前 PR 完整快照

## 关键特性

### 1. 类型化管道

- **JSON-first**: 管道传递的是 JSON 对象/数组，而非文本
- **结构化数据**: 避免文本解析的脆弱性和性能损耗
- **类型安全**: TypeScript 实现，编译时类型检查

### 2. 本地优先

- **无云依赖**: 所有执行都在本地完成
- **无认证层**: Lobster 不持有 OAuth token，依赖环境变量或外部工具
- **快速执行**: 无网络往返延迟

### 3. 可组合宏

- **一步调用**: OpenClaw 可以用一个工具调用执行整个工作流
- **节省 token**: 避免多轮 LLM 对话来规划步骤
- **确定性**: 工作流逻辑固定，执行结果可预测

### 4. 审批门控

- **人机协作**: 关键步骤可以要求人工审批
- **TTY 提示**: 本地运行时弹出交互式提示
- **OpenClaw 集成**: `--emit` 模式将审批请求发送给 OpenClaw

### 5. 条件执行

- **动态流程**: 根据前序步骤的输出决定是否执行
- **错误处理**: 可以基于步骤状态跳过或重试

# NanoClaw

## 基本信息

- **GitHub**: https://github.com/qwibitai/nanoclaw
- **Stars**: 21,451
- **作者**: qwibitai
- **技术栈**: Node.js 20+, TypeScript, Claude Agent SDK 0.2.29, SQLite, Docker/Apple Container
- **许可证**: MIT

## 问题与解决方案

### 核心问题

OpenClaw 虽然功能强大，但存在严重的可理解性和安全性问题：
- **代码复杂度过高**：近 50 万行代码，53 个配置文件，70+ 依赖项
- **安全模型薄弱**：应用层权限控制（allowlist、配对码），而非真正的 OS 级隔离
- **单进程共享内存**：所有功能运行在同一个 Node 进程中，缺乏隔离边界
- **配置膨胀**：功能通过配置文件堆叠，导致系统臃肿

### NanoClaw 的解决方案

**1. 极简可理解架构**
- 单进程 + 少量源文件，无微服务
- 核心代码足够小，可以让 Claude Code 完整讲解整个代码库
- 哲学：小到可以理解（Small enough to understand）

**2. 容器级安全隔离**
- Agent 运行在 Linux 容器中（macOS 用 Apple Container，Linux 用 Docker）
- 文件系统隔离：只能访问显式挂载的目录
- Bash 命令在容器内执行，不影响宿主机
- 非 root 用户执行（uid 1000）
- 临时容器（`--rm` 标志）

**3. 凭证代理机制**
- 真实 API 凭证永不进入容器
- 宿主机运行 HTTP 凭证代理（端口 3001）
- 容器接收占位符 API key，代理注入真实凭证
- Agent 无法从环境变量、文件或 `/proc` 发现真实凭证

**4. 技能系统替代功能堆叠**
- 不向核心代码添加功能，而是通过技能（Skills）转换用户的 fork
- 用户运行 `/add-telegram` 等技能命令，Claude Code 修改代码
- 每个用户得到定制化的干净代码，而非臃肿的通用系统
- 技能作为 git 分支提交，用户通过 merge 应用

## 核心架构

### 系统架构图

```
┌──────────────────────────────────────────────────────────────────┐
│                    宿主机进程（Node.js）                          │
├──────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐              ┌────────────────┐                │
│  │ 通道系统     │─────────────▶│  SQLite 数据库 │                │
│  │ (自注册)     │◀─────────────│  (messages.db) │                │
│  └──────────────┘              └────────┬───────┘                │
│                                         │                         │
│  ┌──────────────┐    ┌──────────────┐  │  ┌──────────────┐      │
│  │ 消息轮询循环 │    │ 调度器循环   │  │  │ IPC 监听器   │      │
│  └──────┬───────┘    └──────┬───────┘  │  └──────────────┘      │
│         │                   │          │                         │
│         └───────────┬───────┘          │                         │
│                     │ 生成容器         │                         │
│                     ▼                  │                         │
├──────────────────────────────────────────────────────────────────┤
│                   容器（Linux VM）                                │
├──────────────────────────────────────────────────────────────────┤
│  工作目录: /workspace/group (从宿主机挂载)                        │
│  卷挂载:                                                          │
│    • groups/{name}/ → /workspace/group                           │
│    • groups/global/ → /workspace/global/ (非主组)                │
│    • data/sessions/{group}/.claude/ → /home/node/.claude/        │
│  工具: Bash, Read, Write, Edit, Glob, Grep, WebSearch, WebFetch  │
│        agent-browser, mcp__nanoclaw__* (通过 IPC)                │
└──────────────────────────────────────────────────────────────────┘
```

### 技术栈

| 组件 | 技术 | 用途 |
|------|------|------|
| 通道系统 | 通道注册表 (`src/channels/registry.ts`) | 通道启动时自注册 |
| 消息存储 | SQLite (better-sqlite3) | 存储消息用于轮询 |
| 容器运行时 | Docker / Apple Container | Agent 执行的隔离环境 |
| Agent | @anthropic-ai/claude-agent-sdk | 运行 Claude 及工具和 MCP 服务器 |
| 浏览器自动化 | agent-browser + Chromium | Web 交互和截图 |
| 运行时 | Node.js 20+ | 路由和调度的宿主进程 |

### 通道系统架构

**自注册模式**：
1. 每个通道技能在 `src/channels/` 添加文件（如 `whatsapp.ts`）
2. 模块加载时调用 `registerChannel()`
3. 桶文件 `src/channels/index.ts` 导入所有通道模块，触发注册
4. 启动时，编排器连接所有有凭证的通道，缺少凭证的通道发出 WARN 日志并跳过

**通道接口**：
```typescript
interface Channel {
  name: string;
  connect(): Promise<void>;
  sendMessage(jid: string, text: string): Promise<void>;
  isConnected(): boolean;
  ownsJid(jid: string): boolean;
  disconnect(): Promise<void>;
  setTyping?(jid: string, isTyping: boolean): Promise<void>;
  syncGroups?(force: boolean): Promise<void>;
}
```

### 消息流

```
通道 --> SQLite --> 轮询循环 --> 容器 (Claude Agent SDK) --> 响应
```

- 单 Node.js 进程
- 通道通过技能添加并在启动时自注册
- Agent 在隔离的 Linux 容器中执行，具有文件系统隔离
- 只有挂载的目录可访问
- 每组消息队列，带并发控制
- 通过文件系统进行 IPC

### 关键文件

- `src/index.ts` - 编排器：状态、消息循环、agent 调用
- `src/channels/registry.ts` - 通道注册表（启动时自注册）
- `src/ipc.ts` - IPC 监听器和任务处理
- `src/router.ts` - 消息格式化和出站路由
- `src/group-queue.ts` - 每组队列，带全局并发限制
- `src/container-runner.ts` - 生成流式 agent 容器
- `src/task-scheduler.ts` - 运行计划任务
- `src/db.ts` - SQLite 操作（消息、组、会话、状态）
- `groups/*/CLAUDE.md` - 每组记忆

## 关键特性

### 1. 多通道消息支持

- 从 WhatsApp、Telegram、Discord、Slack 或 Gmail 与助手对话
- 通过技能添加通道（如 `/add-whatsapp`、`/add-telegram`）
- 可同时运行一个或多个通道

### 2. 隔离的组上下文

- 每个组有自己的 `CLAUDE.md` 记忆
- 隔离的文件系统
- 在自己的容器沙箱中运行，只挂载该文件系统

### 3. 主通道

- 私人通道（自聊）用于管理控制
- 每个组完全隔离

### 4. 计划任务

- 定期作业运行 Claude 并可以回复消息

### 5. Web 访问

- 搜索和获取 Web 内容

### 6. 容器隔离

- Agent 在 Apple Container（macOS）或 Docker（macOS/Linux）中沙箱化

### 7. Agent Swarms

- 启动专门的 agent 团队协作处理复杂任务
- NanoClaw 是第一个支持 agent swarms 的个人 AI 助手

### 8. 可选集成

- 通过技能添加 Gmail（`/add-gmail`）等

### 9. 技能系统架构

**三层解决模型**：
1. **Git 层** - 确定性、程序化。`git merge-file` 合并，`git rerere` 重放缓存的解决方案。无 AI 参与。处理绝大多数情况。
2. **Claude Code 层** - 读取 `SKILL.md`、`.intent.md`、迁移指南和 `state.yaml` 理解上下文。解决 git 无法程序化处理的冲突。通过 `git rerere` 缓存解决方案。
3. **用户层** - 当 Claude Code 缺乏上下文或意图时询问用户。仅在两个功能在应用层面真正冲突时发生。

**技能包结构**：
```
skills/
  add-whatsapp/
    SKILL.md                    # 上下文、意图、功能说明
    manifest.yaml               # 元数据、依赖、环境变量、后应用步骤
    tests/                      # 集成测试
      whatsapp.test.ts
    add/                        # 新文件 - 直接复制
      src/channels/whatsapp.ts
    modify/                     # 修改的代码文件 - 通过 git merge-file 合并
      src/server.ts             # 完整文件：干净核心 + whatsapp 更改
      src/server.ts.intent.md   # 意图说明
```

**结构化操作**：
- `package.json`、`docker-compose.yml`、`.env.example` 等不作为文本合并
- 技能在 manifest 中声明结构化需求，系统程序化应用
- 批量处理：合并所有依赖声明，写入一次 `package.json`，最后运行一次 `npm install`

### 10. 安全模型

**信任模型**：
| 实体 | 信任级别 | 理由 |
|------|---------|------|
| 主组 | 受信任 | 私人自聊，管理控制 |
| 非主组 | 不受信任 | 其他用户可能是恶意的 |
| 容器 agent | 沙箱化 | 隔离的执行环境 |
| WhatsApp 消息 | 用户输入 | 潜在的提示注入 |

**安全边界**：

1. **容器隔离（主要边界）**
   - 进程隔离 - 容器进程不能影响宿主机
   - 文件系统隔离 - 只有显式挂载的目录可见
   - 非 root 执行 - 以非特权 `node` 用户运行（uid 1000）
   - 临时容器 - 每次调用都是新环境（`--rm`）

2. **挂载安全**
   - 外部允许列表 - 挂载权限存储在 `~/.config/nanoclaw/mount-allowlist.json`
   - 在项目根目录之外，永不挂载到容器，agent 无法修改
   - 默认阻止模式：`.ssh`, `.gnupg`, `.aws`, `.azure`, `.gcloud`, `.kube`, `.docker`, `credentials`, `.env`, `.netrc`, `.npmrc`, `id_rsa`, `id_ed25519`, `private_key`, `.secret`
   - 符号链接解析后验证（防止遍历攻击）
   - 容器路径验证（拒绝 `..` 和绝对路径）
   - `nonMainReadOnly` 选项强制非主组只读

3. **只读项目根**
   - 主组的项目根以只读方式挂载
   - agent 需要的可写路径（组文件夹、IPC、`.claude/`）单独挂载
   - 防止 agent 修改宿主应用代码（`src/`、`dist/`、`package.json` 等）

4. **会话隔离**
   - 每个组在 `data/sessions/{group}/.claude/` 有隔离的 Claude 会话
   - 组无法看到其他组的对话历史
   - 防止跨组信息泄露

5. **IPC 授权**
   - 消息和任务操作根据组身份验证

6. **凭证隔离（凭证代理）**
   - 真实 API 凭证永不进入容器
   - 宿主机运行 HTTP 凭证代理
   - 容器接收占位符凭证，代理注入真实凭证
   - Agent 无法发现真实凭证
## 总结

NanoClaw 是 OpenClaw 的轻量级替代品，核心价值在于：
1. **可理解性**：代码库小到可以完整理解
2. **安全性**：容器级隔离 + 凭证代理
3. **可定制性**：技能系统 + AI 辅助修改
4. **AI 原生**：Claude Code 驱动的设置、调试、运维

对 ClawButler 的最大启示是：**控制平面应该保持核心简洁，通过插件/扩展提供丰富功能，用 AI 辅助运维和定制**。NanoClaw 的技能系统、容器隔离、凭证代理、自注册通道等设计都值得 ClawButler 借鉴。

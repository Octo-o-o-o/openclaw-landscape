> https://github.com/openimsdk/open-im-server

# openimsdk/open-im-server

## 基本信息

- **GitHub Stars**: 15,776
- **项目地址**: https://github.com/openimsdk/open-im-server
- **开源协议**: Apache License 2.0
- **主要语言**: Go (Golang)
- **创建时间**: 2021-05-26
- **最新更新**: 2026-03-11
- **Forks**: 2,797
- **Open Issues**: 154
- **项目描述**: IM Chat OpenClaw
- **标签**: aigc, chat, chatbot, chatgpt, go, golang, im, imserver, instant-messaging, messaging, messenger, openim, telegram, wechat

## 问题与解决方案

### 核心问题
OpenIM 解决的核心问题是为开发者提供一个**可集成的即时通讯（IM）解决方案**，而非一个独立的聊天应用。与 Telegram、Signal、Rocket.Chat 等独立聊天应用不同，OpenIM 的定位是：

1. **开发者工具而非终端产品** — 不是直接安装使用的独立聊天应用，而是提供 SDK 和 Server 供开发者集成到自己的应用中
2. **企业级 IM 能力** — 支持海量用户场景（十万级超大群组、千万级用户、百亿级消息）
3. **灵活的业务扩展** — 通过 REST API 和 Webhooks 机制，让业务系统能够深度定制和扩展 IM 功能

### 解决方案架构
OpenIM 采用**双层架构**：
- **OpenIM SDK** — 客户端 SDK，支持跨平台（iOS/Android/Web/PC），提供本地存储、监听器回调、API 封装、连接管理等功能
- **OpenIM Server** — 后端服务，采用微服务架构，支持集群模式，包括网关（gateway）和多个 RPC 服务

## 核心架构

### 1. 微服务架构

OpenIM Server 采用典型的微服务架构，主要包含以下服务模块：

#### 核心服务组件（位于 `cmd/` 和 `internal/`）

1. **openim-api** — REST API 网关，提供 HTTP 接口供业务系统调用
2. **openim-msggateway** — WebSocket 消息网关，处理客户端长连接和实时消息推送
3. **openim-msgtransfer** — 消息转发服务，负责消息的异步处理和持久化
4. **openim-push** — 推送服务，处理离线推送和在线推送
5. **openim-rpc** — 多个 RPC 微服务：
   - `openim-rpc-auth` — 认证服务
   - `openim-rpc-user` — 用户管理
   - `openim-rpc-friend` — 好友关系管理
   - `openim-rpc-group` — 群组管理
   - `openim-rpc-msg` — 消息处理
   - `openim-rpc-conversation` — 会话管理
   - `openim-rpc-third` — 第三方服务集成（对象存储等）
6. **openim-crontask** — 定时任务服务
7. **openim-cmdutils** — 命令行工具

#### 基础设施依赖

- **MongoDB** — 主要数据存储（用户、群组、消息等）
- **Redis** — 缓存和会话管理
- **Kafka** — 消息队列，用于异步消息处理
- **etcd** — 服务发现和配置管理
- **MinIO** — 对象存储（文件、图片、视频等）
- **Prometheus + Grafana** — 监控和告警

### 2. 消息流转架构

```
客户端 (SDK)
    ↓ WebSocket
openim-msggateway (长连接管理)
    ↓ Kafka
openim-msgtransfer (消息转发)
    ↓
    ├→ MongoDB (消息持久化)
    ├→ openim-push (推送服务)
    └→ Webhooks (业务回调)
```

### 3. 服务通信机制

- **客户端 ↔ 服务端** — WebSocket（实时消息）+ REST API（业务操作）
- **服务间通信** — gRPC（同步调用）+ Kafka（异步消息）
- **服务发现** — etcd 实现动态服务注册与发现
- **负载均衡** — 支持多实例部署，通过 etcd 实现自动负载均衡

## 关键特性

### 1. Webhooks 扩展机制

OpenIM 提供了**超过 40 个 Webhook 回调点**（配置文件：`config/webhooks.yml`），覆盖消息、用户、群组、好友等全生命周期事件：

#### 消息相关 Webhooks
- `beforeSendSingleMsg` / `afterSendSingleMsg` — 单聊消息发送前后
- `beforeSendGroupMsg` / `afterSendGroupMsg` — 群聊消息发送前后
- `beforeMsgModify` — 消息修改前
- `afterMsgSaveDB` — 消息保存到数据库后
- `afterGroupMsgRead` / `afterSingleMsgRead` — 消息已读回执
- `afterRevokeMsg` / `afterGroupMsgRevoke` — 消息撤回

#### 用户相关 Webhooks
- `beforeUserRegister` / `afterUserRegister` — 用户注册前后
- `beforeUpdateUserInfo` / `afterUpdateUserInfo` — 用户信息更新前后
- `afterUserOnline` / `afterUserOffline` — 用户上下线
- `afterUserKickOff` — 用户被踢下线

#### 群组相关 Webhooks
- `beforeCreateGroup` / `afterCreateGroup` — 群组创建前后
- `beforeMemberJoinGroup` / `afterJoinGroup` — 成员加入群组前后
- `beforeApplyJoinGroup` — 申请加入群组前
- `afterKickGroupMember` — 踢出群成员后
- `afterDismissGroup` — 解散群组后
- `afterTransferGroupOwner` — 转让群主后
- `beforeSetGroupInfo` / `afterSetGroupInfo` — 群组信息设置前后

#### 好友相关 Webhooks
- `beforeAddFriend` / `afterAddFriend` — 添加好友前后
- `beforeAddFriendAgree` / `afterAddFriendAgree` — 同意好友申请前后
- `afterDeleteFriend` — 删除好友后
- `beforeSetFriendRemark` / `afterSetFriendRemark` — 设置好友备注前后
- `beforeAddBlack` / `afterRemoveBlack` — 黑名单操作

#### 推送相关 Webhooks
- `beforeOfflinePush` — 离线推送前
- `beforeOnlinePush` — 在线推送前
- `beforeGroupOnlinePush` — 群组在线推送前

#### Webhook 配置特性
- **可选启用** — 每个 Webhook 都可以独立启用/禁用
- **超时控制** — 可配置每个 Webhook 的超时时间（默认 5 秒）
- **失败策略** — `failedContinue` 参数控制回调失败时是否继续流程
- **内容过滤** — 部分 Webhook 支持 `deniedTypes` 过滤特定消息类型
- **关注列表** — 部分 Webhook 支持 `attentionIds` 只对特定用户/群组生效

### 2. REST API 扩展

OpenIM 提供了丰富的 REST API（位于 `internal/api/`），主要包括：

- **用户管理** — 注册、信息更新、在线状态查询、订阅状态等
- **好友管理** — 添加、删除、备注、黑名单等
- **群组管理** — 创建、解散、成员管理、权限控制等
- **消息管理** — 发送、撤回、已读回执、历史消息查询等
- **会话管理** — 会话列表、置顶、免打扰等
- **第三方服务** — 文件上传、对象存储等

### 3. 高可用与性能特性

- **水平扩展** — 所有服务支持多实例部署
- **消息可靠性** — Kafka + MongoDB 双重保障
- **缓存优化** — Redis 多级缓存（本地缓存 + 分布式缓存）
- **限流熔断** — 支持 Rate Limiter 和 Circuit Breaker（配置在各服务的 YAML 文件中）
- **监控告警** — Prometheus 指标采集 + Grafana 可视化

### 4. 部署灵活性

- **源码部署** — 支持直接编译运行
- **Docker Compose** — 一键启动完整环境
- **Kubernetes** — 支持 K8s 集群部署（`deployments/deploy/`）
- **跨平台** — 支持 Linux、Windows、macOS，支持 ARM 和 AMD 架构

### 5. 开发者友好

- **多语言 SDK** — Go SDK（openim-sdk-core）为主，支持跨平台编译
- **完善文档** — 官方文档站点 https://docs.openim.io/
- **活跃社区** — Slack 500+ 成员，GitHub 2,797 Forks
- **持续更新** — 最新版本 v3.8.3-patch.15（2025-12-31）

## 与 OpenClaw 的关系

### 项目描述中的 "OpenClaw" 标识

在 GitHub 仓库的描述中，OpenIM 明确标注为 **"IM Chat OpenClaw"**，这表明：

1. **OpenClaw 可能是一个更大的生态系统或品牌** — OpenIM 是其中的即时通讯组件
2. **集成关系** — OpenIM 可能作为 OpenClaw 平台的通讯基础设施
3. **标签关联** — 项目标签包含 `aigc`, `chatbot`, `chatgpt`，暗示与 AI Agent 场景的结合

### 推测的集成场景

虽然代码库中没有直接搜索到 "OpenClaw" 的实现细节，但从架构和特性可以推测：

1. **AI Agent 通讯层** — OpenIM 可以作为 AI Agent 之间的通讯基础设施
2. **Webhook 驱动的 Agent 集成** — 通过 Webhooks 机制，可以在消息流转的各个环节触发 AI Agent 处理
3. **多 Agent 协作** — 群组功能可以支持多个 AI Agent 在同一会话中协作
4. **实时交互** — WebSocket 长连接支持 Agent 与用户的实时交互

### 可能的集成模式

```
用户消息
    ↓
OpenIM (消息接收)
    ↓ beforeSendSingleMsg Webhook
OpenClaw Agent (消息理解、意图识别)
    ↓ 返回处理结果
OpenIM (消息转发/存储)
    ↓ afterSendSingleMsg Webhook
OpenClaw Agent (后续处理、学习)
```
# ClawButler 可以设计类似的 Webhook 配置
webhooks:
  beforeAgentCreate:
    enable: true
    timeout: 5s
    failedContinue: false  # 创建失败则中止
  afterAgentExecute:
    enable: true
    timeout: 3s
    attentionAgentIds: ["agent-001", "agent-002"]  # 只关注特定 Agent
  beforeMCPToolCall:
    enable: true
    deniedTools: ["dangerous-tool"]  # 黑名单机制
```

### 2. 微服务架构与服务发现

**OpenIM 的启示**：
- 采用 etcd 实现服务注册与发现，支持动态扩缩容
- 每个服务都有独立的配置文件（YAML），支持限流、熔断、监控等
- gRPC 用于服务间同步调用，Kafka 用于异步消息

**对 ClawButler 的价值**：
- **异构 Agent 生态管理** — ClawButler 需要连接 OpenClaw、Dify、LangGraph 等多种 Agent 平台，可以借鉴 etcd 的服务发现机制
- **动态路由** — 根据 Agent 的负载、健康状态动态路由请求
- **协议适配层** — 类似 OpenIM 的 RPC 服务，ClawButler 可以为每种 Agent 平台提供独立的适配服务（如 `clawbutler-rpc-openclaw`, `clawbutler-rpc-dify`）

**具体借鉴**：
```
ClawButler 架构设计：
- clawbutler-api (统一 API 网关)
- clawbutler-gateway (A2A 协议网关)
- clawbutler-router (协作路由服务)
- clawbutler-rpc-openclaw (OpenClaw 适配器)
- clawbutler-rpc-dify (Dify 适配器)
- clawbutler-rpc-langgraph (LangGraph 适配器)
- clawbutler-audit (审计服务)
- clawbutler-billing (计费服务)
```

### 3. 配置管理与漂移检测

**OpenIM 的启示**：
- 每个服务都有独立的 YAML 配置文件，支持热更新
- 配置项包括服务地址、限流参数、熔断阈值、监控开关等
- 支持环境变量覆盖配置

**对 ClawButler 的价值**：
- **Config Safety V2** — ClawButler 已经实现了配置快照、语义 diff、漂移检测，可以进一步借鉴 OpenIM 的配置分层设计
- **多租户配置隔离** — 为每个组织（Org）提供独立的配置空间，类似 OpenIM 的多实例部署
- **配置模板** — 类似 OpenIM 的 Webhooks 配置，ClawButler 可以提供 Agent 配置模板（Verified Templates V2.5）

**具体借鉴**：
```yaml
# ClawButler Agent 配置模板
agent_config:
  identity:
    agent_id: "agent-001"
    org_id: "org-123"
  permissions:
    mcp_tools: ["tool-a", "tool-b"]
    a2a_peers: ["agent-002", "agent-003"]
  rate_limiter:
    enable: true
    window: 60s
    max_requests: 100
  circuit_breaker:
    enable: true
    failure_threshold: 0.5
```

### 4. 消息队列与异步处理

**OpenIM 的启示**：
- 使用 Kafka 作为消息队列，实现消息的异步处理和持久化
- `openim-msgtransfer` 服务专门负责消息转发和持久化
- 支持消息的批量处理和重试机制

**对 ClawButler 的价值**：
- **Agent 协作路由** — 当一个 Agent 需要调用另一个 Agent 时（A2A 协议），可以通过消息队列实现异步调用
- **审计日志异步写入** — 避免同步写入审计日志影响 Agent 执行性能
- **成本计算异步处理** — 在后台异步计算和汇总各 Agent 的资源消耗

**具体借鉴**：
```
Agent A 调用 Agent B (A2A)
    ↓
ClawButler Gateway (接收请求)
    ↓ Kafka (异步队列)
ClawButler Router (路由服务)
    ↓
    ├→ Agent B (执行任务)
    ├→ Audit Service (记录审计日志)
    └→ Billing Service (记录成本)
```

### 5. 监控与可观测性

**OpenIM 的启示**：
- 集成 Prometheus 采集指标，Grafana 可视化
- 每个 API 调用都有指标记录（`prommetrics.HttpCall`, `prommetrics.APICall`）
- 支持自定义告警规则（`config/instance-down-rules.yml`）

**对 ClawButler 的价值**：
- **Agent 健康监控** — 实时监控各 Agent 平台的健康状态、响应时间、错误率
- **成本可视化** — 通过 Grafana 展示各 Agent 的资源消耗趋势
- **异常告警** — 当 Agent 执行失败率超过阈值时自动告警

**具体借鉴**：
```go
// ClawButler 可以实现类似的指标采集
func AgentExecuteMetrics(agentID, platform string, success bool, duration time.Duration) {
    prometheus.AgentExecuteTotal.WithLabelValues(agentID, platform, strconv.FormatBool(success)).Inc()
    prometheus.AgentExecuteDuration.WithLabelValues(agentID, platform).Observe(duration.Seconds())
}
```

### 6. 多租户与权限管理

**OpenIM 的启示**：
- 支持多用户、多群组的权限隔离
- 通过 `authverify` 中间件实现 Token 验证和权限检查
- 支持管理员用户（`IMAdminUser.UserIDs`）的特殊权限

**对 ClawButler 的价值**：
- **组织级隔离** — ClawButler 已经实现了 Org-scoped billing，可以进一步借鉴 OpenIM 的多租户设计
- **Agent 权限矩阵** — 定义哪些 Agent 可以调用哪些 MCP 工具、可以与哪些 Agent 协作（A2A）
- **审计追踪** — 记录每个操作的发起者（用户/Agent）、目标（Agent/工具）、结果（成功/失败）

**具体借鉴**：
```go
// ClawButler 权限检查中间件
func AgentPermissionMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        agentID := c.GetHeader("X-Agent-ID")
        orgID := c.GetHeader("X-Org-ID")

        // 检查 Agent 是否属于该 Org
        if !checkAgentBelongsToOrg(agentID, orgID) {
            c.JSON(403, gin.H{"error": "Agent not authorized"})
            c.Abort()
            return
        }

        // 检查 Agent 是否有权限调用目标工具/Agent
        targetResource := c.Param("resource")
        if !checkAgentPermission(agentID, targetResource) {
            c.JSON(403, gin.H{"error": "Permission denied"})
            c.Abort()
            return
        }

        c.Next()
    }
}
```

### 7. 部署与运维

**OpenIM 的启示**：
- 提供一键安装脚本（`install.sh`）
- 支持 Docker Compose 和 Kubernetes 部署
- 提供服务管理工具（类似 ClawButler 的 `clawbutlerctl`）

**对 ClawButler 的价值**：
- **简化部署** — ClawButler 已经实现了 `deploy.sh` 和 `clawbutlerctl`，可以进一步借鉴 OpenIM 的多环境支持
- **健康检查** — 在 Docker Compose 中添加健康检查，确保服务正常启动
- **滚动更新** — 支持零停机更新（类似 OpenIM 的多实例部署）

## 总结

OpenIM 作为一个成熟的开源 IM 解决方案，其架构设计和工程实践对 ClawButler 有重要的借鉴价值：

1. **Webhook 机制** — 提供细粒度的扩展点，支持业务系统深度定制
2. **微服务架构** — 通过服务拆分和服务发现，支持异构系统的统一管理
3. **配置管理** — 分层配置设计，支持多租户隔离和动态更新
4. **异步处理** — 使用消息队列解耦服务，提升系统性能和可靠性
5. **可观测性** — 完善的监控和告警机制，支持运维和故障排查
6. **权限管理** — 多租户权限隔离，支持细粒度的访问控制

ClawButler 可以将这些设计理念应用到 Agent 控制平面的建设中，实现**统一身份、权限、协作路由、审计追踪和成本追踪**的目标，成为异构 Agent 生态系统的统一治理层。

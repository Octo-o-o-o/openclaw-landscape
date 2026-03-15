> https://github.com/openimsdk/open-im-server

# openimsdk/open-im-server

## Basic Info

- **GitHub Stars**: 15,776
- **Project URL**: https://github.com/openimsdk/open-im-server
- **License**: Apache License 2.0
- **Primary Language**: Go (Golang)
- **Created**: 2021-05-26
- **Last Updated**: 2026-03-11
- **Forks**: 2,797
- **Open Issues**: 154
- **Description**: IM Chat OpenClaw
- **Tags**: aigc, chat, chatbot, chatgpt, go, golang, im, imserver, instant-messaging, messaging, messenger, openim, telegram, wechat

## Problem & Solution

### Core Problem
OpenIM addresses the core problem of providing developers with an **integrable instant messaging (IM) solution**, rather than a standalone chat application. Unlike standalone chat apps such as Telegram, Signal, or Rocket.Chat, OpenIM is positioned as:

1. **Developer tool, not end product** — Not a standalone chat app for direct use, but provides SDKs and servers for developers to integrate into their own applications
2. **Enterprise-grade IM capabilities** — Supports massive user scenarios (100K+ super-large groups, tens of millions of users, tens of billions of messages)
3. **Flexible business extensions** — Through REST API and Webhooks mechanisms, enabling business systems to deeply customize and extend IM functionality

### Solution Architecture
OpenIM adopts a **dual-layer architecture**:
- **OpenIM SDK** — Client SDK supporting cross-platform (iOS/Android/Web/PC) with local storage, listener callbacks, API wrappers, and connection management
- **OpenIM Server** — Backend services with microservice architecture supporting cluster mode, including gateway and multiple RPC services

## Core Architecture

### 1. Microservice Architecture

OpenIM Server uses a typical microservice architecture with the following service modules:

#### Core Service Components (in `cmd/` and `internal/`)

1. **openim-api** — REST API gateway providing HTTP interfaces for business systems
2. **openim-msggateway** — WebSocket message gateway handling client long connections and real-time message push
3. **openim-msgtransfer** — Message transfer service for asynchronous message processing and persistence
4. **openim-push** — Push service handling offline and online push
5. **openim-rpc** — Multiple RPC microservices:
   - `openim-rpc-auth` — Authentication service
   - `openim-rpc-user` — User management
   - `openim-rpc-friend` — Friend relationship management
   - `openim-rpc-group` — Group management
   - `openim-rpc-msg` — Message processing
   - `openim-rpc-conversation` — Conversation management
   - `openim-rpc-third` — Third-party service integration (object storage, etc.)
6. **openim-crontask** — Scheduled task service
7. **openim-cmdutils** — Command-line tools

#### Infrastructure Dependencies

- **MongoDB** — Primary data storage (users, groups, messages, etc.)
- **Redis** — Cache and session management
- **Kafka** — Message queue for asynchronous message processing
- **etcd** — Service discovery and configuration management
- **MinIO** — Object storage (files, images, videos, etc.)
- **Prometheus + Grafana** — Monitoring and alerting

### 2. Message Flow Architecture

```
Client (SDK)
    ↓ WebSocket
openim-msggateway (long connection management)
    ↓ Kafka
openim-msgtransfer (message transfer)
    ↓
    ├→ MongoDB (message persistence)
    ├→ openim-push (push service)
    └→ Webhooks (business callbacks)
```

### 3. Service Communication Mechanisms

- **Client <-> Server** — WebSocket (real-time messages) + REST API (business operations)
- **Inter-Service** — gRPC (synchronous calls) + Kafka (asynchronous messages)
- **Service Discovery** — etcd for dynamic service registration and discovery
- **Load Balancing** — Supports multi-instance deployment with automatic load balancing via etcd

## Key Features

### 1. Webhooks Extension Mechanism

OpenIM provides **over 40 Webhook callback points** (config file: `config/webhooks.yml`), covering the full lifecycle of messages, users, groups, and friends:

#### Message Webhooks
- `beforeSendSingleMsg` / `afterSendSingleMsg` — Before/after single chat message send
- `beforeSendGroupMsg` / `afterSendGroupMsg` — Before/after group chat message send
- `beforeMsgModify` — Before message modification
- `afterMsgSaveDB` — After message saved to database
- `afterGroupMsgRead` / `afterSingleMsgRead` — Message read receipts
- `afterRevokeMsg` / `afterGroupMsgRevoke` — Message revocation

#### User Webhooks
- `beforeUserRegister` / `afterUserRegister` — Before/after user registration
- `beforeUpdateUserInfo` / `afterUpdateUserInfo` — Before/after user info update
- `afterUserOnline` / `afterUserOffline` — User online/offline
- `afterUserKickOff` — User kicked offline

#### Group Webhooks
- `beforeCreateGroup` / `afterCreateGroup` — Before/after group creation
- `beforeMemberJoinGroup` / `afterJoinGroup` — Before/after member joins group
- `beforeApplyJoinGroup` — Before group join application
- `afterKickGroupMember` — After group member kicked
- `afterDismissGroup` — After group disbanded
- `afterTransferGroupOwner` — After group ownership transfer
- `beforeSetGroupInfo` / `afterSetGroupInfo` — Before/after group info update

#### Friend Webhooks
- `beforeAddFriend` / `afterAddFriend` — Before/after adding friend
- `beforeAddFriendAgree` / `afterAddFriendAgree` — Before/after accepting friend request
- `afterDeleteFriend` — After deleting friend
- `beforeSetFriendRemark` / `afterSetFriendRemark` — Before/after setting friend remark
- `beforeAddBlack` / `afterRemoveBlack` — Blocklist operations

#### Push Webhooks
- `beforeOfflinePush` — Before offline push
- `beforeOnlinePush` — Before online push
- `beforeGroupOnlinePush` — Before group online push

#### Webhook Configuration Features
- **Individually toggleable** — Each Webhook can be independently enabled/disabled
- **Timeout control** — Configurable timeout per Webhook (default 5 seconds)
- **Failure strategy** — `failedContinue` parameter controls whether to continue the flow on callback failure
- **Content filtering** — Some Webhooks support `deniedTypes` to filter specific message types
- **Watch list** — Some Webhooks support `attentionIds` to target specific users/groups only

### 2. REST API Extensions

OpenIM provides rich REST APIs (in `internal/api/`), including:

- **User management** — Registration, info updates, online status queries, status subscriptions, etc.
- **Friend management** — Adding, deleting, remarks, blocklist, etc.
- **Group management** — Creation, disbanding, member management, permission control, etc.
- **Message management** — Sending, revoking, read receipts, history queries, etc.
- **Conversation management** — Conversation lists, pinning, do-not-disturb, etc.
- **Third-party services** — File upload, object storage, etc.

### 3. High Availability & Performance

- **Horizontal scaling** — All services support multi-instance deployment
- **Message reliability** — Kafka + MongoDB dual guarantee
- **Cache optimization** — Redis multi-level cache (local cache + distributed cache)
- **Rate limiting and circuit breaking** — Rate Limiter and Circuit Breaker support (configured in service YAML files)
- **Monitoring and alerting** — Prometheus metrics collection + Grafana visualization

### 4. Deployment Flexibility

- **Source deployment** — Build and run directly
- **Docker Compose** — One-click full environment startup
- **Kubernetes** — K8s cluster deployment support (`deployments/deploy/`)
- **Cross-platform** — Supports Linux, Windows, macOS, ARM and AMD architectures

### 5. Developer-Friendly

- **Multi-language SDK** — Go SDK (openim-sdk-core) as primary, supporting cross-platform compilation
- **Comprehensive documentation** — Official docs site at https://docs.openim.io/
- **Active community** — Slack 500+ members, GitHub 2,797 Forks
- **Continuous updates** — Latest version v3.8.3-patch.15 (2025-12-31)

## Relationship with OpenClaw

### "OpenClaw" Label in Project Description

The GitHub repository description explicitly labels OpenIM as **"IM Chat OpenClaw"**, suggesting:

1. **OpenClaw may be a larger ecosystem or brand** — OpenIM is the instant messaging component within it
2. **Integration relationship** — OpenIM may serve as the communication infrastructure for the OpenClaw platform
3. **Tag association** — Project tags include `aigc`, `chatbot`, `chatgpt`, hinting at AI Agent scenario integration

### Potential Integration Scenarios

Although no "OpenClaw" implementation details were found directly in the codebase, the architecture and features suggest:

1. **AI Agent communication layer** — OpenIM can serve as communication infrastructure between AI Agents
2. **Webhook-driven Agent integration** — Through the Webhooks mechanism, AI Agent processing can be triggered at various points in the message flow
3. **Multi-Agent collaboration** — Group features can support multiple AI Agents collaborating within the same conversation
4. **Real-time interaction** — WebSocket long connections support real-time interaction between Agents and users

### Possible Integration Pattern

```
User Message
    ↓
OpenIM (message received)
    ↓ beforeSendSingleMsg Webhook
OpenClaw Agent (message understanding, intent recognition)
    ↓ Returns processing result
OpenIM (message forwarding/storage)
    ↓ afterSendSingleMsg Webhook
OpenClaw Agent (follow-up processing, learning)
```

## Summary

OpenIM is a mature open-source IM solution whose architectural design and engineering practices hold significant reference value:

1. **Webhook mechanism** — Provides fine-grained extension points supporting deep business customization
2. **Microservice architecture** — Service decomposition and discovery supporting unified management of heterogeneous systems
3. **Configuration management** — Layered configuration design supporting multi-tenant isolation and dynamic updates
4. **Asynchronous processing** — Message queues for service decoupling, improving system performance and reliability
5. **Observability** — Comprehensive monitoring and alerting for operations and troubleshooting
6. **Permission management** — Multi-tenant permission isolation with fine-grained access control

<!-- lastCommit: 942d155d2dbb0926d25ddbfc4b0d16755d477653 -->

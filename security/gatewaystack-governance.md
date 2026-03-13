# GatewayStack Governance (5 stars)

## 问题与解决方案
OpenClaw 的工具调用缺乏治理层，Agent 可直接执行危险操作（读取 SSH 密钥、执行任意命令），无身份检查、速率限制或审计追踪。GatewayStack Governance 在进程级别拦截每个工具调用，强制执行五项治理检查。

## 关键特性
- **五项核心检查** — Identity（Agent ID 映射到治理身份）→ Scope（deny-by-default 工具白名单）→ Rate Limiting（滑动窗口限制）→ Injection Detection（40+ 攻击模式扫描）→ Audit Logging（append-only JSONL）
- **进程级拦截** — 通过 OpenClaw 的 `before_tool_call` 事件钩子，Agent 无法绕过或跳过检查
- **三项可选功能** — Output DLP（PII 扫描和编辑）、Escalation（人工审批工作流）、Behavioral Monitoring（异常检测）
- **GatewayStack 生态集成** — 使用 `@gatewaystack/transformabl-core`（DLP）和 `@gatewaystack/limitabl-core`（行为监控）
- **零配置核心** — 核心检查无需配置即可工作，可选功能通过 `policy.json` 启用
- **一键安装** — `openclaw plugins install @gatewaystack/gatewaystack-governance`

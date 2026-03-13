# Security Tools

> Security scanning, auditing, and hardening tools for agent deployments.
> Agent 部署的安全扫描、审计和加固工具。

**7 projects** | [Back to overview](../README.md)

---

### AI-Infra-Guard

[Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | Stars: 3,124
Researched: 2026-03-11 | Updated: 2026-03-13

AI-Infra-Guard 解决了 AI 基础设施和 Agent 生态的安全风险问题。随着 OpenClaw、Dify、Coze 等 Agent 平台普及，安全风险（不安全配置、Skill 漏洞、CVE、隐私泄露、越狱攻击）成为企业部署的核心障碍。腾讯朱雀实验室推出的 AI 红队平台，提供 OpenClaw 安全扫描、Agent 扫描、MCP/Skill 扫描、越狱评估等全栈安全能力。

**Features:** OpenClaw 安全扫描（ClawScan）, Agent-Scan 框架, MCP Server & Skill 扫描, 越狱评估, 企业级部署, BlackHat EU 2025 Arsenal

---

### OpenClaw Security Practice Guide

[slowmist/security-practice-guide](https://github.com/slowmist/security-practice-guide) | Stars: 1,659 | 英文 / 简体中文 | MIT
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 作为高权限自主 AI Agent，运行在 root/terminal 环境下，面临以下安全风险：

**Features:** 利用强推理模型（Gemini / Opus / Kimi / MiniMax）的长上下文理解能力, Agent 自动解析 Markdown 指南中的安全策略, Agent 自主生成并执行部署脚本, 无需人工编写配置文件或执行命令

---

### ClawSec

[prompt-security/clawsec](https://github.com/prompt-security/clawsec) | Stars: 709
Researched: 2026-03-11 | Updated: 2026-03-13

ClawSec 解决了 AI Agent 认知架构"安全防护缺失"的痛点。通过完整的安全技能套件（Suite Installer），为 OpenClaw/NanoClaw Agent 提供文件完整性保护（SOUL.md/IDENTITY.md 等关键文件的漂移检测和自动恢复）、实时安全公告（NVD CVE 轮询 + 社区威胁情报）、安全审计（提示注入标记检测）、校验和验证（SHA256）和健康检查（自动更新和完整性验证），防御提示注入、漂移和恶意指令。

**Features:** 一键套件安装, 文件完整性保护（soul-guardian）, 实时安全公告, 安全审计脚本, 校验和验证, 健康检查

---

### OpenClaw Security Guide by Knownsec

[knownsec/openclaw-security](https://github.com/knownsec/openclaw-security) | Stars: 55
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 的快速增长伴随严重安全风险，ZoomEye 数据显示全球 63,026 个可识别实例，GitHub Advisory Database 记录 245 个相关漏洞。Knownsec（知道创宇）发布全生命周期安全实践指南，覆盖安装、配置、使用和维护。

**Features:** 安全安装检查清单, 配置安全审计, SKILL 审查规则, 日常检查脚本, 事件响应流程, 中英双语文档

---

### OpenClaw Secure Stack

[yi-john-huang/secure-stack](https://github.com/yi-john-huang/secure-stack) | Stars: 47 | Go
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 自托管存在恶意技能、提示注入、未授权访问、数据泄露等安全风险。Secure Stack 通过反向代理包装未修改的 OpenClaw 实例，提供认证、技能扫描、提示注入缓解、执行前治理、webhook 集成、网络隔离和完整审计日志。

**Features:** 多阶段安全管道, Webhook 安全中继, Plugin Hook 系统, 离线技能扫描, DNS 白名单, 一键部署

---

### UseAI-pro/openclaw-skills-security

[UseAI-pro/skills-security](https://github.com/UseAI-pro/skills-security) | Stars: 25
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 生态的技能安装缺乏安全审查机制，恶意技能可能窃取凭证、植入后门或执行供应链攻击（如 ClawHavoc 事件）。该项目提供两个审计技能（skill-auditor 审查技能、setup-auditor 审查环境）和 11 个可复用安全模块，覆盖 12 种真实攻击类型的检测。

**Features:** 双审计器架构, 威胁覆盖完整, 风险评级系统, 零依赖设计, 向导式环境审计, 社区驱动

---

### GatewayStack Governance

[davidcrowe/gatewaystack-governance](https://github.com/davidcrowe/gatewaystack-governance) | Stars: 5 | Go
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw 的工具调用缺乏治理层，Agent 可直接执行危险操作（读取 SSH 密钥、执行任意命令），无身份检查、速率限制或审计追踪。GatewayStack Governance 在进程级别拦截每个工具调用，强制执行五项治理检查。

**Features:** 五项核心检查, 进程级拦截, 三项可选功能, GatewayStack 生态集成, 零配置核心, 一键安装

---

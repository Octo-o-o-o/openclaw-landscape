> https://github.com/Tencent/AI-Infra-Guard

# AI-Infra-Guard (3,124 stars)

## 问题与解决方案

AI-Infra-Guard 解决了 AI 基础设施和 Agent 生态的安全风险问题。随着 OpenClaw、Dify、Coze 等 Agent 平台普及，安全风险（不安全配置、Skill 漏洞、CVE、隐私泄露、越狱攻击）成为企业部署的核心障碍。腾讯朱雀实验室推出的 AI 红队平台，提供 OpenClaw 安全扫描、Agent 扫描、MCP/Skill 扫描、越狱评估等全栈安全能力。

## 关键特性

- **OpenClaw 安全扫描（ClawScan）**：一键评估 OpenClaw 安全风险，检测不安全配置、Skill 风险、CVE 漏洞、隐私泄露
- **Agent-Scan 框架**：独立的多 Agent 自动化扫描框架，评估 Dify/Coze 等平台上运行的 Agent 工作流安全性
- **MCP Server & Skill 扫描**：扫描 MCP 服务器和 Agent Skill 的安全漏洞，Skill 安全情报由腾讯朱雀实验室 + 科恩实验室共建
- **越狱评估**：LLM 越狱攻击评估能力，检测 Agent 对抗性输入的鲁棒性
- **企业级部署**：Docker 一键部署，Web UI + API，支持内网自查，无需公网暴露
- **BlackHat EU 2025 Arsenal**：入选 BlackHat 兵器谱，行业认可度高

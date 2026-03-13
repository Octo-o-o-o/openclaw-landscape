# OpenClaw Secure Stack (47 stars)

## 问题与解决方案
OpenClaw 自托管存在恶意技能、提示注入、未授权访问、数据泄露等安全风险。Secure Stack 通过反向代理包装未修改的 OpenClaw 实例，提供认证、技能扫描、提示注入缓解、执行前治理、webhook 集成、网络隔离和完整审计日志。

## 关键特性
- **多阶段安全管道** — Auth Middleware（Bearer token 恒定时间比较）→ Governance（工具调用意图分类、策略验证、人工审批）→ Sanitizer（提示注入模式扫描）→ OpenClaw → Response Scanner（间接注入检测）→ Audit Log
- **Webhook 安全中继** — Telegram/WhatsApp 消息通过签名验证、速率限制、重放保护、大小检查后转发，支持 HMAC-SHA256 和 secret token
- **Plugin Hook 系统** — TypeScript 插件（`prompt-guard`）在 OpenClaw 内部运行，拦截工具结果中的间接注入（`tool_result_persist` hook）和高风险工具调用（`before_tool_call` hook）
- **离线技能扫描** — tree-sitter AST 分析检测危险 API（eval、child_process）、网络泄露（fetch、http）、文件系统滥用（writeFile、rmSync），隔离到 SQLite
- **DNS 白名单** — CoreDNS 阻止技能向非批准域名的出站流量
- **一键部署** — Docker Compose + Caddy 自动 HTTPS，`install.sh` 自动安装 `prompt-guard` 插件

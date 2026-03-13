> https://github.com/moltis-org/moltis

# Moltis (2,077 stars)

## 问题与解决方案

Moltis 解决了 OpenClaw 的安全性和可审计性问题。传统 OpenClaw（TypeScript + Node.js，~430K LoC）存在供应链攻击风险、内存安全隐患、运行时依赖复杂等问题。Moltis 用 Rust 重写，单二进制部署，零 `unsafe` 代码，沙箱隔离执行，核心代码仅 ~5K LoC（Agent 循环 + 模型层），全栈 ~124K LoC，3,100+ 测试，可独立审计。

## 关键特性

- **内存安全**：Rust 所有权系统 + 零 `unsafe` 代码（workspace 级别禁用，仅 FFI 可选），杜绝内存漏洞
- **沙箱隔离**：Docker + Apple Container 双层沙箱，每会话隔离，命令永不在宿主机执行
- **单二进制部署**：无 Node.js、无 npm、无运行时依赖，44MB 单文件，支持 Mac Mini/树莓派/自有服务器
- **可审计架构**：核心 Agent 循环 ~5K LoC，46 个模块化 crate（~196K LoC），可独立审计，3,100+ 测试
- **全功能内置**：语音（15+ 提供商）、记忆、调度、Telegram/Discord/WhatsApp、浏览器自动化、MCP 服务器、Hooks（15 种事件）
- **安全设计**：密钥用 `secrecy::Secret` 包装（drop 时清零），工具输出脱敏，SSRF 防护，Origin 验证，Hook 拦截

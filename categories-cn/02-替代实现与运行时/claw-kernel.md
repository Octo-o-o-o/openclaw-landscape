> https://github.com/creeper-scr/claw-kernel

# claw-kernel (2 stars)

## 问题与解决方案

Claw 生态中的每个项目（OpenClaw、ZeroClaw、OpenCrust）都独立实现相同的基础设施（LLM 调用、工具协议、Agent 循环、记忆系统、渠道集成），导致重复开发和碎片化。claw-kernel 将这些原语提取为单一的、经过充分测试的跨平台 Rust 库，作为生态的共享基础设施层。

## 关键特性

- **分层架构** — 从 Layer 0（Rust 硬核）到 Layer 3（扩展基础），清晰的职责分离和依赖关系
- **跨平台抽象层（PAL）** — 统一的沙箱、IPC（Unix socket / Named Pipe）、进程管理接口
- **8 个 LLM 提供商** — 原生支持 Anthropic、OpenAI、Ollama、DeepSeek、Moonshot、Gemini、Mistral、Azure OpenAI
- **双脚本引擎** — Lua（默认）和 V8/TypeScript（可选），支持热加载和沙箱隔离
- **670+ 测试覆盖** — 完整的单元测试和集成测试，确保跨平台稳定性
- **IPC 守护服务** — claw-server 提供全局的渠道注册、工具桥接、触发器存储和 Webhook 服务

<!-- lastCommit: f70462b -->

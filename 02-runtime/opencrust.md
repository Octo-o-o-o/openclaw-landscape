# OpenCrust (49 stars)

## 问题与解决方案

OpenClaw（Node.js）存在二进制体积大（~1.2 GB）、内存占用高（~388 MB）、冷启动慢（13.9 秒）、凭证明文存储等问题。OpenCrust 使用 Rust 重写，将二进制压缩至 16 MB、内存降至 13 MB、冷启动缩短至 3 ms，并提供 AES-256-GCM 加密凭证存储和默认启用的 WebSocket 认证。

## 关键特性

- **极致性能** — 16 MB 二进制、13 MB 内存占用、3 ms 冷启动，相比 OpenClaw 提升 75-98%
- **安全优先** — AES-256-GCM 加密凭证库、默认启用 WebSocket 配对认证、用户白名单、提示词注入检测
- **跨平台预编译** — 提供 Linux（x86_64/aarch64）、macOS（Intel/Apple Silicon）、Windows（x86_64）预编译二进制
- **配置热加载** — 支持运行时配置热加载，无需重启服务
- **WASM 插件沙箱** — 可选的 WebAssembly 插件系统，提供受控的宿主访问
- **14 个 LLM 提供商** — 原生支持 Anthropic、OpenAI、Ollama，兼容 DeepSeek、Mistral、Gemini、Qwen 等 OpenAI 兼容接口

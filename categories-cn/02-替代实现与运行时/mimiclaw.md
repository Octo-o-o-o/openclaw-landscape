> https://github.com/memovai/mimiclaw

# MimiClaw (4,260 stars)

## 问题与解决方案

MimiClaw 解决了 AI Agent 运行的硬件门槛问题。传统 OpenClaw 需要 Linux/macOS + Node.js + 至少 Mac mini 级别的硬件，而 MimiClaw 将完整的 Agent 运行时压缩到 5 美元的 ESP32-S3 芯片上，无需操作系统，纯 C 实现，功耗仅 0.5W，可 24/7 运行。

## 关键特性

- **极致轻量**：无 Linux、无 Node.js、无运行时依赖，纯 C 实现，单芯片运行完整 Agent 循环
- **硬件要求**：ESP32-S3 开发板（16MB Flash + 8MB PSRAM），成本约 5-10 美元
- **双模型支持**：支持 Anthropic Claude 和 OpenAI GPT，运行时可切换
- **本地存储**：所有数据（记忆、配置）存储在芯片 Flash 中，跨重启持久化
- **Telegram 交互**：通过 WiFi 连接 Telegram Bot，接收指令、调用工具、返回结果
- **两层配置系统**：编译时默认配置（`mimi_secrets.h`）+ 运行时 CLI 覆盖（NVS Flash 存储）

<!-- lastCommit: 6a7050b -->

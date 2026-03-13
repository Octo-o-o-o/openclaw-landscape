> https://github.com/tnm/zclaw

# zclaw (1,874 stars)

## 问题与解决方案

ESP32 硬件资源极度受限（<= 888 KiB 固件预算），传统 AI 助手无法运行。zclaw 用纯 C 实现超轻量级个人 AI 助手，在 ESP32 上提供完整的调度、GPIO 控制、持久化记忆和自定义工具能力，通过自然语言交互控制物联网设备。

## 关键特性

- **极致轻量** — 全固件（含 ESP-IDF/FreeRTOS/Wi-Fi/TLS）<= 888 KiB，应用代码仅约 35 KB
- **完整调度系统** — 支持 `daily`/`periodic`/`once` 时区感知任务，内置 cron 表达式解析
- **GPIO 工具链** — 读写控制 + 批量 `gpio_read_all`，带安全防护
- **多 LLM 后端** — Anthropic/OpenAI/OpenRouter/Ollama（自定义端点）
- **持久化记忆** — 跨重启保留上下文，支持 4 种 persona（neutral/friendly/technical/witty）
- **USB 本地管理台** — 预网络启动、安全模式、恢复诊断
- **一键部署** — `curl | bash` 引导脚本，自动检测 apt/pacman/dnf/zypper，支持加密凭证闪存

# OpenClaw Assistant (157 stars)

## 问题与解决方案
OpenClaw Agent 缺乏原生的移动端语音助手体验，用户无法通过唤醒词或长按 Home 键快速调用 Agent。OpenClaw Assistant 是一个专为 OpenClaw 设计的 Android 语音助手应用，支持自定义唤醒词、离线唤醒词检测、系统助手集成、Wear OS 支持和多种 TTS 提供商。

## 关键特性
- 自定义唤醒词（OpenClaw/Hey Assistant/Jarvis/Computer 或自定义短语）
- 离线唤醒词检测（基于 Vosk 的本地处理，无需联网）
- 语音识别（实时语音转文本 + 部分结果显示 + 可配置静音超时）
- 文本转语音（支持 Android 原生、ElevenLabs、OpenAI、VOICEVOX）
- 连续对话模式（AI 响应后自动恢复监听）
- 系统助手集成（长按 Home 键通过 VoiceInteractionService 激活）
- Wear OS 支持（直接从智能手表使用）
- 应用内聊天界面（文本和语音输入、Markdown 渲染、消息时间戳）
- Agent 选择（从网关动态获取多个 AI Agent）
- 实时流式传输（通过 WebSocket 网关即时查看 AI 响应）
- 设备配对（服务器端设备审批 + Ed25519 加密身份）

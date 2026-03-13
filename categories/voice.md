# Voice

> Voice interfaces and speech integration for agents.
> Agent 的语音接口和语音集成。

**2 projects** | [Back to overview](../README.md)

---

### OpenClaw Assistant

[yuga-hashimoto/openclaw-assistant](https://github.com/yuga-hashimoto/openclaw-assistant) | Stars: 157
Researched: 2026-03-11 | Updated: 2026-03-13

OpenClaw Agent 缺乏原生的移动端语音助手体验，用户无法通过唤醒词或长按 Home 键快速调用 Agent。OpenClaw Assistant 是一个专为 OpenClaw 设计的 Android 语音助手应用，支持自定义唤醒词、离线唤醒词检测、系统助手集成、Wear OS 支持和多种 TTS 提供商。

**Features:** 自定义唤醒词（OpenClaw/Hey Assistant/Jarvis/Computer 或自定义短语）, 离线唤醒词检测（基于 Vosk 的本地处理, 语音识别（实时语音转文本 + 部分结果显示 + 可配置静音超时）, 文本转语音（支持 Android 原生、ElevenLabs、OpenAI、VOICEVOX）, 连续对话模式（AI 响应后自动恢复监听）, 系统助手集成（长按 Home 键通过 VoiceInteractionService 激活）

---

### OpenClaw Voice

[Purple-Horizons/openclaw-voice](https://github.com/Purple-Horizons/openclaw-voice) | Stars: 66
Researched: 2026-03-11 | Updated: 2026-03-13

AI 助手缺乏开源、自托管、隐私优先的语音交互方案，用户的语音数据通常需要上传到云端。OpenClaw Voice 提供了一个基于浏览器的开源语音界面，支持本地 Whisper STT（语音永不离开本机）、ElevenLabs 流式 TTS（逐句流式播放）、Silero VAD（语音活动检测）和智能文本清理，适配桌面和移动端。

**Features:** 本地 STT（Whisper 通过 faster-whisper 本地运行, 流式 TTS（ElevenLabs 逐句流式播放, 语音活动检测（Silero VAD 过滤背景噪音, 智能文本清理（TTS 前去除 Markdown、标签、URL, 任意 AI 后端（OpenAI、Claude 或完整的 OpenClaw Agent + 内存 + 工具）, 基于浏览器（无需安装应用

---

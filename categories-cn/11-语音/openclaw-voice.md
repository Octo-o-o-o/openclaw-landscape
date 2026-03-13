> https://github.com/Purple-Horizons/openclaw-voice

# OpenClaw Voice (66 stars)

## 问题与解决方案
AI 助手缺乏开源、自托管、隐私优先的语音交互方案，用户的语音数据通常需要上传到云端。OpenClaw Voice 提供了一个基于浏览器的开源语音界面，支持本地 Whisper STT（语音永不离开本机）、ElevenLabs 流式 TTS（逐句流式播放）、Silero VAD（语音活动检测）和智能文本清理，适配桌面和移动端。

## 关键特性
- 本地 STT（Whisper 通过 faster-whisper 本地运行，语音永不离开本机）
- 流式 TTS（ElevenLabs 逐句流式播放，边生成边播放）
- 语音活动检测（Silero VAD 过滤背景噪音，适应嘈杂环境）
- 智能文本清理（TTS 前去除 Markdown、标签、URL，避免"井号井号"）
- 任意 AI 后端（OpenAI、Claude 或完整的 OpenClaw Agent + 内存 + 工具）
- 基于浏览器（无需安装应用，桌面和移动端均可使用）
- 连续模式（免提对话，每次响应后自动监听）

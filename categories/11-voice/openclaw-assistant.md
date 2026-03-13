> https://github.com/yuga-hashimoto/openclaw-assistant

# OpenClaw Assistant (157 stars)

## Problem & Solution
OpenClaw Agent lacks a native mobile voice assistant experience — users cannot quickly invoke an Agent via wake words or long-pressing the Home button. OpenClaw Assistant is an Android voice assistant app designed specifically for OpenClaw, supporting custom wake words, offline wake word detection, system assistant integration, Wear OS support, and multiple TTS providers.

## Key Features
- Custom wake words (OpenClaw/Hey Assistant/Jarvis/Computer or custom phrases)
- Offline wake word detection (Vosk-based local processing, no internet required)
- Speech recognition (real-time speech-to-text + partial results display + configurable silence timeout)
- Text-to-speech (supports Android native, ElevenLabs, OpenAI, VOICEVOX)
- Continuous conversation mode (automatically resumes listening after AI response)
- System assistant integration (long-press Home button activation via VoiceInteractionService)
- Wear OS support (use directly from smartwatch)
- In-app chat interface (text and voice input, Markdown rendering, message timestamps)
- Agent selection (dynamically fetches multiple AI Agents from Gateway)
- Real-time streaming (instant AI response viewing via WebSocket Gateway)
- Device pairing (server-side device approval + Ed25519 encrypted identity)

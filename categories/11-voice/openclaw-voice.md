> https://github.com/Purple-Horizons/openclaw-voice

# OpenClaw Voice (66 stars)

## Problem & Solution
AI assistants lack an open-source, self-hosted, privacy-first voice interaction solution — users' voice data typically needs to be uploaded to the cloud. OpenClaw Voice provides a browser-based open-source voice interface supporting local Whisper STT (voice never leaves the device), ElevenLabs streaming TTS (sentence-by-sentence streaming playback), Silero VAD (voice activity detection), and intelligent text cleaning, compatible with both desktop and mobile.

## Key Features
- Local STT (Whisper via faster-whisper runs locally, voice never leaves the device)
- Streaming TTS (ElevenLabs sentence-by-sentence streaming playback, generates and plays simultaneously)
- Voice activity detection (Silero VAD filters background noise, adapts to noisy environments)
- Intelligent text cleaning (removes Markdown, tags, URLs before TTS to avoid reading out "hashtag hashtag")
- Any AI backend (OpenAI, Claude, or full OpenClaw Agent + memory + tools)
- Browser-based (no app installation required, works on both desktop and mobile)
- Continuous mode (hands-free conversation, automatically listens after each response)

> https://github.com/memovai/mimiclaw

# MimiClaw (4,260 stars)

## Problem & Solution

MimiClaw addresses the hardware barrier for running AI Agents. Traditional OpenClaw requires Linux/macOS + Node.js + at least Mac mini-level hardware, whereas MimiClaw compresses the complete Agent runtime onto a $5 ESP32-S3 chip — no operating system needed, pure C implementation, only 0.5W power consumption, capable of running 24/7.

## Key Features

- **Ultra Lightweight**: No Linux, no Node.js, no runtime dependencies — pure C implementation running the complete Agent loop on a single chip
- **Hardware Requirements**: ESP32-S3 development board (16MB Flash + 8MB PSRAM), costing approximately $5-10
- **Dual Model Support**: Supports both Anthropic Claude and OpenAI GPT, switchable at runtime
- **Local Storage**: All data (memory, configuration) stored in chip Flash, persistent across reboots
- **Telegram Interaction**: Connects to Telegram Bot via WiFi, receives commands, invokes tools, and returns results
- **Two-tier Configuration System**: Compile-time default configuration (`mimi_secrets.h`) + runtime CLI override (NVS Flash storage)

<!-- lastCommit: 5ff0920399584f8c29d8082298919410003a1ac4 -->

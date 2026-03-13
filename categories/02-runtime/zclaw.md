> https://github.com/tnm/zclaw

# zclaw (1,874 stars)

## Problem & Solution

ESP32 hardware resources are extremely constrained (<= 888 KiB firmware budget), and traditional AI assistants cannot run on them. zclaw implements an ultra-lightweight personal AI assistant in pure C on the ESP32, providing full scheduling, GPIO control, persistent memory, and custom tool capabilities, enabling natural language interaction to control IoT devices.

## Key Features

- **Ultra Lightweight** — Full firmware (including ESP-IDF/FreeRTOS/Wi-Fi/TLS) <= 888 KiB, application code only ~35 KB
- **Complete Scheduling System** — Supports `daily`/`periodic`/`once` timezone-aware tasks, with built-in cron expression parsing
- **GPIO Toolchain** — Read/write control + batch `gpio_read_all`, with safety protections
- **Multiple LLM Backends** — Anthropic/OpenAI/OpenRouter/Ollama (custom endpoints)
- **Persistent Memory** — Context retained across reboots, supports 4 personas (neutral/friendly/technical/witty)
- **USB Local Console** — Pre-network boot, safe mode, recovery diagnostics
- **One-click Deployment** — `curl | bash` bootstrap script, auto-detects apt/pacman/dnf/zypper, supports encrypted credential flashing

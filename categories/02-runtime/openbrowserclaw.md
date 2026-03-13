> https://github.com/sachaa/openbrowserclaw

# openbrowserclaw (558 stars)

## Problem & Solution

Traditional AI assistants require server infrastructure (databases, filesystems, background processes), increasing deployment costs and privacy risks. openbrowserclaw moves the entire Agent runtime into a browser tab, using IndexedDB/OPFS/Web Worker/WebAssembly to achieve a zero-infrastructure personal AI assistant with fully local data.

## Key Features

- **Pure Browser Architecture** — IndexedDB (messages/tasks/config) + OPFS (file storage) + Web Worker (Agent loop) + WebVM (v86 Alpine Linux sandbox)
- **Zero Server Dependency** — All state and computation on the client side, API keys stored with AES-256-GCM encryption
- **Built-in Toolchain** — `bash` (WebVM sandbox), `javascript` (isolated scope), `read_file`/`write_file`, `fetch_url`, `update_memory`, `create_task`
- **Multi-channel Support** — In-browser chat + Telegram Bot API (pure HTTPS, no WebSocket)
- **PWA Offline Capability** — Service Worker caching, task queue retained after tab closure
- **Cron Scheduler** — In-browser cron expression parsing and task triggering

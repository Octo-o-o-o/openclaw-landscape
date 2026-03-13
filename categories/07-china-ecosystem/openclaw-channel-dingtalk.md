> https://github.com/soimy/channel-dingtalk

# openclaw-channel-dingtalk (1,267 stars)

## Problem & Solution
Enterprise users need to use AI assistants within DingTalk, but OpenClaw lacks native DingTalk connectivity. This project implements DingTalk enterprise internal bot integration through a DingTalk Channel Plugin using Stream mode (no public IP required), supporting private chat, group chat, multiple message types, and interactive cards.

## Key Features
- Stream mode: WebSocket long connection, no public IP or Webhook required
- Supports private chat and group chat (@bot)
- Supports text, images, voice (with built-in recognition), video, files, DingTalk document/DingDisk file cards
- Quote message support: Recovers most quote scenarios (text/image/image-text/file/video/voice/AI card)
- Markdown replies and interactive cards (with streaming update support)
- Process-level in-memory state: Message deduplication, session locks, gateway in-flight duplicate prevention locks
- China mirror source support (npm mirrors)

<!-- lastCommit: 6a7050b -->

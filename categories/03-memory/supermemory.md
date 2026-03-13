> https://github.com/supermemoryai/openclaw-supermemory

# OpenClaw Supermemory (579 stars)

## Problem & Solution

OpenClaw Supermemory addresses the "short-term memory limitation" pain point for Agents. Through the Supermemory cloud service (requires Pro or higher subscription), it provides long-term memory capabilities for OpenClaw Agents: automatically memorizing conversations, recalling relevant context, and building persistent user profiles without local infrastructure. Auto-Recall (querying relevant memories before each AI turn and injecting them into context) + Auto-Capture (sending conversations to the cloud after each AI turn for extraction and deduplication) + custom container tags (work/personal/bookmarks etc., with AI auto-routing) enable fully automated memory management.

## Key Features

- **Cloud-Based Long-Term Memory** -- Built on the Supermemory cloud service, automatically extracts, deduplicates, and builds user profiles without local deployment
- **Auto-Recall** -- Before each AI turn, queries semantically similar historical conversations and user profiles for injection as context (default max 10 entries)
- **Auto-Capture** -- After each AI turn, sends conversations to the cloud for key information extraction and long-term storage (supports `all` to filter short texts or `everything` for full capture)
- **Custom Container Tags** -- Define containers like work/personal/bookmarks, with AI automatically selecting containers based on instructions (e.g., "store work tasks to work")
- **Slash Commands + AI Tools** -- `/remember <text>` for manual saving, `/recall <query>` for memory search; AI autonomously uses `supermemory_store`/`search`/`forget`/`profile` tools
- **CLI Management** -- `openclaw supermemory setup` to configure API Key, `status` to view configuration, `search <query>` to search memories, `profile` to view user profiles, `wipe` to delete all memories
- **Flexible Configuration** -- Supports environment variables (`SUPERMEMORY_OPENCLAW_API_KEY`) or `~/.openclaw/openclaw.json` configuration, with adjustable recall count, profile injection frequency, capture mode, and more

<!-- lastCommit: 6a7050b -->

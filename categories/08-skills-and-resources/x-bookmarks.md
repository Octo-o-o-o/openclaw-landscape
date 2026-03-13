> https://github.com/sharbelxyz/x-bookmarks

# sharbelxyz/x-bookmarks (241 stars)

## Problem & Solution

X/Twitter's bookmark feature lacks export and bulk management capabilities, preventing users from using saved tweets for knowledge management or Agent workflows. This project provides an OpenClaw skill that uses browser automation to bulk export bookmarks as structured data, supporting filtering, search, and integration with other tools.

## Key Features

- **Bulk bookmark export** — Automatically traverses the X bookmark list, extracting tweet IDs, text, authors, timestamps, media links, and other complete metadata
- **Structured output** — Exports to JSON/CSV format for easy import into Notion, Obsidian, and other knowledge management tools, or for Agent consumption
- **Filtering & search** — Supports filtering bookmarks by keyword, date range, and author for quick content location
- **OpenClaw native integration** — As a standard SKILL.md skill, can be installed directly via `npx sundial-hub add x-bookmarks`
- **Incremental sync** — Supports exporting only newly added bookmarks, avoiding reprocessing of already exported content
- **Privacy protection** — Runs locally without uploading bookmark data to third-party servers

<!-- lastCommit: 6a7050b -->

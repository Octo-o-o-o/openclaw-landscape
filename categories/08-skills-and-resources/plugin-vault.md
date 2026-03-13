> https://github.com/pepicrft/plugin-vault

# OpenClaw Vault Plugin (41 stars)

## Problem & Solution
OpenClaw lacks structured knowledge management capabilities, requiring users to rely on external tools (such as Obsidian) for managing notes and knowledge bases. Vault Plugin transforms a local directory into a structured knowledge base, providing fast semantic search and embeddings through qmd while maintaining a pure markdown format.

## Key Features
- **Local-first architecture** — Pure markdown file storage with no external database required; supports git sync (pull before, push after)
- **Convention-based directory structure** — inbox (raw capture), notes (evergreen notes), people (biographies), projects (project briefs), concepts (concept definitions), logs (daily notes)
- **Frontmatter framework** — Required fields (title, created, updated) + recommended fields (summary, status, tags, people, projects, sources)
- **QMD search engine** — Supports keyword, semantic, and hybrid search modes; auto-installs qmd (via bun or npm)
- **CLI + Tools + Gateway RPC** — Three access methods: `openclaw vault init/add/query`, Agent tool calls, and Gateway HTTP endpoints
- **Automatic git commits** — Optional auto git commit and push to maintain knowledge base version control

<!-- lastCommit: 6a7050b -->

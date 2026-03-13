# Contributing to OpenClaw Landscape

Thanks for helping us keep this directory up to date!

## Adding a New Project

1. Fork this repository
2. Add the project to `data/projects.json` in the appropriate category
3. Run `python scripts/generate.py` to regenerate Markdown files
4. Submit a Pull Request

### Project Entry Format

```json
{
  "repo": "owner/repo-name",
  "name": "Display Name",
  "category": "runtime",
  "stars": 0,
  "language": "Python",
  "license": "MIT",
  "description": "A one-line description of what this project does.",
  "features": ["feature 1", "feature 2", "feature 3"],
  "last_researched": "2026-03-13",
  "last_updated": "2026-03-13",
  "status": "active",
  "archived": false
}
```

### Valid Categories

| Category ID | Description |
|-------------|-------------|
| `official` | OpenClaw official projects |
| `runtime` | Alternative implementations and runtimes |
| `memory` | Memory management systems |
| `security` | Security tools |
| `dashboard-and-monitoring` | Dashboards and monitoring |
| `deployment` | Deployment tools |
| `china-ecosystem` | China ecosystem (Feishu, DingTalk, WeChat, etc.) |
| `skills-and-resources` | Skills, templates, and resources |
| `protocols` | A2A / MCP / ACP protocol implementations |
| `ops` | Ops and maintenance tools |
| `voice` | Voice interfaces |
| `routing-and-cost` | LLM routing and cost optimization |
| `orchestration` | Multi-agent orchestration |
| `clients` | Desktop and mobile clients |
| `other` | Other |

### Guidelines

- The project must be related to the OpenClaw / Claw ecosystem
- Include a clear, factual description (no marketing language)
- Stars count will be auto-updated daily — just put `0` if you're unsure
- One project per PR makes review easier

## Updating an Existing Project

If a project description is outdated or incorrect, edit its entry in `data/projects.json` and submit a PR.

## Reporting Issues

If a listed project is no longer maintained, has been archived, or contains inaccurate information, please [open an issue](https://github.com/Octo-o-o-o/openclaw-landscape/issues/new).

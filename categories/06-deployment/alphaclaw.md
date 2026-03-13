> https://github.com/chrysb/alphaclaw

# AlphaClaw (482 stars)

## Problem and Solution

OpenClaw deployment and operations suffer from complex configuration, manual crash recovery, and insufficient observability. AlphaClaw provides a browser-based configuration wizard, a self-healing Watchdog, Git rollback, and full-stack observability, reducing the time from first deployment to first message to under 5 minutes, with one-click deployment support for Railway/Render.

## Key Features

- **Setup UI** -- Password-protected web dashboard covering onboarding, configuration management, and day-to-day operations, with no need for SSH or CLI
- **Gateway Manager** -- Acts as a parent process to manage OpenClaw Gateway startup, monitoring, restart, and proxying
- **Watchdog** -- Crash detection, crash loop recovery, automatic repair (`openclaw doctor --fix`), and Telegram/Discord notifications
- **Channel Orchestration** -- Telegram/Discord bot pairing, credential synchronization, and Telegram multi-threaded Topic grouping wizard
- **Prompt Hardening** -- Built-in anti-drift guided prompts (`AGENTS.md`, `TOOLS.md`) enforcing security practices, commit discipline, and change summaries
- **Git Sync** -- Automatic hourly commits of the OpenClaw workspace to GitHub, with configurable cron scheduling, combined with Prompt Hardening for version control and auditing
- **File Explorer** -- Browser-based file explorer supporting file visibility, inline editing, diff views, and Git-aware synchronization
- **Google Workspace OAuth** -- Gmail/Calendar/Drive/Docs/Sheets/Tasks/Contacts/Meet integration, Gmail watch + Google Pub/Sub push endpoint handling

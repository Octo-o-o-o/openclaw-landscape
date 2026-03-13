> https://github.com/LeoYeAI/openclaw-backup

# openclaw-backup (916 stars)

## Problem & Solution
OpenClaw instance migration and backup lack a standardized solution, requiring users to manually back up configurations, credentials, session history, and other data. This project provides one-click backup and restore functionality, packaging workspace, memory, skills, credentials, bot tokens, API keys, and agent session history into a single archive file, supporting zero-reconfiguration migration to new instances.

## Key Features
- One-click backup: workspace, config, credentials, sessions, cron jobs, scripts
- One-click restore: supports dry-run preview, no re-pairing required after restore
- Browser UI: download/upload/restore backup files
- Server migration: download backup from old machine, upload and restore on new machine
- Security measures: backup files chmod 600, HTTP server enforces token authentication
- Powered by MyClaw.ai, published on ClawHub

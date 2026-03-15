> https://github.com/LeoYeAI/openclaw-guardian

# OpenClaw Guardian

## Basic Info

- **Project Name**: OpenClaw Guardian
- **GitHub**: https://github.com/LeoYeAI/openclaw-guardian
- **Stars**: 938
- **Author**: LeoYeAI (MyClaw.ai team)
- **License**: MIT
- **Purpose**: Production-grade watchdog daemon for OpenClaw Gateway

## Problem & Solution

### Core Problem

Stability challenges facing OpenClaw Gateway in production environments:

1. **Gateway process crashes unexpectedly** — Due to memory leaks, uncaught exceptions, dependency service failures, etc., the Gateway process may suddenly stop during operation
2. **Configuration errors prevent startup** — Users modifying skills, config files, or dependencies in the workspace may introduce syntax or logic errors that prevent normal Gateway startup
3. **Service outages in unattended scenarios** — The MyClaw.ai platform runs thousands of AI Agent instances requiring 24/7 automatic recovery, making manual intervention too costly
4. **Lack of historical rollback mechanism** — When the workspace is corrupted, there is no automatic rollback to the last stable state
5. **Delayed failure notifications** — Operations teams cannot immediately detect Gateway anomalies

### Solution

Guardian provides a three-layer automatic recovery mechanism + notification system:

**Layer 1: Automatic Health Checks**
- Checks every 30 seconds (configurable) whether the Gateway process is alive (via `pgrep -f "openclaw-gateway"`)
- Lightweight, low-overhead monitoring loop

**Layer 2: `openclaw doctor --fix` Auto-Repair**
- Upon detecting Gateway stoppage, automatically runs OpenClaw's official diagnostic repair tool
- Up to 3 attempts (configurable), with 10-second intervals between each
- Resumes monitoring immediately after successful repair, no manual intervention needed

**Layer 3: Git Rollback + Force Restart**
- Triggered when `doctor --fix` fails consecutively
- Automatically identifies the most recent stable commit (excluding `rollback`, `daily-backup`, `auto-backup`, `guardian-auto` auto-commits)
- Executes `git reset --hard <stable-commit>` to revert to the stable version
- Force kills old process and restarts the Gateway
- Creates a rollback record commit for post-incident auditing

**Layer 4: Cooldown Period + Continuous Monitoring**
- If rollback still fails, enters a 300-second (configurable) cooldown period to avoid infinite loops
- Automatically resumes monitoring after cooldown

**Additional Feature: Daily Auto-Snapshots**
- Automatically executes `git add -A && git commit -m "daily-backup: auto snapshot YYYY-MM-DD"` daily
- Provides a stable historical version base for the rollback mechanism

**Optional Notifications: Discord Webhook**
- Supports Discord notifications via the `DISCORD_WEBHOOK_URL` environment variable
- Key events (startup, failure, successful repair, rollback) are pushed to the ops channel in real time

## Core Architecture

### Tech Stack

- **Language**: Bash Shell Script (single file `guardian.sh`, ~150 lines)
- **Dependencies**:
  - `git` — workspace rollback and snapshots
  - `pgrep` / `pkill` — process detection and management
  - `curl` — Discord notifications (optional)
  - `openclaw` CLI — official diagnostic tool

### Architecture Design

```
┌─────────────────────────────────────────────────────────────┐
│                    Guardian Main Loop                         │
│  while true; do                                              │
│    daily_backup()      # Daily snapshot                      │
│    if ! is_gateway_running; then                             │
│      repair_gateway()  # Three-layer repair flow             │
│    fi                                                        │
│    sleep $CHECK_INTERVAL                                     │
│  done                                                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              repair_gateway() Repair Flow                    │
├─────────────────────────────────────────────────────────────┤
│  1. notify("Gateway anomaly, starting repair...")            │
│  2. for i in 1..MAX_REPAIR_ATTEMPTS:                         │
│       try_doctor_fix()                                       │
│       if success: return 0                                   │
│  3. notify("doctor --fix failed, trying git rollback...")    │
│  4. do_rollback()                                            │
│       - get_stable_commit()  # Find stable version           │
│       - git reset --hard <commit>                            │
│       - pkill + restart gateway                              │
│       - if success: return 0                                 │
│  5. notify("All repair methods failed, cooldown...")         │
│  6. sleep $COOLDOWN_PERIOD                                   │
└─────────────────────────────────────────────────────────────┘
```

### Configuration Parameters

| Environment Variable | Default | Description |
|---------|--------|------|
| `GUARDIAN_WORKSPACE` | `$HOME/.openclaw/workspace` | Workspace path (must be a git repo) |
| `GUARDIAN_LOG` | `/tmp/openclaw-guardian.log` | Log file path |
| `GUARDIAN_CHECK_INTERVAL` | `30` | Health check interval (seconds) |
| `GUARDIAN_MAX_REPAIR` | `3` | Max `doctor --fix` attempts |
| `GUARDIAN_COOLDOWN` | `300` | Post-failure cooldown period (seconds) |
| `OPENCLAW_CMD` | `openclaw` | OpenClaw CLI command |
| `DISCORD_WEBHOOK_URL` | _(unset)_ | Discord notification Webhook (optional) |

### Deployment Methods

**1. Manual Deployment**
```bash
# Initialize workspace git repo (required)
cd ~/.openclaw/workspace
git init && git add -A && git commit -m "initial"

# Install Guardian
cp scripts/guardian.sh ~/.openclaw/guardian.sh
chmod +x ~/.openclaw/guardian.sh

# Start in background
nohup ~/.openclaw/guardian.sh >> /tmp/openclaw-guardian.log 2>&1 &
```

**2. AI Agent Auto-Install**
Users simply tell their OpenClaw Agent:
> "Help me install openclaw-guardian to harden my gateway"

The Agent will automatically complete git initialization, script installation, and startup.

**3. Auto-Start on Container Restart**
Add to `~/.openclaw/start-gateway.sh`:
```bash
pkill -f "guardian.sh" 2>/dev/null || true
nohup /home/ubuntu/.openclaw/guardian.sh >> /tmp/openclaw-guardian.log 2>&1 &
```

**4. Install as OpenClaw Skill**
```bash
clawhub install myclaw-guardian
```

## Key Features

### 1. Zero-Configuration Out of the Box

- All parameters have reasonable defaults
- Runs directly without code modifications
- Behavior flexibly adjusted via environment variables

### 2. Progressive Repair Strategy

- Prioritizes the official `doctor --fix` tool (least invasive)
- Only performs git rollback when necessary (preserves user modifications)
- Avoids overly aggressive recovery operations

### 3. Intelligent Stable Version Identification

The `get_stable_commit()` function excludes auto-commits via regex:
```bash
git log --all --oneline -50 | \
  grep -v -E "rollback|daily-backup|auto-backup|guardian-auto" | \
  sed -n '2p' | awk '{print $1}'
```
- Skips the most recent commit (which may be the version that caused the failure)
- Selects the second-to-last manual commit as the rollback target

### 4. Infinite Loop Prevention

- Forces a cooldown period after repair failure (default 5 minutes)
- Prevents continuous resource consumption in unrecoverable situations
- Leaves a time window for manual intervention

### 5. Complementary to gw-watchdog

| Feature | gw-watchdog | Guardian |
|------|-------------|----------|
| Check interval | 15 seconds | 30 seconds |
| Repair action | Quick restart | `doctor --fix` then git rollback |
| Git rollback | No | Yes |
| Discord notifications | No | Yes |
| Daily backup | No | Yes |

Both can run simultaneously:
- `gw-watchdog` handles transient crashes (quick restart)
- `Guardian` handles configuration errors and persistent failures (deep repair)

### 6. Production-Grade Logging and Notifications

**Log format**:
```
[2026-03-11 14:32:15] Guardian daemon started (check=30s, max_repair=3)
[2026-03-11 14:35:42] Gateway anomaly, starting repair flow...
[2026-03-11 14:35:43] Repair attempt 1/3
[2026-03-11 14:35:53] doctor --fix repair successful, Gateway recovered
```

**Discord notification example**:
```
**OpenClaw Guardian**: Gateway anomaly, starting repair flow...
**OpenClaw Guardian**: doctor --fix repair successful (attempt 1)
```

### 7. Security Considerations

- Script uses `set -euo pipefail` strict mode
- Records current commit SHA before rollback for post-incident recovery
- All git operations execute within the workspace directory, not affecting other repos
- Discord Webhook URL passed via environment variable, not hardcoded in the script

## Summary

OpenClaw Guardian is a **production-grade, zero-configuration, progressive repair** Agent watchdog solution. Its core value lies in:

1. **Automated operations**: Handles 90% of common failures without manual intervention
2. **Progressive repair**: From least invasive (restart) to deep recovery (git rollback), avoiding excessive aggression
3. **Intelligent rollback**: Automatically identifies stable versions, avoiding rollback to equally problematic configurations
4. **Lightweight design**: Single Bash script, no additional dependencies, minimal resource footprint
5. **Production-proven**: Battle-tested running thousands of instances on the MyClaw.ai platform

<!-- lastCommit: aabd2a02365c5ec63e679e99bc6ac6e125c550d9 -->

> https://github.com/openclawq/clawmonitor

# ClawMonitor

> openclawq/clawmonitor · ⭐ 32 · Python · MIT
> Research date: 2026-03-13

## Overview

ClawMonitor is a lightweight real-time monitoring tool for OpenClaw Agent sessions. It provides both TUI (Terminal User Interface) and CLI interaction modes, capable of tracking the status, message exchanges, and execution progress of multiple Agent sessions.

## Core Features

| Feature | Description |
|---------|-------------|
| Session Status Tracking | Real-time display of each session's status (WORKING / FINISHED / INTERRUPTED / NO_MESSAGE) |
| TUI Interface | Full-screen terminal interface with color coding (OK=green / RUN=cyan / IDLE=yellow / ALERT=red) |
| Offline Monitoring | Works via `*.jsonl.lock` files even when the Gateway is unavailable |
| Nudge Function | Proactively prompts Agents to report progress via `chat.send` |
| Snapshot Export | Exports a snapshot of all current session states |
| Report Generation | Generates session reports |
| Log Integration | Optional Gateway log tailing with special rules for Feishu/Telegram |

## Tech Stack

- **Language**: Python
- **Interface**: TUI (Terminal User Interface)
- **Configuration**: TOML (`~/.config/clawmonitor/config.toml`)
- **Logging**: JSONL (`~/.local/state/clawmonitor/events.jsonl`)
- **Distribution**: PyPI (`pip install clawmonitor`)

## CLI Commands

```bash
clawmonitor init       # Initialize configuration
clawmonitor tui        # Launch interactive monitoring
clawmonitor status     # Display session status
clawmonitor snapshot   # Export current state
clawmonitor nudge      # Send progress nudge request
clawmonitor report     # Generate session report
```

## Architecture Highlights

1. **Security-Aware**: Automatically redacts tokens, does not dump sensitive configurations
2. **XDG Compliant**: Follows XDG directory specification (config / state / cache separation)
3. **Offline Degradation**: Maintains basic monitoring via lock files when Gateway is disconnected
4. **ClawHub Integration**: Provides a `skills/claw-monitor/` directory for use as an OpenClaw skill
5. **IM-Aware**: Detects Telegram thread binding routes (`BOUND_OTHER` marker)

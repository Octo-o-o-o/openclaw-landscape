> https://github.com/tugcantopaloglu/dashboard

# tugcantopaloglu/openclaw-dashboard (N/A stars)

> Research date: 2026-03-13 (updated)
> Positioning: Real-time Agent monitoring dashboard with authentication and TOTP MFA, emphasizing security hardening

## Problem & Solution

OpenClaw Agent operational information is scattered across logs and CLI, and lacks a secure remote access solution. This project provides a zero-npm-dependency Node.js dashboard emphasizing security hardening (TOTP MFA, CSP, audit logs, rate limiting), with support for secure remote access via Tailscale.

## Key Features

### Monitoring & Analytics
- **Real-Time Session Management** — Active session status tracking, search and filter by status/model/date
- **API Rate Limit Tracking** — Visualization of Claude and Gemini API rate limits
- **Cost Analysis** — Cost breakdown by model/session
- **Activity Heatmap** — 30-day activity visualization + daily streak tracking
- **System Health** — CPU, RAM, disk, temperature + 24-hour sparkline mini-charts

### Agent Management
- **Memory Browser** — Browse MEMORY.md, HEARTBEAT.md, daily notes
- **Cron Management** — View/enable/disable/manually trigger cron jobs
- **Service Control** — Restart OpenClaw, Dashboard, and other services
- **Git Activity** — Cross-repository Git activity tracking
- **Config Editor** — JSON validation + automatic backup

### System Integration
- **Tailscale** — Status and peer monitoring
- **Docker** — Container/image management, resource cleanup
- **Security Panel** — UFW rules, open ports, fail2ban monitoring
- **System Logs** — Auto-refreshing log viewer

## Security Architecture (Core Highlight)

| Security Feature | Implementation Details |
|-----------------|----------------------|
| Password Storage | PBKDF2 + 100,000 SHA-512 iterations |
| MFA | TOTP (Google Authenticator / Authy compatible), +/-1 window tolerance |
| Brute Force Protection | 5 failures -> 15-minute soft lock, 20 failures -> hard lock |
| Password Comparison | Timing-safe comparison to prevent timing attacks |
| HTTPS Policy | Only localhost (127.0.0.1) and Tailscale (100.64.0.0/10) exempt from HTTPS |
| Security Headers | HSTS, CSP (no inline scripts), X-Frame-Options: DENY, X-Content-Type-Options: nosniff |
| CORS | Same-origin policy, no wildcards |
| Audit Log | All authentication and destructive operations logged to `data/audit.log` |
| File Protection | Path traversal prevention + 1MB payload limit |
| Auto Backup | Automatically creates `.bak` files before overwrites |
| Password Recovery | Environment variable recovery token mechanism |

## UX Highlights

- **Keyboard Shortcuts** — 1-7 to switch panels, Space to refresh, / to search, Esc to close, ? for help
- **Browser Notifications** — Pushes native browser notifications when usage approaches limits
- **Remember Me** — 3-hour persistent login vs. session-level login
- **Responsive Design** — Desktop + tablet + mobile

<!-- lastCommit: 6a7050b -->

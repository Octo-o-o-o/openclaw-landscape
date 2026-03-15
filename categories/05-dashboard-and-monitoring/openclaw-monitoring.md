> https://github.com/video-db/openclaw-monitoring

# OpenClaw Monitoring by VideoDB (16 stars)

## Problem & Solution
Remotely running AI Agents lack observability — users cannot understand Agent execution status and behavior in real time, reduced to "send task -> wait -> receive success message -> hope for the best." VideoDB Monitoring transforms each Agent run into an observable, auditable, and shareable video recording through live streaming and replayable recordings.

## Key Features
- **Live Streaming + Replayable Recordings** — Each run generates a shareable URL (not a static video file), supporting both live viewing and post-hoc playback
- **Searchable Moments** — Find specific actions through VideoDB's video indexing (e.g., "when did it open the spreadsheet")
- **Webhook Alerts** — Sends notifications when anomalous behavior is detected
- **Two Integration Modes** — OpenClaw Skill (on-demand recording) and Docker Sidecar (continuous recording)
- **Agent Self-Analysis** — Agents can query their own recordings ("summarize the past 2 hours of work", "create a highlight video of today's work and publish to YouTube")
- **Multi-Scenario Applications** — Security audits (capture out-of-bounds behavior), QA testing (replay failed flows), compliance audits (complete visual audit trail), dataset preparation (build training data for computer use)

<!-- lastCommit: 724d83ee9112e5f4c6b107a0f0b2c8ce4b32f815 -->

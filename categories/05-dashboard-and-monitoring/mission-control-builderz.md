> https://github.com/builderz-labs/mission-control

# Mission Control (2,069 stars)

## Problem & Solution
Running AI Agents at scale lacks unified orchestration and monitoring tools, with tasks, costs, and logs scattered across multiple systems. Mission Control provides an open-source Agent orchestration dashboard that achieves full-stack observability through 28 panels (tasks, Agents, logs, tokens, memory, cron, alerts, webhooks, pipelines), supporting multi-gateway connections and real-time monitoring.

## Key Features
- 28 monitoring panels covering tasks, Agents, costs, logs, memory, cron, alerts, webhooks, and pipelines
- Real-time push (WebSocket + SSE) with smart polling that pauses when the user navigates away
- Zero external dependencies (SQLite + single command startup, no Redis/Postgres/Docker required)
- Role-based access control (Viewer/Operator/Admin) + Session + API Key authentication
- Quality gate system requiring review sign-off before task completion
- Multi-gateway support (OpenClaw and more coming soon)

<!-- lastCommit: 24493638682463a65ec29ebb550a00bd14098816 -->

> https://github.com/coollabsio/openclaw

# coollabsio-openclaw (287 stars)

## Problem and Solution
OpenClaw does not officially provide Docker images, requiring users to manually write Dockerfiles, install dependencies, and configure environment variables. With new versions released daily, the cost of manual updates is high. This project provides a fully automated Docker build solution that checks for new versions every 6 hours and automatically builds and pushes images. All settings are configured via environment variables, with a built-in Nginx reverse proxy and HTTP Basic Auth, plus one-click deployment support for Coolify.

## Key Features
- Automatic update workflow: checks for new versions every 6 hours, matrix builds for amd64/arm64, merged into a single manifest
- Environment variable configuration system: reads environment variables via configure.js and writes them to openclaw.json, supporting 20+ AI providers
- Nginx reverse proxy: unified entry point :8080 -> :18789, with WebSocket support and optional HTTP Basic Auth
- Browser Sidecar mode: standalone browser container communicates via CDP protocol, with VNC access and session reuse support
- Persistent storage: single /data volume stores configuration and user data, supporting cross-container migration
- Two-layer Docker build: base image (built from source) + final image (adds nginx + configuration scripts), accelerating builds
- Smoke testing: automatically verifies `openclaw --version` after build

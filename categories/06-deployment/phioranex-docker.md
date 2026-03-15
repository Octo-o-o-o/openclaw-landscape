> https://github.com/phioranex/openclaw-docker

# openclaw-docker (551 stars)

## Problem and Solution

OpenClaw officially requires building from source, with complex dependency management and environment configuration, creating a high barrier for first-time deployment. phioranex/openclaw-docker provides pre-built images and a one-click installation script, with automatic daily builds and upstream update checks every 6 hours, ensuring users always have the latest version and significantly reducing deployment costs.

## Key Features

- **Pre-built Images** -- `ghcr.io/phioranex/openclaw-docker:latest`, no need to compile the Node.js project locally
- **One-Click Installation Script** -- Linux/macOS `curl | bash`, Windows PowerShell `irm | iex`, with automatic Docker prerequisite checks
- **Automatic Update Mechanism** -- Daily builds + upstream release checks every 6 hours, fully automated CI/CD
- **Rich Installation Options** -- `--pull-only` (pull image only), `--skip-onboard` (skip wizard), `--no-start` (don't start gateway), `--install-dir` (custom directory)
- **Docker Compose Integration** -- Provides `docker-compose.yml` template for simplified multi-container orchestration
- **Persistent Volume Mapping** -- `~/.openclaw` configuration and `~/.openclaw/workspace` workspace automatically mounted

## Recent Updates

- ac13a03: Update OpenClaw version tracker to v2026.3.12

<!-- lastCommit: f1d9943981423c69847d11d2ad91953f7cdfaa92 -->

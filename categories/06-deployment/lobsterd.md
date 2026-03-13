> https://github.com/tsconfigdotjson/lobsterd

# lobsterd (25 stars)

## Problem and Solution
Multi-tenant OpenClaw deployments lack strong isolation, and shared hosts pose security risks and resource contention. lobsterd uses Firecracker MicroVMs to provide each tenant with a lightweight virtual machine, achieving network isolation, per-tenant overlay file systems, and independent OpenClaw Gateway instances.

## Key Features
- **Firecracker MicroVM Orchestration** -- Each tenant runs in an independent lightweight VM, with suspend/resume support (zero RAM footprint)
- **Per-tenant Overlay File System** -- Overlay images based on Alpine rootfs, with complete tenant data isolation
- **Network Isolation** -- Each VM has an independent network stack, unified access through Caddy reverse proxy
- **Complete CLI Toolchain** -- `spawn` (create tenant), `exec` (SSH into tenant), `configure` (open OpenClaw TUI), `devices` (list paired devices), `evict` (delete tenant), `molt` (health check and repair)
- **Watchdog Daemon** -- systemd service that automatically monitors tenant health, with auto-restart and snapshot support
- **REST API** -- `buoy` command starts an HTTP server mirroring CLI functionality, with Bearer token authentication
- **Tailscale Integration** -- Remote access provided by default via Tailscale Serve (port 8443)

<!-- lastCommit: 6a7050b -->

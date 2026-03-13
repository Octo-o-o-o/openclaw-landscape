> https://github.com/openclaw/openclaw-ansible

# openclaw/openclaw-ansible

## Basic Information

- **Stars**: 481
- **URL**: https://github.com/openclaw/openclaw-ansible
- **Purpose**: Automated, hardened deployment tool for OpenClaw
- **Tech Stack**: Ansible 2.14+ + Bash + YAML
- **Supported Platforms**: Debian 11+ / Ubuntu 20.04+ (macOS support removed on 2026-02-06)
- **Status**: Actively maintained

## Problem & Solution

### Core Problems

1. **Deployment complexity**: OpenClaw depends on multiple components (Node.js, pnpm, Docker, Tailscale, firewall, systemd), making manual installation error-prone and time-consuming
2. **Security risks**: Default configurations may expose unnecessary ports, lacking firewall and intrusion protection
3. **Environment inconsistency**: Configuration differences across servers lead to inconsistent deployment outcomes
4. **Permission management**: OpenClaw requires specific user permissions and systemd service configuration
5. **Remote access**: Secure remote access is needed without directly exposing service ports
6. **Automatic updates**: Lack of automated security patching increases maintenance burden

### Solution

openclaw-ansible provides a **one-click deployment script** that delivers:

- **Automated installation**: One command completes installation and configuration of all components
- **Security hardening**: Enables UFW firewall, Fail2ban, and automatic security updates by default
- **VPN integration**: Built-in Tailscale support, no need to expose service ports
- **Docker isolation**: Sandbox environments use Docker, preventing containers from exposing ports
- **Non-root execution**: OpenClaw runs as a non-privileged user, limiting permission scope
- **systemd service**: Auto-start, crash restart, and log management
- **Idempotency**: Can be run repeatedly, supports configuration updates and version upgrades

## Core Architecture

### 1. Installation Modes

#### Release Mode (Default, recommended for production)

```bash
curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
```

- **Installation method**: `pnpm install -g openclaw@latest`
- **Version source**: Latest stable version from the npm registry
- **Update method**: `pnpm install -g openclaw@latest`
- **Advantages**: Stable, fast, suitable for production environments

#### Development Mode (for development and testing)

```bash
git clone https://github.com/openclaw/openclaw-ansible.git
cd openclaw-ansible
ansible-playbook playbook.yml --ask-become-pass -e openclaw_install_mode=development
```

- **Installation method**: Clones source code from `https://github.com/openclaw/openclaw.git`
- **Build**: `pnpm install && pnpm build`
- **Symlink**: Binary linked to `~/.local/bin/openclaw`
- **Development tools**: Provides `openclaw-rebuild`, `openclaw-dev`, `openclaw-pull` aliases
- **Advantages**: Suitable for development, debugging, and code contributions

### 2. Security Architecture

#### Firewall (UFW)

- **Default policy**: Deny all inbound connections
- **Open ports**: SSH (22) and Tailscale (41641/udp) only
- **Docker isolation**: DOCKER-USER chain blocks containers from exposing ports to external networks
- **Verification**: `nmap -p- YOUR_SERVER_IP` should show only port 22

#### Intrusion Protection (Fail2ban)

- **SSH protection**: Monitors SSH login failures
- **Ban policy**: 5 failed attempts -> 1-hour ban
- **Logs**: `/var/log/fail2ban.log`

#### Automatic Updates (unattended-upgrades)

- **Security patches**: Automatically installs security updates
- **Reboot policy**: Automatic reboot when necessary (configurable)
- **Notifications**: Configurable email notifications

#### Systemd Hardening

- **NoNewPrivileges**: Prevents privilege escalation
- **PrivateTmp**: Isolates temporary files
- **ProtectSystem**: Protects system directories
- **Non-root**: OpenClaw runs as the `openclaw` user
- **Limited sudo**: Only allows service management commands (`systemctl restart openclaw`)

#### Tailscale VPN

- **Zero-trust networking**: No need to expose service ports to the public internet
- **End-to-end encryption**: All traffic is encrypted
- **Automatic configuration**: Supports authkey auto-connection
- **Optional**: Tailscale can be skipped, using SSH only

### 3. Component Installation

#### System Dependencies

- **DBus**: Used for systemd communication
- **Git**: Repository cloning (Development mode)
- **curl**: Downloading scripts and dependencies

#### Node.js and pnpm

- **Version**: Node.js 22.x (via NodeSource repository)
- **Package manager**: pnpm (globally installed)
- **Environment variables**: Automatically configures `PATH`

#### Docker

- **Version**: Docker CE + Compose V2
- **Purpose**: Sandbox environment for OpenClaw
- **Security**: Containers cannot expose ports to external networks (DOCKER-USER chain)
- **User group**: `openclaw` user added to the `docker` group

#### OpenClaw

- **User**: Dedicated `openclaw` system user
- **Home directory**: `/home/openclaw`
- **Installation path**:
  - Release mode: `~/.local/share/pnpm/global/5/node_modules/openclaw`
  - Development mode: `~/code/openclaw`
- **Binary**: `~/.local/bin/openclaw` (added to `PATH`)

#### Systemd Service

- **Service name**: `openclaw.service`
- **Start**: `systemctl start openclaw`
- **Auto-start**: `systemctl enable openclaw`
- **Logs**: `journalctl -u openclaw -f`
- **Restart**: `systemctl restart openclaw`

### 4. Configuration System

#### Configuration Variables

All configuration variables are defined in `roles/openclaw/defaults/main.yml` and can be overridden in three ways:

1. **Command-line arguments**:
```bash
ansible-playbook playbook.yml --ask-become-pass \
  -e openclaw_install_mode=development \
  -e "openclaw_ssh_keys=['ssh-ed25519 AAAAC3... user@host']"
```

2. **Variable files**:
```bash
cat > vars.yml << EOF
openclaw_install_mode: development
openclaw_ssh_keys:
  - "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGxxxxxxxx user@host"
tailscale_authkey: "tskey-auth-xxxxxxxxxxxxx"
EOF

ansible-playbook playbook.yml --ask-become-pass -e @vars.yml
```

3. **Direct editing**: Modify `roles/openclaw/defaults/main.yml`

#### Key Configuration Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `openclaw_user` | `openclaw` | System username |
| `openclaw_home` | `/home/openclaw` | User home directory |
| `openclaw_install_mode` | `release` | Installation mode (`release` or `development`) |
| `openclaw_ssh_keys` | `[]` | SSH public key list |
| `openclaw_repo_url` | `https://github.com/openclaw/openclaw.git` | Git repository (Development mode) |
| `openclaw_repo_branch` | `main` | Git branch (Development mode) |
| `tailscale_authkey` | `""` | Tailscale auth key |
| `nodejs_version` | `22.x` | Node.js version |

### 5. Deployment Workflow

#### Quick Deployment (Release Mode)

```bash
# 1. One-click install
curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash

# 2. Switch to the openclaw user
sudo su - openclaw

# 3. Run the quickstart wizard
openclaw onboard --install-daemon
```

#### Manual Deployment (Release Mode)

```bash
# 1. Install dependencies
sudo apt update && sudo apt install -y ansible git

# 2. Clone the repository
git clone https://github.com/openclaw/openclaw-ansible.git
cd openclaw-ansible

# 3. Install Ansible collections
ansible-galaxy collection install -r requirements.yml

# 4. Run the playbook
./run-playbook.sh
```

#### Development Mode Deployment

```bash
# Same as above, but add the development mode flag
./run-playbook.sh -e openclaw_install_mode=development
```

#### Post-installation Configuration

```bash
# Switch to the openclaw user
sudo su - openclaw

# Option 1: Quickstart wizard (recommended)
openclaw onboard --install-daemon

# Option 2: Manual configuration
openclaw configure
openclaw providers login
openclaw gateway
openclaw daemon install
openclaw daemon start

# Check status
openclaw status
openclaw logs
```

### 6. Operations Tools

#### Service Management

```bash
# Start the service
sudo systemctl start openclaw

# Stop the service
sudo systemctl stop openclaw

# Restart the service
sudo systemctl restart openclaw

# Check status
sudo systemctl status openclaw

# View logs
sudo journalctl -u openclaw -f
```

#### Updates

```bash
# Release mode
sudo su - openclaw
pnpm install -g openclaw@latest
sudo systemctl restart openclaw

# Development mode
sudo su - openclaw
openclaw-pull  # Pull code, install dependencies, rebuild
sudo systemctl restart openclaw
```

#### Development Tools (Development Mode)

```bash
# Rebuild
openclaw-rebuild

# Enter the repository directory
openclaw-dev

# Pull and rebuild
openclaw-pull
```

### 7. Security Audit

#### Pre-audit Checks

```bash
# Clone the repository
git clone https://github.com/openclaw/openclaw-ansible.git
cd openclaw-ansible

# Review the playbook and roles
cat playbook.yml
ls -la roles/

# Dry run (no actual execution)
ansible-playbook playbook.yml --check --diff

# Actual execution
ansible-playbook playbook.yml --ask-become-pass
```

#### Security Verification

```bash
# Check open ports
nmap -p- YOUR_SERVER_IP

# Check firewall rules
sudo ufw status verbose

# Check Fail2ban status
sudo fail2ban-client status sshd

# Check systemd service permissions
systemctl show openclaw | grep -E "(User|NoNewPrivileges|PrivateTmp|ProtectSystem)"

# Check Docker isolation
sudo iptables -L DOCKER-USER -n
```

## Key Features

### 1. One-click Deployment

- **Zero configuration**: Default settings work for most scenarios
- **Fast**: Complete deployment in 5-10 minutes
- **Idempotent**: Can be run repeatedly without breaking existing configuration

### 2. Security Hardening

- **Firewall first**: Denies all inbound connections by default
- **Intrusion protection**: Fail2ban auto-bans brute-force attempts
- **Automatic updates**: Security patches installed automatically
- **Docker isolation**: Containers cannot expose ports
- **Non-root**: Principle of least privilege

### 3. VPN Integration

- **Tailscale**: Zero-configuration mesh VPN
- **No port forwarding needed**: Services are not exposed to the public internet
- **End-to-end encryption**: All traffic is encrypted
- **Cross-platform**: Supports Windows, macOS, Linux, iOS, Android

### 4. Dual-mode Support

- **Release mode**: Stable, fast, suitable for production
- **Development mode**: Flexible, suitable for development and debugging

### 5. Systemd Integration

- **Auto-start**: OpenClaw starts automatically on system boot
- **Crash restart**: Automatically restarts after process crashes
- **Log management**: Integrated with journald
- **Resource limits**: Configurable CPU and memory limits

### 6. Configuration Flexibility

- **Multiple override methods**: Command line, variable files, direct editing
- **Environment isolation**: Different environments use different config files
- **Version control**: Configuration files can be managed with Git

### 7. Comprehensive Documentation

- **Configuration guide**: `docs/configuration.md`
- **Development mode**: `docs/development-mode.md`
- **Security architecture**: `docs/security.md`
- **Technical details**: `docs/architecture.md`
- **Troubleshooting**: `docs/troubleshooting.md`
- **Agent guide**: `AGENTS.md`

> https://github.com/openclaw/openclaw-ansible

# openclaw/openclaw-ansible

## 基本信息

- **Stars**: 481
- **URL**: https://github.com/openclaw/openclaw-ansible
- **定位**: OpenClaw 的自动化、加固部署工具
- **技术栈**: Ansible 2.14+ + Bash + YAML
- **支持平台**: Debian 11+ / Ubuntu 20.04+（macOS 支持已于 2026-02-06 移除）
- **状态**: 活跃维护中

## 问题与解决方案

### 核心问题

1. **部署复杂度**: OpenClaw 依赖多个组件（Node.js、pnpm、Docker、Tailscale、防火墙、systemd），手动安装容易出错且耗时
2. **安全风险**: 默认配置可能暴露不必要的端口，缺乏防火墙和入侵防护
3. **环境一致性**: 不同服务器的系统配置差异导致部署结果不一致
4. **权限管理**: OpenClaw 需要特定的用户权限和 systemd 服务配置
5. **远程访问**: 需要安全的远程访问方式，避免直接暴露服务端口
6. **自动更新**: 缺乏自动安全补丁机制，增加维护负担

### 解决方案

openclaw-ansible 提供了一个**一键部署脚本**，实现：

- **自动化安装**: 一条命令完成所有组件的安装和配置
- **安全加固**: 默认启用 UFW 防火墙、Fail2ban、自动安全更新
- **VPN 集成**: 内置 Tailscale 支持，无需暴露服务端口
- **Docker 隔离**: 沙箱环境使用 Docker，防止容器暴露端口
- **非 root 运行**: OpenClaw 以非特权用户运行，限制权限范围
- **systemd 服务**: 自动启动、崩溃重启、日志管理
- **幂等性**: 可重复运行，支持配置更新和版本升级

## 核心架构

### 1. 安装模式

#### Release 模式（默认，推荐生产环境）

```bash
curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
```

- **安装方式**: `pnpm install -g openclaw@latest`
- **版本来源**: npm registry 的最新稳定版
- **更新方式**: `pnpm install -g openclaw@latest`
- **优点**: 稳定、快速、适合生产环境

#### Development 模式（开发和测试）

```bash
git clone https://github.com/openclaw/openclaw-ansible.git
cd openclaw-ansible
ansible-playbook playbook.yml --ask-become-pass -e openclaw_install_mode=development
```

- **安装方式**: 从 `https://github.com/openclaw/openclaw.git` 克隆源码
- **构建**: `pnpm install && pnpm build`
- **符号链接**: 二进制文件链接到 `~/.local/bin/openclaw`
- **开发工具**: 提供 `openclaw-rebuild`、`openclaw-dev`、`openclaw-pull` 等别名
- **优点**: 适合开发、调试、贡献代码

### 2. 安全架构

#### 防火墙（UFW）

- **默认策略**: 拒绝所有入站连接
- **开放端口**: 仅 SSH (22) 和 Tailscale (41641/udp)
- **Docker 隔离**: DOCKER-USER 链阻止容器暴露端口到外部网络
- **验证**: `nmap -p- YOUR_SERVER_IP` 应仅显示端口 22

#### 入侵防护（Fail2ban）

- **SSH 保护**: 监控 SSH 登录失败
- **封禁策略**: 5 次失败尝试 → 封禁 1 小时
- **日志**: `/var/log/fail2ban.log`

#### 自动更新（unattended-upgrades）

- **安全补丁**: 自动安装安全更新
- **重启策略**: 必要时自动重启（可配置）
- **通知**: 可配置邮件通知

#### Systemd 加固

- **NoNewPrivileges**: 防止权限提升
- **PrivateTmp**: 隔离临时文件
- **ProtectSystem**: 保护系统目录
- **非 root**: OpenClaw 以 `openclaw` 用户运行
- **限制 sudo**: 仅允许服务管理命令（`systemctl restart openclaw`）

#### Tailscale VPN

- **零信任网络**: 无需暴露服务端口到公网
- **端到端加密**: 所有流量加密
- **自动配置**: 支持 authkey 自动连接
- **可选**: 可以不安装 Tailscale，仅使用 SSH

### 3. 组件安装

#### 系统依赖

- **DBus**: 用于 systemd 通信
- **Git**: 克隆仓库（Development 模式）
- **curl**: 下载脚本和依赖

#### Node.js 和 pnpm

- **版本**: Node.js 22.x（通过 NodeSource 仓库）
- **包管理器**: pnpm（全局安装）
- **环境变量**: 自动配置 `PATH`

#### Docker

- **版本**: Docker CE + Compose V2
- **用途**: OpenClaw 的沙箱环境
- **安全**: 容器无法暴露端口到外部网络（DOCKER-USER 链）
- **用户组**: `openclaw` 用户加入 `docker` 组

#### OpenClaw

- **用户**: 专用的 `openclaw` 系统用户
- **主目录**: `/home/openclaw`
- **安装路径**:
  - Release 模式: `~/.local/share/pnpm/global/5/node_modules/openclaw`
  - Development 模式: `~/code/openclaw`
- **二进制**: `~/.local/bin/openclaw`（已加入 `PATH`）

#### Systemd 服务

- **服务名**: `openclaw.service`
- **启动方式**: `systemctl start openclaw`
- **自动启动**: `systemctl enable openclaw`
- **日志**: `journalctl -u openclaw -f`
- **重启**: `systemctl restart openclaw`

### 4. 配置系统

#### 配置变量

所有配置变量定义在 `roles/openclaw/defaults/main.yml`，可通过三种方式覆盖：

1. **命令行参数**:
```bash
ansible-playbook playbook.yml --ask-become-pass \
  -e openclaw_install_mode=development \
  -e "openclaw_ssh_keys=['ssh-ed25519 AAAAC3... user@host']"
```

2. **变量文件**:
```bash
cat > vars.yml << EOF
openclaw_install_mode: development
openclaw_ssh_keys:
  - "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGxxxxxxxx user@host"
tailscale_authkey: "tskey-auth-xxxxxxxxxxxxx"
EOF

ansible-playbook playbook.yml --ask-become-pass -e @vars.yml
```

3. **直接编辑**: 修改 `roles/openclaw/defaults/main.yml`

#### 关键配置变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `openclaw_user` | `openclaw` | 系统用户名 |
| `openclaw_home` | `/home/openclaw` | 用户主目录 |
| `openclaw_install_mode` | `release` | 安装模式（`release` 或 `development`） |
| `openclaw_ssh_keys` | `[]` | SSH 公钥列表 |
| `openclaw_repo_url` | `https://github.com/openclaw/openclaw.git` | Git 仓库（Development 模式） |
| `openclaw_repo_branch` | `main` | Git 分支（Development 模式） |
| `tailscale_authkey` | `""` | Tailscale 认证密钥 |
| `nodejs_version` | `22.x` | Node.js 版本 |

### 5. 部署流程

#### 快速部署（Release 模式）

```bash
# 1. 一键安装
curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash

# 2. 切换到 openclaw 用户
sudo su - openclaw

# 3. 运行快速启动向导
openclaw onboard --install-daemon
```

#### 手动部署（Release 模式）

```bash
# 1. 安装依赖
sudo apt update && sudo apt install -y ansible git

# 2. 克隆仓库
git clone https://github.com/openclaw/openclaw-ansible.git
cd openclaw-ansible

# 3. 安装 Ansible collections
ansible-galaxy collection install -r requirements.yml

# 4. 运行 playbook
./run-playbook.sh
```

#### 开发模式部署

```bash
# 同上，但添加 development 模式标志
./run-playbook.sh -e openclaw_install_mode=development
```

#### 后续配置

```bash
# 切换到 openclaw 用户
sudo su - openclaw

# 方式 1: 快速启动向导（推荐）
openclaw onboard --install-daemon

# 方式 2: 手动配置
openclaw configure
openclaw providers login
openclaw gateway
openclaw daemon install
openclaw daemon start

# 检查状态
openclaw status
openclaw logs
```

### 6. 运维工具

#### 服务管理

```bash
# 启动服务
sudo systemctl start openclaw

# 停止服务
sudo systemctl stop openclaw

# 重启服务
sudo systemctl restart openclaw

# 查看状态
sudo systemctl status openclaw

# 查看日志
sudo journalctl -u openclaw -f
```

#### 更新

```bash
# Release 模式
sudo su - openclaw
pnpm install -g openclaw@latest
sudo systemctl restart openclaw

# Development 模式
sudo su - openclaw
openclaw-pull  # 拉取代码、安装依赖、重新构建
sudo systemctl restart openclaw
```

#### 开发工具（Development 模式）

```bash
# 重新构建
openclaw-rebuild

# 进入仓库目录
openclaw-dev

# 拉取并重新构建
openclaw-pull
```

### 7. 安全审计

#### 审计前检查

```bash
# 克隆仓库
git clone https://github.com/openclaw/openclaw-ansible.git
cd openclaw-ansible

# 审查 playbook 和 roles
cat playbook.yml
ls -la roles/

# 干运行（不实际执行）
ansible-playbook playbook.yml --check --diff

# 实际执行
ansible-playbook playbook.yml --ask-become-pass
```

#### 安全验证

```bash
# 检查开放端口
nmap -p- YOUR_SERVER_IP

# 检查防火墙规则
sudo ufw status verbose

# 检查 Fail2ban 状态
sudo fail2ban-client status sshd

# 检查 systemd 服务权限
systemctl show openclaw | grep -E "(User|NoNewPrivileges|PrivateTmp|ProtectSystem)"

# 检查 Docker 隔离
sudo iptables -L DOCKER-USER -n
```

## 关键特性

### 1. 一键部署

- **零配置**: 默认配置适合大多数场景
- **快速**: 5-10 分钟完成完整部署
- **幂等**: 可重复运行，不会破坏现有配置

### 2. 安全加固

- **防火墙优先**: 默认拒绝所有入站连接
- **入侵防护**: Fail2ban 自动封禁暴力破解
- **自动更新**: 安全补丁自动安装
- **Docker 隔离**: 容器无法暴露端口
- **非 root**: 最小权限原则

### 3. VPN 集成

- **Tailscale**: 零配置的 mesh VPN
- **无需端口转发**: 服务不暴露到公网
- **端到端加密**: 所有流量加密
- **跨平台**: 支持 Windows、macOS、Linux、iOS、Android

### 4. 双模式支持

- **Release 模式**: 稳定、快速、适合生产
- **Development 模式**: 灵活、适合开发和调试

### 5. Systemd 集成

- **自动启动**: 系统启动时自动启动 OpenClaw
- **崩溃重启**: 进程崩溃后自动重启
- **日志管理**: 集成 journald
- **资源限制**: 可配置 CPU、内存限制

### 6. 配置灵活性

- **多种覆盖方式**: 命令行、变量文件、直接编辑
- **环境隔离**: 不同环境使用不同配置文件
- **版本控制**: 配置文件可纳入 Git 管理

### 7. 文档完善

- **配置指南**: `docs/configuration.md`
- **开发模式**: `docs/development-mode.md`
- **安全架构**: `docs/security.md`
- **技术细节**: `docs/architecture.md`
- **故障排查**: `docs/troubleshooting.md`
- **Agent 指南**: `AGENTS.md`

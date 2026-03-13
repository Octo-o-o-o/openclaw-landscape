> https://github.com/mithun50/openclaw-termux

# mithun50/openclaw-termux

## Basic Info

- **Stars**: 563
- **URL**: https://github.com/mithun50/openclaw-termux
- **License**: MIT
- **Author**: Mithun Gowda B (NextGenX)
- **Platform**: Android 10+

## Problem & Solution

### Core Problem

OpenClaw was originally designed to run only on desktop systems (macOS/Linux/Windows), with mobile users facing the following challenges:

1. **Cannot run on Android**: OpenClaw requires Node.js 22+ and a full Linux environment
2. **Termux compatibility issues**: Android's Bionic libc is incompatible with Node.js's `os.networkInterfaces()`
3. **Complex configuration**: Requires manually installing proot-distro, Ubuntu, Node.js, OpenClaw
4. **No GUI**: Termux is pure command-line, difficult for regular users
5. **Background running difficulties**: Android battery optimization kills background processes

### Solution

openclaw-termux provides **two methods** for running OpenClaw on Android:

#### Method 1: Flutter App (Recommended)

- **One-click install**: Download APK, tap "Begin Setup" to auto-complete environment configuration
- **Built-in terminal**: Full-featured terminal emulator with copy/paste/URL clicking
- **Gateway controls**: Start/stop Gateway with real-time status indicator
- **Web Dashboard**: Built-in WebView loading the dashboard
- **Node device capabilities**: Exposes 7 device capabilities (15 commands) to AI
- **Foreground service**: Keeps Gateway running in background, displays uptime
- **SSH remote access**: Start SSH server for remote management

#### Method 2: Termux CLI

- **One-click install script**: `curl -fsSL ... | bash`
- **Bionic Bypass**: Fixes `os.networkInterfaces()` crash
- **Smart loading**: Shows spinner until Gateway is ready
- **Command passthrough**: `openclawx` command directly invokes OpenClaw

## Core Architecture

### Flutter App Architecture

```
┌───────────────────────────────────────────────────┐
│                Flutter App (Dart)                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐       │
│  │ Terminal  │ │ Gateway  │ │ Web Dashboard│       │
│  │ Emulator  │ │ Controls │ │   (WebView)  │       │
│  └─────┬────┘ └─────┬────┘ └──────┬───────┘       │
│        │            │             │               │
│  ┌─────┴────────────┴─────────────┴─────────────┐ │
│  │           Native Bridge (Kotlin)             │ │
│  └─────────────────┬────────────────────────────┘ │
│                    │                              │
│  ┌─────────────────┴────────────────────────────┐ │
│  │         Node Provider (WebSocket)            │ │
│  │  Camera · Flash · Location · Screen          │ │
│  │  Sensor · Haptic · Canvas                    │ │
│  └─────────────────┬────────────────────────────┘ │
└────────────────────┼──────────────────────────────┘
                     │
┌────────────────────┼──────────────────────────────┐
│  proot-distro      │              Ubuntu          │
│  ┌─────────────────┴──────────────────────────┐   │
│  │   Node.js 22 + Bionic Bypass               │   │
│  │   ┌─────────────────────────────────────┐  │   │
│  │   │  OpenClaw AI Gateway                │  │   │
│  │   │  http://localhost:18789             │  │   │
│  │   │  <- Node WS: 15 device commands     │  │   │
│  │   └─────────────────────────────────────┘  │   │
│  │   Optional: Go, Homebrew                   │   │
│  └────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────┘
```

### Bionic Bypass Implementation

**Problem**: Android's Bionic libc does not support `getifaddrs()`, causing Node.js's `os.networkInterfaces()` to crash.

**Solution**:

```javascript
// ~/.openclaw/bionic-bypass.js
const os = require('os');
const originalNetworkInterfaces = os.networkInterfaces;

os.networkInterfaces = function() {
  try {
    const interfaces = originalNetworkInterfaces.call(os);
    if (interfaces && Object.keys(interfaces).length > 0) {
      return interfaces;
    }
  } catch (e) {}

  // Fallback to loopback
  return {
    lo: [{
      address: '127.0.0.1',
      netmask: '255.0.0.0',
      family: 'IPv4',
      mac: '00:00:00:00:00:00',
      internal: true,
      cidr: '127.0.0.1/8'
    }]
  };
};
```

**Loading method**:

```bash
export NODE_OPTIONS="--require ~/.openclaw/bionic-bypass.js"
```

## Key Features

### 1. Node Device Capabilities (7 Capabilities, 15 Commands)

The Flutter App connects to the Gateway via WebSocket, exposing Android hardware to AI as a **Node**.

| Capability | Commands | Permission |
|------|------|------|
| **Camera** | `camera.snap`, `camera.clip`, `camera.list` | Camera |
| **Canvas** | `canvas.navigate`, `canvas.eval`, `canvas.snapshot` | None (not implemented) |
| **Flash** | `flash.on`, `flash.off`, `flash.toggle`, `flash.status` | Camera (flashlight) |
| **Location** | `location.get` | Location |
| **Screen** | `screen.record` | MediaProjection consent |
| **Sensor** | `sensor.read`, `sensor.list` | Body Sensors |
| **Haptic** | `haptic.vibrate` | None |

### 2. One-Click Setup Wizard

**Flow**:

```
1. Download Ubuntu rootfs (~300MB)
   ├─ Display progress bar
   └─ Notification bar shows download progress

2. Install proot-distro
   └─ Configure Ubuntu environment

3. Install Node.js 22
   ├─ Add NodeSource repository
   └─ apt install nodejs

4. Install OpenClaw
   └─ npm install -g openclaw

5. Configure Bionic Bypass
   ├─ Create ~/.openclaw/bionic-bypass.js
   └─ Add to ~/.bashrc

6. Optional package installation (user choice)
   ├─ Go (Golang) - ~150MB
   ├─ Homebrew - ~500MB
   └─ OpenSSH - ~10MB
```

**Features**:
- **Resume downloads**: Failed downloads can continue
- **Progress notifications**: Notification bar shows installation progress
- **Error handling**: Installation failures show detailed error messages
- **Retryable**: Failed installations can be re-run

### 3. Built-in Terminal Emulator

**Features**:
- **Full-featured terminal**: Supports ANSI escape sequences, colors, cursor control
- **Extra key toolbar**: Tab, Ctrl, Esc, Alt, arrow keys
- **Copy/paste**: Long-press to select text, copy to clipboard
- **URL clicking**: Click URLs to auto-open browser
- **Font size adjustment**: Pinch-to-zoom for font size

### 4. SSH Remote Access

**Features**:
- **Start SSH server**: Launch sshd in the Ubuntu environment
- **Set root password**: Set password for SSH login
- **Display connection info**: IP address, port, username, password
- **Copyable command**: One-click copy of SSH connection command

### 5. Foreground Service Keep-Alive

**Problem**: Android battery optimization kills background processes.

**Effect**:
- Notification bar shows "OpenClaw Gateway is running"
- Displays uptime (e.g., "Running for 2h 15m")
- User can stop the service from the notification bar

### 6. Optional Package Management

**Supported Packages**:

| Package | Install Method | Size | Purpose |
|---|---|---|---|
| **Go (Golang)** | `apt install golang` | ~150MB | Go language runtime |
| **Homebrew** | Official install script (with root bypass) | ~500MB | Package manager |
| **OpenSSH** | `apt install openssh-server` | ~10MB | SSH server |

## Summary

mithun50/openclaw-termux is an engineering achievement that successfully ports OpenClaw to the Android platform. Its value lies in:

1. **Platform expansion**: Porting a desktop application to mobile
2. **User experience**: One-click install, built-in terminal, foreground service
3. **Device capabilities**: Exposing Android hardware to AI
4. **Compatibility solution**: Bionic Bypass resolves platform differences

<!-- lastCommit: 6a7050b -->

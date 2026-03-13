> https://github.com/mithun50/openclaw-termux

# mithun50/openclaw-termux

## 基本信息

- **Stars**: 563
- **URL**: https://github.com/mithun50/openclaw-termux
- **License**: MIT
- **作者**: Mithun Gowda B (NextGenX)
- **平台**: Android 10+

## 问题与解决方案

### 核心问题

OpenClaw 原本只能在桌面系统（macOS/Linux/Windows）上运行，移动端用户面临以下困难：

1. **无法在 Android 上运行**：OpenClaw 需要 Node.js 22+ 和完整的 Linux 环境
2. **Termux 兼容性问题**：Android 的 Bionic libc 与 Node.js 的 `os.networkInterfaces()` 不兼容
3. **配置复杂**：需要手动安装 proot-distro、Ubuntu、Node.js、OpenClaw
4. **缺少 GUI**：Termux 纯命令行，普通用户难以使用
5. **后台运行困难**：Android 电池优化会杀死后台进程

### 解决方案

openclaw-termux 提供了**两种方式**在 Android 上运行 OpenClaw：

#### 方式一：Flutter App（推荐）

- **一键安装**：下载 APK，点击"Begin Setup"自动完成环境配置
- **内置终端**：全功能终端模拟器，支持复制/粘贴/URL 点击
- **Gateway 控制**：启动/停止 Gateway，实时状态指示
- **Web Dashboard**：内置 WebView 加载仪表板
- **Node 设备能力**：暴露 7 种设备能力（15 个命令）给 AI
- **前台服务**：保持 Gateway 在后台运行，显示运行时间
- **SSH 远程访问**：启动 SSH 服务器，远程管理

#### 方式二：Termux CLI

- **一键安装脚本**：`curl -fsSL ... | bash`
- **Bionic Bypass**：修复 `os.networkInterfaces()` 崩溃
- **智能加载**：显示 spinner 直到 Gateway 就绪
- **命令透传**：`openclawx` 命令直接调用 OpenClaw

## 核心架构

### Flutter App 架构

```
┌───────────────────────────────────────────────────┐
│                Flutter App (Dart)                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐       │
│  │ Terminal │ │ Gateway  │ │ Web Dashboard│       │
│  │ Emulator │ │ Controls │ │   (WebView)  │       │
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
│  │   │  ← Node WS: 15 device commands      │  │   │
│  │   └─────────────────────────────────────┘  │   │
│  │   Optional: Go, Homebrew                   │   │
│  └────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────┘
```

### Flutter App 目录结构

```
flutter_app/lib/
├── main.dart                  # 应用入口
├── constants.dart             # 常量、URL、作者信息
├── models/
│   ├── gateway_state.dart     # Gateway 状态、日志、token URL
│   ├── node_state.dart        # Node 连接状态
│   ├── node_frame.dart        # WebSocket 帧模型（req/res/event）
│   ├── setup_state.dart       # 安装向导进度
│   ├── optional_package.dart  # 可选包元数据（Go, Homebrew）
│   └── ai_provider.dart       # AI 提供商数据模型（7 个）
├── providers/
│   ├── gateway_provider.dart  # Gateway 状态管理
│   ├── node_provider.dart     # Node 能力 + 权限管理
│   └── setup_provider.dart    # 安装状态管理
├── screens/
│   ├── splash_screen.dart     # 启动屏幕
│   ├── setup_wizard_screen.dart    # 首次安装 + 可选包
│   ├── onboarding_screen.dart      # API key 配置终端
│   ├── dashboard_screen.dart       # 主仪表板
│   ├── terminal_screen.dart        # 全功能终端模拟器
│   ├── configure_screen.dart       # openclaw configure 终端
│   ├── web_dashboard_screen.dart   # OpenClaw 仪表板 WebView
│   ├── providers_screen.dart       # AI 提供商列表
│   ├── provider_detail_screen.dart # API key + 模型配置
│   ├── ssh_screen.dart             # SSH 服务器管理
│   ├── packages_screen.dart        # 可选包管理器
│   ├── package_install_screen.dart # 基于终端的包安装器
│   ├── logs_screen.dart            # Gateway 日志查看器
│   └── settings_screen.dart        # 应用设置和关于
├── services/
│   ├── native_bridge.dart     # Kotlin 平台通道桥接
│   ├── gateway_service.dart   # Gateway 生命周期、健康检查、配置修补
│   ├── node_service.dart      # Node WebSocket 连接 + 调用处理
│   ├── node_ws_service.dart   # 原始 WebSocket 传输
│   ├── node_identity_service.dart # 设备身份 + 加密签名
│   ├── terminal_service.dart  # proot shell 配置
│   ├── bootstrap_service.dart # 环境安装编排
│   ├── package_service.dart   # 可选包状态检查
│   ├── preferences_service.dart # 持久化设置（token URL 等）
│   ├── provider_config_service.dart # AI 提供商配置读写
│   ├── ssh_service.dart       # SSH 服务器管理（通过 native bridge）
│   └── capabilities/
│       ├── capability_handler.dart   # 基类，带权限处理
│       ├── camera_capability.dart    # 照片/视频捕获
│       ├── canvas_capability.dart    # WebView 存根（未实现）
│       ├── flash_capability.dart     # 手电筒开/关/切换
│       ├── location_capability.dart  # GPS，带超时 + 回退
│       ├── screen_capability.dart    # 屏幕录制（MediaProjection）
│       ├── sensor_capability.dart    # 加速度计、陀螺仪等
│       └── vibration_capability.dart # 触觉反馈
└── widgets/
    ├── gateway_controls.dart  # 启动/停止、URL 显示、复制按钮
    ├── node_controls.dart     # Node 启用/禁用、状态徽章
    ├── terminal_toolbar.dart  # 额外按键（Tab, Ctrl, Esc, 箭头）
    ├── status_card.dart       # 可重用状态卡片
    └── progress_step.dart     # 安装向导步骤指示器
```

### Bionic Bypass 实现

**问题**：Android 的 Bionic libc 不支持 `getifaddrs()`，导致 Node.js 的 `os.networkInterfaces()` 崩溃。

**解决方案**：

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

  // 回退到 loopback
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

**加载方式**：

```bash
export NODE_OPTIONS="--require ~/.openclaw/bionic-bypass.js"
```

## 关键特性

### 1. Node 设备能力（7 种能力，15 个命令）

Flutter App 通过 WebSocket 连接到 Gateway，作为 **Node** 暴露 Android 硬件给 AI。

| 能力 | 命令 | 权限 |
|------|------|------|
| **Camera** | `camera.snap`, `camera.clip`, `camera.list` | Camera |
| **Canvas** | `canvas.navigate`, `canvas.eval`, `canvas.snapshot` | 无（未实现） |
| **Flash** | `flash.on`, `flash.off`, `flash.toggle`, `flash.status` | Camera（手电筒） |
| **Location** | `location.get` | Location |
| **Screen** | `screen.record` | MediaProjection 同意 |
| **Sensor** | `sensor.read`, `sensor.list` | Body Sensors |
| **Haptic** | `haptic.vibrate` | 无 |

**实现原理**：

1. **启动时自动修补配置**：清空 `openclaw.json` 中的 `denyCommands`，设置 `allowCommands` 为所有 15 个命令
2. **权限主动请求**：启用 Node 时主动请求所有需要的权限
3. **WebSocket 通信**：Gateway 通过 WebSocket 发送命令，App 执行后返回结果

**示例：拍照命令**

```dart
// services/capabilities/camera_capability.dart
Future<Map<String, dynamic>> handleSnap(Map<String, dynamic> params) async {
  // 1. 请求 Camera 权限
  if (!await Permission.camera.isGranted) {
    await Permission.camera.request();
  }

  // 2. 拍照
  final XFile photo = await _camera.takePicture();

  // 3. 保存到临时目录
  final String path = '${Directory.systemTemp.path}/${DateTime.now().millisecondsSinceEpoch}.jpg';
  await photo.saveTo(path);

  // 4. 返回结果
  return {
    'success': true,
    'path': path,
    'timestamp': DateTime.now().toIso8601String()
  };
}
```

### 2. 一键安装向导

**流程**：

```
1. 下载 Ubuntu rootfs (~300MB)
   ├─ 显示进度条
   └─ 通知栏显示下载进度

2. 安装 proot-distro
   └─ 配置 Ubuntu 环境

3. 安装 Node.js 22
   ├─ 添加 NodeSource 仓库
   └─ apt install nodejs

4. 安装 OpenClaw
   └─ npm install -g openclaw

5. 配置 Bionic Bypass
   ├─ 创建 ~/.openclaw/bionic-bypass.js
   └─ 添加到 ~/.bashrc

6. 可选包安装（用户选择）
   ├─ Go (Golang) - ~150MB
   ├─ Homebrew - ~500MB
   └─ OpenSSH - ~10MB
```

**特点**：
- **断点续传**：下载失败可以继续
- **进度通知**：通知栏显示安装进度
- **错误处理**：安装失败显示详细错误信息
- **可重试**：安装失败可以重新运行

### 3. 内置终端模拟器

**功能**：
- **全功能终端**：支持 ANSI 转义序列、颜色、光标控制
- **额外按键工具栏**：Tab、Ctrl、Esc、Alt、方向键
- **复制/粘贴**：长按选择文本，复制到剪贴板
- **URL 点击**：点击 URL 自动打开浏览器
- **字体大小调整**：捏合缩放调整字体大小

**实现**：

```dart
// screens/terminal_screen.dart
import 'package:xterm/xterm.dart';

final terminal = Terminal();
final terminalController = TerminalController();

// 连接到 proot shell
final pty = Pty.start(
  '/data/data/com.termux/files/usr/bin/proot-distro',
  arguments: ['login', 'ubuntu'],
  environment: {'TERM': 'xterm-256color'}
);

// 双向数据流
pty.output.listen(terminal.write);
terminal.onOutput = (data) => pty.write(data);
```

### 4. SSH 远程访问

**功能**：
- **启动 SSH 服务器**：在 Ubuntu 环境中启动 sshd
- **设置 root 密码**：为 SSH 登录设置密码
- **显示连接信息**：IP 地址、端口、用户名、密码
- **可复制命令**：一键复制 SSH 连接命令

**实现**：

```kotlin
// android/app/src/main/kotlin/SshService.kt
class SshService(private val context: Context) {
    fun startSshServer(password: String): Result<SshInfo> {
        // 1. 在 proot 环境中设置 root 密码
        execInProot("echo 'root:$password' | chpasswd")

        // 2. 启动 sshd
        execInProot("/usr/sbin/sshd -D -p 2222")

        // 3. 获取 IP 地址
        val ip = getLocalIpAddress()

        return Result.success(SshInfo(
            host = ip,
            port = 2222,
            username = "root",
            password = password
        ))
    }
}
```

### 5. 前台服务保活

**问题**：Android 电池优化会杀死后台进程。

**解决方案**：

```dart
// services/gateway_service.dart
import 'package:flutter_foreground_task/flutter_foreground_task.dart';

void startForegroundService() {
  FlutterForegroundTask.init(
    androidNotificationOptions: AndroidNotificationOptions(
      channelId: 'openclaw_gateway',
      channelName: 'OpenClaw Gateway',
      channelDescription: 'Keeps OpenClaw Gateway running',
      channelImportance: NotificationChannelImportance.LOW,
      priority: NotificationPriority.LOW,
      iconData: const NotificationIconData(
        resType: ResourceType.mipmap,
        resPrefix: ResourcePrefix.ic,
        name: 'launcher',
      ),
    ),
  );

  FlutterForegroundTask.startService(
    notificationTitle: 'OpenClaw Gateway',
    notificationText: 'Running for 2h 15m',
    callback: startCallback,
  );
}
```

**效果**：
- 通知栏显示"OpenClaw Gateway 正在运行"
- 显示运行时间（如"Running for 2h 15m"）
- 用户可以从通知栏停止服务

### 6. 可选包管理

**支持的可选包**：

| 包 | 安装方式 | 大小 | 用途 |
|---|---|---|---|
| **Go (Golang)** | `apt install golang` | ~150MB | Go 语言运行时 |
| **Homebrew** | 官方安装脚本（带 root 绕过） | ~500MB | 包管理器 |
| **OpenSSH** | `apt install openssh-server` | ~10MB | SSH 服务器 |

**安装位置**：
- **安装向导**：首次安装完成后显示包卡片
- **仪表板**："Packages" 卡片在快速操作中
- **设置**：系统信息下显示安装状态
## 总结

mithun50/openclaw-termux 是一个**工程奇迹**，成功将 OpenClaw 移植到 Android 平台。其价值在于：

1. **平台扩展**：将桌面应用移植到移动端
2. **用户体验**：一键安装、内置终端、前台服务
3. **设备能力**：暴露 Android 硬件给 AI
4. **兼容性解决**：Bionic Bypass 解决平台差异

ClawButler 可以借鉴其**移动端架构**、**设备能力暴露**、**一键安装体验**，开发 ClawButler Mobile App，让用户可以在移动设备上管理和监控 Agent 集群。

<!-- lastCommit: 137e138 -->

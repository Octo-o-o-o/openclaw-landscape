> https://github.com/pjasicek/OpenClaw

# pjasicek/OpenClaw

## 基本信息

- **Stars**: 448
- **URL**: https://github.com/pjasicek/OpenClaw
- **License**: 未明确标注（开源）
- **类型**: 游戏引擎重新实现
- **平台**: Windows / Linux / macOS / Android / WebAssembly

## 问题与解决方案

### 核心问题

**注意**：这个项目与 OpenClaw AI Agent 框架**完全无关**。这是一个 1997 年经典平台游戏《Captain Claw》的 C++ 重新实现项目。

### 项目背景

- **原游戏**：Captain Claw（1997 年发布的 2D 平台游戏）
- **目标**：用现代 C++ 和跨平台库重新实现游戏引擎
- **代码库**：完全从头编写，不使用原始代码
- **资源**：使用原始游戏的资源文件（CLAW.REZ）

## 核心架构

### 技术栈

```
OpenClaw (游戏引擎)
├── 编程语言：C++
├── 图形/输入/音频：SDL2 库
│   ├── SDL2
│   ├── SDL_Image
│   ├── SDL_TTF
│   ├── SDL_Mixer
│   └── SDL2_Gfx
├── 物理引擎：Box2D
├── XML 解析：Tinyxml
└── 构建系统：CMake
```

### 支持平台

- **Windows**：Visual Studio 2017 / CMake
- **Linux**：Debian / Ubuntu / Fedora / CentOS / Arch
- **macOS**：通过 CMake 构建
- **Android**：原生 Android 构建
- **WebAssembly (Emscripten)**：在浏览器中运行

## 关键特性

### 1. 跨平台支持

**构建方式**：

```bash
# Linux
sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libsdl2-gfx-dev
git clone https://github.com/pjasicek/OpenClaw.git
cd OpenClaw
cmake .
make

# Windows (Visual Studio)
cmake -G "Visual Studio 15 2017" ..
msbuild OpenClaw.sln

# WebAssembly
emcmake cmake -DEmscripten=1 ..
make
```

### 2. WebAssembly 支持

**特点**：
- 编译为 wasm 代码，在现代浏览器中运行
- 无需额外运行时依赖
- 一次编译，跨设备运行

**限制**：
- 某些旧浏览器不支持 WebAssembly
- 某些浏览器不支持 `.wav` 文件格式
- 所有浏览器都不支持 `.xmi` (MIDI) 文件格式
- 死亡和传送淡入效果损坏

### 3. 音频支持

**背景音乐**：
- 需要安装 **timidity (或 timidity++)** 和 **freepats**
- 某些 Linux 发行版默认包含，某些不包含（Fedora、Arch Linux）
## 总结

pjasicek/OpenClaw 是一个**游戏引擎项目**，与 AI Agent 框架无关。虽然名字相似，但两者完全不同：

- **pjasicek/OpenClaw**：1997 年游戏《Captain Claw》的 C++ 重新实现
- **OpenClaw AI Agent**：自托管的开源 AI Agent 框架

对 ClawButler 没有直接借鉴价值。

<!-- lastCommit: 137e138 -->

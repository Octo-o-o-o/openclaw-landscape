> https://github.com/pjasicek/OpenClaw

# pjasicek/OpenClaw

## Basic Info

- **Stars**: 448
- **URL**: https://github.com/pjasicek/OpenClaw
- **License**: Not explicitly labeled (open source)
- **Type**: Game engine reimplementation
- **Platforms**: Windows / Linux / macOS / Android / WebAssembly

## Problem & Solution

### Core Problem

**Note**: This project is **completely unrelated** to the OpenClaw AI Agent framework. This is a C++ reimplementation of the 1997 classic platform game "Captain Claw."

### Project Background

- **Original Game**: Captain Claw (2D platform game released in 1997)
- **Goal**: Reimplment the game engine using modern C++ and cross-platform libraries
- **Codebase**: Written entirely from scratch, does not use original code
- **Assets**: Uses the original game's resource files (CLAW.REZ)

## Core Architecture

### Tech Stack

```
OpenClaw (Game Engine)
├── Language: C++
├── Graphics/Input/Audio: SDL2
│   ├── SDL2
│   ├── SDL_Image
│   ├── SDL_TTF
│   ├── SDL_Mixer
│   └── SDL2_Gfx
├── Physics Engine: Box2D
├── XML Parsing: Tinyxml
└── Build System: CMake
```

### Supported Platforms

- **Windows**: Visual Studio 2017 / CMake
- **Linux**: Debian / Ubuntu / Fedora / CentOS / Arch
- **macOS**: CMake build
- **Android**: Native Android build
- **WebAssembly (Emscripten)**: Run in browser

## Key Features

### 1. Cross-Platform Support

**Build methods**:

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

### 2. WebAssembly Support

**Features**:
- Compiles to wasm code, runs in modern browsers
- No additional runtime dependencies
- Compile once, run across devices

**Limitations**:
- Some older browsers don't support WebAssembly
- Some browsers don't support `.wav` file format
- No browsers support `.xmi` (MIDI) file format
- Death and teleport fade effects are broken

### 3. Audio Support

**Background Music**:
- Requires **timidity (or timidity++)** and **freepats** installed
- Some Linux distributions include these by default, some don't (Fedora, Arch Linux)

## Summary

pjasicek/OpenClaw is a **game engine project** unrelated to AI Agent frameworks. Although the names are similar, they are completely different:

- **pjasicek/OpenClaw**: C++ reimplementation of the 1997 game "Captain Claw"
- **OpenClaw AI Agent**: Self-hosted open-source AI Agent framework

<!-- lastCommit: 5ee5740 -->

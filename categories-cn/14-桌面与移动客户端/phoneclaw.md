> https://github.com/rohanarun/phoneclaw

# PhoneClaw (392 stars)

## 问题与解决方案

Android 手机自动化需要 root 权限或复杂的 ADB 配置，普通用户难以使用。PhoneClaw 基于 Android Accessibility Service 实现无 root 自动化，通过 ClawScript（嵌入式 JS 引擎）在运行时生成自动化逻辑，结合视觉辅助 UI 定位（Moondream 视觉模型），实现跨应用的自适应工作流。

## 关键特性

- **无 root 自动化** — 基于 Android Accessibility Service，无需 root 或 ADB，支持所有应用（包括侧载 APK）
- **ClawScript 脚本引擎** — 嵌入式 JS 引擎，提供 `magicClicker`（自然语言 UI 定位）、`magicScraper`（屏幕内容提取）、`schedule`（cron 调度）等 API
- **视觉辅助定位** — 通过截图 + 视觉模型（Moondream）定位 UI 元素，无需硬编码坐标，适应不同设备尺寸和布局
- **运行时生成脚本** — 通过语音命令生成自动化脚本（如"每小时打开 Twitter 并点击蓝色发布按钮"），立即执行并可编辑
- **跨应用工作流** — 支持浏览器、邮件、媒体、消息应用的链式操作，单个流程内完成多步骤任务
- **验证码自动化** — 通过 `magicScraper` 提取 OTP 验证码，结合 `magicClicker` 自动填写和提交

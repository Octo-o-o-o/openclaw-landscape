> https://github.com/rohanarun/phoneclaw

# PhoneClaw (392 stars)

## Problem & Solution

Android phone automation requires root access or complex ADB configuration, making it difficult for regular users. PhoneClaw uses Android Accessibility Service for root-free automation, generating automation logic at runtime through ClawScript (embedded JS engine), combined with visual-assisted UI targeting (Moondream vision model), to achieve cross-app adaptive workflows.

## Key Features

- **Root-Free Automation** — Based on Android Accessibility Service, no root or ADB needed, supports all apps (including sideloaded APKs)
- **ClawScript Engine** — Embedded JS engine providing `magicClicker` (natural language UI targeting), `magicScraper` (screen content extraction), `schedule` (cron scheduling), and other APIs
- **Visual-Assisted Targeting** — Uses screenshots + vision model (Moondream) to locate UI elements without hardcoded coordinates, adapting to different device sizes and layouts
- **Runtime Script Generation** — Generate automation scripts via voice commands (e.g., "Open Twitter every hour and click the blue post button"), immediately executable and editable
- **Cross-App Workflows** — Supports chained operations across browser, email, media, and messaging apps, completing multi-step tasks within a single flow
- **CAPTCHA Automation** — Extracts OTP codes via `magicScraper`, combined with `magicClicker` for auto-fill and submission

<!-- lastCommit: 6a7050b -->

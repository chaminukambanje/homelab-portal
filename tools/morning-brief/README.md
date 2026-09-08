# Morning News Brief & WhatsApp Gateway Automation

Automated daily morning news digest for macOS and WhatsApp, pulling live updates from the homelab [News & Trends Dashboard](https://news.npcsolutions.co.uk) running on `portal.npcsolutions.co.uk`.

## 🌐 Covered Regions
* 🇬🇧 **United Kingdom**
* 🇿🇼 **Zimbabwe**
* 🇿🇦 **South Africa**
* 🇨🇳 **China**
* 🇮🇷 **Iran**
* 🇨🇦 **Canada**
* 🇩🇪 **Germany**
* 🇫🇷 **France**
* 🌐 **Rest of World / International**

## 🚀 Features
* **Multi-Channel Delivery**:
  * **WhatsApp**: Formatted digest with emojis, bold headlines, sources, and links sent via self-hosted WAHA gateway.
  * **macOS Notification**: Native notification center alert with sound (`Glass`).
  * **HTML Digest**: Curated daily dark-mode HTML deck saved to `~/Documents/MorningBriefs/`.
* **Flexible Recipients**:
  * Send to primary recipient or override on the fly via `--to <number>`.
  * Multi-number support: `--to 447xxx,447yyy`.
  * WhatsApp group support (`<group_id>@g.us`).
* **Scheduled Execution**: Native macOS `launchd` service triggering daily at **07:30 AM** with automatic run-on-wake if asleep.

## 📦 Components
* `morning_brief.py`: Main engine script.
* `com.npcsolutions.morningbrief.plist`: LaunchAgent scheduler.
* `../whatsapp-gateway/docker-compose.yml`: Self-hosted WAHA WhatsApp HTTP API container.

## 🛠️ Quick Commands
```bash
# Manual run
morning-brief

# Open HTML card in browser
morning-brief --open

# Send to custom number
morning-brief --to 447565297807
```

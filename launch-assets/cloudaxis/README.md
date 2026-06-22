# CloudAxis launch asset kit

**Public share:** https://github.com/CloudAxisAi/cloudybot-ai/tree/main/launch-assets/cloudaxis  
**For:** G2, Capterra, GetApp, AlternativeTo, SaaSHub, Product Hunt (~5 weeks)  
**Brand:** CloudAxis only (not CloudyBot)  
**Updated:** 2026-06-14

---

## Quick start tomorrow

1. Open **`copy/LISTING-COPY.md`** — paste tagline, 160-char, and 500-word description into each directory form.
2. Upload from **`screenshots-v2/`** (full 1920×1080 frames — use these, not legacy `screenshots/`).
3. Optional video demos in **`video/*.webm`** (convert to MP4 for some platforms with ffmpeg).
4. Website URL: **https://cloudaxis.ai** · Product URL: **https://app.cloudaxis.ai**

---

## Folder map

| Folder | Contents |
|--------|----------|
| `screenshots-v2/` | **Primary** — Playwright captures at 1920×1080 from app + marketing site |
| `screenshots/` | Legacy partial captures (ignore) |
| `logos/` | SVG + PNG (256, 512, white background, transparent) |
| `og/` | PH hero + directory banner (1200×630 PNG) + HTML sources |
| `copy/` | Listing copy, maker comment, reply templates |
| `video/` | Auto-recorded WebM demos + manual script fallback |

---

## Screenshot index (`screenshots-v2/`)

| File | Use for |
|------|---------|
| `18-marketing-hero.png` | **Hero** — PH gallery #1, G2 banner, social |
| `19-marketing-comparison.png` | **Comparison** — PH gallery, AlternativeTo |
| `03-agents-board-full.png` | **Scheduled agents** — task board |
| `21-agents-board-scrolled.png` | Agent columns / duties (scrolled) |
| `05-workflows-pipeline.png` | **Multi-agent pipeline** |
| `09-browser-session.png` | **Cloud browser** (live session) |
| `08-browser-idle.png` | Browser app idle / connect CTA |
| `06-files-workspace.png` | **Files / workspace** |
| `07-files-list.png` | File list view |
| `10-chat-cloudia.png` | **Chat** overview |
| `11-chat-cloudia-builder.png` | **Cloudia** Team Builder thread |
| `14-settings-vpn-residential.png` | **VPN / residential IP** selector |
| `12-settings-overview.png` | Settings appearance / OS feel |
| `13-settings-connected-accounts.png` | Connected accounts |
| `15-settings-billing.png` | Plan & billing |
| `16-settings-usage.png` | Usage meters |
| `01-desktop-home.png` | **Desktop home** + command bar |
| `02-launchpad.png` | Launchpad app grid |
| `02b-launchpad-connect.png` | Connect integrations on home |
| `17-desktop-command-bar.png` | Ask CloudAxis spotlight |
| `20-marketing-team-board.png` | Marketing team-board section |

**Product Hunt gallery (recommended order):**
1. `og/ph-hero-1200x630.png`
2. `18-marketing-hero.png`
3. `01-desktop-home.png`
4. `03-agents-board-full.png`
5. `19-marketing-comparison.png`
6. `05-workflows-pipeline.png`
7. `09-browser-session.png`
8. `14-settings-vpn-residential.png`

---

## Launch teaser (`video/LaunchTeaser*`)

| File | Use |
|------|-----|
| `LaunchTeaser-1080p.mp4` | **PH gallery / hunter** — 60s product overview |
| `LaunchTeaser-720p.mp4` | Smaller download |
| `LaunchTeaser-poster.png` | Thumbnail / social |
| YouTube | https://youtu.be/X80a_OZMiaQ |

**Hunter one-pager:** [`HUNTER-PACK.md`](./HUNTER-PACK.md) — send Rohan this file or the YouTube + raw MP4 links above.

---

## Video demos (`video/`)

| File | ~Duration | Content |
|------|-----------|---------|
| `LaunchTeaser-1080p.mp4` | 60 sec | **Launch teaser** — full product story (primary PH video) |
| `05-full-desktop-walkthrough-3min.webm` | 3–5 min | Desktop → Launchpad → all apps |
| `02-browser-automation-90s.webm` | 90 sec | Connect browser, live session |
| `03-file-persistence-60s.webm` | 60 sec | Files app, close/reopen |
| `01-cloudia-intro-45s.webm` | 45 sec | Cloudia chat thread |
| `04-vpn-geo-60s.webm` | 60 sec | VPN settings → browser |

WebM plays in browsers; for MP4: `ffmpeg -i input.webm -c:v libx264 -crf 23 output.mp4`

**Regenerate** (requires credentials in env, never commit):

```bash
cd api
set CLOUDAXIS_CAPTURE_EMAIL=you@example.com
set CLOUDAXIS_CAPTURE_PASSWORD=secret
node scripts/capture-cloudaxis-launch-media.mjs all    # shots + videos
node scripts/capture-cloudaxis-launch-media.mjs shots  # screenshots only
node scripts/capture-cloudaxis-launch-media.mjs videos # videos only
```

---

## Logos

| File | When to use |
|------|-------------|
| `logos/cloudaxis-logo-mark.svg` | Web, scalable |
| `logos/cloudaxis-logo-white-bg-512.png` | G2, Capterra (require white/light bg) |
| `logos/cloudaxis-logo-transparent-512.png` | PH, dark UIs |
| `logos/cloudaxis-logo-512.png` | General |

---

## OG / social images (1200×630)

| File | Use |
|------|-----|
| `og/ph-hero-1200x630.png` | Product Hunt thumbnail, Twitter card |
| `og/directory-banner-1200x630.png` | G2/Capterra banner, LinkedIn |

Regenerate: `cd api && node scripts/generate-cloudaxis-launch-assets.mjs`

---

## Hunter one-pager (send this week)

- **Pack:** [`HUNTER-PACK.md`](./HUNTER-PACK.md) — teaser video links, gallery order, copy
- **Launch teaser YouTube:** https://youtu.be/X80a_OZMiaQ
- **Launch teaser MP4 (1080p):** https://github.com/CloudAxisAi/cloudybot-ai/raw/main/launch-assets/cloudaxis/video/LaunchTeaser-1080p.mp4
- **URL:** https://app.cloudaxis.ai (offer beta Pro access)
- **Positioning:** Isolated cloud computer for AI agents — not a chatbot
- **3 demos:** (1) launch teaser 60s, (2) cloud browser + VPN, (3) multi-agent workflow
- **Copy:** `copy/LISTING-COPY.md`
- **Assets:** this folder + PH gallery order above

---

## Notes

- Use **`screenshots-v2/`** only — v1 `screenshots/` were partial viewport crops.
- Some embedded UI strings still say "Cloudy" in browser chrome — cosmetic only.
- Do **not** commit credentials. This kit has no secrets.

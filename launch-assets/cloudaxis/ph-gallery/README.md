# Product Hunt gallery (1270×760)

Render from `api/`:

```bash
npm run render:cloudaxis:ph-gallery          # all slides
node scripts/render-cloudaxis-ph-gallery.mjs 03-cloudia
```

## Upload order (8 slides)

| # | Output | Source screenshot | Story |
|---|--------|-------------------|-------|
| 01 | `01-home.png` | `18-marketing-hero.png` | Marketing hero |
| 02 | `02-app-home.png` | `01-desktop-home.png` | Cloud desktop home |
| 02 | `02-app-home.gif` | desktop → launchpad → scroll | Optional animated #2 |
| 03 | `03-cloudia.png` | `10-chat-cloudia.png` | Cloudia team builder |
| 04 | `04-agents.png` | `03-agents-board-full.png` | Scheduled agent board |
| 05 | `05-browser.png` | `09b-browser-browsing.png` | Real cloud browser (live site in PiP) |
| 06 | `06-files.png` | `06-files-workspace.png` | Persistent ~/files workspace |
| 07 | `07-workflows.png` | `05-workflows-pipeline.png` | Multi-agent workflow recipes |
| 08 | `08-comparison.png` | `19-marketing-comparison.png` | vs chat / local / headless |

Edit caption text in `ph-gallery-*.html`, then re-render PNGs:

```bash
node scripts/render-cloudaxis-ph-gallery.mjs 02-app-home
```

Animated GIF (slide 02):

```bash
node scripts/render-cloudaxis-ph-gallery-gif.mjs 02-app-home
```

Refresh browser source (`09b-browser-browsing.png`) from a real night-run capture (PiP shows live site):

```bash
node scripts/capture-cloudaxis-scene-01-night.mjs
# then extract best frame, e.g. ffmpeg -ss 60 -i video/scene-01-already-inside-live.mp4 -frames:v 1 -update 1 screenshots-v2/09b-browser-browsing.png
node scripts/render-cloudaxis-ph-gallery.mjs 05-browser
```

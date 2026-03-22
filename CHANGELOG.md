# Changelog

All notable updates to CloudyBot are documented here.

---

## [v1.8] — 2026-03-15
### Added
- WhatsApp task routing: send tasks directly from WhatsApp, get results back in the same thread
- Improved memory for long multi-step tasks — context no longer drops after 10 steps

### Improved
- Cloud browser stability on sites with heavy JavaScript (SPAs, React apps)
- LinkedIn automation speed improved by 40%

---

## [v1.7] — 2026-03-01
### Added
- Knowledge base: upload PDFs and Word docs, ask questions directly
- Multi-file support — query across multiple documents in one session

### Fixed
- Form-fill edge cases on sites with CAPTCHA challenges
- Session timeout handling for long-running tasks

---

## [v1.6] — 2026-02-15
### Added
- Hard-cap pricing enforcement — monthly cap is now a hard block, not a soft warning
- Task scheduling: set recurring tasks (daily, weekly, custom cron)

### Improved
- Web scraping accuracy on paginated results
- Better error messages when a site blocks automated browsing

---

## [v1.5] — 2026-02-01
### Added
- Browser screenshot previews — see what CloudyBot is looking at mid-task
- Export results to CSV directly from chat

### Fixed
- LinkedIn rate limiting — added smart delays to avoid account flags
- Memory leak in long sessions (5+ hours)

---

## [v1.4] — 2026-01-15
### Added
- Multi-step task chains: "First do X, then if Y do Z"
- Slack notification support for task completions

---

## [v1.3] — 2026-01-01
### Added
- WhatsApp integration (beta)
- Task history — review and re-run past tasks

---

## [v1.2] — 2025-12-15
### Added
- LinkedIn profile research mode
- Batch processing: run the same task across a list of URLs

---

## [v1.1] — 2025-12-01
### Added
- Web research mode
- Result formatting: table, bullet list, or paragraph

---

## [v1.0] — 2025-11-15
### Initial Release
- Cloud browser task execution
- Chat interface
- Basic web scraping and form-fill
- Hard-capped pricing model

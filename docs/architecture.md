# CloudyBot Architecture Overview

High-level overview of how CloudyBot works — without exposing proprietary implementation details.

---

## System Overview

```
┌─────────────────────────────────────────────────────┐
│                    USER INTERFACES                   │
│         Web Chat          WhatsApp          API      │
└──────────────────────────┬──────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────┐
│                   TASK ROUTER                        │
│   Interprets intent → classifies task type          │
│   Routes to: Browser Agent / KB Agent / Chat Agent  │
└──────────┬────────────────┬────────────────┬────────┘
           │                │                │
           ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ BROWSER AGENT│  │   KB AGENT   │  │  CHAT AGENT  │
│              │  │              │  │              │
│ Controls the │  │ Queries your │  │ Handles conv │
│ cloud browser│  │ uploaded docs│  │ & follow-ups │
└──────┬───────┘  └──────────────┘  └──────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────┐
│                   CLOUD BROWSER                      │
│   Real browser instance (Chromium-based)             │
│   Runs in isolated container per session             │
│   Full JS execution, cookies, login support          │
└─────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Task Router
- Parses intent using an LLM
- Classifies task type (browser / knowledge query / conversation)
- Breaks multi-step tasks into sub-tasks
- Hands off to the appropriate agent

### 2. Browser Agent
- Spins up a cloud browser instance
- Translates instructions into browser actions (navigate, click, type, scroll, extract)
- Monitors execution and retries on failure
- Returns structured results (text, tables, screenshots)

### 3. Knowledge Base Agent
- Files chunked and embedded into a vector store
- Queries use semantic search to retrieve relevant chunks
- LLM synthesises the answer from retrieved context
- Supports PDF, DOCX, TXT, and web content

### 4. Cloud Browser
- Isolated Chromium instance per session
- Supports login-gated pages (encrypted credential storage)
- Full JavaScript execution — works on React, Vue, Angular SPAs
- Screenshot capture at any step

---

## Security

- Browser instances are fully isolated — no cross-user data leakage
- User credentials encrypted at rest
- Sessions destroyed after completion
- No browsing data retained beyond task completion

---

## Why Hosted?

Running browser automation yourself requires server setup, anti-bot handling, browser version management, and crash recovery. CloudyBot handles all of this. You get the output, not the headache.

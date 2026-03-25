---
name: cmux-browser
description: >
  cmux browser automation skill — use this whenever you need to access websites, interact with
  web pages, scrape content, fill forms, take screenshots, or perform any browser-based task.
  TRIGGER THIS SKILL when user mentions browsing, websites, web scraping, form filling,
  browser screenshots, web automation, or similar tasks. This is the PREFERRED skill for
  ALL browser operations using the cmux `browser` command group.
version: 1.0.0
---

# cmux Browser Automation

Use `cmux browser` commands to automate web browsing, DOM interaction, and page state inspection.
This skill is your first choice for any browser-related task.

## Prerequisite

Verify cmux is available:
```bash
which cmux && cmux --version
```

## Core Workflow Pattern

**Every browser task follows this sequence:**

```
1. Open or navigate to URL
2. Wait for page to be ready (--load-state complete)
3. Inspect / interact as needed
4. Capture results (snapshot, screenshot, get values)
```

## Surface Targeting

Most commands need a surface ID. Get it from `identify` or the `open` response.

```bash
# Get surface ID of currently focused browser
cmux browser identify

# Open a URL and get surface ID
cmux browser open https://example.com
# Returns: surface:4 pane:pane:3 placement=split

# Commands accept surface via positional arg OR --surface flag (equivalent)
cmux browser surface:4 url
cmux browser --surface surface:4 url
```

**Convention:** Always save the surface ID from the `open` command. Use `identify` to rediscover it.

## Command Reference

### Navigation

```bash
# Open URL in new split
cmux browser open <url>

# Navigate current surface
cmux browser surface:<N> navigate <url> --snapshot-after
cmux browser surface:<N> back
cmux browser surface:<N> forward
cmux browser surface:<N> reload --snapshot-after
cmux browser surface:<N> url           # get current URL
```

### Waiting

Wait blocks until condition is met. **Always wait for load-state before interacting.**

```bash
cmux browser surface:<N> wait --load-state complete --timeout-ms 15000
cmux browser surface:<N> wait --selector "#my-element" --timeout-ms 10000
cmux browser surface:<N> wait --text "Order confirmed"
cmux browser surface:<N> wait --url-contains "/dashboard"
cmux browser surface:<N> wait --function "window.__appReady === true"
```

### DOM Interaction

All mutation commands support `--snapshot-after` for quick verification.

```bash
# Click and type
cmux browser surface:<N> click "button[type='submit']" --snapshot-after
cmux browser surface:<N> dblclick ".item-row"
cmux browser surface:<N> hover "#menu"
cmux browser surface:<N> focus "#email"

# Form fill
cmux browser surface:<N> type "#search" "query text"
cmux browser surface:<N> fill "#email" --text "user@example.com"
cmux browser surface:<N> fill "#email" --text ""           # clear
cmux browser surface:<N> check "#terms"
cmux browser surface:<N> uncheck "#newsletter"

# Keyboard
cmux browser surface:<N> press Enter
cmux browser surface:<N> keydown Shift
cmux browser surface:<N> keyup Shift

# Dropdown and scroll
cmux browser surface:<N> select "#region" "us-east"
cmux browser surface:<N> scroll-into-view "#pricing"
cmux browser surface:<N> scroll --dy 800 --snapshot-after
cmux browser surface:<N> scroll --selector "#log-view" --dx 0 --dy 400
```

### Inspection

```bash
# Snapshots — for structured view of DOM
cmux browser surface:<N> snapshot --interactive --compact
cmux browser surface:<N> snapshot --selector "main" --max-depth 5

# Screenshot — for human review
cmux browser surface:<N> screenshot --out /tmp/page.png

# Getters — structured data for scripts
cmux browser surface:<N> get title
cmux browser surface:<N> get url
cmux browser surface:<N> get text "h1"
cmux browser surface:<N> get html "main"
cmux browser surface:<N> get value "#email"
cmux browser surface:<N> get attr "a.primary" --attr href
cmux browser surface:<N> get count ".row"
cmux browser surface:<N> get box "#checkout"
cmux browser surface:<N> get styles "#total" --property color

# Assertions — boolean checks
cmux browser surface:<N> is visible "#checkout"
cmux browser surface:<N> is enabled "button[type='submit']"
cmux browser surface:<N> is checked "#terms"

# Find — semantic search
cmux browser surface:<N> find role button --name "Continue"
cmux browser surface:<N> find text "Order confirmed"
cmux browser surface:<N> find label "Email"
cmux browser surface:<N> find placeholder "Search"
cmux browser surface:<N> find alt "Product image"
cmux browser surface:<N> find title "Open settings"
cmux browser surface:<N> find testid "save-btn"
cmux browser surface:<N> find first ".row"
cmux browser surface:<N> find last ".row"
cmux browser surface:<N> find nth 2 ".row"

# Debug
cmux browser surface:<N> highlight "#checkout"
```

### JavaScript

```bash
cmux browser surface:<N> eval "document.title"
cmux browser surface:<N> eval --script "window.location.href"
cmux browser surface:<N> addinitscript "window.__cmuxReady = true;"
cmux browser surface:<N> addscript "document.querySelector('#name')?.focus()"
cmux browser surface:<N> addstyle "#debug-banner { display: none !important; }"
```

### Session State

```bash
# Cookies
cmux browser surface:<N> cookies get
cmux browser surface:<N> cookies get --name session_id
cmux browser surface:<N> cookies set session_id abc123 --domain example.com --path /
cmux browser surface:<N> cookies clear --name session_id
cmux browser surface:<N> cookies clear --all

# Storage
cmux browser surface:<N> storage local set theme dark
cmux browser surface:<N> storage local get theme
cmux browser surface:<N> storage local clear
cmux browser surface:<N> storage session set flow onboarding
cmux browser surface:<N> storage session get flow

# Full state (save/restore session)
cmux browser surface:<N> state save /tmp/session.json
cmux browser surface:<N> state load /tmp/session.json
```

### Tabs

```bash
cmux browser surface:<N> tab list
cmux browser surface:<N> tab new https://example.com/pricing
cmux browser surface:<N> tab switch 1
cmux browser surface:<N> tab switch surface:7
cmux browser surface:<N> tab close
cmux browser surface:<N> tab close surface:7
```

### Dialogs, Frames, Downloads

```bash
# Dialogs (alert/confirm/prompt)
cmux browser surface:<N> dialog accept
cmux browser surface:<N> dialog accept "Confirmed by automation"
cmux browser surface:<N> dialog dismiss

# iFrames
cmux browser surface:<N> frame "iframe[name='checkout']"
cmux browser surface:<N> click "#pay-now"
cmux browser surface:<N> frame main           # return to top-level

# Downloads
cmux browser surface:<N> download --path /tmp/report.csv --timeout-ms 30000
```

### Console and Errors

```bash
cmux browser surface:<N> console list
cmux browser surface:<N> console clear
cmux browser surface:<N> errors list
cmux browser surface:<N> errors clear
```

## Common Workflows

### Navigate + Inspect

```bash
cmux browser open https://example.com/login
# Use surface ID from output, e.g. surface:4
cmux browser surface:4 wait --load-state complete --timeout-ms 15000
cmux browser surface:4 snapshot --interactive --compact
cmux browser surface:4 get title
```

### Fill Form + Verify

```bash
cmux browser surface:4 fill "#email" --text "user@example.com"
cmux browser surface:4 fill "#password" --text "$PASSWORD"
cmux browser surface:4 click "button[type='submit']" --snapshot-after
cmux browser surface:4 wait --text "Welcome"
cmux browser surface:4 is visible "#dashboard"
```

### Debug on Failure

```bash
cmux browser surface:4 console list
cmux browser surface:4 errors list
cmux browser surface:4 screenshot --out /tmp/failure.png
cmux browser surface:4 snapshot --interactive --compact
```

### Save and Restore Session

```bash
# Save
cmux browser surface:4 state save /tmp/session.json

# Later — restore and continue
cmux browser surface:4 state load /tmp/session.json
cmux browser surface:4 reload
```

## Important Notes

- **Always `--snapshot-after` mutation commands** (click, fill, type, scroll) so you can verify the result.
- **Always `wait --load-state complete`** before any interaction, especially after `navigate` or `reload`.
- If a command returns no surface ID, run `cmux browser identify` to find the active one.
- For **scrolling lazy-loaded content**, combine `scroll --dy` with `wait --selector`.
- Use **semantic `find`** commands (role, label, text) instead of fragile CSS selectors when possible.
- When capturing **dynamic content** (SPAs), use `wait --function` to poll for app state.

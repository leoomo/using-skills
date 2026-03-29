# Custom Skills for Claude Code

A collection of custom skills extending Claude Code's capabilities across document processing, frontend design, backend architecture, debugging workflows, and web automation.

## Skills Overview

### 📄 Document Processing

| Skill | Description |
|-------|-------------|
| **docx** | Create, read, edit, and manipulate Word documents (.docx). Handles tables of contents, headings, tracked changes, comments, and professional formatting. |
| **pdf** | Comprehensive PDF operations: read/extract text and tables, merge/split PDFs, fill forms, OCR scanned documents, encrypt/decrypt, and add watermarks. |
| **pptx** | Create and edit PowerPoint presentations. Supports templates, layouts, speaker notes, and slide manipulation. |
| **md2pdf** | Convert Markdown to PDF using pandoc + typst. Compatible with Obsidian Markdown including wikilinks and frontmatter. |
| **md2epub** | Convert Markdown to EPUB format for e-readers. Supports batch folder conversion and automatic image downloading. |
| **md2kindle** | Convert Markdown to AZW3 format for Kindle devices. Requires Calibre. |

### 📐 Diagram & Modeling

| Skill | Description |
|-------|-------------|
| **drawio** | Create diagrams, flowcharts, architecture diagrams, ER diagrams, sequence diagrams, and more as native `.drawio` files. Export to PNG, SVG, or PDF with embedded editable XML. |
| **solar-storage-diagram** | Specialized for solar+energy storage systems (光储系统). Create system architecture diagrams, electrical single-line diagrams, and ESS layout diagrams. Inherits all drawio capabilities. |

### 🎨 Frontend & Design

| Skill | Description |
|-------|-------------|
| **design-taste-frontend** | Senior UI/UX engineer skill that enforces metric-based design rules, strict component architecture, CSS hardware acceleration, and balanced design engineering. |
| **chrome-ext-expert** | Develop Google Chrome extensions (Manifest V3). Covers chrome.* APIs, service workers, content scripts, permissions, and debugging. |

### 🔧 Backend Architecture

| Skill | Description |
|-------|-------------|
| **fastapi-templates** | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. |
| **pyside6-architecture** | Build high-performance desktop apps with PySide6 following MVC/MVVM patterns. Covers multi-threading, signals/slots, and resource management. |
| **tauri-architecture** | Build secure desktop apps with Tauri v2 combining Rust backend and modern frontend. Covers command patterns, state management, and security best practices. |

### 🐛 Workflow & Debugging

| Skill | Description |
|-------|-------------|
| **autoresearch** | Autonomous goal-directed iteration inspired by Karpathy's autoresearch. Modify → Verify → Keep/Discard → Repeat. Includes security audit, debug, fix, and ship subcommands. |
| **ai-planning-workflow** | AI programming workflow: never let AI write code until a written plan is approved. Enforces planning discipline. |
| **git-bug-hunter** | Deep bug hunting with Git: bisect for version localization, reflog for recovery, analyze recent commits, resolve merge conflicts. |
| **socratic-questioning** | Guided deep thinking framework for strategic analysis, creative problem solving, and multi-step reasoning. |
| **simplify** | Review changed code for reuse, quality, and efficiency, then fix any issues found. |

### 🌐 Web & Browser Automation

| Skill | Description |
|-------|-------------|
| **web-access** | Handle all web operations: search, scrape, login-required sites, social media content (Xiaohongshu, Weibo, Twitter), and dynamic pages requiring real browser. |
| **cmux-browser** | Browser automation via cmux `browser` command group. Navigate websites, fill forms, take screenshots, and scrape content. |
| **follow-builders** | AI builders digest — tracks top AI builders on X and YouTube podcasts, delivers curated summaries. No API keys required. |

### 🛠 Skill Development

| Skill | Description |
|-------|-------------|
| **skill-creator** | Create new skills, modify existing ones, run evals, benchmark performance with variance analysis, and optimize descriptions for triggering accuracy. |
| **skill-optimizer** | Optimize and refine Claude Code instruction documents including skills, CLAUDE.md files, agent definitions, and custom commands. |

### 💼 Productivity

| Skill | Description |
|-------|-------------|
| **miles_work** | Technical co-founder assistant for building real, usable products. |

## Installation

Clone this repository to your Claude Code skills directory:

```bash
git clone https://github.com/YOUR_USERNAME/using-skills.git ~/.claude/skills/using-skills
```

Or copy individual skill folders to your skills directory:

```bash
cp -r skills/<skill-name> ~/.claude/skills/
```

## Structure

```
skills/
├── <skill-name>/
│   ├── SKILL.md          # Main skill definition
│   ├── references/       # Additional documentation (loaded on demand)
│   └── scripts/          # Helper scripts (if any)
```

## License

MIT

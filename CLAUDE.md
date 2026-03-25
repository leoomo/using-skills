# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Custom skills for Claude Code that extend capabilities across document processing, frontend design, backend architecture, debugging workflows, and web automation.

## Skill Architecture

### Structure

Each skill follows this pattern:
```
skills/<skill-name>/
├── SKILL.md           # Main skill definition (<500 lines)
├── references/        # Large docs loaded on demand
└── scripts/           # Helper scripts (Python/JS, optional)
```

### Progressive Disclosure

Skills use three levels of loading:
1. **Metadata** (name + description in frontmatter) — always in context for triggering
2. **SKILL.md body** — loaded when skill is triggered
3. **Bundled resources** (references/, scripts/) — loaded explicitly when needed

### SKILL.md Format

```yaml
---
name: skill-name-with-hyphens
description: Use when [specific triggers]. Include symptoms, contexts, user phrases.
---
```

The description is critical for triggering accuracy — it must capture the specific phrases and contexts where this skill should activate.

### Writing Conventions

- Explain WHY, not just WHAT
- Use imperative form
- One good example > many mediocre ones
- Keep SKILL.md under 500 lines; split large content to `references/`
- Use `references/` for detailed docs, schemas, and extended examples

## Skill Testing Workflow

Skills can be benchmarked using the skill-creator's evaluation system:

1. Create test cases in `evals/evals.json`
2. Spawn parallel subagents (with-skill vs baseline)
3. Results go in `<skill-name>-workspace/iteration-N/`
4. Grade with assertions, aggregate with `python -m scripts.aggregate_benchmark`
5. Iterate until satisfied

See `skills/skill-creator/SKILL.md` for full benchmark workflow.

## Categories

- **Document Processing**: docx, pdf, pptx, md2pdf, md2epub, md2kindle
- **Frontend & Design**: design-taste-frontend, chrome-ext-expert
- **Backend Architecture**: fastapi-templates, pyside6-architecture, tauri-architecture
- **Workflow & Debugging**: autoresearch, ai-planning-workflow, git-bug-hunter, socratic-questioning, simplify
- **Web & Browser**: web-access, cmux-browser, follow-builders
- **Skill Development**: skill-creator, skill-optimizer
- **Productivity**: miles_work

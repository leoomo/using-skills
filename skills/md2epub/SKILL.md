---
name: md2epub
description: Convert Markdown to EPUB for e-readers with Kindle email support. Use when user wants to convert .md files to EPUB format, send to Kindle, or upload to iReader. Triggered by keywords like "convert markdown to epub", "md to epub", "send to kindle", "ebook", "ireader". Auto-handles Obsidian wikilinks and downloads external images concurrently.
---

# Markdown to EPUB Converter

Convert Obsidian-flavored Markdown to EPUB format, with Kindle email delivery built-in.

## Setup

Dependencies managed by uv. Run once to install:

```bash
cd ~/.claude/skills/md2epub && uv sync
```

## Usage

All commands must be run from the md2epub directory:

```bash
cd ~/.claude/skills/md2epub
```

### Single File

```bash
uv run python -m src "/path/to/file.md" [output.epub]
```

### Batch Folder

```bash
uv run python -m src "/path/to/folder/" [output.epub]
```

### Convert and Send to Kindle

```bash
uv run python -m src "/path/to/file.md" --send
uv run python -m src "/path/to/folder/" --send
```

### Skip Images (faster)

```bash
uv run python -m src "/path/to/folder/" --no-images --send
```

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--send` | Send to Kindle via email after conversion | - |
| `--no-images` | Skip downloading and embedding images | - |
| `--kindle-email` | Kindle email address | leoomo_1984@kindle.com |
| `--sender-email` | Your email address | zengleo@163.com |
| `--password` | Email password/auth code | (configured) |
| `--smtp-server` | SMTP server | smtp.163.com |
| `--smtp-port` | SMTP port | 465 |

## Workflow

1. **Check input type:**
   - File → single file conversion
   - Folder → batch merge all `.md` files

2. **Auto-processing:**
   - Parse YAML frontmatter (title, author, date)
   - Convert `[[WikiLinks]]` to HTML links
   - Download & optimize external images (concurrent, 4 workers, 8s timeout)
   - Split into chapters at H1/H2 headings
   - Generate table of contents

3. **Output:** EPUB file + optional Kindle email delivery

### With iReader Upload

If user mentions "ireader":

```bash
IREADER_IP="192.168.3.17"

if ! curl -s --connect-timeout 3 "http://${IREADER_IP}:10123/" > /dev/null 2>&1; then
    IREADER_IP=$(python3 ~/.claude/skills/md2epub/scripts/find_ireader.py 2>/dev/null)
fi

curl -X POST "http://${IREADER_IP}:10123/test.php?action=addBook" \
  -F "Filename=book.epub" \
  -F "Filedata=@book.epub" \
  -F "Upload=Submit Query"
```

## Examples

- `"Convert article.md to EPUB"`
- `"Merge all markdown in Notes/ to one ebook"`
- `"Convert Clippings/ and send to Kindle"`
- `"Convert to EPUB and upload to ireader"`

## Features

- Obsidian wikilinks & frontmatter support
- Concurrent image download with timeout protection
- `--no-images` flag for faster conversion
- Hierarchical TOC for folder conversion
- Kindle email delivery built-in
- iReader upload support
- Chinese language optimized
- Managed by uv, single venv

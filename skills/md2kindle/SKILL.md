---
name: md2kindle
description: Convert Markdown files to AZW3 format for Kindle devices. Use when the user wants to convert .md files to Kindle format (AZW3/KF8). Requires Calibre to be installed. Supports batch folder conversion and automatically downloads external images. Uses md2epub as intermediate format.
---

# Markdown to Kindle Converter

Convert Markdown (especially Obsidian-flavored) to AZW3 format for Kindle e-readers.

## Requirements

- **Calibre** must be installed: `brew install --cask calibre`

## Usage

### Single File
```bash
python3 -m md2kindle "path/to/file.md" [output.azw3]
```

### Batch Folder
```bash
python3 -m md2kindle "path/to/folder/" [output.azw3]
```

## Workflow

When user asks to convert markdown to Kindle/AZW3:

1. **Generate EPUB** using md2epub skill
2. **Convert to AZW3** using Calibre's `ebook-convert`
3. **Clean up** intermediate EPUB file (optional)

## Examples

**Single file:**
```
Convert "article.md" to Kindle format
```

**Folder batch:**
```
Convert all markdown in "Clippings/" to AZW3
```

## Features

- **Kindle Optimized**: AZW3/KF8 format with better typography
- **Obsidian Support**: Handles wikilinks, frontmatter, tags
- **Image Handling**: Auto-downloads external images, optimizes for e-readers
- **Batch Conversion**: Convert entire folders

## Dependencies

```
# Calibre (required)
brew install --cask calibre

# Python packages (via md2epub)
pip install ebooklib markdown Pillow requests PyYAML
```

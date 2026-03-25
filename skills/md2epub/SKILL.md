---
name: md2epub
description: Convert Markdown files to EPUB format for e-readers. Use when the user wants to convert .md files to EPUB format for reading on Kindle, iReader, or other e-book devices. Supports batch folder conversion and automatically downloads external images. If the user mentions 'ireader', automatically scans the network for port 10123 and uploads the generated EPUB.
---

# Markdown to EPUB Converter

Convert Markdown (especially Obsidian-flavored) to EPUB format for comfortable reading on e-readers, tablets, and phones.

## Usage

### Single File
```bash
python3 -m md2epub "path/to/file.md" [output.epub]
```

### Batch Folder
```bash
python3 -m md2epub "path/to/folder/" [output.epub]
```

## Workflow

When user asks to convert markdown to EPUB:

1. **Check if it's a file or folder:**
   - File: `convert_file(input_path, output_path)`
   - Folder: `convert_folder(input_path, output_path)`

2. **The converter automatically:**
   - Parses YAML frontmatter (title, author, date, tags)
   - Converts Obsidian wikilinks (`[[Note]]`) to HTML links
   - Downloads external images and embeds them
   - Optimizes images for e-readers (resize to max 1200px, JPEG compression)
   - Splits content into chapters at H1/H2 headings
   - Generates table of contents

3. **Output:** EPUB file with adaptive typography

### With iReader Upload

If user mentions "ireader":

```bash
# Find iReader device
python3 ~/.claude/skills/md2epub/scripts/find_ireader.py

# Upload EPUB
curl -X POST "http://<ip>:10123/test.php?action=addBook" \
  -F "Filename=book.epub" \
  -F "Filedata=@book.epub" \
  -F "Upload=Submit Query"
```

## Examples

**Single file:**
```
Convert "Clippings/article.md" to EPUB
```

**Folder batch:**
```
Convert all markdown in "Clippings/" to a single EPUB
```

**With iReader:**
```
Convert "book.md" to EPUB and upload to ireader
```

## Features

- **Obsidian Support**: Handles wikilinks, frontmatter, tags
- **Image Handling**: Auto-downloads external images, optimizes for e-readers
- **Adaptive Typography**: Reflowable text, adjustable fonts, dark mode support
- **Auto Chapter Split**: Splits at H1/H2 headings
- **Table of Contents**: Auto-generated from document structure

## Dependencies

```
pip install ebooklib markdown Pillow requests PyYAML
```

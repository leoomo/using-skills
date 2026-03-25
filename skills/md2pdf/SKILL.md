---
name: md2pdf
description: Convert Markdown files to PDF using pandoc + typst. Use when the user wants to convert .md files to PDF format. If the user mentions 'ireader' or similar e-reader terms, automatically scan the local network (192.168.x.x) for a service on port 10123 and upload the generated PDF to it. Compatible with Obsidian Markdown including wikilinks and frontmatter.
---

# Markdown to PDF Converter

Convert Markdown files to PDF with optional automatic upload to iReader devices.

## Workflow

### Basic PDF Conversion

When the user asks to convert a markdown file to PDF:

1. **Validate input**: Check that the markdown file exists
2. **Convert using pandoc + typst**:
   ```bash
   pandoc "<input.md>" -o "<output.pdf>" --pdf-engine=typst --resource-path=<file_dir> --from=markdown-citations
   ```
3. **Verify output**: Confirm the PDF was created
4. **Report**: Tell user the PDF path and size

### With iReader Upload

If the user mentions "ireader" or similar terms, in addition to conversion:

1. **Scan for iReader service**:
   ```bash
   python3 ~/.claude/skills/md2pdf/scripts/find_ireader.py
   ```
2. **Upload if found**: If an iReader is found at `http://<ip>:10123`:
   ```bash
   curl -X POST "http://<ip>:10123/test.php?action=addBook" \
     -F "Filename=<pdf_filename>" \
     -F "Filedata=@<output.pdf>" \
     -F "Upload=Submit Query"
   ```
3. **Report results**: Tell user both the local PDF path and upload status

## Parameters

The skill automatically detects:
- **Input file**: Any `.md` file path mentioned by the user
- **Output location**: Same directory as input, same filename with `.pdf` extension
- **iReader mode**: Triggered by keywords like "ireader", "upload", "send to"

## Examples

**Example 1 - Basic conversion:**
User: "把 notes.md 转成 pdf"
→ Convert `notes.md` to `notes.pdf` in the same directory

**Example 2 - With iReader upload:**
User: "把 book.md 转成 pdf 传到 ireader"
→ Convert `book.md` to `book.pdf`, scan 192.168.x.x for port 10123, upload if found

**Example 3 - Multiple files:**
User: "转换 Chapter1.md 和 Chapter2.md 到 pdf"
→ Convert both files separately, report all output paths

## Error Handling

- If pandoc is not installed: Tell user to install it (`brew install pandoc`)
- If typst is not installed: Tell user to install it (`brew install typst`)
- If input file doesn't exist: Report error and stop
- If iReader not found: Still create PDF, report that upload was skipped
- If upload fails: Report the error but keep the PDF file

## Dependencies

Required tools:
- `pandoc` - for markdown to PDF conversion
- `typst` - PDF rendering engine (lighter than LaTeX)
- `curl` - for uploading to iReader
- `python3` - for network scanning

## Notes

- The `--from=markdown-citations` flag prevents issues with `[@username]` style links (common in Obsidian/twitter links)
- `--resource-path` is set to the input file's directory so relative image paths resolve correctly
- Network scan covers 192.168.0.0/16 range on port 10123

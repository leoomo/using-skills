"""Main converter module for Markdown to EPUB."""
import re
import markdown
from pathlib import Path
from typing import Optional, List

from .markdown_parser import parse_frontmatter, convert_wikilinks
from .image_handler import process_images
from .epub_builder import build_epub


def convert_file(input_path: Path, output_path: Optional[Path] = None) -> Path:
    """Convert a single markdown file to EPUB."""

    if output_path is None:
        output_path = input_path.with_suffix('.epub')

    # Read markdown
    content = input_path.read_text(encoding='utf-8')

    # Parse frontmatter
    metadata, body = parse_frontmatter(content)

    # Use filename as title if not in frontmatter
    if 'title' not in metadata:
        metadata['title'] = input_path.stem

    # Convert wikilinks
    body = convert_wikilinks(body)

    # Process images
    base_path = input_path.parent
    body, images = process_images(body, base_path)

    # Split into chapters
    chapters = split_into_chapters(body)

    # Build EPUB
    build_epub(metadata, chapters, images, output_path)

    return output_path


def split_into_chapters(content: str) -> List[dict]:
    """Split markdown content into chapters based on headings."""
    # Convert markdown to HTML first
    md = markdown.Markdown(extensions=['tables', 'fenced_code'])
    html_content = md.convert(content)

    # Split at h1 and h2
    pattern = r'(<h[12][^>]*>.*?</h[12]>)'
    parts = re.split(pattern, html_content, flags=re.DOTALL)

    chapters = []
    current_title = "Content"
    current_content = ""

    for part in parts:
        if re.match(r'<h[12]', part):
            if current_content:
                chapters.append({
                    'title': current_title,
                    'content': current_content
                })
            # Extract title from heading
            match = re.search(r'<h[12][^>]*>(.*?)</h[12]>', part, re.DOTALL)
            current_title = match.group(1) if match else "Chapter"
            current_content = part
        else:
            current_content += part

    # Don't forget last chapter
    if current_content:
        chapters.append({
            'title': current_title,
            'content': current_content
        })

    # If no chapters found, treat whole content as one chapter
    if not chapters:
        chapters = [{'title': 'Content', 'content': html_content}]

    return chapters


def convert_folder(folder_path: Path, output_path: Optional[Path] = None) -> Path:
    """Convert all markdown files in a folder to a single EPUB."""

    # Find all markdown files
    md_files = sorted(folder_path.glob('*.md'))

    if not md_files:
        raise ValueError(f"No markdown files found in {folder_path}")

    if output_path is None:
        output_path = folder_path / f"{folder_path.name}.epub"

    # Collect parts (each file is a part with sub-chapters)
    parts = []
    all_images = {}
    metadata = {'title': folder_path.name, 'author': 'Unknown'}

    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')

        # Parse frontmatter from first file only
        file_metadata, body = parse_frontmatter(content)
        if file_metadata.get('title') and metadata.get('title') == folder_path.name:
            metadata['title'] = file_metadata.get('title', folder_path.name)
        if file_metadata.get('author'):
            metadata['author'] = file_metadata.get('author')

        # Use file title from frontmatter or filename
        file_title = file_metadata.get('title', md_file.stem)

        # Convert wikilinks
        body = convert_wikilinks(body)

        # Process images
        body, images = process_images(body, folder_path, all_images)
        all_images.update(images)

        # Convert to HTML and split into chapters
        chapters = split_into_chapters(body)

        # Create a part with sub-chapters
        parts.append({
            'title': file_title,
            'chapters': chapters
        })

    # Build EPUB with hierarchical structure
    build_epub(metadata, parts, all_images, output_path, hierarchical=True)

    return output_path

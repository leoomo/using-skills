"""EPUB builder using ebooklib."""
import os
from pathlib import Path
from ebooklib import epub
from typing import Dict, List, Any, Optional


def build_epub(metadata: Dict[str, Any], content: Any, images: Dict[str, bytes], output_path: Path, hierarchical: bool = False):
    """Build EPUB file from chapters or parts and images."""

    book = epub.EpubBook()

    # Set metadata
    title = metadata.get('title', 'Untitled')
    author = metadata.get('author', 'Unknown')
    if isinstance(author, list):
        author = ', '.join(author)

    book.set_identifier(f"md2epub-{hash(title)}")
    book.set_title(title)
    book.set_language('zh-CN')
    book.add_author(author)

    if 'date' in metadata:
        book.add_metadata('DC', 'date', metadata['date'])
    if 'description' in metadata:
        book.add_metadata('DC', 'description', metadata['description'])
    if 'tags' in metadata:
        tags = metadata['tags'] if isinstance(metadata['tags'], list) else [metadata['tags']]
        book.add_metadata('DC', 'subject', ', '.join(tags))

    # Add CSS
    style_path = Path(__file__).parent.parent / 'templates' / 'style.css'
    if style_path.exists():
        with open(style_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
    else:
        css_content = 'body { font-family: serif; }'

    style = epub.EpubItem(uid="style", file_name="style.css", media_type="text/css", content=css_content)
    book.add_item(style)

    # Add images
    for filename, data in images.items():
        ext = filename.split('.')[-1].lower()
        mime = 'image/jpeg' if ext in ('jpg', 'jpeg') else 'image/png' if ext == 'png' else 'image/gif'
        img_item = epub.EpubItem(uid=filename, file_name=f"images/{filename}", media_type=mime, content=data)
        book.add_item(img_item)

    if hierarchical:
        return _build_hierarchical(book, content, style, output_path)
    else:
        return _build_flat(book, content, style, output_path)


def _build_flat(book: epub.EpubBook, chapters: List[Dict], style: epub.EpubItem, output_path: Path):
    """Build flat EPUB structure."""

    # Create chapters
    epub_chapters = []
    for i, chapter in enumerate(chapters):
        c = epub.EpubHtml(
            title=chapter['title'],
            file_name=f'chapter_{i+1:03d}.xhtml',
            lang='zh-CN'
        )
        c.content = chapter['content']
        c.add_item(style)
        book.add_item(c)
        epub_chapters.append(c)

    # Create Table of Contents page
    toc_html = '<h1>目录</h1><nav epub:type="toc"><ol>'
    for i, chapter in enumerate(chapters):
        toc_html += f'<li><a href="chapter_{i+1:03d}.xhtml">{chapter["title"]}</a></li>'
    toc_html += '</ol></nav>'

    toc_page = epub.EpubHtml(
        title='目录',
        file_name='toc.xhtml',
        lang='zh-CN'
    )
    toc_page.content = toc_html
    toc_page.add_item(style)
    book.add_item(toc_page)

    # Create table of contents
    book.toc = [(epub.Section(ch['title']), [c]) for ch, c in zip(chapters, epub_chapters)]

    # Add navigation
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define spine (TOC first, then chapters)
    book.spine = [toc_page] + epub_chapters

    # Write to file
    epub.write_epub(str(output_path), book)


def _build_hierarchical(book: epub.EpubBook, parts: List[Dict], style: epub.EpubItem, output_path: Path):
    """Build hierarchical EPUB structure with parts and sub-chapters."""

    # Create chapters for all parts
    epub_chapters = []
    chapter_idx = 0

    for part in parts:
        part_chapters = []
        for chapter in part['chapters']:
            c = epub.EpubHtml(
                title=chapter['title'],
                file_name=f'chapter_{chapter_idx+1:03d}.xhtml',
                lang='zh-CN'
            )
            c.content = chapter['content']
            c.add_item(style)
            book.add_item(c)
            epub_chapters.append(c)
            part_chapters.append(c)
            chapter_idx += 1
        # Store reference to part chapters
        part['epub_chapters'] = part_chapters

    # Create hierarchical Table of Contents page
    toc_html = '<h1>目录</h1><nav epub:type="toc">'
    chapter_idx = 0
    for part in parts:
        toc_html += f'<h2>{part["title"]}</h2><ol>'
        for chapter in part['chapters']:
            toc_html += f'<li><a href="chapter_{chapter_idx+1:03d}.xhtml">{chapter["title"]}</a></li>'
            chapter_idx += 1
        toc_html += '</ol>'
    toc_html += '</nav>'

    toc_page = epub.EpubHtml(
        title='目录',
        file_name='toc.xhtml',
        lang='zh-CN'
    )
    toc_page.content = toc_html
    toc_page.add_item(style)
    book.add_item(toc_page)

    # Create hierarchical table of contents for navigation
    book.toc = []
    for part in parts:
        section = epub.Section(part['title'])
        book.toc.append((section, part['epub_chapters']))

    # Add navigation
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Define spine (TOC first, then chapters)
    book.spine = [toc_page] + epub_chapters

    # Write to file
    epub.write_epub(str(output_path), book)

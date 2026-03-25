"""Main converter module for Markdown to Kindle AZW3."""
import subprocess
import sys
from pathlib import Path
from typing import Optional


def check_calibre() -> bool:
    """Check if Calibre ebook-convert is available."""
    try:
        result = subprocess.run(
            ['ebook-convert', '--version'],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def convert_to_kindle(
    input_path: Path,
    output_path: Optional[Path] = None,
    keep_epub: bool = False
) -> Path:
    """Convert markdown file or folder to Kindle AZW3 format."""

    # Check Calibre
    if not check_calibre():
        raise RuntimeError(
            "Calibre not found. Install with: brew install --cask calibre"
        )

    # Determine output paths
    if output_path is None:
        output_path = input_path.with_suffix('.azw3') if input_path.is_file() \
            else input_path.parent / f"{input_path.name}.azw3"

    # Create temporary EPUB
    epub_path = output_path.with_suffix('.epub')

    # Step 1: Generate EPUB using md2epub CLI
    print(f"Generating EPUB: {epub_path}")
    md2epub_path = Path(__file__).parent.parent.parent / 'md2epub'

    result = subprocess.run(
        [sys.executable, '-m', 'src', str(input_path), str(epub_path)],
        cwd=str(md2epub_path),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"EPUB generation failed: {result.stderr}")
    print(result.stdout.strip())

    # Step 2: Convert to AZW3
    print(f"Converting to AZW3: {output_path}")
    result = subprocess.run([
        'ebook-convert',
        str(epub_path),
        str(output_path)
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Warning: {result.stderr}")

    # Step 3: Clean up intermediate EPUB
    if not keep_epub and epub_path.exists():
        epub_path.unlink()
        print(f"Cleaned up: {epub_path}")

    return output_path

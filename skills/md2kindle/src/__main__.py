"""Command line entry point for md2kindle."""
import sys
import argparse
from pathlib import Path

from .converter import convert_to_kindle, check_calibre


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to Kindle AZW3')
    parser.add_argument('input', help='Input markdown file or folder')
    parser.add_argument('output', nargs='?', help='Output AZW3 path (optional)')
    parser.add_argument('--keep-epub', action='store_true',
                        help='Keep intermediate EPUB file')

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None

    if not input_path.exists():
        print(f"Error: Input not found: {input_path}")
        sys.exit(1)

    if not check_calibre():
        print("Error: Calibre not found.")
        print("Install with: brew install --cask calibre")
        sys.exit(1)

    try:
        result = convert_to_kindle(input_path, output_path, args.keep_epub)
        print(f"Successfully created: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

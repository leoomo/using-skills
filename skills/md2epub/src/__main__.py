"""Command line entry point for md2epub."""
import sys
import argparse
from pathlib import Path

from .converter import convert_file, convert_folder


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to EPUB')
    parser.add_argument('input', help='Input markdown file or folder')
    parser.add_argument('output', nargs='?', help='Output EPUB path (optional)')

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None

    if not input_path.exists():
        print(f"Error: Input not found: {input_path}")
        sys.exit(1)

    try:
        if input_path.is_file():
            result = convert_file(input_path, output_path)
        else:
            result = convert_folder(input_path, output_path)
        print(f"Successfully created: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

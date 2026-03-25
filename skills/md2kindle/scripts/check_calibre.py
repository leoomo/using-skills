#!/usr/bin/env python3
"""Check if Calibre is installed and ebook-convert is available."""
import subprocess
import sys


def check_calibre():
    """Check if Calibre ebook-convert is available."""
    try:
        result = subprocess.run(
            ['ebook-convert', '--version'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✓ Calibre is installed")
            print(f"  {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass

    print("✗ Calibre not found")
    print("\nInstall with:")
    print("  macOS:   brew install --cask calibre")
    print("  Linux:   sudo apt install calibre")
    print("  Windows: choco install calibre")
    return False


if __name__ == '__main__':
    sys.exit(0 if check_calibre() else 1)

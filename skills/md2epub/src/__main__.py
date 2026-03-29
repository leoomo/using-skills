"""Command line entry point for md2epub (with Kindle email support)."""
import sys
import argparse
from pathlib import Path

from .converter import convert_file, convert_folder
from .email_sender import send_to_kindle, DEFAULT_SMTP_SERVER, DEFAULT_SMTP_PORT


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to EPUB (with Kindle support)')
    parser.add_argument('input', help='Input markdown file or folder')
    parser.add_argument('output', nargs='?', help='Output EPUB path (optional)')

    # Conversion options
    conv_group = parser.add_argument_group('Conversion Options')
    conv_group.add_argument('--no-images', action='store_true',
                            help='Skip downloading and embedding external images')

    # Email options
    email_group = parser.add_argument_group('Email Options')
    email_group.add_argument('--send', action='store_true',
                             help='Send to Kindle via email after conversion')
    email_group.add_argument('--kindle-email',
                             default='leoomo_1984@kindle.com',
                             help='Kindle email address')
    email_group.add_argument('--sender-email',
                             default='zengleo@163.com',
                             help='Your email address')
    email_group.add_argument('--password',
                             default='NTiYWrMuPrqGT9Uc',
                             help='Email password or authorization code')
    email_group.add_argument('--smtp-server',
                             default=DEFAULT_SMTP_SERVER,
                             help=f'SMTP server (default: {DEFAULT_SMTP_SERVER})')
    email_group.add_argument('--smtp-port', type=int,
                             default=DEFAULT_SMTP_PORT,
                             help=f'SMTP port (default: {DEFAULT_SMTP_PORT})')

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None

    if not input_path.exists():
        print(f"Error: Input not found: {input_path}")
        sys.exit(1)

    try:
        # Convert to EPUB
        if input_path.is_file():
            result = convert_file(input_path, output_path, no_images=args.no_images)
        else:
            result = convert_folder(input_path, output_path, no_images=args.no_images)
        print(f"Successfully created: {result}")

        # Send to Kindle if requested
        if args.send:
            print(f"\nSending to Kindle: {args.kindle_email}")
            send_to_kindle(
                file_path=result,
                kindle_email=args.kindle_email,
                sender_email=args.sender_email,
                sender_password=args.password,
                smtp_server=args.smtp_server,
                smtp_port=args.smtp_port,
            )

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

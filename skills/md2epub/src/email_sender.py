"""Email sender module for sending EPUB files to Kindle."""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from pathlib import Path
from typing import Optional
import ssl

try:
    import certifi
    _CERTIFI_AVAILABLE = True
except ImportError:
    _CERTIFI_AVAILABLE = False


# Default configuration
DEFAULT_SMTP_SERVER = "smtp.163.com"
DEFAULT_SMTP_PORT = 465


def send_to_kindle(
    file_path: Path,
    kindle_email: str,
    sender_email: str,
    sender_password: str,
    subject: Optional[str] = None,
    body: Optional[str] = None,
    smtp_server: str = DEFAULT_SMTP_SERVER,
    smtp_port: int = DEFAULT_SMTP_PORT,
) -> bool:
    """
    Send EPUB file to Kindle via email.

    Args:
        file_path: Path to the EPUB file
        kindle_email: Kindle email address (e.g., xxx@kindle.com)
        sender_email: Your email address
        sender_password: Email password or app-specific password
        subject: Email subject (optional)
        body: Email body text (optional)
        smtp_server: SMTP server address
        smtp_port: SMTP server port

    Returns:
        True if sent successfully
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = kindle_email
    msg['Subject'] = subject or f"Kindle Document: {file_path.stem}"

    # Add body
    msg.attach(MIMEText(body or "Document for Kindle", 'plain'))

    # Attach file
    with open(file_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            'attachment',
            filename=file_path.name
        )
        msg.attach(part)

    # Send email
    try:
        if _CERTIFI_AVAILABLE:
            context = ssl.create_default_context(cafile=certifi.where())
        else:
            context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, kindle_email, msg.as_string())
        print(f"Successfully sent to Kindle: {kindle_email}")
        return True
    except smtplib.SMTPAuthenticationError:
        raise RuntimeError(
            "SMTP authentication failed. Please check your email and password. "
            "For 163.com, you may need to use an authorization code instead of your login password."
        )
    except smtplib.SMTPException as e:
        raise RuntimeError(f"SMTP error: {e}")
    except Exception as e:
        raise RuntimeError(f"Failed to send email: {e}")

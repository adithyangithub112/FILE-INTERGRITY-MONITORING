import smtplib
from email.mime.text import MIMEText
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER = os.getenv("ALERT_EMAIL")
PASSWORD = os.getenv("ALERT_EMAIL_PASSWORD")
RECEIVER = os.getenv("ALERT_EMAIL_RECEIVER")


def send_email(file_path, old_hash, new_hash):
    body = f"""
File Integrity Alert

File: {file_path}
Old Hash: {old_hash}
New Hash: {new_hash}
"""

    msg = MIMEText(body)
    msg["Subject"] = "🚨 File Integrity Alert"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER, PASSWORD)
        server.send_message(msg)

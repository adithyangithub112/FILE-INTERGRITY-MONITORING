import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER = os.getenv("ALERT_EMAIL")
PASSWORD = os.getenv("ALERT_EMAIL_PASSWORD")
RECEIVER = os.getenv("ALERT_EMAIL_RECEIVER")


def send_email(subject, body):
    if not all([SENDER, PASSWORD, RECEIVER]):
        print("[ERROR] Email environment variables not set")
        return

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER, PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"[ERROR] Email sending failed: {e}")

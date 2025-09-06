import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import aiosmtplib

from app.core.config.settings import settings

async def send_email(subject: str, body: str, email_to: str):
    message = MIMEMultipart()
    message["From"] = settings.MAIL_FROM
    message["To"] = email_to
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    await aiosmtplib.send(
        message,
        hostname=settings.MAIL_SERVER,
        port=settings.MAIL_PORT,
        start_tls=settings.MAIL_TLS,
        username=settings.MAIL_USERNAME,
        password=settings.MAIL_PASSWORD,
    )

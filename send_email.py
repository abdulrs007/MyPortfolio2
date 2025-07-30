import smtplib
import ssl
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(message):
    """
    Send email using Gmail SMTP with Streamlit secrets for deployment
    """
    try:
        # Email configuration
        host = "smtp.gmail.com"
        port = 465

        # Get credentials from Streamlit secrets (for cloud deployment)
        try:
            username = st.secrets["gmail"]["username"]
            password = st.secrets["gmail"]["app_password"]
            receiver = st.secrets["gmail"]["receiver"]
        except KeyError:
            # Fallback to environment variables (for local development)
            import os
            username = os.getenv("GMAIL_USERNAME")
            password = os.getenv("GMAIL_APP_PASSWORD")
            receiver = os.getenv("GMAIL_RECEIVER", username)

        # Validate credentials
        if not username or not password:
            raise ValueError("Email credentials not configured properly.")

        # Create SSL context
        context = ssl.create_default_context()

        # Parse the message to extract subject if present
        lines = message.split('\n')
        subject = "New Portfolio Contact"
        body_start = 0

        # Check if first line contains subject
        if lines[0].startswith("Subject:"):
            subject = lines[0].replace("Subject:", "").strip()
            body_start = 1

        # Get the message body (skip empty lines)
        body = "\n".join(lines[body_start:]).strip()

        # Create proper email message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = receiver
        msg['Subject'] = subject

        # Attach body to email
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        # Convert to string
        text = msg.as_string()

        # Send email
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, text)

        return True

    except Exception as e:
        print(f"Error sending email: {str(e)}")
        raise e
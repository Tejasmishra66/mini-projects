import pandas as pd
import base64
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_emails(service, excel_path, logger):
    """
    Sends plain text emails without attachments.
    """
    df = pd.read_excel(excel_path)

    for index, row in df.iterrows():
        to = str(row['Email']) if not pd.isna(row['Email']) else ""
        subject = str(row['Subject']) if not pd.isna(row['Subject']) else ""
        body = str(row['Body']) if not pd.isna(row['Body']) else ""

        if not to or not subject or not body:
            print(f"⚠️ Skipping row {index+2}: Missing required fields.")
            logger(df, index, "Skipped: Missing fields")
            continue

        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

        try:
            service.users().messages().send(userId="me", body={'raw': raw}).execute()
            print(f"✅ Sent to {to}")
            logger(df, index, "Sent")
        except Exception as e:
            print(f"❌ Failed to send to {to}: {e}")
            logger(df, index, f"Failed: {e}")

def send_emails_with_attachments(service, excel_path, attachment_paths, logger):
    """
    Sends emails with attachments.
    """
    df = pd.read_excel(excel_path)

    for index, row in df.iterrows():
        to = str(row['Email']) if not pd.isna(row['Email']) else ""
        subject = str(row['Subject']) if not pd.isna(row['Subject']) else ""
        body = str(row['Body']) if not pd.isna(row['Body']) else ""

        if not to or not subject or not body:
            print(f"⚠️ Skipping row {index+2}: Missing required fields.")
            logger(df, index, "Skipped: Missing fields")
            continue

        message = MIMEMultipart()
        message['to'] = to
        message['subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        for path in attachment_paths:
            if not os.path.exists(path):
                print(f"⚠️ Attachment not found: {path}")
                continue

            filename = os.path.basename(path)
            with open(path, 'rb') as f:
                part = MIMEApplication(f.read(), Name=filename)
                part['Content-Disposition'] = f'attachment; filename="{filename}"'
                message.attach(part)

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

        try:
            service.users().messages().send(userId="me", body={'raw': raw}).execute()
            print(f"✅ Sent to {to} with attachments")
            logger(df, index, "Sent with attachments")
        except Exception as e:
            print(f"❌ Failed to send to {to}: {e}")
            logger(df, index, f"Failed: {e}")
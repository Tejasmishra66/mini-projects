from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import base64

def create_message_with_attachment(to, subject, body, file_path):
    message = MIMEMultipart()
    message['to'] = to
    message['subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with open(file_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='pdf')
        attachment.add_header('Content-Disposition', 'attachment', filename=file_path)
        message.attach(attachment)

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}
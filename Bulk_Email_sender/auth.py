from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    # Load credentials and launch local server for OAuth
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)
    print("✅ Gmail service authenticated successfully.")
    return service

if __name__ == "__main__":
    service = authenticate_gmail()
    # You can now call functions to send emails using `service`
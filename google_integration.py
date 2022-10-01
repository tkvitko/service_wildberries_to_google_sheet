from __future__ import print_function

import logging
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SPREADSHEET_ID = '1z3FWhfV9pOSJ2qViqZdwRBoL30bI1a9HmIIHYqyJ8GI'   # development
SPREADSHEET_ID = ''  # prod
RANGE_NAME = 'A1:B3'


def add_to_sheet(data):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    resource = {
        "majorDimension": "ROWS",
        "values": data
    }
    spreadsheet_id = SPREADSHEET_ID
    range_ = RANGE_NAME

    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()


if __name__ == '__main__':
    # Testing
    values_to_add = [['Next', 'Nexxxxxt'], ['Bruce', 'Willis']]
    add_to_sheet(values_to_add)

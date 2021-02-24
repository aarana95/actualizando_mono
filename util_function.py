from oauth2client.service_account import ServiceAccountCredentials
import gspread


def connect_to_sheet(key_file):
    # Authorize the API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(key_file, scope)
    client = gspread.authorize(creds)

    return(client)

def open_sheet(client, sheet_name):
    sheet = client.open(sheet_name)

    return(sheet)

def open_worksheet(sheet, name):

    sheet_instance = sheet.worksheet(name)

    return(sheet_instance)
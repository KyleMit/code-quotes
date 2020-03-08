from __future__ import print_function
from googleapiclient.discovery import build
from creds import get_creds

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1Bjm9VDXDBOd2krO4hUDNPtyU4iCPZhlWGtMqVhl6Jwk'
quotesRange = 'Sheet1!A1:3'

def main():
    """ Retrieves cell data via Google Sheets API"""

    # get credentials either cached or requested
    creds = get_creds()

    apiService = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = apiService.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=quotesRange).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            # Print each each line
            print(row[0])

# run in main file
if __name__ == '__main__':
    main()
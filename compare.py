import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load credentials from credentials.json file
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('Business Interruption').sheet1

# Read the number and net_premium from the Google Sheet
number_from_sheet = int(sheet.acell('B11').value.replace(',',''))
net_premium =  float(sheet.acell('B6').value.replace(',',''))

# Compare the numbers
if net_premium > number_from_sheet:
    print(f"Net Premium {net_premium} is greater than the number {number_from_sheet} mentioned in the Google Sheet")
elif net_premium < number_from_sheet:
    print(f"Net Premium {net_premium} is lesser than the number {number_from_sheet} mentioned in the Google Sheet")
else:
    print(f"Net Premium is {net_premium} equal to the number {number_from_sheet} mentioned in the Google Sheet")
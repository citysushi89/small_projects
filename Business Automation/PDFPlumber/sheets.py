import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("varda-credentials.json", scopes) #access the json key you downloaded earlier
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("varda_instructors_testing") #open sheet

all_cells = sheet.named_range(('A1:D1'))

for cell in all_cells:
    print(cell.value)


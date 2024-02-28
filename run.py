import gspread
from google.oauth2.service_account import Credentials

import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-pp3')

# possible_words = SHEET.worksheet('words')


# select word
words = possible_words.get_all_values()
print(words)

word = random.choice(words)
print(word[0].lower())

def select_random_word():

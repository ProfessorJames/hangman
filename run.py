import gspread
from google.oauth2.service_account import Credentials

import random
from logo import logo

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-pp3')

def select_random_word():
    words = SHEET.worksheet('Words').get_all_values()
    word = random.choice(words)
    return word[0].lower()

def display_logo():
    print(logo)

def display_welcome_message():
    print("""
    Welcome to Hangman!!!
    Guess letters to uncover the secret word.
    Try to guess the word before the hangman is fully drawn.
    Win by guessing the word correctly, or lose if the hangman is completed.
    """)

def play_game():
    display_logo()
    display_welcome_message()

    word = select_random_word()
    print(word)
    word_length = len(word)

    display = ''
    for _ in range(word_length):
        display += '_'

    print(display)

play_game()
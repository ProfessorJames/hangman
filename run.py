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


# Main game functionality

def select_random_word():
    """
    This function retrieves all the words from a worksheet named 'Words' in a Google Sheets
    document accessed via the global variable SHEET. It then selects a random word from
    the list of words and returns it in lowercase.
    """
    words = SHEET.worksheet('Words').get_all_values()
    word = random.choice(words)
    return word[0].lower()

def display_logo():
    """
    This function prints the logo stored in the variable `logo`. 
    """
    print(logo)

def display_welcome_message():
    """
    This function prints a welcome message for the Hangman game, providing players
    with instructions on how to play. It explains the objective of the game, which
    is to guess letters to uncover the secret word before the hangman is fully drawn.
    """
    print("""
    Welcome to Hangman!!!
    Guess letters to uncover the secret word.
    Try to guess the word before the hangman is fully drawn.
    Win by guessing the word correctly, or lose if the hangman is completed.
    """)

def get_letter_input():
    """
    Prompts the user to enter a single letter and returns it in lowercase.
    A valid input is a single alphabetical character. If the user
    provides an invalid input (such as multiple characters or non-alphabetical
    characters), an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input("Please enter a letter: ").lower()
        if len(user_input) == 1 and user_input.isalpha():
            return(user_input) 
        else:
            print("Please enter only one letter.")

def check_guessed_letter_in_word(letter, word, display):
    """
    """
    for i in range(len(word)):
        if word[i] == letter:
            display[i] = letter
    print(''.join(display))
    return display


def play_game():
    display_logo()
    display_welcome_message()

    word = select_random_word()
    print(word)
    word_length = len(word)

    display = ['']
    for _ in range(word_length-1):
        display += '_'

    print(''.join(display))

    while True:
        # Create function to get user input, validate user input i.e. only one letter, not a digit, keep asking user to enter a letter until letter is inputted.
        guess = get_letter_input()

        # create a function to check letter guessed bu user is in the word and update the display
        check_guessed_letter_in_word(guess, word, display)

play_game()
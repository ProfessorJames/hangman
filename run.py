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

def get_letter_input(letters_guessed):
    """
    Prompts the user to enter a single letter and returns it in lowercase.
    A valid input is a single alphabetical character. If the user
    provides an invalid input (such as multiple characters or non-alphabetical
    characters), an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input("Please enter a letter: ").lower()
        if len(user_input) == 1 and user_input.isalpha():
           if user_input in letters_guessed:
                print("You have picked that letter already. Please choose a new letter.")
           else:
                return user_input
        else:
            print("Please enter only one letter.")

def play_game():
    
# set up game variables
    game_over = False
    lives = 3
    guessed_letters = []
    word = select_random_word()
    word_length = len(word)

# display logo and welcome message
    display_logo()
    display_welcome_message()

# print word while developing. Delete before deployment.
    print(word)

# display a blank space for each letter in secret word
    display = []
    for _ in range(word_length):
        display += '_'
    print(''.join(display))

    while not game_over:
       
        guess = get_letter_input(guessed_letters)
        guessed_letters.append(guess)
        
        # create a function to check letter guessed by user is in the word and update the display? Shoudl this be refactored??
        for i in range(len(word)):
            if word[i] == guess:
              display[i] = guess
        if guess not in word:
            lives -= 1
            if lives > 0:
                print(f"Incorrect! Attempts remaining: {lives}")
    
        if lives == 0:
            game_over = True
            print('Incorrect!\nGame over. You lose.')
        else:
                print(''.join(display))
                print(f"Guessed letters: {guessed_letters}")

        # if display == word:
            # print('You guessed the word correctly. You win!')
        if ''.join(display) == word:
            print('Congratulations. You guessed the word correctly. You win.')
            game_over = True
     
play_game()

# functionality
# edit input so gives message if non letter is entered. could possibly use regex.
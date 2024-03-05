import gspread
from google.oauth2.service_account import Credentials

import random
import os
import time
from logo import green_logo
from graphics import GRAPHICS
from Colours import Colours

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-pp3')

def pause(seconds):
    """
    Pauses the program execution for a specified duration in seconds.   
    """
    time.sleep(seconds)

def clear_console():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def select_random_word():
    """
    This function retrieves all the words from a worksheet named 'Words' in a Google Sheets
    document accessed via the global variable SHEET. It then selects a random word from
    the list of words and returns it in lowercase.
    """
    try:
        words = SHEET.worksheet('Words').get_all_values()
        if words is None:
            raise ValueError
        word = random.choice(words)
        return word[0].lower()
    except gspread.exceptions.APIError as e:
        raise gspread.exceptions.APIError(f"Error accessing Google Sheets API: {e}")
        return None
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return None    

def display_logo(color_logo):
    """
    This function prints the logo stored in the variable `logo`. 
    """
    print(color_logo)

def display_welcome_message():
    """
    This function prints a welcome message for the Hangman game, providing players
    with instructions on how to play. It explains the objective of the game, which
    is to guess letters to uncover the secret word before the hangman is fully drawn.
    """
    print("""
=====================================================
|                 Welcome to Hangman!               |
=====================================================
|      Guess one letter at a time to reveal         |    
|      the secret word.                             |                                        
|      Try to guess the word before the hangman     |
|      is fully drawn.                              |             
|      Win by guessing the word correctly, or lose  |
|      if the hangman is completed.                 |
=====================================================
""")

def get_letter_input(letters_guessed):
    """
    Prompts the user to enter a single letter and returns it in lowercase.
    A valid input is a single alphabetical character. If the user
    provides an invalid input (such as multiple characters or non-alphabetical
    characters), an error message is displayed, and the user is prompted again.
    """
    while True:
        user_input = input("Guess a letter: ").lower()
        if len(user_input) == 1 and user_input.isalpha():
           if user_input in letters_guessed:
                print("You have picked that letter already. Guess a new letter.")
           else:
                return user_input
        else:
            print("You can only guess one letter at a time.")

def user_wants_to_play_game():
    """
    Function that asks the user if they want to play a game of Hangman. 
    User enters 'y' if they want to play, or enters 'n' otherwise.
    """
    while True:
        user_input = input("Do you want to play Hangman? (Enter 'y' for Yes, or 'n' for No): ").lower()
        if user_input == 'y':
            return True
        elif user_input =='n':
            print('Goodbye.')
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# create a function to check letter guessed by user is in the word and update the display? Shoudl this be refactored??
        ## function to check if guess_in_word

#Create display function
def create_word_display(len_word):
    """
    Creates a display for a word, where each character is represented by an underscore '_'.
    """
    word_display = []
    for _ in range(len_word):
        word_display += '_'
    print(''.join(word_display))
    return word_display

def update_display(word, guess, display):
    """
    Updates the display if the guessed letter is in the word.
    """
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess

# def incorrect_guess():
#         print(GRAPHICS[-lives])
#         lives -= 1
#         print(f"Incorrect! Attempts remaining: {lives}")

def display_guessed_letters(guessed_letters_list):
    """
    Displays the letters guessed by the user.
    """
    print("Guessed letters:", ", ".join(guessed_letters_list))

def handle_incorrect_guess(num_lives, graphics):
    num_lives -= 1
    print(graphics[-num_lives])
    print(f"Incorrect! Attempts remaining: {num_lives}")
    return num_lives

def check_if_player_loses(num_lives, graphics):
    if num_lives == 0:
        print(graphics[-num_lives])
        print('Incorrect!\nGame over. You lose.')
        return True
    return False

def play_game(): 
# set up game variables
    game_over = False
    lives = 6
    guessed_letters = []
    word = select_random_word()
    word_length = len(word)
    display = create_word_display(word_length)

    while not game_over:
       
        guess = get_letter_input(guessed_letters)
        guessed_letters.append(guess)
              
        if guess in word:
            update_display(word, guess, display)
        else:
            lives = handle_incorrect_guess(lives, GRAPHICS)
        
        game_over = check_if_player_loses(lives, GRAPHICS)

# display logo and welcome message
display_logo(green_logo)
display_welcome_message()

pause(2)

while user_wants_to_play_game():
    play_game()
    pause(2)
    # clear_console()
    display_logo(green_logo)
    display_welcome_message()


import gspread
from google.oauth2.service_account import Credentials

import random
import re
import os
import time
from logo import green_logo
from graphics import GRAPHICS
from colours import Colours

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
    This function retrieves all the words from a worksheet named 'Words'
    in a Google Sheets document accessed via the global variable SHEET.
    It then selects a random word from the list of words and returns
    it in lowercase.
    """
    try:
        words = SHEET.worksheet('Words').get_all_values()
        if words is None:
            raise ValueError
        word = random.choice(words)
        return word[0].lower()
    except gspread.exceptions.APIError as e:
        raise gspread.exceptions.APIError(f"""Error accessing Google
        Sheets API: {e}""")
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
    This function prints a welcome message for the Hangman game,
    providing players with instructions on how to play. It explains
    the objective of the game, which is to guess letters to uncover
    the secret word before the hangman is fully drawn.
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
        if re.match("^[a-zA-Z]$", user_input):
            if user_input in letters_guessed:
                print("You have picked that letter already.")
                print("You must guess a new letter.")
            else:
                return user_input
        else:
            print("Invalid input. Please enter a single letter.")


def user_wants_to_play_game():
    """
    Function that asks the user if they want to play a game of Hangman.
    User enters 'y' if they want to play, or enters 'n' otherwise.
    """
    while True:
        user_input = input("Do you want to play Hangman? "
                           "(Enter 'y' for Yes, or 'n' for No): ").lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            print('Goodbye.')
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def create_word_display(len_word):
    """
    Creates a display for a word, where each character is
    represented by an underscore '_'.
    """
    word_display = []
    for _ in range(len_word):
        word_display += '_'
    print(''.join(word_display))
    return word_display


def update_word_display(game_word, user_guess, word_display):
    """
    Updates the display if the guessed letter is in the word.
    """
    for i in range(len(game_word)):
        if game_word[i] == user_guess:
            word_display[i] = user_guess
    print(''.join(word_display))


def display_guessed_letters(guessed_letters_list):
    """
    Displays the letters guessed by the user.
    """
    print("Guessed letters:", ", ".join(guessed_letters_list))


def handle_incorrect_guess(num_lives, graphics, word_display):
    if num_lives > 1:
        print(graphics[-num_lives])
        num_lives -= 1
        print(f"Incorrect! Attempts remaining: {num_lives}")
        return num_lives
    else:
        num_lives -= 1
        return num_lives


def check_if_player_wins(game_display, game_word):
    if ''.join(game_display) == game_word:
        print('Congratulations. You guessed the word correctly. You win.')
        return True
    return False


def check_if_player_loses(num_lives, graphics):
    if num_lives == 0:
        print(graphics[-1])
        print('Incorrect!\nGame over. You lose.')
        return True
    return False


def play_game():
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
            update_word_display(word, guess, display)
        else:
            lives = handle_incorrect_guess(lives, GRAPHICS, display)
            update_word_display(word, guess, display)

        if check_if_player_wins(display, word):
            game_over = True
        elif check_if_player_loses(lives, GRAPHICS):
            game_over = True
        else:
            display_guessed_letters(guessed_letters)


display_logo(green_logo)
display_welcome_message()

pause(2)

while user_wants_to_play_game():
    play_game()
    pause(2)
    clear_console()
    display_logo(green_logo)
    display_welcome_message()

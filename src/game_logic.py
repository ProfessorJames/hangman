import gspread
import random
import re
from src.google import SHEET


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
    """
     Handles an incorrect guess by displaying appropriate graphics and updating the number of lives.
    """
    if num_lives > 1:
        print(graphics[-num_lives])
        num_lives -= 1
        print(f"Incorrect! Attempts remaining: {num_lives}")
        return num_lives
    else:
        num_lives -= 1
        return num_lives


def check_if_player_wins(game_display, game_word):
    """
    Checks if the player has won the game by comparing the displayed word with the actual word.
    """
    if ''.join(game_display) == game_word:
        print('Congratulations. You guessed the word correctly. You win.')
        return True
    return False


def check_if_player_loses(num_lives, graphics):
    """
    Checks if the player has lost the game by running out of lives.
    """
    if num_lives == 0:
        print(graphics[-1])
        print('Incorrect!\nGame over. You lose.')
        return True
    return False

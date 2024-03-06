import random
import re
from src.art import green_logo, GRAPHICS, display_logo, display_welcome_message
from src.utils import pause, clear_console
from src.google import SHEET
from src.colours import Colours
from src.game_logic import select_random_word, get_letter_input, user_wants_to_play_game 
from src.game_logic import create_word_display, update_word_display, display_guessed_letters
from src.game_logic import handle_incorrect_guess, handle_incorrect_guess, check_if_player_loses, check_if_player_wins


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

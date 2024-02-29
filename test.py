import os
import time


print("this is a string")
time.sleep(2)
os.system('clear')


def ask_to_play_game():
    """
    Function that asks the user if they want to play a game of Hangman. 
    User enters 'y' if they want to play, or enters 'n' otherwise.
    """
    while True:
        user_input = input("Do you want to play Hangman? (Enter 'y' for Yes, or 'n' for No)").lower()
        if user_input == 'y':
            return True
        elif user_input =='n':
            print('Maybe next time. Have a nice day.')
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")
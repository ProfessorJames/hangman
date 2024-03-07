import time
import os


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

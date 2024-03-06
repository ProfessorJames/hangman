from src.colours import Colours

logo = """
 __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   
 | || |  /   \ | \| |  / __||  \/  | /   \ | \| |  
 | __ |  | - | | .` | | (_ || |\/| | | - | | .` |  
 |_||_|  |_|_| |_|\_|  \___||_|__|_| |_|_| |_|\_| 
 ------------------------------------------------
"""

green_logo = Colours.colourize(logo, 'green')

GRAPHICS = ['''
        ____   
       /    |
      |     
      |    
      |    
      |
  =============''','''
  
        ____   
       /    |
      |     O
      |    
      |    
      |
  ============= ''','''
        ____   
       /    |
      |     O
      |    / 
      |    
      |
  ============= ''','''
        ____   
       /    |
      |     O
      |    /|\\
      |    
      |
  ============= ''','''
        ____   
       /    |
      |     O
      |    /|\\
      |    / 
      |
  =============''','''
        ____   
       /    |
      |     O
      |    /|\\
      |    / \\
      |
  ============='''
]

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

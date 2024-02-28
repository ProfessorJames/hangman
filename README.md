# Hangman

Welcome to the Python CLI Hangman Game! 
This command-line game is a fun and interactive way to test your vocabulary and word-guessing skills. Challenge yourself or play with friends to see who can guess the hidden word correctly.
### Deployed website [Hangman](xxx/ 'Hangman')

# How to Play
Hangman is a word-guessing game where one player (the computer) thinks of a word, and the other player (you) tries to guess that word by suggesting letters. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game) 'Hangman').

Here's how to play:

- Setup: The computer randomly selects a word and displays it as underscores for each letter (e.g., "_ _ _ _ _ _ _").

- Guessing: You start by guessing one letter at a time. If the guessed letter is correct, it's revealed in the word. If incorrect, the computer keeps track of incorrect guesses.

- Objective: Your goal is to guess the word before the computer completes drawing the hangman figure.

- Win or Lose: You win if you guess the word correctly. The computer wins if it completes the hangman figure before you guess the word.

- Strategy: Start with common vowels, avoid repeating incorrect guesses, and pay attention to the hangman figure's progress.

Enjoy playing Hangman against the computer in our Python CLI game!
# Features

## Existing Features
- Word Selection: 
 The game randomly selects a word from a predefined list of words for the player to guess.
- Guessing: The player can guess letters one by one to reveal the hidden word.
- Incorrect Guess Tracking: The game keeps track of incorrect guesses and displays a hangman figure using ASCII art as the game progresses.
- Win/Lose Conditions: The game ends when the player correctly guesses the word or makes too many incorrect guesses (hangman is fully drawn).
- Word Reveal: After the game ends, the hidden word is revealed, and the player is given the option to play again.
## Future Features

## Data Model
The data model includes integration with Google Sheets using the Google Drive API and the gspread library in Python.
Authentication and authorization mechanisms are implemented to securely access the designated Google Spreadsheet. 
The Hangman game utilizes a designated Google Spreadsheet to store the words used in the game.
Each word is stored in a separate cell within the spreadsheet.
The data model includes functionalities to retrieve word data from the Google Spreadsheet programmatically using the gspread library.
When a new game is started the programme fetches the word data from the spreadsheet.
For each game session, the data model randomly selects a word from the retrieved list of words.
It then randomly selects a word from the retrieved list to be used in the current game session.


# Testing 
# Deployment

# Credits
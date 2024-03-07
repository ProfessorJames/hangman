# Hangman

Welcome to the Python CLI Hangman Game! 
This command-line game is a fun and interactive way to test your vocabulary and word-guessing skills. Challenge yourself or play with friends to see who can guess the hidden word correctly.

### Deployed website [Hangman](https://pp3-hangman-prof-james-512b326abe7e.herokuapp.com/ 'Hangman')

![Welcome screen](docs/images/welcome_screen.png)

## Table of Contents
* [Purpose](#purpose)
* [UX](#ux "UX")
    * [User Goals](#user-goals "User Goals")
    * [User Stories](#user-stories "User Stories")
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
         * [Requirements](#requirements)
         * [Expectations](#expectations)
* [How to Play](#how-to-play)
* [Planning](#planning)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Incorrect Guess Tracking](#incorrect-guess-tracking)
* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Programs, frameworks, libraries](#programs-frameworks-libraries-and-tools)
* [Testing](#testing)
   * [UX Testing](#ux-testing)
   * [Automated Testing](#automated-testing)
      * [Code Validation](#code-validation)
* [Bugs](#bugs)
  - [Unfixed-Bugs](#unfixed-Bugs)
* [Deployment](#deployment)
* [Credits](#credits)

## Purpose

The purpose of this programme is to make an interactive Hangman CLI game for users to play.

This programme is developed to demonstrate competency in python programming and is for educational purposes.

# UX

## User Goals
* Instructions on how to play the game.
* Know when it's the users go
* Knowledge of the game's outcome, whether it's a win or loss.
* Continual feedback throughout the game

## User Stories
* As a user, I want clear guidance on how to play the game.
* As a user, I want to be prompted when to guess.
* As a user, I want the ability to enter letters to guess the hidden word.
* As a user, I want feedback on my performance after each guess.
* As a user, I want to be informed of the game's outcome (win, or lose).

## Site owners Goals
* Present clear instructions to the user.
* Offer feedback on the user's performance.
* Ensure validation for expected user inputs.

## User Requirements and Expectations

### Requirements
* Ensure a single-page layout for straightforward navigation.
* Offer ongoing feedback on performance throughout the game.
* Provide a clear indication of the game's start and end.
* Implement input validation.
* Deliver feedback on the user's input throughout the game rounds.

### Expectations
* I expect to have the rules of the game explained to me 
* I expect to know when the game starts and finishes
* I expect input validation to ensure accurate letter guesses 
* I expect to receive feedback on my accuracy in guessing letters
* I expect to receive feedback on how many lives are remaining
* I expect to receive feedback on letters that have been guessed previously
* I expect visual cues indicating the position of guessed letters within the word to enhance my gameplay experience.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# How to Play
Hangman is a word-guessing game where one player (the computer) thinks of a word, and the other player (you) tries to guess that word by suggesting letters. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game) 'Hangman').

Here's how to play:

- Setup: The computer randomly selects a word and displays it as underscores for each letter (e.g., "_ _ _ _ _ _ _").

- Guessing: You start by guessing one letter at a time. If the guessed letter is correct, it's revealed in the word. If incorrect, the computer keeps track of incorrect guesses.

- Objective: Your goal is to guess the word before the computer completes drawing the hangman figure.

- Win or Lose: You win if you guess the word correctly. The computer wins if it completes the hangman figure before you guess the word.

- Strategy: Start with common vowels, avoid repeating incorrect guesses, and pay attention to the hangman figure's progress.

Enjoy playing Hangman against the computer in our Python CLI game!

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Planning

Initially I planned out the game going through each of the possible steps that could be involved in the game. This was to give me a better understanding of how the game should funtion programatically.

The game was broken down into steps that would be required to navigate through the game. This was an iterative process. The steps were documented. 

![Initial Planningwelcome screen](docs/images/planning.png)

# Features

## Existing Features
### Welcome screen
* When the game loads the player sees the Hangman logo. The logo has been created using ascii art, a welcome message and instructions on how to play the game are displayed.
* The user is asked if they want to play Hangman and prompted to enter 'y' for Yes or 'n' for No.

![welcome screen](docs/images/welcome_screen.png)

### Input validation
* The player input is validated. If the user does not enter either 'y' or 'n' they are prompted to enter a correct option.

![welcome screen validation](docs/images/welcome_validation.png)

### User selects 'n'
* If the user enters 'n' the game ends and a goodbye message is printed to the screen.

![welcome screen goodbye](docs/images/welcome_goodbye.png)

### User selects 'y'
* If the user enters 'y' the game begins. 
* The programme makes a call to the Google Spreadsheet where various words are saved. 
* The programme randomly selects a word from a predefined list of words for the player to guess. 
* The programmes displays a blank space for each letter in the word (e.g. '________').

![welcome screen yes](docs/images/welcome_yes.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

### Guessing 
* The player can guess letters one by one to reveal the hidden word.
* If the letter guessed by the player is a letter in the word, the display be will be updated with occureneces of that letter. 
* The programme will only accept a single alphanumeric character (a through z). 
* If the user doesn't enter a single alphanumeric character they will be asked to enter a single letter. 
* If the user has already entered a letter in a previous guess, they will be asked to enter a new letter.
* The letters that the user has guessed are displayed
 on the screen.

![guess validation](docs/images/guess_validation.png)

## Incorrect Guess Tracking: 
* The game keeps track of incorrect guesses and displays a hangman figure using ASCII art as the game progresses.
* The player has 6 lives when the game starts. Each time a player guesses incorrectly they lose a life and the hangman art is updated and displayed.

### Incorrect Guess One
![incorrect guess one](docs/images/incorrect_guess1.png)
### Incorrect Guess Two
![incorrect guess two](docs/images/incorrect_guess2.png)
### Incorrect Guess Three
![incorrect guess three](docs/images/incorrect_guess3.png)
### Incorrect Guess Four
![incorrect guess four](docs/images/incorrect_guess4.png)
### Incorrect Guess Five
![incorrect guess five](docs/images/incorrect_guess5.png)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Win/Lose Conditions: 
* The game ends when the player either correctly guesses the word or makes too many incorrect guesses (hangman is fully drawn).

## Player Loses
* When the player runs out of lives the game ends.
* The completed hangman graphic is displayed along with a message telling thh user their letter chocie was incorrect and the game is over.

![incorrect guess six](docs/images/incorrect_guess6.png)

* This message is displayed for a number of seconds, after which the console is cleared and the game is loaded again. 
* The welcome screen is loaded and the player has the option to start a new game.

![welcome screen](docs/images/welcome_screen.png)

## Player Wins

* When the player guesses all letters in the word they have won and the game ends.
* The completed word is displayed along with a message telling the user they have guessed the word correctly and they have won the game.

![Player wins](docs/images/player_wins.png)

* This message is displayed for a number of seconds, after which the console is cleared and the game is loaded again. 
* The welcome screen is loaded and the player has the option to start a new game.

![welcome screen](docs/images/welcome_screen.png)

## Future Features

* Difficulty levels: Implement different difficulty levels (easy, medium, hard) with varying word lengths, timer or limited guesses for a more challenging experience.
* Hint system: Allow players to use hints to reveal a letter in the word, at the cost of lives.
* Theme selection: Provide different themes or categories for word selection (e.g., animals, countries, movies) to add variety to gameplay.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Flowchart

![Flowchart](docs/images/flowchart_hangman.png)


## Data Model
* The data model includes integration with Google Sheets using the Google Drive API and the gspread library in Python.
* Authentication and authorization mechanisms are implemented to securely access the designated Google Spreadsheet. 
* The Hangman game utilizes a designated Google Spreadsheet to store the words used in the game.
* Each word is stored in a separate cell within the spreadsheet.
* The data model includes functionalities to retrieve word data from the Google Spreadsheet programmatically using the gspread library.
* When a new game is started the programme fetches the word data from the google spreadsheet.
* For each game session, the data model randomly selects a word from the retrieved list of words.
* The data model then randomly selects a word from the retrieved list to be used in the current game session.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Technologies used

### Languages
* [Python](https://www.python.org/)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript 'JS'): Used in Code Institutes' Python Template to generate the workspace for the project
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML 'HTML'): Used in Code Institutes' Python Template to generate the workspace for the project
* [Markdown](https://en.wikipedia.org/wiki/Markdown): Used for content of README file

### Programs, frameworks, libraries and tools
* [Drawio](https://app.diagrams.net/):  Used to create a flowchart during the planning stage 
* [Python](https://www.python.org/): Used to provide functionality to the site.
* [Google Drive](https://developers.google.com/drive): Used to process requests to a google sheet stored on google drive
* [Google Sheets](https://www.google.com/sheets/about/): Used to host application data.
* [Gitpod](https://www.gitpod.io): Used to create the code and content for the repository.
* [Git](https://git-scm.com/): Used to provide version control (to commit and push code to the repository). 
* [Github](https://github.com/): Used to host the repository.
* [Heroku](https://www.heroku.com/): Used to deploy and host the live app.
* [Code Institute's Python Template](https://github.com/Code-Institute-Org/p3-template): Used to generate the workspace for the project.
* [Code Institute's PEP8 Validator](https://pep8ci.herokuapp.com//): Used to enusre python code complies with pep8.
- [Markdown Tables Generator](https://www.tablesgenerator.com/ 'Markdown Tables Generator'): Used to generate markdown table for the project.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Python Packages Used

* [GSpread](https://pypi.org/project/gspread/): Used to manipulate data in google sheets.
* [time](https://docs.python.org/3/library/time.html): Used to pause execution of programme.
* [os](https://docs.python.org/3/library/os.html): Used to clear the terminal.
* [re](https://docs.python.org/3/library/re.html): Used to validate input.
* [random](https://docs.python.org/3/library/random.html): Used to randomly select word.


[Back to top](#contents)


# Testing 

* Testing was essential to ensure the project functions correctly and meets the desired user experience. 
* The app was manually tested in Chrome, Safari and Firefox on Windows.

The following testing was conducted throughout the development of the project:

### Testing User Stories

| User Stories                                                             | Achieved By                                                                                                                                                                                                                                                                                                                      | Test Status |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| As a user, I want clear guidance on how to play the game.                | Instructions on how to play the game are displayed on the welcome screen                                                                                                                                                                                                                                                         | Pass        |
| As a user, I want to be prompted when the programme is ready for me to guess a letter.             | User is promted to guess a letter when the programme is ready                                                                                                                                                                                                                                                                    | Pass        |
| As a user, I want the ability to enter letters to guess the hidden word. | User is promted to guess a letter when the programme is ready                                                                                                                                                                                                                                                                    | Pass        |
| As a user, I want feedback on my performance after each guess.           | Programme provides feedback to user after each letter guess. If letter is in word the blanks spaces are filled in where that letter is present in the word. If letter is not in word the hangman graphic is displayed. Letters guessed already are also displayed along with number of lives remaining in case of incorrect guess | Pass        |

### UX Testing

| Requirements & Expectations | Implemented | Tested | Comments
| ------------ | ----------- | ------ | --------
|Single page layout | Yes | Yes | Provided by Code Institute template
|Offer ongoing feedback on performance throughout the game | Yes | Yes | Various feedback is provided  depending on the user input, letters guessed, lives remaining etc.
| Provide a clear indication of the game's start and end | Yes | Yes | Text and graphics displayed to user to signal both the beginning and end of the game, and also game outcome if user has won or lost.
|Implement input validation to minimize errors.| Yes | Yes | Validation on all inputs and feedback also provided to user to prompt next action
| Deliver feedback on the user's input throughout the game rounds. | Yes | Yes | Continual updates to the user on the letters they have chosen, which letters are in the secret word, how many attempts remaining. Feedback is provided by text and graphically.

\
&nbsp;
[Back to top](#table-of-contents)
\
&nbsp;

* I've conducted tests to verify the project's ability to handle invalid inputs, including numbers or strings containing numbers.

* Testing has been performed on both Gitpod and Code Institute's Heroku Terminal to ensure comprehensive validation of functionality.
<details>
 <summary>Testing Results</summary>

 Welcome Validation
![welcome validation](docs/images/welcome_validation.png)
 Guess Validation
![guess validation](docs/images/guess_validation.png)
 Incorrect Guesses
![Incorrect Guess 1](docs/images/incorrect_guess1.png)
![Incorrect Guess 2](docs/images/incorrect_guess2.png)
![Incorrect Guess 3](docs/images/incorrect_guess3.png)
![Incorrect Guess 4](docs/images/incorrect_guess4.png)
![Incorrect Guess 5](docs/images/incorrect_guess5.png)
![Incorrect Guess 6](docs/images/incorrect_guess6.png)
Correct Guesses
![Correct Guess](docs/images/player_wins.png)

</details>

## Automated testing
**[PEP 8](https://pep8ci.herokuapp.com//) - Python Validation**
* All custom python files were run through the Code Institute PEP8 validator. 
* No errors were detected.

<details>
 <summary>PEP8 Testing Results</summary>

 run.py
![run.py](docs/validation/pep8_run.png)
 game_logic.py
![game_logic.py](docs/validation/pep8_game_logic.png)
 utils.py
![utils.py](docs/validation/pep8_utils.png)
 google.py
![google.py](docs/validation/pep8_google.png)
 colours.py
![colours.py](docs/validation/pep8_colours.png)
 art.py
![art.py](docs/validation/pep8_art.png)
</details>

## Bugs
* All known bugs within the project have been resolved. Each bug identified during the development phase was thoroughly analyzed, and appropriate solutions were implemented to address them.

### Solved Bugs
* During development, an issue arose where the display was showing one more blank space than the actual number of letters in the word to be guessed. Initially, this issue was fixed by updating the range to be one less than the length of the word. However, this was an inccorect approach which was revealed during testing. Subsequently the code was refactored and the error was removed. 
* During development, it was noticed that a user could enter the same letter more than once when attempting to guess the word. To improve the user experience and prevent duplicate guesses, the input function has been updated. Now, a letter can only be guessed by the user once, ensuring a smoother gameplay flow. If the user enters a duplicate letter, they are prompted to guess a new letter. A message is displayed asking them to input a different letter.
* An error was encountered occasionally, with the message: "File 'run.py', line 138, in play_game, print(GRAPHICS[counter]), IndexError: list index out of range." This error likely occurred due to the counter variable incrementing incorrectly when the same letter was picked multiple times. To address this, the code has been refactored to eliminate the need for a counter variable. This modification ensures smoother gameplay, especially when a player selects a letter they have already chosen.
* There was an issue with the check_if_player_loses function. If a player ran out of lives and lost the game the incorrect graphic was being displayed. The code was updated so that if a user runs out of lives the last item in the GRAPHICS array is displayed (the completed hangman). This way when a player runs out of lives and the game is over the correct graphic is displayed.
* When the app was deployed on Heroku, an error message occasionally appeared indicating that the logo file contained incorrect escape characters. This error stemmed from the backslash (\) characters used in the Hangman logo within the art.py file. To resolve this issue, the backslashes were appropriately escaped within the Hangman logo string, ensuring that Python interpreted them as literal characters rather than escape characters.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Deployment

## Deployment and Development

* The project was developed using [Gitpod](https://www.gitpod.io/#get-started) to create the code and files required.
* The project files, code, and information are hosted by [Github](https://github.com/).

### Deploying the App

The deployment of the project was done using [Heroku](https://www.heroku.com/) through the following steps.

1. Log in to Heroku or create an account if necessary.
2. Click on the button labeled "New" from the dashboard in the top right corner and select the "Create new app" option in the drop-down menu.
3. Enter a unique name for the application and select the region you are in.
   * For this project, the unique name is "pp3-hangman-prof-james" and the region selected is Europe.
4. Click on "create app".
5. Navigate to the settings tab and locate the "Config Vars" section and click "Reveal config vars".
6. Add a config var (if the project uses creds.json file.)
   * In the "KEY" field:
      * enter "CREDS" in capital letters.
   * In the "VALUE" field:
      * copy and paste the contents of your creds.json file and click "Add".
7. Scroll to the "Buildpacks" section and click "Add buildpack".
8. Select Python and save changes.
9. Add another buildpack and select Nodejs then save changes again.
10. Ensure that the python buildpack is above the Nodejs buildpack.
11. Navigate to the "Deploy" section by clicking the "Deploy" tab in the top navbar.
12. Select "GitHub" as the deployment method and click "Connect to GitHub".
13. Search for the GitHub repository name in the search bar.
14. Click on "connect" to link the repository to Heroku.
15. Scroll down and click on "Deploy Branch".
16. Once the app is deployed, Heroku will notify you and provide a button to view the app.

NB - If you wish to rebuild the deployed app automatically every time you push to GitHub, you may click on "Enable Automatic Deploys".

[Back to Top](#table-of-contents)

### Forking The Repository

This can be done to create a copy of the repository. The copy can be viewed and edited without affecting the original repository.

To fork the repository through GitHub, take the following steps:
1. In the "hanmgman" repository, click on the "fork" tab in the top right corner.
2. Click on "create fork" to fork the repository.

### Cloning The Repository

To clone the repository through GitHub:

1. In the repository, select the "code" tab located just above the list of files and next to the gitpod button.
2. Ensure HTTPS is selected in the dropdown menu.
3. Copy the URL under HTTPS.
4. Open Git Bash in your IDE of choice.
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type "git clone" and paste the URL that was copied from the repository.
7. Press the "enter" key to create the clone.

[Back to Top](#table-of-contents)

### APIs 
In order for the app to function properly, APIs need to be set up and connected. In particular, the following APIs were used for this project:

* Google Drive API.
   * This helps with getting credentials to access the files within google drive.
* Google Sheets API.
   * This is the API for the google sheets where the data is stored for the program.

I followed the steps in a video from the [Code Institute](https://codeinstitute.net/global/) Love Sandwiches project on how to set up and connect APIs. The link to this video is [here](https://www.youtube.com/watch?v=WTll5p4N7hE).

[Back to Top](#table-of-contents)

# Credits

* [Simen Daehlin](https://github.com/Eventyret "Simen Daehlin") for advice and direction
* [Tony118g](https://github.com/Tony118g/doctor-diary) for detailed descriptions used in deployment section
* For regex pattern to identify only single character entered by user, https://bobbyhadz.com/blog/python-input-only-accept-one-character

## Code
- Information on Python3 [Python Documentation](https://docs.python.org/3/).
- Information on Google Spreadsheet API was sourced from [Gspread Documentation](https://docs.gspread.org/en/latest/index.html).
- Inffo on Regex pattern to identify only single character entered by user: [Regex pattern](https://bobbyhadz.com/blog/python-input-only-accept-one-character)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;
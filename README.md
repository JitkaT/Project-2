# Project 2
Python project in English

# Bulls & Cows

Your task is to create a program that simulates the game Bulls and Cows. After displaying the introductory text to the user, the guessing of the secret four-digit number can begin. The program must meet the following requirements:

At the beginning, describe your file with a header so that we can contact you more easily:

  """
projekt_2.py: second project for Engeto Online Python Academy

author: Petr Svetr

email: petr.svetr@gmail.com

discord: Petr Svetr#4490
"""

Import necessary modules.

The program greets the user and displays the introductory text.

The program creates a secret 4-digit number (the digits must be unique and cannot start with 0).

The player guesses the number. The program alerts if the input is shorter or longer than 4 digits, contains duplicates, starts with zero, or contains non-numeric characters.

The program evaluates the user's guess.

The program then displays the number of bulls (if the user guesses both the number and its position) and cows (if the user guesses only the number but not its position). The returned evaluation must consider singular and plural in the output. Thus, 1 bull and 2 bulls (same for cow/cows).

The code should be organized into short and clear functions.

Introductory text:

Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
Example game with the number 2017:
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
1234
0 bulls, 2 cows
-----------------------------------------------
6147
1 bull, 1 cow
-----------------------------------------------
2417
3 bulls, 0 cows
-----------------------------------------------
2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's {amazing, average, not so good, ...}

The program can do more. You can add, for example:

    Counting the time it takes for the user to guess the secret number
    Keeping statistics of the number of guesses for each game


"""

projekt_2.py: the second project to the Engeto Online Python Akademie

author: Jitka Tichá

email: jitka.ticha@gmail.com

discord: jitkaticha

"""
import random

def creating_random_number():
    """This function creates a 4-digit random number from the interval 0 to 9, which cannot start with 0 and must be unique."""
    while True:
        random_number = random.sample(range(10), 4)
        if random_number[0] != 0:
            break
    return ''.join(f"{digit}" for digit in random_number)

def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")

    secret_number = creating_random_number()
    attempts = 0
    #This game gives user 20 attempts, but this total number can be changed.
    max_attempts = 20 
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}, enter your guess: ")
        
        if not input_check(guess):
            print("Invalid input! Please enter a 4-digit number with unique digits, not starting with 0.")
            continue
        
        bulls, cows = bulls_and_cows_game (guess, secret_number)
        print(f"Attempt: {guess}, Bulls: {bulls}, Cows: {cows}")
        
        if bulls == 4:
            print(f"Correct, you have guessed the right number {secret_number} in {attempts + 1} guesses!")
            break
        
        attempts += 1
    else:
        print(f"You have lost! The secret number was {secret_number}.")

def input_check(input_from_user):
    """This function checks whether the input from the user contains 4 digits, does not start with 0, and is unique."""
    if len(input_from_user) != 4:
        return False
    if not input_from_user.isdigit():
        return False
    if input_from_user[0] == 0:
        return False
    if len(set(input_from_user)) != 4:
        return False
    return True

def bulls_and_cows_game (user_guess, secret_number):
    """This function shows the count of bulls and cows by comparing the user's input (the user_guess) with the secret number."""
    bulls = 0
    cows = 0
    
    # Counting bulls
    for i in range(4):
        if user_guess[i] == secret_number[i]:
            bulls += 1

    # Counting cows
    for i in range(4):
        if user_guess[i] != secret_number[i] and user_guess[i] in secret_number:
            cows += 1

    return bulls, cows

if __name__ == "__main__":
    main()

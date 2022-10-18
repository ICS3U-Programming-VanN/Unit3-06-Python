#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 17, 2022
# This program asks the user to try and guess the randomly generated number between 0-9
# and displays a message depending on if they get it right or not
# This program contains exception handling


import random


def main():
    # Tries to get a number and then cast it into an integer
    try:
        # Declared CORRECT_ANSWER constants
        CORRECT_ANSWER = random.randint(0, 9)

        # Asks the user for their guess
        user_guess_string = input("Guess the number (1-9): ")

        # Attempts to cast user input into integer
        user_guess = int(user_guess_string)

    # Handles exceptions from user input
    except Exception:
        print(
            f"{user_guess_string} is not an integer. Please restart the program and try again."
        )

    # If there are not any exceptions
    else:

        # IF the user guesses the number correctly
        if user_guess == CORRECT_ANSWER:
            print("You guessed the number correctly!")

        # IF the user guesses the number incorrectly
        else:
            print(
                f"You guessed the number incorrectly! The correct answer was: {CORRECT_ANSWER}"
            )

    # Displays message regardless of exceptions
    finally:
        print("\nThanks for playing!")


if __name__ == "__main__":
    main()

# quest_25_number_wizard.py
import random

# pick a random number between 1 and 100, this is what the player has to guess
secret_number = 67
guess = None

# keep asking until they get it right
while guess != secret_number:
    guess = int(input("Guess the number (1-100): "))

    # tell them which way to go next
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")

print("You found it.")

# quest_29_code_breaker.py
secret_code = 42
attempts = 0
max_attempts = 3
solved = False

# stop either when they run out of tries or they get it right
while attempts < max_attempts and not solved:
    guess = int(input("Guess the secret code: "))
    attempts += 1

    if guess == secret_code:
        print("Correct. You cracked the code.")
        solved = True
    else:
        print("Wrong guess.")

if not solved:
    print(f"Out of attempts. The code was {secret_code}.")

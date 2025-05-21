# Modified guessing game with error handling
import random
print("Starting guessing game...")
number_to_guess = random.randint(1, 10)
guess = 0

while guess != number_to_guess:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number.")
        else:
            print(f"Try again! Your guess was {guess}")
    except ValueError:
        print("Please enter a valid number!")
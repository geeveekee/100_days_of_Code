import random
import sys


def game(lives):
    while (lives):
        lives -=1
        guess = int(input("Guess the number: "))
        if lives == 0:
            print(f"You have run out of guesses, the number was {chosen_num}")
            sys.exit()
        elif guess>chosen_num:
            print("Too high.\nGuess again")
        elif guess<chosen_num:
            print("Too low.\nGuess again")
        elif guess == chosen_num:
            print("Yay!, you guessed the number correctly!")
            sys.exit()
        print(f"You have {lives} attempts to guess the number")
        game(lives)
    return

print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
chosen_num = random.randint(1, 100)

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == 'hard':
    attempts = 5
    print(f"You have {attempts} attempts to guess the correct no.")
    game(attempts)
else:
    attempts = 10
    print(f"You have {attempts} attempts to guess the correct no.")
    game(attempts)



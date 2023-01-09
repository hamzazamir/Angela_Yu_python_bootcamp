import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, random_number, turns):
    if guess > random_number:
        print("You guessed too high. Try again")
        return turns - 1
    elif guess < random_number:
        print("You guessed too low. Try again")
        return turns - 1
    else:
        print(f"Well done you got it, the number is {guess}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    print(random_number)

    turns = set_difficulty()
    guess = 0

    while guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, random_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return


game()

import random
from rps_ascii_art import *

game_images = [rock, paper, scissors]

use_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))

if use_choice >= 3 or use_choice < 0:
    print("You typed an invalid number, you lose")
else:
    print(game_images[use_choice])

    computer_choice = random.randrange(0,3)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if use_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 2 and use_choice == 0:
        print("You lose")
    elif computer_choice > use_choice:
        print("You lose")
    elif use_choice > computer_choice:
        print("You win!")
    elif computer_choice == use_choice:
        print("It's a draw")

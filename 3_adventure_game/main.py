from multiprocessing.spawn import spawn_main


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!!")
print("Your mission is to find the treasure.")

first_choice = input(
    "You're at the cross road. Where do you want to go? Type 'left' or 'right' ").lower()

if first_choice == "left":
    second_choice = input(
        "You have arrived at a river. Do you want to swim or wait for a boat? Type 'swim' or 'wait' ").lower()
    if second_choice == "wait":
        third_choice = input(
            "The boat has taken you to three doors. Which door do you want to open? Type 'one', 'two' or 'three' ").lower()
        if third_choice == "one":
            print("Well done you found the treasure!!")
        elif third_choice == "two":
            print("The second room is full of fire. Game Over")
        elif third_choice == "three":
            print("The third room is empty. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game Over.")

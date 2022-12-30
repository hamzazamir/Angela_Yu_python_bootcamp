def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def devide(num_1, num_2):
    return num_1 / num_2


def times(num_1, num_2):
    return num_1 * num_2


continue_calculating = True

choices = ("+", "-", "/", "*")

while continue_calculating == True:

    user_choice = input(
        f"\nWhich function would you like to use {choices}: \n")

    num_1 = int(input("\nPlease enter the first number: \n"))
    num_2 = int(input("\nPlease enter the second number: \n"))

    if user_choice == "+":
        print(num_1, " + ", num_2, " = ", add(num_1, num_2))
    elif user_choice == "-":
        print(num_1, "-", num_2, "=", subtract(num_1, num_2))
    elif user_choice == "*":
        print(num_1, "*", num_2, "=", times(num_1, num_2))
    elif user_choice == "/":
        print(num_1, "/", num_2, "=", devide(num_1, num_2))
    else:
        print("Invalid input")

    check_to_continue = input(
        "Would you like to do another calculation? yes or no\n").lower()

    if check_to_continue == "no":
        continue_calculating = False

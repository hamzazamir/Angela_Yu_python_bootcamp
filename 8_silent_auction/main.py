from ascii_art import logo
import os

print(logo)
print("Welcome to the esecret auction program.")


user_bids = {}
bidding_finished = False


def find_highest_bid(user_bids):
    hightest_bid = 0
    winner = ""

    for bidder in user_bids:
        bid_amount = user_bids[bidder]
        if bid_amount > hightest_bid:
            hightest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of £{hightest_bid}")


while bidding_finished == False:
    user_name = input("What is your name?\n")
    user_bid = int(input("What is your bid?\n£"))

    user_bids.update({user_name: user_bid})

    should_continue = input(
        "Are there other users who want to bid? yes or no\n").lower()

    if should_continue == "no":
        bidding_finished = True
        find_highest_bid(user_bids)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

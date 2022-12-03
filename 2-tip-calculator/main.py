print("Welcome to the tip calculator.")

bill = float(input("What as the total bill? "))

number_of_people = int(input("How many people to split the bill? "))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

total_bill = tip_percentage / 100 * bill + bill

bill_per_person = total_bill / number_of_people
round(bill_per_person, 2)
bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person needs to pay £{bill_per_person}")



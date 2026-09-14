# Trong Tran
# 9/14/2026
# P1HW2 Assignment
# Program use to get input from user about travel

print("This program calculates your travel expense:")
print("Welcome to Travel Cal: ")

# Get user to enter budget value
expense_budget = int(input("Enter your budget here: "))

# Get user to enter the travel destination
Travel_destination = input("Enter your travel destination: ")

# Get user to enter expense for gas 
Gasses_fuel =int(input("Enter the amount that you will spend on gas: "))

# Get user to enter the expense of on accommodation
living_place = int(input("How much will you spend on accomodation: "))

# Get user to enter how much they spend on food
food_bud = int(input("How much money will you spend on food: "))
print()
print()

# Display travel expense 
print("-------Travel Expenses-------")
print()
# Display user travel location
print("Location:",Travel_destination )
print()
# Display the intial expense budget
print("Starting Budget:",expense_budget)
print()
# Display the gas money information get from user
print("Gas:",Gasses_fuel)
# Display the accomodation cost
print("Accomodation:",living_place)
# Display food expenses from the user
print("Food:",food_bud)

# Calculate total expenses
total_expenses = Gasses_fuel + living_place + food_bud
# Calculate the remaining expense 
answer = expense_budget - total_expenses
# Display result
print()
print("Remaining Balance:",answer)
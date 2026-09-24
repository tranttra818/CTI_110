# Trong Tran
# 9/24/2026
# P2HW1 Assignment
# Program calculate travel expense budget and then formatting output to the user

print("This program calculates your travel expense:")
print("Welcome to Travel Cal: ")

# Get user to enter budget value
expense_budget = float(input("Enter your budget here: "))

# Get user to enter the travel destination
Travel_destination = input("Enter your travel destination: ")

# Get user to enter expense for gas 
Gasses_fuel =float(input("Enter the amount that you will spend on gas: "))

# Get user to enter the expense of on accommodation
living_place = float(input("How much will you spend on accommodation: "))

# Get user to enter how much they spend on food
food_bud = float(input("How much money will you spend on food: "))

print()
print()

# Display travel expense 
# print("-" * 15 + "Travel Expenses" + "-" *15)
# print(f"{"-" * 15}Travel Expenses{"-" * 15}")
# print("----------- Travel Expenses------------")
print("-------------Travel Expenses------------")

print()
# Display user travel location
print(f"{'Location:':<22}{Travel_destination:<22}")
# Display the initial expense budget
print(f"{'Starting Budget:':<22}${expense_budget:<22,.2f}")
# Display the gas money information get from user
print(f"{'Fuel:':<22}${Gasses_fuel:<22,.2f}")
# Display the accommodation cost
print(f"{'Accommodation:':<22}${living_place:<22,.2f}")
# Display food expenses from the user
print(f"{'Food:':<22}${food_bud:<22,.2f}")

# print a format dash line
print("-" * 40)

# Calculate total expenses
total_expenses = Gasses_fuel + living_place + food_bud
# Calculate the remaining expense 
answer = expense_budget - total_expenses
# Display result
print()
print(f"{'Remaining Balance:':<22}${answer:<22,.2f}")


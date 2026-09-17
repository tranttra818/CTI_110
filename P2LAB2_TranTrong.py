# Trong Tran
# 9/17/2026
# P2LAB2 
# Use a dictionary to determine amount of fuel needed from user inputs

# Create the dictionary - cars are the keys and mpgs are the values
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Select only the keys
keys = cars.keys()

#  Display keys to user
print()
print(keys)
# Get a car choice from the user
car_choice = input("Enter a car to see it's mpg: ")

# Using car_choice, pull the associated mpg from the dictionary
mpg = cars[car_choice]

# Display car choice and mpg back to the user
print()
print(f"The {car_choice} gets {mpg} mpg.")

# Get the miles to drive fro the users as a float
print()
miles = float(input(f"How many miles will you will drive the {car_choice}? "))

# Calculate the gallons of gas needed
gallons = miles/mpg

# Display 
print()
print(f"{gallons:.2f} gallons of gas are need to drive the {car_choice} {miles} miles.")



















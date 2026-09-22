# Trong Tran
# 9/22/2026
# P2HW2
# Create a program that ask user input to calculate their grade

# Get 6 input from the user for the test grade in each module - Step 2
module1 =float(input("Please enter the test grade for module 1: "))
module2 =float(input("Please enter the test grade for module 2: "))
module3 =float(input("Please enter the test grade for module 3: "))
module4 =float(input("Please enter the test grade for module 4: "))
module5 =float(input("Please enter the test grade for module 5: "))
module6 =float(input("Please enter the test grade for module 6: "))

# Create a List to hold the these test grade input - Step 3
module_test_grade = [module1, module2, module3, module4, module5, module6]

# Calculation the test result using input from user to calculate the data - Step 4

# Using the sum function to calculate the total of grade first
total_grade = sum(module_test_grade)

# Using the len function to calculate the average of grade by using the list
average = sum(module_test_grade) / len(module_test_grade)

# Now after finish calculation is Display and format the result - step 5 
print()
print("--------------Result--------------")

# Print the test grade result, and sum and average with spacing format
print(f"The Lowest Grade:         {min(module_test_grade):.2f} ")
print(f"The Highest Grade:        {max(module_test_grade):.2f} ")
print(f"The Sum of Grade:         {total_grade:.2f}")
print(f"The Average:              {average:.2f} ")

# print space format 
print("------------------------------------------")
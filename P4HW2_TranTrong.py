# Trong Tran
# 10/22/2026
# P4HW2
# Program that calculate employee input and using loop to determine if the user want to run the program again

# request employee information

total_employees = 0
total_overtime = 0
total_regular = 0
total_gross = 0

name = input("Enter the employee's name or 'Done' to quit: ")

while name != "done":
    total_employees += 1
    hoursWorked = float(input("How many hours did " + name + " work this week? "))

    payRate = float(input("What is " + name + "'s hourly pay rate? "))

    #evalute overtime

    if hoursWorked >40 :

        #calculate overtime
        overtimeHours = hoursWorked - 40
        #Calculate overPay
        overPay = overtimeHours * (payRate * 1.5)

        #calculate salary for reg hours

        regPay = 40 * payRate

        # calculate gross pay

        grossPay = regPay + overPay
    else:

        overPay = 0
        overtimeHours = 0

        regPay = hoursWorked * payRate
        grossPay = regPay
    total_overtime += overPay
    total_regular += regPay
    total_gross += grossPay
    # Display output

    print("------------------------------------------------------------------------------")
    print("Employee name:  ",name,"\n")

    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('--------------------------------------------------------------------------------------------------')
    print(f'{hoursWorked:<15}{payRate:<12.2f}{overtimeHours:<12}{overPay:<20.2f}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')
    # Ask the user for the next employee or Done
    print()
    name = input("Enter another employee's name or 'Done' to quit: ").lower()

# loop breaks here. Display your totals below
print(f'{"The total number of employees enrered:":<45}{total_employees:<20}')
print(f'{"The total amount paid for overtime:":<45}${total_overtime:<20.2f}')
print(f'{"The total amount paid for regular hours:":<45}${total_regular:<20.2f}')
print(f'{"The total amount paid in gross:":<45}${total_gross:<20.2f}')

    

# Trong Tran
# 10/22/2026
# Use nested loop to validate user inputs
score_list = []
# Get number of scores from the user as int
num_of_scores = int(input("How many grades will you enter? "))

# Make a for loop that runs nums_of_scores times
for scores in range(1,num_of_scores + 1):
    input_score = float(input(f"Enter score #{scores}: "))
    
    # While loop that traps the user while input_score is invalid
    while input_score < 0 or input_score > 100:
        print()
        print("Invalid Score entered!!!!")
        print("Score should be between 0 and 100")
        # Ask them for a new value for input score
        input_score = float(input(f"Enter score #{scores} again: "))
    score_list.append(input_score)
    # Display Results
print(score_list)
print()
print()
print("---------------------Results----------------------")
print(f'{"The Lowest Score:":<30}{min(score_list):<20.2f}')
print(f'{"The Highest Score:":<30}{max(score_list):<20.2f}')
print(f'{"The Modified List:":<30}{score_list}')

# Calculate average then display score average
average = sum(score_list) / len(score_list)
print(f'{"The Score Average:":<30}{average:<20.2f} ')

# Using if/elif to determine the corresponding letter grade base on calculation of the average
if average >= 90:
    grade_letter = "A"
elif average >= 80:
    grade_letter = "B"
elif average >= 70:
    grade_letter = "C"
elif average >= 60:
    grade_letter = "D"
else:
    grade_letter = "F"
print(f'{"Grade            :":<30}{grade_letter:20}')
# print this dashes line as showing in assignment
print("------------------------------------------------------------")
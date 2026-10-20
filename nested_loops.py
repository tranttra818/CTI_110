# Use a nested loop to simulate a clock
# Loop can run 12 times for the hours

# Outer loop that run 12 times for the hours
for hour in range(1,13):
    #print(hour)
    # Inner loop that runs 60 times for the minutes
    for minute in range(0,60):
        if minute <= 9:
            print(f"{hour}:0{minute}")
        else:
            print(f"{hour}:{minute}")
        
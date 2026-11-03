# Define the main function
# The code for the entire program goes in the main

# calculate the cost corresponding to area value
def get_area_cost(area, cost):
    total_cost = area * cost
    return total_cost

# define a function that calculate the area
# It must accept 2 parameter - length and width
def get_area(length, width):
    area = length * width 
    return area 

def main():
    print("The program is running : )")
    # get user input for length and width
    length = float(input("Enter the length to calculate the area: "))
    width  = float(input("Enter the width to calculate the area: "))
    
    # Call the function to get area
    area = get_area(length,width)
    print(f"The area is {area} from inside the main.")
    
    cost = float(input("Enter the cost per unit: "))
    total_cost = get_area_cost(area,cost)
    
    print(f"The total cost is ${total_cost:,.2f}")

# Call the main function
if __name__ == "__main__":
    main()
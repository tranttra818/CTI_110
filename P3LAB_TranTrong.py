# Trong Tran
# 10/1/2026
# Use branching and functions to display coin combinations

money = float(input("Enter the amount of money: $"))
if money == 0.00:
    print("No change")

# Convert money to an integer
money_int = int(money * 100)

#print(money_int)
############################# DOLLARS ##########################
# Determine how many dollars are needed
dollars = money_int // 100
# Remove the dollars from money_int
money_int = money_int % 100
#print(f"Dollars: {dollars}")
#print(f"Leftover: {money_int}")



############################# QUARTERS ##########################
# Determine how many quarters are needed
quarters = money_int // 25
# Remove the quarters from money_int
money_int = money_int % 25
#print(f"Quarters: {quarters}")
#print(f"Leftover: {money_int}")



############################# DIMES ##########################
# Determine how many dimes are needed
dimes = money_int // 10
# Remove the dimes from money_int
money_int = money_int % 10
#print(f"Dimes: {dimes}")
#print(f"Leftover: {money_int}")



#############################  NICKELS ##########################
# Determine how many nickels are needed
nickels = money_int // 5
# Remove the nickels from money_int
money_int = money_int % 5
#print(f"Nickels: {nickels}")
#print(f"Leftover: {money_int}")


############################# PENNIES ##########################
# Determine how many pennies are needed
pennies = money_int // 1

#print(f"Pennies: {pennies}")
#print(f"Leftover: {money_int}")


# Define a function to show the coins only if needed
def show_coins(coin, coin_name):
    if coin > 0:
        if coin == 1:
            print(f"1 {coin_name}")
        if coin > 1:
            if coin_name == "Penny":
                print(f"{coin} Pennies")
            else:
                print(f"{coin} {coin_name}s")
            
# Call the function for each of the coins
show_coins(dollars, "Dollar")
show_coins(quarters, "Quarter")
show_coins(dimes, "Dime")
show_coins(nickels, "Nickel")
show_coins(pennies, "Penny")
















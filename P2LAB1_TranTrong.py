# Trong Tran
# 9/15/2026
# Calculate components of circle using pi from the math library

import math


# Get radius from user
radius = float(input("Enter the radius: "))

print()

# Calculate the diameter
diameter = 2 * radius

# Display the diameter using an f- string
print(f"The diameter of the circle is {diameter:.1f} ")

# Calculate the circumference
circumference = 2 * math.pi * radius

# Display circumference using the f-string
print(f"The circumference of the circle is {circumference:.2f}")

# Calculate the area
area = math.pi * math.pow(radius, 2)

# Display area with f-string
print(f"The area of the circle is {area:.3f}")


# Trong Tran
# 10/15/2026
# Use a for loop and a while loop to draw shapes

import turtle

# Set up the window and drawing object (turtle)
window = turtle.Screen()
timmy = turtle.Turtle()

timmy.pensize(4)
timmy.pencolor("blue")

# For loop to draw a square
for side in range(4):
    timmy.forward(200)
    timmy.right(90)
    
# while loop that draw a triangle
num = 1
while num <= 3:
    # Draw a side
    timmy.forward(200)
    timmy.left(120)
    
    # Increment num
    num = num + 1





# Keep Window open
window.mainloop()
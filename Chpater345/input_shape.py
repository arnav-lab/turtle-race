import turtle

# Create a turtle object
t = turtle.Turtle()

# Ask the user for input
shape = input("Enter the shape you want to draw (square or circle): ")

# Check the user input and draw the corresponding shape
if shape == "square":
    side_length = int(input("Enter the side length of the square: "))
    for i in range(4):
        t.forward(side_length)
        t.right(90)
elif shape == "circle":
    radius = int(input("Enter the radius of the circle: "))
    t.circle(radius)
else:
    print("Invalid shape! Please enter either 'square' or 'circle'.")

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
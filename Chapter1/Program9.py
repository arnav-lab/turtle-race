# Activity Hulk eyes

# Import turtle
import turtle

# Set the turtle screen(canvas)
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Creating a turtle object(pen)
t = turtle.Turtle()
t.shape("turtle")
#t.shape("triangle")
#t.shape("square")
#t.shape("classic")
#t.shape("arrow")

# Set the pen color
t.pencolor("red")

# Creating one eye of Hulk
# Set the color to red
t.color("red")
# Begin to fill color
t.begin_fill()
# Creating a circle with a radius of 50
t.circle(50)
# End-filling color
t.end_fill()
# Creating another circle with a radius of 80
t.circle(80)

# Using pen up
t.penup()

# Moving turtle in the forward direction
t.forward(250)
# Using pen down
t.pendown()

# Creating another eye of Hulk
# Set the color to red
t.color("red")
# Begin to fill color
t.begin_fill()
# Creating a circle with a radius of 50
t.circle(50)
# End-filling color
t.end_fill()
# Creating another circle with a radius of 80
t.circle(80)

screen.mainloop()
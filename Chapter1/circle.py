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

# Creating a circle with a radius of 50
t.circle(50)

screen.mainloop()
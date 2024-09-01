import turtle
# Fullscreen the canvas
# background color
turtle.bgcolor("lightblue")
#creating a turtle object with name "t" You can try any name
t=turtle.Turtle()
t.shape("turtle")
t.circle(50)
t.penup() #hiding pen movement
t.goto(0,-150) #goto(x = 0,y = -150)
t.pendown()
t.circle(50)
turtle.done()
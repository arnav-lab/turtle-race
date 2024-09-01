import turtle

t1 = turtle.Turtle()  #Creating a first turtle object.
t1.shape("turtle")
t1.circle(50)
t2 = turtle.Turtle()  #Creating a second turtle object.
t2.shape("triangle")
t2.color("red")
t2.penup()
t2.forward(200)
t2.pendown()
#Task: Draw a square using turtle t2
t2.forward(100)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(100)
t2.left(90)
t2.forward(100)
t2.left(90)
turtle.done()

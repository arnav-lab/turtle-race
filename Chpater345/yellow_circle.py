import turtle
turtle.bgcolor("black")
# Begin!
t = turtle.Turtle()
t.color("yellow")
t.fillcolor("yellow")
t.penup()
t.left(90)
t.forward(20)
t.right(90)
t.forward(100)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()
t.hideturtle()
turtle.done()
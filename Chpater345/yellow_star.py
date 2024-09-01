import turtle
# Begin!
t = turtle.Turtle()
t.shape("turtle")
t.color("yellow")
t.begin_fill()
for i in range(5):
    t.left(144)
    t.forward(100)
t.end_fill()
t.hideturtle()
turtle.done()
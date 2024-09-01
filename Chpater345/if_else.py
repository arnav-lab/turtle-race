import turtle
turtle.bgcolor("black")
# Begin!
t = turtle.Turtle()
t.color("red")
t.shape("turtle")
t.forward(50)
if t.xcor() > 50:
    t.color("red")
else:
    t.color("blue")
    t.forward(60)
if t.xcor() > 50:
    t.color("red")
else:
    t.color("blue")
turtle.done()
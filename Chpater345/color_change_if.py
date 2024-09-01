import turtle
turtle.bgcolor("lightgreen")
# Begin!
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.speed(1)
t.goto(-100,0)
if t.xcor()<0:
    t.color("red")
    t.goto(0,100)
if t.ycor()>0:
    t.color("blue")
    t.goto(100,0)
if t.xcor()>0:
    t.color("green")
    t.goto(0,-100)
if t.ycor()<0:
    t.color("purple")
turtle.done()
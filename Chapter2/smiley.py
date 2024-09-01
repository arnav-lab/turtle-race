import turtle
t=turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()
t.goto(-40,120)
t.pendown()
t.circle(20)
#Task: Make the other eye
t.penup()
t.goto(40,120)
t.pendown()
t.circle(20)

#Task1: Make Smiley using the knowledge from Activity 2.4
#Task2: Give the smiley face your fave color
t.penup()
t.goto(-40,50)
t.pendown()
t.forward(90)
t.hideturtle()
turtle.done()

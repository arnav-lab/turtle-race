import turtle
import time

from turtle import Turtle
from random import randint

turtle.setup(1.0, 1.0)
turtle.bgcolor("forestgreen")
turtle.up()
turtle.goto(200, 200)
turtle.down()
turtle.color("white", "black")
for i in range(10):
  turtle.begin_fill()
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(40)
  turtle.right(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.forward(40)
  turtle.up()
  turtle.backward(40)
  turtle.right(90)
  turtle.down()
  turtle.end_fill()
turtle.up()
turtle.home()
turtle.backward(100)
turtle.down()
turtle.hideturtle()

blue_turtle=Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300, 150)
blue_turtle.pendown()

red_turtle = Turtle()
red_turtle.color("red")
red_turtle.shape("turtle")
red_turtle.shapesize(1.5)
red_turtle.penup()
red_turtle.goto(-300, 50)
red_turtle.pendown()

yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300, -50)
yellow_turtle.pendown()

white_turtle = Turtle()
white_turtle.color("white")
white_turtle.shape("turtle")
white_turtle.shapesize(1.5)
white_turtle.penup()
white_turtle.goto(-300, -150)
white_turtle.pendown()

while blue_turtle.xcor() <= 200 and red_turtle.xcor(
) <= 200 and yellow_turtle.xcor() <= 200 and white_turtle.xcor() <= 200:
  blue_turtle.forward(randint(1, 10))
  red_turtle.forward(randint(1, 10))
  yellow_turtle.forward(randint(1, 10))
  white_turtle.forward(randint(1, 10))

if blue_turtle.xcor() > red_turtle.xcor() and blue_turtle.xcor(
) > yellow_turtle.xcor() and blue_turtle.xcor() > white_turtle.xcor():
  print("Blue turtle wins")
  blue_turtle.shapesize(2.5)
  turtle.write("Blue turtle wins", font=("Arial", 20, "bold"), align="center")

elif red_turtle.xcor() > blue_turtle.xcor() and red_turtle.xcor(
) > yellow_turtle.xcor() and red_turtle.xcor() > white_turtle.xcor():
  print("Red tuurtle wins")
  red_turtle.shapesize(2.5)
  turtle.write("Red turtle wins", font=("Arial", 20, "bold"), align="center")

elif yellow_turtle.xcor() > blue_turtle.xcor() and yellow_turtle.xcor(
) > red_turtle.xcor() and yellow_turtle.xcor() > white_turtle.xcor():
  print("Yellow turtle wins")
  yellow_turtle.shapesize(2.5)
  turtle.write("Yellow turtle wins", font=("Arial", 20, "bold"), align="center")

else:
  print("White turtle wins")
  white_turtle.shapesize(2.5)
  turtle.write("White turtle wins", font=("Arial", 20, "bold"), align="center")

turtle.done()

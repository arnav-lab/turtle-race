import turtle as t
import random

t.speed(0)
t.Screen().bgcolor('black')
t.setup(1000, 800)
t.color('black')
t.up()
t.backward(500)
t.right(90)
t.forward(400)
t.left(90)
t.down()
t.begin_fill()
t.color('#1d557d')  #037a8a #fireword bg color

for i in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(800)
    t.left(90)
t.end_fill()

t.up()
t.left(90)
t.forward(450)
t.right(90)
t.down()

t.begin_fill()
t.color('#036194')  #water color
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(450)
    t.right(90)
t.end_fill()

t.up()
t.right(90)
t.forward(200)
t.left(90)
t.down()

t.width(5)
t.color('silver')  # bride color
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(100)
    t.right(90)

for i in range(25):
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.right(90)

t.up()
t.right(90)
t.forward(105)
t.right(90)
t.down()

t.begin_fill()
t.color('black')  #075419 #b38b4b #gross color
for i in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

t.up()
t.right(90)
t.forward(200)
t.left(90)
t.forward(150)
t.down()

t.width(1)
t.begin_fill()  #Boat
t.color('black', '#806608')
t.forward(50)
t.right(45)
t.forward(50)
t.right(135)
t.forward(120)
t.right(180)
t.right(-45)
t.forward(50)
t.right(45)
t.end_fill()

t.up()
t.forward(600)
t.right(90)
t.forward(85)
t.left(90)
t.down()

t.begin_fill()  #2Boat
t.color('black', '#524f24')
t.forward(40)
t.right(45)
t.forward(30)
t.right(135)
t.forward(80)
t.right(180)
t.right(-45)
t.forward(30)
t.right(45)
t.end_fill()

t.up()
t.right(10)
t.goto(-400, 370)
t.down()
t.left(180)

t.begin_fill()
t.color('black', 'white')
t.shape()
t.right(90)
t.circle(50, 180)
t.backward(10)
t.left(180)
t.circle(-50, 175)
t.forward(15)
t.end_fill()

t.setheading(0)
t.up()
t.forward(50)
t.down()
# Drawring the stars
for i in range(5):
    colors = ['red', 'blue', 'white', 'green', 'yellow', 'pink',
    'purple', 'grey', 'brown', 'indigo', 'black', 'magenta', 'orange', '#806608']
    chices = random.choice(colors)
    t.begin_fill()
    t.color(chices)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.forward(25)
    t.left(215)
    t.end_fill()
    t.up()
    t.forward(200)
    t.setheading(0)
    t.down()

t.up()
t.home()
t.down()
t.hideturtle()

t.done()

import turtle as t
#import random

# Initial setup
t.speed(0)
t.Screen().bgcolor('black')
t.setup(800, 600)
t.color('black')
t.up()
t.backward(500)
t.right(90)
t.forward(400)
t.left(90)
t.down()

# Drawing the background
t.begin_fill()
t.color('#1d557d')  # Background color
for i in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(800)
    t.left(90)
t.end_fill()

# Drawing the water
t.up()
t.left(90)
t.forward(450)
t.right(90)
t.down()
t.begin_fill()
t.color('#036194') # Water color
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(450)
    t.right(90)
t.end_fill()

# Drawing the bridge
t.up()
t.right(90)
t.forward(200)
t.left(90)
t.down()
t.width(5)
t.color('silver') # Bridge color
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(100)
    t.right(90)

# Bridge rails
for i in range(25):
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.right(90)

# Adding the road
t.up()
t.right(90)
t.forward(105)
t.right(90)
t.down()

t.begin_fill()
t.color('black')
for i in range(2):
    t.forward(1000)
    t.left(90)
    t.forward(150)
    t.left(90)

t.end_fill()

t.done()

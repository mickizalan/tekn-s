import turtle
import random
import math

wn = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.shape("circle")
t.shapesize(0.5)
t.speed(0)

shoot = 0
piros = 0
for i in range(10000):
    shoot += 1
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.goto(x, y)
    d = math.sqrt(x ** 2 + y ** 2)
    if d < 400:
        t.color("red")
        piros += 1
    else:
        t.color("blue")
    t.stamp()
    print(4 * piros/shoot)

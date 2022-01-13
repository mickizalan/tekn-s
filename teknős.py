import turtle
import random
import math

wn = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.shape("circle")
t.shapesize(0.5)
t.speed(0)

for i in range(13000):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    t.goto(x, y)
    d = math.sqrt(x ** 2 + y ** 2)
    if d < 400:
        t.color("red")
    else:
        t.color("blue")
    t.stamp()
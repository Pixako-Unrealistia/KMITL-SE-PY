import turtle
import math

screen = turtle.Screen()
instance = turtle.Turtle()
#turtle.tracer(0)
turtle.speed(0)

for x in range (0,6):
    instance.forward(100)
    instance.left(60)

instance.penup()
instance.right(90)
instance.forward(150)

instance.pendown()

for x in range(360):
    instance.forward(1.75)
    instance.left(1)

instance.left(90)
instance.penup()
instance.forward(100)
instance.right(180)
instance.forward(3)
instance.write(math.pi * 100 * 100)

#turtle.done()
input()
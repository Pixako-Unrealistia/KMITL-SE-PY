import turtle
import sys

temp = int(sys.stdin.readline())
screen = turtle.Screen()
turtle.penup()
turtle.forward(temp/2)
turtle.left(90)
turtle.forward(temp/2)
turtle.right(90)
turtle.pendown()
for x in range(5):
        turtle.left(216)
        turtle.forward(temp)

turtle.done()

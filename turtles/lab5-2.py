import turtle
import sys

sys.stdout.write("Your input:\n")
prompt = int(sys.stdin.readline())
locat = 100/prompt

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)


turtle.forward(100)
turtle.right(90)

turtle.forward(100)
turtle.right(90)


turtle.setheading(0)

for x in range(1,prompt):
    turtle.penup()
    turtle.goto(-100, locat * (x))
    turtle.pendown()
    turtle.forward(100)

turtle.setheading(90)

for x in range(1,prompt):
    turtle.penup()
    turtle.goto(-locat * (x), 0)
    turtle.pendown()
    turtle.forward(100)


turtle.done()
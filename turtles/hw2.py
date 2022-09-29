import turtle

screen = turtle.Screen()
#turtle.tracer(0)
def mkpic(rang, forward, left):
    for x in range(rang):
        turtle.forward(forward)
        turtle.left(left)

mkpic(4, 200, 90)
turtle.penup()

turtle.forward(100)
turtle.right(90)
turtle.forward(40)
turtle.left(135)

turtle.pendown()
mkpic(4 , 200 , 90)
turtle.right(45)

mkpic(360 , 2.5 , 1)

turtle.right(90)
turtle.color("pink")
turtle.forward(200)

turtle.penup()
turtle.forward(50)
turtle.pendown()

turtle.hideturtle()
turtle.write("Magic circle to summon\nyour dream house!", align="center")
turtle.done()
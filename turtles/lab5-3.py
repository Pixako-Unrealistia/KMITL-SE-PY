import turtle
import sys

sys.stdout.write("Your input:")
prompt = int(sys.stdin.readline())

locat = 100//prompt
turtle.tracer(0)

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()

def genblack():
    turtle.setheading(0)
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.forward(locat)
    turtle.right(90)
    turtle.forward(locat)
    turtle.right(90)
    turtle.forward(locat)
    turtle.right(90)
    turtle.forward(locat)
    turtle.end_fill()


seg = list(reversed([-x*locat for x in range(1,prompt+1)]))
print(list(seg))
pentel = 1
supercoolcounter = 0
for c in seg:
    for x in range(1,prompt+1):
            if pentel == 1:
                turtle.penup()
                turtle.goto(c, locat * (x))
                turtle.pendown()
                genblack()
                pentel = 0
            else:
                pentel = 1
    pentel = 1
    supercoolcounter += 1
    if (supercoolcounter % 2) != 0:
        pentel = 0

turtle.penup()
turtle.goto(seg[0],0)
turtle.pendown()
turtle.goto(seg[0],0)
turtle.goto(0,0)
turtle.goto(0,-seg[0])
turtle.goto(seg[0],-seg[0])
turtle.goto(seg[0],0)
turtle.update()
turtle.done()
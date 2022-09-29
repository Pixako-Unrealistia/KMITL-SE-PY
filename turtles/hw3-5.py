import turtle
import sys

sys.stdout.write("Please input in the following format: (x,y)\n")
#example of valid inputs (I, myself tested with these)
#(100,200)
#(-100,200)
#(-140,100)


for x in range(3):
    exec(f"{chr(65 + x)} = eval(sys.stdin.readline())")

screen = turtle.Screen()
turtle.penup()
turtle.goto(A[0],A[1])
turtle.pendown()
for x in range(0,4):
    try:
        exec(f"turtle.goto({chr(65+x)}[0], {chr(65+x)}[1])")
    except:
        turtle.goto(A[0], A[1])
turtle.penup()
turtle.goto(((A[0]+B[0]+C[0])/2) ,min([A[1],B[1],C[1]]) - 50)
turtle.write(f"The area is {abs(0.5*(A[0]*(B[1] - C[1]) + B[0]*(C[1] - A[1]) + C[0]*(A[1] - B[1])))}", align="center")

turtle.ht()
turtle.done()

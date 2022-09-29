import turtle

screen = turtle.Screen()
turtle.speed(0)
turtle.width(5)
turtle.tracer(0)
def mkcir(color,x,y, r1, r2,direction):
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    if direction == "left":
        for x in range(r2):
            if x == r1:
                turtle.pendown()
            turtle.forward(1.5)
            turtle.left(1)
        turtle.setheading(0)
    else:
        for x in range(r2):
            if x == r1:
                turtle.pendown()
            turtle.forward(1.5)
            turtle.right(1)
        turtle.setheading(180)

mkcir("blue",-200,-25, 0,360, "left")
mkcir("black",0,-25, 0,360, "left")
mkcir("red", 200,-25, 0,360, "left")
mkcir("yellow",-100,-100, 0,360, "left")
mkcir("green", 100,-100, 0,360, "left")

mkcir("blue",-200,-25, 50, 100, "left")
mkcir("black",0,-25,50,100, "left")
turtle.setheading(180)
mkcir("red",200,-25, 0, 40, "right")
mkcir("black",0,-25,0,40, "right")

turtle.ht()
turtle.update()
turtle.done()


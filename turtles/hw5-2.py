import turtle

month = (31,28,31,30,31,30,31,31,30,31,30,31)
days = ("Su","Mo","Tu","We","Th","Fr","Sa")
date = 0
week = 7
turtle.tracer(0)
turtle.penup()
turtle.goto(-380,280)
turtle.pendown()
turtle.hideturtle()

class mytle():
    def writer(msg):
        turtle.forward(5)
        turtle.write(msg)
        turtle.backward(5)

    def fwd_box(N):
        counter = 0
        while counter < N:
            turtle.forward(25)
            turtle.left(90)
            turtle.forward(15)
            turtle.left(90)
            counter += 1

    def fwd_wide(fwd):
        turtle.left(90)
        turtle.forward(fwd)
        turtle.left(90)
x = 0
while x < 12:
    if x != 0 and x % 5 == 0:
        turtle.penup()
        tempo = turtle.pos()
        turtle.goto(tempo[0] + 260, 280)
        turtle.pendown()

    y = 0
    while y < 7:
        mytle.writer(days[y])
        mytle.fwd_box(2)
        turtle.forward(25)
        y += 1
    mytle.fwd_wide(30)
    turtle.forward(175)
    mytle.fwd_wide(15)
    mytle.writer(f"Month#{x+1}")
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    date = month[x]
    while date > 0:
        a = 1
        while a < 8:
            if a == week and date > 0 :
                date -= 1
                turtle.forward(5)
                turtle.write(month[x] - date)
                turtle.back(5)
                mytle.fwd_box(2)
                turtle.forward(25)
                if week < 7:
                    week = week + 1
                else:
                    week = 1
            else:
                mytle.fwd_box(2)
                turtle.forward(25)
            a+= 1
        if date > 0 :
            turtle.back(175)
            turtle.right(90)
            turtle.forward(15)
            turtle.left(90)
        else:
            turtle.back(175)
            turtle.right(90)
            turtle.penup()
            turtle.forward(45)
            turtle.pendown()
            turtle.left(90)
    x += 1
turtle.update()
turtle.done()
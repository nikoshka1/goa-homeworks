from turtle import *
speed(100)
def square(feri,x,y):
    pensize(0.5)
    color(feri)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    fd(5)
    left(90)
    fd(5)
    left(90)
    fd(5)
    left(90)
    fd(5)
    left(90)
    end_fill()
def blacks():
    color('black','black')
    penup()
    goto(0,130)
    pendown()
    begin_fill()
    fd(25)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    for i in range(4):
        left(90)
        fd(5)
        right(90)
        fd(5)
    fd(5)
    left(90)
    fd(5)
    left(90)
    fd(10)
    for i in range(4):
        fd(5)
        right(90)
        fd(5)
        left(90)
    right(90)
    fd(10)
    right(90)
    fd(15)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(15)
    for i in range(2):
        left(90)
        fd(5)
        right(90)
        fd(5)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(35)
    for i in range(2):
        right(90)
        fd(5)
        left(90)
        fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(100)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    for i in range(2):
        left(90)
        fd(5)
        right(90)
        fd(10)
    left(90)
    fd(5)
    right(90)
    fd(35)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(15)
    for i in range(2):
        left(90)
        fd(5)
        right(90)
        fd(5)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(15)
    right(90)
    fd(15)
    for i in range(3):
        right(90)
        fd(5)
        left(90)
        fd(5)
    right(90)
    fd(15)
    left(90)
    fd(5)
    left(90)
    fd(10)
    for i in range(4):
        right(90)
        fd(5)
        left(90)
        fd(5)
    for i in range(2):
        left(90)
        fd(5)
        right(90)
        fd(5)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(25)
    end_fill()
def greys():
    color('grey','grey')
    penup()
    goto(-5,50)
    pendown()
    begin_fill()
    fd(10)
    left(90)
    fd(25)
    right(90)
    fd(5)
    left(90)
    fd(25)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(25)
    left(90)
    fd(5)
    right(90)
    fd(25)
    end_fill()
    penup()
    goto(10,105)
    pendown()
    begin_fill()
    left(90)
    fd(10)
    for i in range(3):
        right(90)
        fd(5)
        left(90)
        fd(5)
    right(90)
    fd(45)
    right(90)
    fd(5)
    right(90)
    fd(40)
    for i in range(4):
        left(90)
        fd(5)
        right(90)
        fd(5)
    end_fill()
    square('grey',30,40)
    square('grey',25,35)
    z = 30
    for i in range(5):
        square('grey',20,z)
        z-=5
    square('grey',15,10)
    square('grey',10,5)
    square('grey',5,0)
    square('grey',0,0)
    square('grey',-5,5)
    square('grey',-10,10)
    x = 10
    for i in range(5):
        square('grey',-15,x)
        x+=5
    square('grey',-20,35)
    square('grey',-25,40)
    penup()
    goto(-35,45)
    pendown()
    begin_fill()
    right(90)
    fd(5)
    left(90)
    fd(40)
    for i in range(4):
        right(90)
        fd(5)
        left(90)
        fd(5)
    left(90)
    fd(5)
    for i in range(4):
        fd(5)
        left(90)
        fd(5)
        right(90)
    left(90)
    fd(40)
    end_fill()
    penup()
    goto(-70,105)
    pendown()
    begin_fill()
    left(90)
    for i in range(4):
        fd(5)
        right(90)
        fd(5)
        left(90)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(25)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(15)
    right(90)
    fd(5)
    left(90)
    fd(15)
    for i in range(2):
        left(90)
        fd(5)
        right(90)
        fd(15)
    right(90)
    fd(5)
    for i in range(2):
        right(90)
        fd(10)
        left(90)
        fd(5)
    right(90)
    fd(35)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(15)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    end_fill()
    square('grey',-45,-15)
    square('grey',50,-15)
    penup()
    goto(50,-10)
    pendown()
    begin_fill()
    right(90)
    for i in range(2):
        fd(5)
        left(90)
        fd(10)
        right(90)
    fd(5)
    left(90)
    fd(35)
    left(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    for i in range(2):
        fd(5)
        right(90)
        fd(5)
        left(90)
    right(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    left(90)
    fd(5)
    for i in range(3):
        left(90)
        fd(5)
        right(90)
        fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(25)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(15)
    left(90)
    fd(5)
    right(90)
    fd(15)
    for i in range(2):
        right(90)
        fd(5)
        left(90)
        fd(15)
    end_fill()
def slategreys():
    color('slategrey','slategrey')
    penup()
    goto(-5,50)
    pendown()
    left(90)
    begin_fill()
    for i in range(4):
        fd(10)
        right(90)
    end_fill()
    
    square('slategrey',-25,40)
    square('slategrey',-20,35)
    square('slategrey',20,40)
    square('slategrey',15,35)
    penup()
    goto(-30,55)
    pendown()
    begin_fill()
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(10)
    left(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    right(90)
    fd(15)
    left(90)
    fd(20)
    left(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(30)
    end_fill()
    penup()
    goto(25,55)
    pendown()
    begin_fill()
    left(90)
    fd(5)
    left(90)
    fd(30)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    left(90)
    fd(20)
    left(90)
    fd(15)
    right(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(10)
    end_fill()
    penup()
    goto(-25,10)
    pendown()
    begin_fill()
    fd(20)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(20)
    left(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    end_fill()
    left(180)
    square('slategrey',-30,-15)
    square('slategrey',25,-15)
    square('slategrey',-20,120)
    square('slategrey',15,120)
    penup()
    goto(-15,120)
    pendown()
    begin_fill()
    fd(30)
    right(90)
    fd(10)
    right(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(20)
    left(90)
    fd(5)
    right(90)
    fd(5)
    right(90)
    fd(10)
    end_fill()
def limes():
    color('lime','lime')
    penup()
    goto(-5,50)
    pendown()
    begin_fill()
    for i in range(3):
        fd(5)
        left(90)
        fd(5)
        right(90)
    left(90)
    fd(5)
    left(90)
    fd(10)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(15)
    end_fill()
    penup()
    goto(5,50)
    pendown()
    begin_fill()
    fd(15)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    left(90)
    fd(10)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    end_fill()
    square('lime',10,-5)
    square('lime',10,-10)
    square('lime',20,-10)
    square('lime',-15,-5)
    square('lime',-15,-10)
    square('lime',-25,-10)
    penup()
    goto(-25,25)
    pendown()
    begin_fill()
    fd(15)
    right(90)
    fd(5)
    left(90)
    fd(20)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    right(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(10)
    left(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(5)
    right(90)
    fd(15)
    left(90)
    fd(5)
    right(90)
    for i in range(4):
        fd(5)
        right(90)
        fd(5)
        left(90)
    right(90)
    fd(10)
    end_fill()
    penup()
    goto(25,25)
    pendown()
    begin_fill()
    fd(10)
    for i in range(4):
        fd(5)
        right(90)
        fd(5)
        left(90)
    left(180)
    fd(5)
    left(90)
    fd(15)
    right(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(10)
    left(90)
    fd(5)
    left(90)
    fd(10)
    left(90)
    fd(5)
    right(90)
    fd(10)
    right(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(5)
    right(90)
    fd(20)
    left(90)
    fd(5)
    right(90)
    fd(15)
    end_fill()
def greens():
    color('green','green')
    penup()
    goto(45,50)
    pendown()
    begin_fill()
    right(90)
    fd(10)
    right(90)
    fd(15)
    left(90)
    fd(5)
    right(90)
    fd(15)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    for i in range(3):
        right(90)
        fd(5)
        left(90)
        fd(5)
    right(90)
    fd(5)
    right(90)
    fd(5)
    left(90)
    fd(10)
    right(90)
    fd(5)
    left(90)
    fd(10)
    end_fill()
    penup()
    goto(-45,50)
    pendown()
    begin_fill()
    left(180)
    for i in range(2):
        fd(10)
        left(90)
        fd(5)
        right(90)
    for i in range(4):
        fd(5)
        right(90)
        fd(5)
        left(90)
    left(180)
    fd(10)
    left(90)
    fd(5)
    right(90)
    for i in range(2):
        fd(15)
        right(90)
        fd(5)
        left(90)
    right(90)
    fd(5)
    end_fill()
def purples():
    square('purple',-40,0)
    square('purple',-40,-5)
    square('purple',-45,-10)
    square('purple',-45,-15)
    square('purple',35,0)
    square('purple',35,-5)
    square('purple',40,-10)
    square('purple',40,-15)
def oranges():
    square('orange',0,110)
    square('orange',-5,110)
def saddlebrowns():
    square('saddlebrown',5,110)
    square('saddlebrown',-10,110)
blacks()
greys()
slategreys()
limes()
greens()
purples()
oranges()
saddlebrowns()
hideturtle()
exitonclick()
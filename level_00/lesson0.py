from turtle import *



pensize(7)
color('purple', 'purple')
speed(1000)
begin_fill()
for i in range(4):
    fd(200)
    lt(90)
end_fill()

#end of square

fd(70)
color('yellow', 'yellow')
begin_fill()
for i in range(2):
    fd(60)
    lt(90)
    fd(120)
    lt(90)
end_fill()


penup() 
goto(0, 200) 
pendown() 
color('red', 'red') 
begin_fill()
fd(200)
lt(120) 
fd(200) 
lt(120) 
fd(200)
end_fill()


penup()
goto(15, 180)
pendown()
color('blue', 'blue')
begin_fill()
lt(120)
for i in range(4):
    fd(30)
    rt(90)
end_fill()

penup()
goto(155, 180)
pendown()
begin_fill()
for i in range(4):
    fd(30)
    rt(90)
end_fill()

exitonclick()
hideturtle()
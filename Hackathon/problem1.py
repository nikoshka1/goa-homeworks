from turtle import *

pensize(1)
begin_fill()
fd(40)
right(85)
z = 1
for i in range(10):
    right(z)
    fd(5)
for i in range(85):
    fd(1)
    right(1)
exitonclick()

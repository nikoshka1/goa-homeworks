from turtle import *

def walk():
    fd(200)
    left(90)

def fall_back():
    left(90)
    fd(200)

walk()
fall_back()

exitonclick()
hideturtle()
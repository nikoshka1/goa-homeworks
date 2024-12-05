from turtle import *

speed(100)

def draw_triangles():
    a = 5  
    for i in range(1, 121):  
        if i % 2 == 1:  
            pencolor("green")
        else:  
            pencolor("blue")

        penup()
        goto(a, 0)  
        pendown()

        
        for _ in range(3):
            forward(20)  
            left(120)  
        a += 10 

draw_triangles()

def hello_world():
    print("hello_world")

hello_world()

n = input("შეიყვანეთ რიცხვი")

def even_or_odd(n):
    if n % 2 == 1:
        print("კენტი")
    else:
        print("არ არის კენტი")



even_or_odd(n)  
even_or_odd(n)
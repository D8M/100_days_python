import turtle
from turtle import *

def draw_square():
    window = turtle.Screen()
    window.bgcolor("green")

    # dave = turtle.Turtle()
    # dave.shape("turtle")
    # dave.color("yellow")
    # dave.speed(4)



    color('red', 'yellow')
    begin_fill()
    while True:

        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

    window.exitonclick()

#draw_square()
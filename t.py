import turtle
from random import randint

circ = turtle.Turtle()
turtle.colormode(255)
turtle.screensize(bg = "gray")
radius = 20

number = 10



circ.fillcolor(randint(0,255),randint(0,255),randint(0,255))


# circ.begin_fill()
# circ.circle(20)
# circ.end_fill()

for i in range(1, number + 1, 1):
   circ.circle( radius * i)
   circ.pencolor(randint(0,255),randint(0,255),randint(0,255))

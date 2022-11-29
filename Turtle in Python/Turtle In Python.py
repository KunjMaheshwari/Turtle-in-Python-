# Drawing Different Shapes Using Turtle

from turtle import Turtle, Screen
import random


timmy = Turtle()


def drawshape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape in range(3, 11):
    colorchoice = ["red", "blue", "green", "yellow", "orange",
                   "purple", "pink", "black", "brown", "grey"]
    select = random.choice(colorchoice)
    timmy.color(select)
    drawshape(shape)


screen = Screen()
screen.exitonclick()

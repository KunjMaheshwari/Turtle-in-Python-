# Draw a Spirograph in Python Using Turtle

from turtle import Turtle, Screen
import random

colour = ["red", "orange", "yellow", "green", "blue",
          "purple", "pink", "black", "white", "grey"]


timmy = Turtle()
timmy.speed("fastest")

i = 0
while i <= 360:
    timmy.color(random.choice(colour))
    timmy.circle(100)
    timmy.right(1)
    i += 1


screen = Screen()
screen.exitonclick()

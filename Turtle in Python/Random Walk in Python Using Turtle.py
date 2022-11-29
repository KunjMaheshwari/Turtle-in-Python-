# Random Walk in Python using Turtle

from turtle import Turtle, Screen
import random

timmy = Turtle()

directions = [0, 90, 180, 270]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
timmy.width(15)
timmy.speed("fastest")


i = 1
while i <= 100:
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    timmy.color(random.choice(colors))
    i += 1


screen = Screen()
screen.exitonclick()

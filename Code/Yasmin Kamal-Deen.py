import turtle
import random

timmy = turtle.Turtle()
timmy.speed(0)
timmy.goto(0, 100)
screen = turtle.Screen()
screen.bgcolor("black")


def spike_ball(step, angle):
    colors = ["white", "green", "pink", "red", "yellow"]
    the_color = random.choice(colors)

    while True:
        timmy.color(the_color)
        timmy.forward(step)
        timmy.right(angle)
        step += 3
        angle += 1
        if angle == 210:
            break


spike_ball(0, 0)


screen.exitonclick()
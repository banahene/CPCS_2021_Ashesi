# T-square Fractal
# Idea from: https://en.wikipedia.org/wiki/T-square_(fractal)
# Algorithmic description :
# Image 1:
# Start with a square.
# Image 2:
# At each convex corner of the previous image,
# place another square, centered at that corner,
# with half the side length of the square from the previous image.
# Take the union of the previous image with the collection of smaller squares placed in this way.
# Images 3–6:
# Repeat step 2.
from turtle import Turtle, Screen, mainloop


# turtle setup
t = Turtle()
t.speed("fastest")
t.ht()
t.pencolor("white")
t.pensize(1)

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)


def draw_square(x_start_pos, y_start_pos, side_length):
    """this function draws a square based on side lengh and starting x,y position"""
    t.penup()
    x = x_start_pos - side_length / 2
    y = y_start_pos - side_length / 2
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.forward(side_length)
        t.left(90)
    t.end_fill()
    t.fillcolor("white")


def draw_t_square_fractal(x_start_pos, y_start_pos, side_length, n):
    """this function takes in the x, y, side length of squares and the recursive number to draw a T-square fractal"""

    if n == 0:  # base case
        return n

    else:  # recursive case
        draw_t_square_fractal(x_start_pos - side_length / 2, y_start_pos - side_length / 2, side_length / 2, n - 1)
        draw_t_square_fractal(x_start_pos + side_length / 2, y_start_pos + side_length / 2, side_length / 2, n - 1)
        draw_t_square_fractal(x_start_pos - side_length / 2, y_start_pos + side_length / 2, side_length / 2, n - 1)
        draw_t_square_fractal(x_start_pos + side_length / 2, y_start_pos - side_length / 2, side_length / 2, n - 1)
        draw_square(x_start_pos, y_start_pos, side_length)


draw_t_square_fractal(0, 0, 200, 7)
screen.update()
mainloop()

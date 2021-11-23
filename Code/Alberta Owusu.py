import turtle
import random

fractal = turtle.Turtle()
fractal.up()
fractal.goto(-250, -250)
fractal.down()
colors = ["red", "pink", "blue", "purple", "black"]
increment = 0

# function that draw fractal squares 
def fractal_squares(side):
    global increment
    if side == 300:
        return None
    else:
        increment += 10
        fractal.pencolor(random.choice(colors))
        fractal.color(random.choice(colors))
        fractal.begin_fill()
        for i in range(4):
            fractal.width(5)
            fractal.forward(side)
            fractal.left(90)
        fractal.goto(-250 + increment, -250 + increment)
        fractal.end_fill()
        fractal_squares(side + 10)
    
fractal_squares(100)
turtle.mainloop()
    

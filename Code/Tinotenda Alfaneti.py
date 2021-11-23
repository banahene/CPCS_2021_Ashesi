import turtle
import random

#initializing the turtle
fractal_drawer = turtle.Turtle()
fractal_drawer.speed(0)
fractal_drawer.penup()
fractal_drawer.goto(-300, -300)
fractal_drawer.pendown()

#drawing the first part of the pattern        
def drawing_initial_pattern(length, number_of_times):
    
    if number_of_times == 0:
        return None
    else:
        fractal_drawer.left(30)
        fractal_drawer.forward(length)
        fractal_drawer.right(90)
        fractal_drawer.forward(length)
        fractal_drawer.right(30)
        fractal_drawer.forward(length)
        drawing_initial_pattern(length-1, number_of_times-1)
        
#duplicating the shapes horizontally
def duplicating_shape_horizontally(number_of_shapes):
    
    if number_of_shapes == 0:
        return None
    
    else:
        fractal_drawer.setheading(90)
        drawing_initial_pattern(50, 100)
        fractal_drawer.setposition(fractal_drawer.xcor(), fractal_drawer.ycor() + 50)
        duplicating_shape_horizontally(number_of_shapes-1)

#number of rows to be drawn
x_increase = 0
y_increase = 0
number_of_rows = 3

for i in range(number_of_rows):
    fractal_drawer.penup()
    fractal_drawer.goto(-300 - x_increase , -300 + y_increase)
    fractal_drawer.pendown()
    duplicating_shape_horizontally(4)
    x_increase += 50
    y_increase += 135

turtle.mainloop()

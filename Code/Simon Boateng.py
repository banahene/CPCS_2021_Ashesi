import turtle
fractal1=turtle.Turtle()
turtle.bgcolor('Yellow')
def draw_flower(angle, radius):
    if radius<1:
        return 'Done'
    
    else:
        fractal1.speed(0.01)
        fractal1.fillcolor('green')
        fractal1.pencolor('lightgreen')
        fractal1.begin_fill()
        fractal1.circle(radius, angle)
        fractal1.left(angle)
        fractal1.circle(radius, angle)
        fractal1.left(120)
        fractal1.end_fill()
        draw_flower(angle, radius-1)

flower1=draw_flower(90, 190)
# flower2=draw_flower(90, 170)
# flower3=draw_flower(90, 160)
# flower3=draw_flower(90, 70)
turtle.done()






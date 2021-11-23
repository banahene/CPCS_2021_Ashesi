import turtle 
t = turtle.Turtle()
turtle.bgcolor('green') 
t.speed(150)

t.shape('triangle')
t.fillcolor('yellow')
# This function drwas the recursive triangle

def recursive_triangle(length, order):
    t.begin_fill()
    if order==0:
        t.stamp()
    else:
        for i in range(0, 3):
            t.forward(length)
            recursive_triangle(length/2, order-1)
            t.backward(length)
            t.left(120)
    t.end_fill()
#Test case
recursive_triangle(150, 5)

turtle.mainloop()
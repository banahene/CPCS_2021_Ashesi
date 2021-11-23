# drawing an interesting pattern with recursion

import turtle
t = turtle.Turtle()
t.speed(15)

# A function to draw a circle
def draw_circle(radius):
        t.circle(radius)
       

# A recursive function to draw a number of concentric circles
# The parameter radius represents the radius of the largest
# (outermost) circle
Colour=['red','orange', 'yellow', 'green','blue', 'indigo','violet']
def concentric_circle(radius):
    if (radius < 10): # base case - do nothing
        pass

    # recursive case - draw a circle and make a recursive
    # call to draw the smaller circle
    else:
        t.begin_fill()
        draw_circle(radius)
        t.color(Colour[0])
        t.end_fill()
        Colour.pop(0)
        t.penup()
        t.setposition(t.xcor()+5, t.ycor()+5)
        t.pendown()
        concentric_circle(radius - 30)

# call the recursive concentric_squares function
concentric_circle(200)


t.getscreen()._root.mainloop()

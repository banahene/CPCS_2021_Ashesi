import turtle
import random
t = turtle.Turtle()

t.speed(0)

# Creating a function that draws a flower, taking in the parameters: radius and the 
# center space

def flower1(radius, centre_space):
    
    colours = ["black", "green", "violet", "magenta", "blue"]
    turtle.Screen().bgcolor("khaki2")
    pick_color = random.choice(colours)
    
    if radius == 180:
        pass
    else:
        
        t.setposition(0, 130)
        t.color(pick_color)
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(radius, centre_space)
        t.left(90)
        t.circle(radius, centre_space)
        t.left(10)
        flower1(radius+1, centre_space) #Making a recursive call that increases the radius by 1
        
# After making the flower, I will set a new position that draws a stick that connects to the center of the flower       
    t.setposition(0, 130)    
    t.right(-5)
    t.forward(-5)
    t.color("brown2")
    t.circle(35)
    t.setposition(0, -200)
    t.right(180)
    t.pensize(1)
    t.forward(25)

        
flower1(100, 90)
turtle.mainloop()        



import turtle

turtle.speed(50)
turtle.bgcolor("black")


def circle(radius, colour = 0):
    '''This function draws a set of 10 circles with the colours alternate per set'''
    
    colours = ["blue", "purple"]
    turtle.pencolor(colours[colour])
    
    for x in range(10):
        turtle.circle(radius)
        turtle.left(36)
        
        
def fractal_flower(radius, colour = 0):
    ''' This function uses recurring circles to make a flower. The purpose of the if statement
    in the else block is to prevent an error from occuring should the index number be found
    outside the range of colours '''
    
    if radius > 200:
        pass
    else:
        
        if colour == 2:
            colour = 0
            circle(radius, colour)
            colour += 1
            fractal_flower(radius + 5, colour)
        else:
            circle(radius, colour)
            colour += 1
            fractal_flower(radius + 5, colour)
            
            

fractal_flower(150)
turtle.mainloop()
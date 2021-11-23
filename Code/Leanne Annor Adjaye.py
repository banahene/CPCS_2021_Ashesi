import turtle
t = turtle.Turtle()
t.goto(0,0)
ts = turtle.Screen()
ts.bgcolor("black")

colours = ["deepskyblue", "dodgerblue", "cyan"]
#colours = ["lightgray", "white", "gray"]
#colours = ["plum", "violet", "indigo"]
#defining a function that draws the base of a hexagon
def base_hexagon(width):
    """function to draw the hexagon

        Parameters:
        width (float): stores the length of each side of the hexagon"""
   #using a loop to draw three sides of the hexagon and changing the colour of
   #the pen for each line drawn
    for i in range(3):
        t.pencolor(colours[i])
        t.forward(width)
        t.left(59.7)
       
#defining a function that draws multiple hexagons    
def spiral_hexagon(width):
    """defining a function that draws concentric hexagons
        
        Parameters:
        width(float): stores the length of each side of the hexagon"""
   #checking if the width is greater than or equal to 300 and stopping the
   #hexagon from drawing if it is.
    if width >= 300:
        pass
    else:
       #drawing hexagon so long as the width is less than 300
        base_hexagon(width)
        #increasing width by 5 after each hexagon is drawn
        spiral_hexagon(width+ 1)

        
t.speed(8000)


#Testing codes

#spiral_hexagon(8)
#spiral_hexagon(6)
#spiral_hexagon(10)
spiral_hexagon(9)

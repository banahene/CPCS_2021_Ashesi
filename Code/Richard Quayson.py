#this program designs a perspective drawing of a road


#import needed modules from python's library
import turtle
import math
import random


#define the turtle
#set pensize to 2
#set turtle speed to 5
t = turtle.Turtle()
t.pensize(2)
t.speed(5)


#set the values of frame
#use the math module to compute the hypotenuse,
#and the angle between the width and hypotenuse
length = 1000
width = 600
hypotenuse = math.sqrt(length**2 + width**2)
angle_between_hypotenuse_length = math.atan(width/length)
angle_in_radian = math.degrees(angle_between_hypotenuse_length)


def frame(start_posx = -450, start_posy = -300):

    #set the position of the turtle facing right
    #create a loop that uses the height and width to create a rectangular frame
    t.up()
    t.setposition(start_posx, start_posy)
    t.down()
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)


def frame_disector(): 

    #define the color mode of the turtle to accept rgb color format
    #fill the lower part of frame with fillcolor green
    #use the angle between width and hypotense to move turtle along the hypotenuse
    #set fillcolor to gray turn the turtle midway the width of frame
    #follow the diagonal (hypotenuse) to the end of right corner of frame
    #end the fillcolor to create an image that depicts a road
    turtle.colormode(255)
    t.fillcolor(50,205,50)
    t.begin_fill()
    t.left(90)
    t.forward(width/2)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width/2)
    t.right(90)
    t.forward(length)
    t.left(180)
    t.end_fill()
    t.fillcolor("gray")
    t.begin_fill()
    t.left(angle_in_radian)
    t.forward(hypotenuse/2)
    t.right(2*angle_in_radian)
    t.forward(hypotenuse/2)
    t.end_fill()
    t.left(angle_in_radian)

def sky():

    #set turtle position facing upwards
    #set the fillcolor to a shade of blue
    #move along the other half of the frame and end fill to paint upper frame
    #set turtle position to face right
    t.left(90)
    t.forward(width/2)
    turtle.colormode(255)
    t.fillcolor(137,207,240)
    t.begin_fill()
    for i in range(2):
        t.forward(width/2)
        t.left(90)
        t.forward(length)
        t.left(90)
    t.end_fill()
    t.right(90)
    

def left_street_lights(road_separation, height_difference, light_size, start_posx = -450, start_posy = -300):

    #initialise the height of the first street light
    #stop the recursion if the height of street light is less than 20
    #else, set the angle of the turtle to follow the diagonal (hypotenuse)
    #move along it by a margin and draw a light stand
    #set the angle of the turtle and draw two arcs that meeting at the apex of the light stand
    #note that the angle should sum up to 360
    #fill the resulting figure white and repeat the process reducing the light stand by 50
    #however, if the light stand is 50 in height, reduce the amount of height difference by 30
    initial_height = 300
    height = initial_height - height_difference
    if height < 20:
        pass
    else:
        t.up()
        t.setposition(start_posx, start_posy)
        t.down()
        t.left(angle_in_radian)
        t.forward(-50 + road_separation)
        t.left(90 - angle_in_radian)
        t.forward(initial_height - height_difference)
        t.fillcolor("white")
        t.begin_fill()
        t.right(150)
        t.circle(70 - light_size, 90)
        t.left(90)
        t.circle(70 - light_size, 90)
        t.right(210)
        t.end_fill()
        if (height == 50):
            left_street_lights(road_separation + 70, height_difference + 30, light_size + 10)
        else:
            left_street_lights(road_separation + 100, height_difference + 50, light_size + 10)
            
        
def right_street_lights(road_separation, height_difference, light_size, start_posx = 550, start_posy = -300):

    #repeat the process for the left_street_lights function but be wery of the turtle's angle
    #note the angles still sum up to 360 but it's left not right
    initial_height = 300
    height = initial_height - height_difference
    if height < 20:
        pass
    else:
        t.up()
        t.setposition(start_posx, start_posy)
        t.down()
        t.left(180 - angle_in_radian)
        t.forward(-50 + road_separation)
        t.right(90 - angle_in_radian)
        t.forward(initial_height - height_difference)
        t.fillcolor("white")
        t.begin_fill()
        t.left(60)
        t.circle(70 - light_size, 90)
        t.left(90)
        t.circle(70 - light_size, 90)
        t.left(300)
        t.end_fill()
        if (height == 50):
            right_street_lights(road_separation + 70, height_difference + 30, light_size + 10)
        else:
            right_street_lights(road_separation + 100, height_difference + 50, light_size + 10)
            
    
def clouds():

    #set the position of the turtle, facing upwards
    #set fillcolor to white
    #loop an arc three times
    #move by the edge of the frame to enclose your arcs, and endfill
    #set angle of turtle to face right
    t.up()
    t.setposition(180,100)
    t.down()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(3):
        t.right(30)
        t.circle(-90, 90)
        t.left(120)
    t.left(180)
    t.forward(100)
    t.end_fill()
    t.right(180)
    

def sun():

    #set position of the turtle to desired location of sun
    #set fillcolor to yellow
    #draw your circle with the desired radius and endfill
    #set position of the turtle to face upwards
    t.up()
    t.setposition(450, 180)
    t.down()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.left(90)
    

def compute_position(x, y):
    #create a function that prints the cordinates of the position user clicks
    #(necessary for setting the position of trees)
    t.up()
    print(x,y)
    t.goto(x,y)

    
def tree_position(set_posx, set_posy, stem):

    #set position of tree in desired area using results from the compute_position function
    #draw the stem of the tree
    t.up()
    t.setposition(set_posx, set_posy)
    t.down()
    t.backward(stem)
    

def tree(branches):

    #creating a fractal tree
    #set the pencolor to brown and draw the branches
    #make recursive calls to draw several branches until the branch length is less than 10
    #draw circles at intermittent positions on the branches
    #use the random.choice() method to determine the color of fruits (circles)
    #with orange being riped and green being unriped
    t.color("brown")
    t.pensize(3)
    if branches < 10:
        return
    else:
        t.forward(branches)
        t.color(random.choices(["orange", "green"]))
        t.circle(4)
        t.color("brown")
        t.left(30)
        tree(3*branches/4)
        t.right(60)
        tree(3*branches/4)
        t.left(30)
        t.backward(branches)


#function calls

#draw the frame, frame disector, and sky
frame()
frame_disector()
sky()

#draw street lights in perspective on the hypotenuse, setting
#road_separation to 100, height_difference to 50 and the light_size to 10
left_street_lights(100, 50, 10)
right_street_lights(100, 50, 10)

#draw the sun and clouds
sun()
clouds()

#used for calculating positions on frame
t.getscreen().onclick(compute_position)

#set the position of tree, draw the stem
#and call the tree function to draw the branches and fruits
#populate several areas with tress
tree_position(450, -180, 50)
tree(50)
tree_position(-425.0, -157.0, 30)
tree(20)
tree_position(-374.0, -182.0, 30)
tree(20)
tree_position(-314.0, -122.0, 30)
tree(20)
tree_position(-373.0, -106.0, 30)
tree(20)
tree_position(-293.0, -137.0, 30)
tree(20)
tree_position(-109.0, -53.0, 20)
tree(15)
tree_position(-253.0, -102.0, 30)
tree(20)
tree_position(218.0, -76.0, 15)
tree(15)
tree_position(123.0, -27.0, 15)
tree(15)
tree_position(-184.0, -91.0, 15)
tree(15)
tree_position(-27.0, -24.0, 15)
tree(15)
tree_position(236.0, -86.0, 15)
tree(15)
tree_position(181.0, -50.0, 15)
tree(15)
tree_position(-216.0, -126.0, 20)
tree(15)
tree_position(269.0, -72.0, 30)
tree(20)
tree_position(310.0, -110.0, 30)
tree(20)
tree_position(517.0, -246.0, 30)
tree(20)
tree_position(515.0, -192.0, 30)
tree(20)

turtle.mainloop()


#end of program

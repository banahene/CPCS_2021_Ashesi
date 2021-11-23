import turtle, random
t = turtle.Turtle()

turtle.bgcolor('black') 
turtle.colormode(255)

def spheral_rectangle(number, len):
    ''' This functions draws an image of a rotating and enlarging polygon with each
    line composing of different colours'''
    if number <= 0:
        return
    r = random.randint(0,255) 
    g = random.randint(0,255)  
    b = random.randint(0,255) 
  
    turtle.pencolor(r,g,b)

    turtle.fd(len + 2) 
    turtle.rt(90.991)
    spheral_rectangle(number-len, len+2)
    
try:
    num = int(input('''Number of lines for the circular fractal.
For a nicer image use numbers greater than 1000 \n: '''))
    spheral_rectangle(num*2, 2)

except:
    print('Enter a number')

turtle.mainloop()
import turtle

t = turtle.Turtle()
t.speed(150)
turtle.Screen().bgcolor('darkslategray')
        
def nucleus_of_a_star(length):
  
    if length > 700:
        pass
    else:
        
        t.pencolor("deepskyblue")     
        t.forward(length)
        t.circle(3,140)
        t.pencolor("aquamarine")
        t.forward(length)
        t.circle(3,140)
        t.pencolor("aquamarine")  
        t.forward(length)
        t.circle(3,140)
        t.pencolor("deepskyblue") 
        t.forward(length)
        t.circle(3,140)
    
        t.penup()
        t.setposition(t.xcor(),t.ycor())
        t.pendown()
         
        
        length = length + 10
        nucleus_of_a_star(length)
    
nucleus_of_a_star(10)

turtle.mainloop()
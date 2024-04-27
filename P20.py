import turtle

screen = turtle.Screen()
screen.title("Graphic")
screen.bgcolor("white")

t = turtle.Turtle()

# Outline circle
t.penup()
t.goto(0, -150)
t.pendown()
t.color("light green")
t.pensize(12)
t.circle(150)

# Left eye
t.penup()
t.goto(-50, 0)
t.pendown()
t.begin_fill()
t.color("red")
t.circle(30)
t.end_fill()

# Right eye
t.penup()
t.goto(50, 0)
t.pendown()
t.begin_fill()
t.color("blue")
t.circle(30)
t.end_fill()

# Yellow Line
t.penup()
t.goto(-50, -50)  
t.pendown()
t.color("yellow")
t.pensize(23)
t.goto(50, -50)  

# Upside down triangle
t.penup()
t.goto(-50, -110)  
t.pendown()
t.color("black", "white")
t.pensize(30)
t.begin_fill()
t.goto(50, -110)  
t.goto(0, -190)   
t.goto(-50, -110)  
t.end_fill()

t.hideturtle()
screen.mainloop()

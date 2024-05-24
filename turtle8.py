import turtle
t1 = turtle.Turtle()
t1.forward(50)

for i in range(3):
    t1.circle(50,90)
    t1.forward(80)

t1.circle(50,90)
t1.forward(50)
t1.penup()
t1.left(90)
t1.forward(80)
t1.right(90)
t1.pendown()
t1.write(">>>Hello World")
turtle.done()
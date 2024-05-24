import turtle

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red")
for i in range(1):
    t1.circle(100,180)
    t2.circle(100,-180)

t1.left(90)
t1.forward(200)
t2.circle(100,90)
t2.left(90)
t2.forward(200)
turtle.done()
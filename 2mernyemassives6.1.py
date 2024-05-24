import turtle

t = turtle.Turtle()
fill_color = "red"
size = 100
t.fillcolor(fill_color)
t.begin_fill()
for _ in range(5):
    t.forward(size)
    t.right(144)
t.end_fill()
turtle.done()
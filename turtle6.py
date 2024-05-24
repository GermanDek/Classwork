import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(12):
    turtle.color(colors[i % len(colors)])
    turtle.circle(100)
    turtle.right(30) if i < 6 else turtle.left(30)
turtle.done()
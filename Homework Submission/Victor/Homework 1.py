import turtle

t = turtle.Turtle()
# Draw a triangle
for _ in range(3):
    t.forward(100)
    t.right(120)

# Draw a hexagon
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
draw_polygon(6, 80)

# Draw a blue rectangle
t.fillcolor("blue")
t.begin_fill()
for _ in range(2):
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(125)
t.end_fill()

# Draw a red pentagon
t.fillcolor("red")
t.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()

# Draw a circle
t.circle(100)

turtle.done()

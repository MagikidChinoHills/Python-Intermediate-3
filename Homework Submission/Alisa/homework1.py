import turtle
t = turtle.Turtle()
# 1
for _ in range(3):
    t.forward(100)
    t.right(120)
# 2
def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)
draw_polygon(6, 80)
# 3
t.fillcolor("blue")
t.begin_fill()
for _ in range(2):
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(125)
t.end_fill()
# 4
t.fillcolor("red")
t.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()
# 5
t.circle(100)
turtle.done()
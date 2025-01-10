''' # 1
turtle.colormode(255)
def get_color(step):
    r = (step * 3) % 256
    g = (step * 5) % 256
    b = (step * 7) % 256
    return(r, g, b)
t = turtle.Turtle()

t.speed(0)
t.pencolor("green")

angle = 15
distance = 1
increment = 0.01

for step in range(1080):
    t.pencolor(get_color(step))
    t.forward(distance)
    t.right(angle)
    distance += increment

turtle.done()
'''
''' # 2
t = turtle.Turtle()

t.left(45)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

turtle.done()
'''
''' # 3
t = turtle.Turtle()

t.color("red")
t.begin_fill()

t.left(50)
t.forward(100)

t.circle(50, 200)
t.right(140)
t.circle(50, 200)

t.forward(100)
t.end_fill()

turtle.done()
'''
'''  # 4
t = turtle.Turtle()

t.color("blue", "purple")
t.begin_fill()
for _ in range(36):
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(60)

t.end_fill()

turtle.done()
''' 
import turtle
t = turtle.Turtle()
colors = ["red", "yellow", "green", "blue", "purple"]
def square(length, color):
    t.color(colors[color % len(colors)])
    if length > 0:
        for i in range (4):
            t.forward(length)
            t.right(90)
    if length <= 0:
        return
    return square(length - 5, color + 1)
square(100, 0)

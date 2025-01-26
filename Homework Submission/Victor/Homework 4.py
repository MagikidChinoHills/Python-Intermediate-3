import turtle
import time

def draw_hexagon(side_length, color):
    t = turtle.Turtle()
    t.color(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(side_length)
        t.right(60)
    t.end_fill()

def draw_mandala(radius, num_circles):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    for i in range(num_circles):
        t.circle(radius + i * 10)

def animate_triangle():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, -50)
    t.pendown()
    for _ in range(3):
        t.forward(100)
        t.left(120)

    for _ in range(30):
        t.right(12)
        time.sleep(0.1)

def draw_nested_squares(side_length, num_squares):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    for i in range(num_squares):
        t.penup()
        t.goto(-(side_length + i * 10) / 2, -(side_length + i * 10) / 2)
        t.pendown()
        for _ in range(4):
            t.forward(side_length + i * 10)
            t.right(90)

def draw_fractal_triangle(length, depth):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-length / 2, -length / 2 * 0.866)
    t.pendown()

    def draw_triangle(length, depth):
        if depth == 0:
            for _ in range(3):
                t.forward(length)
                t.left(120)
        else:
            for _ in range(3):
                t.forward(length)
                t.left(120)
                draw_triangle(length / 2, depth - 1)
                t.right(120)
                t.forward(length)
                t.left(120)

    draw_triangle(length, depth)

# Example usage:
draw_hexagon(80, "blue")
turtle.done()

draw_mandala(50, 10)
turtle.done()

animate_triangle()
turtle.done()

draw_nested_squares(50, 10)
turtle.done()

draw_fractal_triangle(200, 3)
turtle.done()

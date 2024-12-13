'''
Lesson 1: Turtle Functions
Objective: Review the basics of the Python Turtle library by creating various shapes.

Introduction to Turtle Graphics

Turtle Library Basics:
The Turtle library is a popular way for introducing programming to kids. It provides a virtual canvas where you can draw using a turtle that moves on the screen.
Basic commands:
forward(distance): Move the turtle forward by the specified distance.
backward(distance): Move the turtle backward by the specified distance.
right(angle): Turn the turtle clockwise by the specified angle.
left(angle): Turn the turtle counterclockwise by the specified angle.
penup(): Lift the pen so that moving the turtle does not draw on the canvas.
pendown(): Lower the pen to draw when the turtle moves.
'''

import turtle # Import thr turtle graphics library for drawing

t = turtle.Turtle() # Intializes turtle object named 't'
'''
# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)
'''

'''
Using Pen Colors and Fill Colors

pencolor(color) - Set the color of the pen.
fillcolor(color) - Set the color used to fill shapes.
begin_fill() - Begin filling the shape with the current fill color.
end_fill() - End filling the shape with the current fill color.
'''

'''
# Draw a filled star
t.fillcolor("yellow")
t.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()
'''

# Function to draw a polygon with a specific number of sides and length
def draw_polygon(sides, length):
    angle = 360 / sides # Calculate the angle between sides
    for _ in range(sides):
        t.forward(length) # Moves the turtle forward by specified length
        t.right(angle) # Turn the turtle by calculated angle

#draw_polygon(8,100)

import turtle
'''
t = turtle.Turtle()
t.speed(0)  # Set the turtle speed to the maximum

# Draw a colorful spiral
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(360):
    t.pencolor(colors[i % 6]) # Cycle through colors
    t.width(i // 100 + 1) # Increase line with by 1 each loop
    t.forward(i)
    t.right(59)

turtle.done()
'''
t.speed(0)

def draw_branch():
    for _ in range(3):
        t.forward(50)
        t.backward(50)
        t.right(45)
    t.left(90)
    for _ in range(3):
        t.forward(50)
        t.backward(50)
        t.left(45)
    t.right(90)

for _ in range(1000):
    draw_branch()
    t.right(1)

turtle.done()

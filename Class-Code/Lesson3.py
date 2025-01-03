'''
Lesson 3: Turtle and Math
Objective: Utilize the Math library to model mathematical concepts and recursive algorithms.

Introduction to the Math Library

Using math functions:
math.sin(x), math.cos(x): Return the sine and cosine of x (in radians).
math.pi: The mathematical constant π.
'''

import turtle
import math
'''
# Create a turtle object
t = turtle.Turtle()

t.pencolor("black")

# Draw a sin wave
t.penup()
t.goto(-360, 0)
t.pendown()  # Lower the pen to start drawing
for x in range(-360, 361):  # Iterate through x values from -360 to 360
    y = math.sin(math.radians(x)) * 100  # Calculate y using the sine of x (converted to radians) scaled by 100
    t.goto(x,y)

turtle.done()
'''

'''
Recursive Algorithms with Turtle

Introduction to recursion:
Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
'''
'''
t = turtle.Turtle()

# Function to draw a fractal tree
def draw_tree(branch_length):
    if branch_length > 0: # Base case: stop recursion when branch length is too short
        t.forward(branch_length) # Draw current branch length
        t.right(20) # Turn right to draw right subtree
        draw_tree(branch_length - 15) # Recursively draw the right subtree with shorter branches
        t.left(40) # Turn left to draw the left subtree
        draw_tree(branch_length - 15) # Recursively draw the left subtree with shorter branches
        t.right(20)  # Restore the original orientation
        t.backward(branch_length)  #Move the turtle back to starting point

# Set up the intial position and orientation for drawing
t.left(90)
t.penup()
t.goto(0, -200)
t.pendown()

draw_tree(30)

turtle.done()
'''

'''
# Create a parabola
t = turtle.Turtle()
t.speed(0)
t.pencolor("purple")

# Move turtle to starting position for parabola
t.goto(-200,0)
t.pendown()

# Draw parabola
for x in range(-200, 201):
    y = 0.01 * (x ** 2)
    t.goto(x,y)

t.penup()

turtle.done()
'''

# Draw a spiral (Homework question)
'''
# Set up the turtle environment
turtle.colormode(255)  # Enable RGB color mode (0-255)

# Function to generate color dynamically
def get_color(step):
    r = (step * 3) % 256  # Cycle red value
    g = (step * 5) % 256  # Cycle green value
    b = (step * 7) % 256  # Cycle blue value
    return (r, g, b)

t = turtle.Turtle()
t.speed(0)
t.pencolor("purple")

# Draw a spiral
angle = 15  # Angle to turn at each step
distance = 10  # Initial distance between spiral loops
increment = 0.1  # Increase the distance with each step for the spiral effect

for step in range(1080):
    t.pencolor(get_color(step))
    t.forward(distance)
    t.right(angle)
    distance += increment

turtle.done()
'''

'''
# Draw a diamond (Homework question)
t = turtle.Turtle()

# Draw the diamond
t.left(45)      # Rotate the turtle to start the diamond
t.forward(100)  # Draw the first side
t.right(90)     # Turn right
t.forward(100)  # Draw the second side
t.right(90)     # Turn right
t.forward(100)  # Draw the third side
t.right(90)     # Turn right
t.forward(100)  # Draw the fourth side

turtle.done()
'''

'''
# Draw a heart (Homework question)
t = turtle.Turtle()

t.color("red")
t.begin_fill()

# Start at bottom of heart
t.left(50)
t.forward(100)

t.circle(50, 200)
t.right(140)
t.circle(50, 200)

t.forward(100)
t.end_fill()

turtle.done()
'''

# Draw a flower pattern (Homework question)
t = turtle.Turtle()

t.color("blue", "lightblue")

t.begin_fill()
for _ in range(36):
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(60)
t.end_fill()

turtle.done()

'''
Lesson 2: Turtle and Random
Objective: Learn to create spirographs and intricate drawings with Turtle and the Random library.

Introduction to the Random Library

Generating random numbers:
random.randint(a, b): Return a random integer N such that a <= N <= b.
random.choice(sequence): Return a randomly chosen element from a non-empty sequence.
'''
import turtle  # Import the turtle graphics library for drawing
import random  # Import the random library to generate random numbers


# Create a turtle object
t = turtle.Turtle()

# Random walk
for _ in range(100):
    t.forward(30)
    t.right(random.randint(0, 360)) # Turn the turtle right by random angle between 0 and 360

turtle.done()


'''
Creating Spirographs

Understanding spirographs and their mathematical basis:
A spirograph is a geometric drawing that produces a curve known as a hypotrochoid.
Using loops and turtle, we can create these intricate designs.
'''
import turtle  # Import the turtle graphics library for drawing
import random  # Import the random library to generate random colors


t = turtle.Turtle()
t.speed(0)

# Function to draw spirograph
def draw_spirograph(size):
    for _ in range(int(360 / size)):
        t.pencolor(random.choice(['red', 'green', 'blue']))
        t.circle(100)
        t.right(size)

draw_spirograph(10)

turtle.done()


# Create a screen
screen = turtle.Screen()
screen.bgcolor('black')


# Create an object
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.hideturtle()

# Function to draw a star
def draw_star(size, color):
    star_turtle.color(color)
    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
    star_turtle.end_fill()

# Draw 20 random stars
for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(10,50)
    color = random.choice(['red', 'green', 'blue'])
    star_turtle.penup()
    star_turtle.goto(x,y)
    star_turtle.pendown()
    draw_star(size, color)

turtle.done()



t = turtle.Turtle()
t.speed(0)


# Function to create a random shape
def draw_shape(sides, length):
    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)

# Kaleidoscope pattern
for _ in range(360):
    t.pencolor(random.choice(['red', 'green', 'blue']))
    draw_shape(random.randint(3,8), random.randint(50,100))
    t.right(10)
turtle.done()


import time

# Create screen
screen = turtle.Screen()
screen.title("Traffic light simulation")

# Create object
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to draw traffic light
def draw_light(position, color, active):
    t.penup()
    t.goto(position)
    t.dot(100, color if active else "gray") # Bright color if active, otherwise grey/off

# Initial setup
positions = [(0,100), (0,0), (0,-100)] #Top, middle, bottom traffic lights
colors = ['red', 'green', 'yellow']

# Traffic light actual simulation
while True:
    for i in range(3):
        for j in range(3):
            draw_light(positions[j], colors[i], j == i)
        time.sleep(3)

turtle.done()

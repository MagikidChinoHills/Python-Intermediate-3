'''
Lesson 4: Turtle Project
Objective: Apply the knowledge of Turtle graphics to create a comprehensive project.

Project Planning and Design

Brainstorming project ideas:
Choose a project that incorporates various Turtle graphics concepts learned so far.
Examples: Drawing a complex fractal, creating a scene with multiple objects.
Activity: Outline and design your Turtle project.
'''

import turtle  # Import the turtle graphics library

# Create a turtle object
t = turtle.Turtle()  # Initializes a turtle object for drawing

# Example Project 1: Drawing a Complex Fractal - Koch Snowflake

def koch_snowflake(t, length, depth):
    """
    Draws a Koch snowflake fractal.
    
    Parameters:
    t - The turtle object used for drawing
    length - The length of each side of the snowflake
    depth - The recursion depth of the fractal
    """
    if depth == 0:
        t.forward(length)  # Draw a straight line if depth is 0
    else:
        for angle in [60, -120, 60, 0]:  # Koch curve angles
            koch_snowflake(t, length / 3, depth - 1)  # Recursively draw smaller segments
            t.left(angle)  # Change direction according to the Koch curve pattern

# Set up the drawing environment
t.penup()  # Lift the pen to move the turtle without drawing
t.goto(-150, 90)  # Move to starting position for drawing the snowflake
t.pendown()  # Lower the pen to start drawing
t.speed(0)  # Set the drawing speed to the fastest

# Draw the Koch snowflake with initial side length of 300 and depth of 4
for _ in range(3):
    koch_snowflake(t, 300, 4)  # Draw one side of the snowflake
    t.right(120)  # Turn to draw the next side of the snowflake

turtle.done()  # Finish the turtle drawing and close the window

'''
Project Ideas:

1. **Complex Fractal Patterns**
   - Create intricate fractal patterns such as the Mandelbrot set or Julia set using recursive algorithms.
   - Use Turtle graphics to visualize these mathematical concepts in a creative way.

2. **Interactive Scene with Turtle Graphics**
   - Design an interactive scene with various objects like trees, houses, and animals.
   - Implement user interactions such as clicking or key presses to modify the scene or animate objects.

3. **Turtle Animation**
   - Create a short animation with moving objects or characters.
   - Utilize loops and Turtle’s drawing capabilities to animate simple movements or actions.

4. **Geometric Art**
   - Design and draw complex geometric shapes and patterns, such as spirals, polygons, or mandalas.
   - Experiment with different colors, sizes, and angles to create visually appealing artwork.

5. **Educational Visualization**
   - Develop visualizations to help explain mathematical concepts such as sine waves, polar coordinates, or probability distributions.
   - Use Turtle graphics to create interactive diagrams or animations that illustrate these concepts.

Activity: Outline and Design Your Turtle Project
- Choose a project idea from above or come up with your own.
- Break down the project into smaller tasks or components.
- Design each component and plan how to implement them using Turtle graphics.
- Write code for each task, test it thoroughly, and combine the tasks to complete the project.
- Document your code and project to explain how it works and what each part does.

'''

import turtle

# Setup screen
screen= turtle.Screen()
screen.bgcolor("skyblue")

tree = turtle.Turtle()
house = turtle.Turtle()
controller = turtle.Turtle()

tree.hideturtle()
house.hideturtle()
controller.hideturtle()

# Draw tree
def draw_tree():
    tree.penup()
    tree.goto(-200, -150)
    tree.pendown()
    tree.color("brown")
    tree.begin_fill()
    for _ in range(2):
        tree.forward(40)
        tree.left(90)
        tree.forward(100)
        tree.left(90)
    tree.end_fill()
    tree.penup()
    tree.goto(-220, -50)
    tree.pendown()
    tree.color("green")
    tree.begin_fill()
    tree.circle(60)  # Draw tree leaves
    tree.end_fill()

def draw_house():
    house.penup()
    house.goto(50, -150)
    house.pendown()
    house.color("red")
    house.begin_fill()
    for _ in range(4):
        house.forward(100)
        house.left(90)
    house.end_fill()
    house.penup()
    house.goto(50, -50)
    house.pendown()
    house.color("yellow")
    house.begin_fill()
    for _ in range(3):
        house.forward(100)
        house.left(120)
    house.end_fill()

def change_background():
    screen.bgcolor("lightyellow" if screen.bgcolor() == "skyblue" else "skyblue")

# Animate the tree leaves
def animate_tree():
    for size in range(30, 40, 10):  # Grow the tree leaves
        tree.penup()
        tree.goto(-220, -50)
        tree.pendown()
        tree.color("green")
        tree.begin_fill()
        tree.circle(size)
        tree.end_fill()

# Key binds
screen.listen()

screen.onkey(change_background, "b")
screen.onkey(animate_tree, "t")

draw_tree()
draw_house()

screen.mainloop()

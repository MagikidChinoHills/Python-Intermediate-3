import turtle
import random

# Create a screen object
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Shape Drawing")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# List of shapes
shape_var = ["Square", "Triangle", "Circle", "Rectangle", "Octagon"]

# Dictionary to store color values
color_dict = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
}

# Function to calculate the area of a shape
def calculate_area(shape, side1, side2=0):
    if shape == "Square":
        return side1 * side1
    elif shape == "Triangle":
        return 0.5 * side1 * side2
    elif shape == "Circle":
        return 3.14159 * side1 * side1
    elif shape == "Rectangle":
        return side1 * side2
    elif shape == "Octagon":
        return 2 * (1 + 2 ** 0.5) * side1 * side1
    else:
        return 0

# Function to animate a shape
def animate_shape(shape, side1, side2=0):
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()
    
    # Define a color based on area
    area = calculate_area(shape, side1, side2)
    color_name = random.choice(list(color_dict.keys()))
    color = color_dict[color_name]
    pen.color(color)

    if shape == "Square":
        for _ in range(4):
            pen.forward(side1)
            pen.left(90)
    elif shape == "Triangle":
        pen.forward(side1)
        pen.left(120)
        pen.forward(side2)
        pen.left(120)
        pen.forward(side1)
    elif shape == "Circle":
        pen.circle(side1)
    elif shape == "Rectangle":
        for _ in range(2):
            pen.forward(side1)
            pen.left(90)
            pen.forward(side2)
            pen.left(90)
    elif shape == "Octagon":
        for _ in range(8):
            pen.forward(side1)
            pen.left(45)

# Get user input for shape and dimensions
shape_choice = screen.textinput("Shape Choice", f"Choose a shape from: {shape_var}")
while shape_choice not in shape_var:
    shape_choice = screen.textinput("Shape Choice", f"Invalid shape. Choose from: {shape_var}")

side1 = screen.numinput("Side 1", "Enter the length of side 1:", minval=1)
side2 = screen.numinput("Side 2", "Enter the length of side 2 (if applicable):", minval=0)

# Animate the chosen shape
animate_shape(shape_choice, side1, side2)

# Keep the window open until closed manually
screen.exitonclick()

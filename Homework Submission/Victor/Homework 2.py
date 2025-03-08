import turtle

# Set up the turtle and colors
t = turtle.Turtle()
colors = ["red", "yellow", "green", "blue", "purple"]

# Define a function to draw a square
def square(length, color):
    # Set the color of the square
    t.color(colors[color % len(colors)])
    
    # Draw the square if the length is greater than 0
    if length > 0:
        for i in range(4):
            t.forward(length)
            t.right(90)
    
    # If the length is less than or equal to 0, stop drawing
    if length <= 0:
        return
    
    # Recursively draw smaller squares with different colors
    return square(length - 5, color + 1)

# Draw the initial square
square(100, 0)

turtle.done()

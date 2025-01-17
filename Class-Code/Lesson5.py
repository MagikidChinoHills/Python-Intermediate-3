import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
from math import cos, sin, pi

def calculate_area():
    shape = shape_var.get()
    try:
        if shape == "Circle":
            radius = float(entry1.get())
            area = 3.14159 * radius * radius
        elif shape == "Square":
            side = float(entry1.get())
            area = side * side
        elif shape == "Rectangle":
            width = float(entry1.get())
            height = float(entry2.get())
            area = width * height
        elif shape == "Triangle":
            base = float(entry1.get())
            height = float(entry2.get())
            area = 0.5 * base * height
        elif shape == "Pentagon":
            side = float(entry1.get())
            area = (1/4) * (5 ** 0.5 * (5 + 2 * (5 ** 0.5))) * side * side
        elif shape == "Hexagon":
            side = float(entry1.get())
            area = (3 * (3 ** 0.5) * side * side) / 2
        else:
            messagebox.showerror("Error", "Please select a shape")
            return
        
        result_var.set(f"Area: {area:.2f}")
        draw_shape(shape, area)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def update_fields(*args):
    shape = shape_var.get()
    if shape == "Rectangle" or shape == "Triangle":
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
    else:
        label2.grid_forget()
        entry2.grid_forget()

def draw_shape(shape, area):
    canvas.delete("all")
    color = get_color_from_area(area)
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    max_dim = min(canvas_width, canvas_height) * 0.4  # Max dimension to ensure it fits well
    if shape == "Circle":
        radius = float(entry1.get())
        scale = max_dim / (2 * radius)
        animate_circle(canvas_width / 2, canvas_height / 2, radius * scale, color, radius)
    elif shape == "Square":
        side = float(entry1.get())
        scale = max_dim / side
        animate_square(canvas_width / 2, canvas_height / 2, side * scale, color, side)
    elif shape == "Rectangle":
        width = float(entry1.get())
        height = float(entry2.get())
        scale = max_dim / max(width, height)
        animate_rectangle(canvas_width / 2, canvas_height / 2, width * scale, height * scale, color, width, height)
    elif shape == "Triangle":
        base = float(entry1.get())
        height = float(entry2.get())
        scale = max_dim / max(base, height)
        animate_triangle(canvas_width / 2, canvas_height / 2, base * scale, height * scale, color, base, height)
    elif shape == "Pentagon":
        side = float(entry1.get())
        scale = max_dim / side
        animate_pentagon(canvas_width / 2, canvas_height / 2, side * scale, color, side)
    elif shape == "Hexagon":
        side = float(entry1.get())
        scale = max_dim / side
        animate_hexagon(canvas_width / 2, canvas_height / 2, side * scale, color, side)

def get_color_from_area(area):
    # Function to determine color based on area size
    if area < 50:
        return "green"
    elif area < 100:
        return "blue"
    elif area < 200:
        return "yellow"
    else:
        return "red"

def animate_circle(x, y, r, color, original_radius):
    steps = 100
    for i in range(steps + 1):
        canvas.delete("all")
        radius = r * i / steps
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        canvas.update()
        time.sleep(0.01)
    canvas.create_text(x, y + r + 20, text=f"Radius = {original_radius}", fill="black")

def animate_square(x, y, s, color, original_side):
    steps = 100
    for i in range(steps + 1):
        canvas.delete("all")
        side = s * i / steps
        canvas.create_rectangle(x - side / 2, y - side / 2, x + side / 2, y + side / 2, fill=color)
        canvas.update()
        time.sleep(0.01)
    canvas.create_text(x, y + s / 2 + 20, text=f"Side = {original_side}", fill="black")

def animate_rectangle(x, y, w, h, color, original_width, original_height):
    steps = 100
    for i in range(steps + 1):
        canvas.delete("all")
        width = w * i / steps
        height = h * i / steps
        canvas.create_rectangle(x - width / 2, y - height / 2, x + width / 2, y + height / 2, fill=color)
        canvas.update()
        time.sleep(0.01)
    canvas.create_text(x, y + h / 2 + 20, text=f"Width = {original_width}, Height = {original_height}", fill="black")

def animate_triangle(x, y, b, h, color, original_base, original_height):
    steps = 100
    for i in range(steps + 1):
        canvas.delete("all")
        base = b * i / steps
        height = h * i / steps
        canvas.create_polygon(x, y - height / 2, x + base / 2, y + height / 2, x - base / 2, y + height / 2, fill=color)
        canvas.update()
        time.sleep(0.01)
    canvas.create_text(x, y + h / 2 + 20, text=f"Base = {original_base}, Height = {original_height}", fill="black")

def animate_pentagon(x, y, s, color, original_side):
    steps = 100
    for i in range(steps + 1):
        canvas.delete("all")
        side = s * i / steps
        points = calculate_pentagon_points(x, y, side)
        canvas.create_polygon(points, fill=color)
        canvas.update()
        time.sleep(0.01)
    canvas.create_text(x, y + s + 20, text=f"Side = {original_side}", fill="black")

def animate_hexagon(x, y, s, color, original_side):
    steps = 100
    for i in range(steps + 1):
        canvas.delete("all")
        side = s * i / steps
        points = calculate_hexagon_points(x, y, side)
        canvas.create_polygon(points, fill=color)
        canvas.update()
        time.sleep(0.01)
    canvas.create_text(x, y + s + 20, text=f"Side = {original_side}", fill="black")

def calculate_pentagon_points(x, y, s):
    points = []
    for i in range(5):
        angle = 2 * pi * i / 5 - pi / 2
        px = x + s * cos(angle)
        py = y + s * sin(angle)
        points.append((px, py))
    return points

def calculate_hexagon_points(x, y, s):
    points = []
    for i in range(6):
        angle = 2 * pi * i / 6 - pi / 2
        px = x + s * cos(angle)
        py = y + s * sin(angle)
        points.append((px, py))
    return points

root = tk.Tk()
root.title("Area Calculator")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

shape_var = tk.StringVar()
shape_var.trace("w", update_fields)

shapes = ["Circle", "Square", "Rectangle", "Triangle", "Pentagon", "Hexagon"]

ttk.Label(root, text="Select Shape:").grid(row=0, column=0, padx=10, pady=10)
shape_menu = ttk.Combobox(root, textvariable=shape_var, values=shapes)
shape_menu.grid(row=0, column=1, padx=10, pady=10)

label1 = ttk.Label(root, text="Dimension 1:")
label1.grid(row=1, column=0, padx=10, pady=10)
entry1 = ttk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=10)

label2 = ttk.Label(root, text="Dimension 2:")
entry2 = ttk.Entry(root)

result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_area)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

canvas = tk.Canvas(root, width=screen_width, height=screen_height - 200)
canvas.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

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

import tkinter as tk
import random

# --- Global Variables ---
WIDTH = 600
HEIGHT = 400
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
LEFT_SCORE = 0
RIGHT_SCORE = 0
GAME_RUNNING = True

# --- Functions ---
def create_rectangle(canvas, x, y, width, height, color):
    return canvas.create_rectangle(x, y, x + width, y + height, fill=color)

def move_paddle(event):
    global paddle_left, paddle_right

    if event.keysym == 'w':
        y = canvas.coords(paddle_left)[1]
        if y > 0:
            canvas.move(paddle_left, 0, -PADDLE_SPEED)
    elif event.keysym == 's':
        y = canvas.coords(paddle_left)[1]
        if y < HEIGHT - PADDLE_HEIGHT:
            canvas.move(paddle_left, 0, PADDLE_SPEED)

    if event.keysym == 'Up':
        y = canvas.coords(paddle_right)[1]
        if y > 0:
            canvas.move(paddle_right, 0, -PADDLE_SPEED)
    elif event.keysym == 'Down':
        y = canvas.coords(paddle_right)[1]
        if y < HEIGHT - PADDLE_HEIGHT:
            canvas.move(paddle_right, 0, PADDLE_SPEED)

def move_ball():
    global ball, BALL_SPEED_X, BALL_SPEED_Y, LEFT_SCORE, RIGHT_SCORE

    x1, y1, x2, y2 = canvas.coords(ball)

    # Check for collisions with paddles
    if x1 <= PADDLE_WIDTH and y1 <= canvas.coords(paddle_left)[3] and y2 >= canvas.coords(paddle_left)[1]:
        BALL_SPEED_X = -BALL_SPEED_X
    if x2 >= WIDTH - PADDLE_WIDTH and y1 <= canvas.coords(paddle_right)[3] and y2 >= canvas.coords(paddle_right)[1]:
        BALL_SPEED_X = -BALL_SPEED_X

    # Check for collisions with top and bottom walls
    if y1 <= 0 or y2 >= HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Check for ball going off the screen
    if x1 <= 0:
        RIGHT_SCORE += 1
        score_label.config(text=f"Left: {LEFT_SCORE}  Right: {RIGHT_SCORE}")
        reset_ball()
    if x2 >= WIDTH:
        LEFT_SCORE += 1
        score_label.config(text=f"Left: {LEFT_SCORE}  Right: {RIGHT_SCORE}")
        reset_ball()

    canvas.move(ball, BALL_SPEED_X, BALL_SPEED_Y)

    if GAME_RUNNING:
        canvas.after(10, move_ball)

def reset_ball():
    global ball, BALL_SPEED_X, BALL_SPEED_Y

    canvas.coords(ball, WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, 
                  WIDTH / 2 + BALL_SIZE / 2, HEIGHT / 2 + BALL_SIZE / 2)

    BALL_SPEED_X = random.choice([BALL_SPEED_X, -BALL_SPEED_X])
    BALL_SPEED_Y = random.choice([BALL_SPEED_Y, -BALL_SPEED_Y])

def change_ball_speed():
    global BALL_SPEED_X, BALL_SPEED_Y
    BALL_SPEED_X *= 1.2
    BALL_SPEED_Y *= 1.2

def pause_game():
    global GAME_RUNNING
    GAME_RUNNING = not GAME_RUNNING

# --- Create Main Window ---
window = tk.Tk()
window.title("Pong Game")
window.resizable(False, False)

# --- Create Canvas ---
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# --- Create Ball ---
ball = create_rectangle(canvas, WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, 
                       BALL_SIZE, BALL_SIZE, "white")

# --- Create Paddles ---
paddle_left = create_rectangle(canvas, 0, HEIGHT / 2 - PADDLE_HEIGHT / 2, 
                              PADDLE_WIDTH, PADDLE_HEIGHT, "blue")
paddle_right = create_rectangle(canvas, WIDTH - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2, 
                               PADDLE_WIDTH, PADDLE_HEIGHT, "red")

# --- Create Score Label ---
score_label = tk.Label(window, text=f"Left: {LEFT_SCORE}  Right: {RIGHT_SCORE}", 
                       font=("Arial", 20), fg="white", bg="black")
score_label.pack()

# --- Create Buttons ---
change_speed_button = tk.Button(window, text="Change Speed", command=change_ball_speed)
change_speed_button.pack()

pause_button = tk.Button(window, text="Pause", command=pause_game)
pause_button.pack()

# --- Bind Keys ---
window.bind("<w>", move_paddle)
window.bind("<s>", move_paddle)
window.bind("<Up>", move_paddle)
window.bind("<Down>", move_paddle)

# --- Start Game ---
move_ball()
window.mainloop()

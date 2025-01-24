import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Pong Game with Score Tracker")

# Create a canvas for the game
canvas = tk.Canvas(root, width=600, height=300, bg="black")
canvas.pack()

# Create paddles and ball
paddle1 = canvas.create_rectangle(10, 100, 20, 200, fill="white")
paddle2 = canvas.create_rectangle(580, 100, 590, 200, fill="white")
ball = canvas.create_oval(290, 140, 310, 160, fill="white")


# Variables for ball movement
ball_dx = 8
ball_dy = 8

# Initialize scores
score1 = 0
score2 = 0

# Display scores on the canvas
score_display = canvas.create_text(300, 20, text="Player 1: 0   Player 2: 0", fill="white", font=("Arial", 16))

# Function to move paddles
def move_paddle(event):
    key = event.keysym
    if key == "w" and canvas.coords(paddle1)[1] > 0:  # Paddle 1 moves up
        canvas.move(paddle1, 0, -20)
    elif key == "s" and canvas.coords(paddle1)[3] < 300:  # Paddle 1 moves down
        canvas.move(paddle1, 0, 20)
    elif key == "Up" and canvas.coords(paddle2)[1] > 0:  # Paddle 2 moves up
        canvas.move(paddle2, 0, -20)
    elif key == "Down" and canvas.coords(paddle2)[3] < 300:  # Paddle 2 moves down
        canvas.move(paddle2, 0, 20)

# Bind key presses to the paddle movement function
canvas.bind_all("<KeyPress>", move_paddle)

# Function to update the score
def update_score():
    global score1, score2
    canvas.itemconfig(score_display, text=f"Player 1: {score1}   Player 2: {score2}")

# Function to move the ball and handle collisions
def move_ball():
    global ball_dx, ball_dy, score1, score2
    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)

    # Ball collision with top and bottom edges
    if ball_pos[1] <= 0 or ball_pos[3] >= 300:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_pos[0] <= canvas.coords(paddle1)[2] and
        canvas.coords(paddle1)[1] < ball_pos[3] and
        canvas.coords(paddle1)[3] > ball_pos[1]) or \
       (ball_pos[2] >= canvas.coords(paddle2)[0] and
        canvas.coords(paddle2)[1] < ball_pos[3] and
        canvas.coords(paddle2)[3] > ball_pos[1]):
        ball_dx = -ball_dx

    # Ball resets if it goes out of bounds and updates scores
    if ball_pos[0] <= 0:  # Player 2 scores
        score2 += 1
        update_score()
        canvas.coords(ball, 290, 140, 310, 160)  # Reset ball to the center
        ball_dx = abs(ball_dx)  # Ensure ball moves to the right

    if ball_pos[2] >= 600:  # Player 1 scores
        score1 += 1
        update_score()
        canvas.coords(ball, 290, 140, 310, 160)  # Reset ball to the center
        ball_dx = -abs(ball_dx)  # Ensure ball moves to the left

    root.after(30, move_ball)

# Start moving the ball
move_ball()

# Run the application
root.mainloop()

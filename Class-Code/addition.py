
import random

# List of motivational quotes
quotes = [
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "The secret of getting ahead is getting started. – Mark Twain",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Act as if what you do makes a difference. It does. – William James"
]

def show_motivational_quote():
    random_quote = random.choice(quotes)  # Pick a random quote
    messagebox.showinfo("Motivational Quote", random_quote)  # Show it in a message box

# Button to display a motivational quote
quote_button = tk.Button(root, text="Need Motivation?", command=show_motivational_quote)
quote_button.pack(pady=10)  # Add padding for better spacing


# Start the main event loop
root.mainloop()  # Run the Tkinter event loop to display the window and handle user interactions

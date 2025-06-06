import random

choices = ["rock", "paper", "scissors", "sword", "wooden shield", "arrow"]

rules = {
    "rock": ["scissors", "arrow"],
    "paper": ["rock", "wooden shield"],
    "scissors": ["paper"],
    "sword": ["wooden shield", "scissors"],
    "wooden shield": ["arrow", "scissors"],
    "arrow": ["sword", "paper"]
}

win_messages = [
    "You crushed it!",
    "Nice one! You win this round!",
    "Victory is yours!",
    "Boom! You nailed that!",
    "You're unstoppable!"
]

lose_messages = [
    "Oops! Better luck next time!",
    "Oh no, you lost this round!",
    "Computer wins this time!",
    "Defeated! Try again!",
    "Not your lucky round!"
]

def show_help():
    print("Game Rules:")
    print("Rock beats Scissors and Arrow")
    print("Paper beats Rock and Wooden Shield")
    print("Scissors beats Paper")
    print("Sword beats Wooden Shield and Scissors")
    print("Wooden Shield beats Arrow and Scissors")
    print("Arrow beats Sword and Paper")

def play():
    while True:
        print()
        print("Type: rock, paper, scissors, sword, wooden shield, arrow")
        print("Type 'help' to see rules or 'quit' to stop playing")
        player = input("Your move: ").lower()
        if player == "quit":
            print("Thanks for playing!")
            break
        if player == "help":
            show_help()
            continue
        if player not in choices:
            print("That’s not a valid choice.")
            continue
        computer = random.choice(choices)
        print("Computer chose:", computer)
        if player == computer:
            print("It's a tie!")
        elif computer in rules[player]:
            print(random.choice(win_messages))
        else:
            print(random.choice(lose_messages))

play()

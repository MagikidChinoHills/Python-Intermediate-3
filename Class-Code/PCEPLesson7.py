# Lesson 7: Rock, Paper, Scissors Game Using Functions and the Random Module

import random

options = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower().strip()
        if choice in options:
            return choice
        else:
            print("Invalid choice, please try again.")

def get_computer_choice():
    return random.choice(options)

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or \
            (user == "scissors" and computer == "paper") or \
            (user == "paper" and computer == "rock"):
        return "User Wins"
    else:
        return "Computer Wins"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "Tie":
        print("It's a tie!")
    elif winner == "User Wins":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors Game")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        if result == "User Wins":
            user_score += 1
        elif result == "Computer Wins":
            computer_score += 1

        display_result(user_choice, computer_choice, result)
        print(f"Score - You {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()

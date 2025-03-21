'''
import random
import tkinter as tk
from tkinter import messagebox


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        return f"{self.name} took {damage} damage! Health: {self.health}"


class GameUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dice Battle Game")
        self.geometry("400x300")

        self.dice = Dice(6)
        self.player = Character("Wizard", 100, 20)
        self.enemy = Character("Orc", 100, 20)

        # Labels for player and enemy health
        self.player_health = tk.Label(self, text=f"{self.player.name} Health: {self.player.health}")
        self.player_health.pack()

        self.enemy_health = tk.Label(self, text=f"{self.enemy.name} Health: {self.enemy.health}")
        self.enemy_health.pack()

        # Attack button
        self.attack_button = tk.Button(self, text="Roll and Attack", command=self.attack)
        self.attack_button.pack(pady=10)

        # Quit button
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(pady=5)

        # Result display
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def attack(self):
        roll = self.dice.roll()
        if roll < 4:
            result = self.enemy.take_damage(self.player.damage)
            self.result_label.config(text=f"You rolled {roll}. {result}")
        else:
            result = self.player.take_damage(self.enemy.damage)
            self.result_label.config(text=f"You rolled {roll}. {result}")

        # Update health labels
        self.player_health.config(text=f"{self.player.name} Health: {self.player.health}")
        self.enemy_health.config(text=f"{self.enemy.name} Health: {self.enemy.health}")

        # Check for winner
        if self.player.health <= 0:
            messagebox.showinfo("Game Over", "Enemy wins!")
            self.quit()
        elif self.enemy.health <= 0:
            messagebox.showinfo("Game Over", "Player wins!")
            self.quit()


if __name__ == "__main__":
    app = GameUI()
    app.mainloop()
'''


import random

# Card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class Deck:
    def __init__(self):
        self.cards = [card for card in CARD_VALUES.keys()] * 4
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

def calculate_hand(hand):
    total = sum(CARD_VALUES[card] for card in hand)
    aces = hand.count('A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def print_hand(name, hand, hide_first_card=False):
    if hide_first_card:
        print(f"{name} hand: [?, {', '.join(hand[1:])}]")
    else:
        print(f"{name} hand: {', '.join(hand)} (Total: {calculate_hand(hand)})")

def player_turn(deck, player_hand):
    while True:
        print_hand("Your", player_hand)
        if calculate_hand(player_hand) > 21:
            print("You busted!")
            return False
        choice = input("Hit or Stand? (h/s): ").strip().lower()
        if choice == 'h':
            player_hand.append(deck.draw())
        elif choice == 's':
            break

    return True

def dealer_turn(deck, dealer_hand):
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.draw())

def determine_winner(player_hand, dealer_hand):
    player_score = calculate_hand(player_hand)
    dealer_score = calculate_hand(dealer_hand)

    print_hand("Dealer", dealer_hand)

    if player_score > 21:
        print("You busted. Dealer wins!")
    elif dealer_score > 21:
        print("Dealer busted. You win!")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

def play_game():
    deck = Deck()
    player_hand = [deck.draw(), deck.draw()]
    dealer_hand = [deck.draw(), deck.draw()]

    print_hand("Dealer", dealer_hand, hide_first_card=True)

    # Player's turn
    if not player_turn(deck, player_hand):
        print("Dealer wins!")
        return

    # Dealer's turn
    dealer_turn(deck, dealer_hand)

    # Determine winner
    determine_winner(player_hand, dealer_hand)

if __name__ == "__main__":
    print("🃏 Welcome to Blackjack! 🃏")
    play_game()

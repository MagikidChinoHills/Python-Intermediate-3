import tkinter as tk
from tkinter import ttk, messagebox
import random

CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

SUITS = ['♠', '♥', '♦', '♣']

class Deck:
    def __init__(self):
        self.cards = [(value, suit) for value in CARD_VALUES.keys() for suit in SUITS]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class BlackjackGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Blackjack")
        self.geometry("800x500")
        self.configure(bg="#1C1C1C")

        self.balance = 500
        self.bet = 0
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # Balance display
        self.balance_label = ttk.Label(self, text=f"Balance: ${self.balance}", font=("Arial", 20), background="#1C1C1C", foreground="white")
        self.balance_label.pack(pady=10)

        # Bet input
        self.bet_frame = ttk.Frame(self)
        self.bet_frame.pack(pady=5)
        ttk.Label(self.bet_frame, text="Enter Bet:", font=("Arial", 16)).pack(side="left", padx=5)
        self.bet_entry = ttk.Entry(self.bet_frame, font=("Arial", 16), width=10)
        self.bet_entry.pack(side="left", padx=5)
        self.start_button = ttk.Button(self.bet_frame, text="Start", command=self.start_round)
        self.start_button.pack(side="left", padx=5)

        # Status label
        self.status_label = ttk.Label(self, text="", font=("Arial", 18), background="#1C1C1C", foreground="white")
        self.status_label.pack(pady=10)

        # Player cards frame
        self.player_label = ttk.Label(self, text="Your Hand:", font=("Arial", 18), background="#1C1C1C", foreground="white")
        self.player_label.pack()
        self.player_frame = ttk.Frame(self)
        self.player_frame.pack(pady=5)

        # Dealer cards frame
        self.dealer_label = ttk.Label(self, text="Dealer's Hand:", font=("Arial", 18), background="#1C1C1C", foreground="white")
        self.dealer_label.pack()
        self.dealer_frame = ttk.Frame(self)
        self.dealer_frame.pack(pady=5)

        # Buttons for Hit and Stand
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10)
        self.hit_button = ttk.Button(self.button_frame, text="Hit", command=self.hit, state="disabled")
        self.hit_button.pack(side="left", padx=5)
        self.stand_button = ttk.Button(self.button_frame, text="Stand", command=self.stand, state="disabled")
        self.stand_button.pack(side="left", padx=5)

    def reset_game(self):
        self.bet = 0
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.status_label.config(text="")

        for widget in self.player_frame.winfo_children():
            widget.destroy()
        for widget in self.dealer_frame.winfo_children():
            widget.destroy()

        self.hit_button["state"] = "disabled"
        self.stand_button["state"] = "disabled"

        self.update_display()

    def start_round(self):
        try:
            self.bet = int(self.bet_entry.get())
            if self.bet <= 0 or self.bet > self.balance:
                messagebox.showerror("Invalid Bet", "Invalid bet amount.")
                return
        except ValueError:
            messagebox.showerror("Invalid Bet", "Please enter a valid bet.")
            return

        self.balance -= self.bet
        self.update_display()

        # Deal initial cards
        self.player_hand = [self.deck.draw(), self.deck.draw()]
        self.dealer_hand = [self.deck.draw(), self.deck.draw()]

        self.display_cards(self.player_hand, self.player_frame)
        self.display_cards(self.dealer_hand[:1], self.dealer_frame)  # Hide second dealer card

        self.hit_button["state"] = "normal"
        self.stand_button["state"] = "normal"

        if self.calculate_hand(self.player_hand) == 21:
            self.end_round("Blackjack! You win!")

    def hit(self):
        self.player_hand.append(self.deck.draw())
        self.display_cards(self.player_hand, self.player_frame)

        if self.calculate_hand(self.player_hand) > 21:
            self.end_round("Busted! Dealer wins.", win=False)

    def stand(self):
        self.hit_button["state"] = "disabled"
        self.stand_button["state"] = "disabled"

        while self.calculate_hand(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw())

        self.display_cards(self.dealer_hand, self.dealer_frame)
        self.check_winner()

    def calculate_hand(self, hand):
        total = sum(CARD_VALUES[card[0]] for card in hand)
        aces = sum(1 for card in hand if card[0] == 'A')

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def check_winner(self):
        player_score = self.calculate_hand(self.player_hand)
        dealer_score = self.calculate_hand(self.dealer_hand)

        if dealer_score > 21:
            self.end_round("Dealer busts! You win!", win=True)
        elif player_score > dealer_score:
            self.end_round("You win!", win=True)
        elif player_score < dealer_score:
            self.end_round("Dealer wins.", win=False)
        else:
            self.end_round("It's a tie!", tie=True)

    def end_round(self, result, win=False, tie=False):
        self.status_label.config(text=result)

        if win:
            self.balance += self.bet * 2
        elif tie:
            self.balance += self.bet

        self.update_display()

        # Reset after a short delay
        self.after(2000, self.reset_game)

    def display_cards(self, hand, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        for card in hand:
            value, suit = card
            card_text = f"{value}{suit}"
            label = ttk.Label(frame, text=card_text, font=("Arial", 24), background="#1C1C1C", foreground="white", padding=5)
            label.pack(side="left", padx=5)

    def update_display(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

if __name__ == "__main__":
    app = BlackjackGame()
    app.mainloop()

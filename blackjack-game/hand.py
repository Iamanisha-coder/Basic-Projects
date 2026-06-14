from .card import Card

VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class Hand:
    """Represents the cards held by either the player or the dealer."""
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.value += VALUES[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self) -> None:
        # If total value is over 21 and we have aces, convert Ace from 11 to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

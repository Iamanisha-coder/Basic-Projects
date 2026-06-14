import random
from .card import Card

SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def deal(self) -> Card:
        return self.deck.pop()

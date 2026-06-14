from .deck import Deck
from .hand import Hand

class BlackjackGame:
    """Controls the core game flow and rules."""
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def display_hands(self, hide_dealer_card: bool = True) -> None:
        print("\n" + "="*35)
        if hide_dealer_card:
            print(f"Dealer's Hand: [{self.dealer_hand.cards[0]}], [Hidden]")
        else:
            print(f"Dealer's Hand: {', '.join(str(c) for c in self.dealer_hand.cards)} (Total: {self.dealer_hand.value})")
        
        print(f"Your Hand:   {', '.join(str(c) for c in self.player_hand.cards)} (Total: {self.player_hand.value})")
        print("="*35)

    def play(self) -> None:
        print("\n♣ ♦ ♥ ♠ Blackjack Turn ♠ ♥ ♦ ♣")
        
        # Initial Deal
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

        self.player_hand.adjust_for_ace()
        self.dealer_hand.adjust_for_ace()

        # Player's Loop
        while self.player_hand.value < 21:
            self.display_hands(hide_dealer_card=True)
            choice = input("Would you like to [H]it or [S]tand? ").strip().lower()
            
            if choice in ['h', 'hit']:
                self.player_hand.add_card(self.deck.deal())
                self.player_hand.adjust_for_ace()
            elif choice in ['s', 'stand']:
                break
            else:
                print("Invalid input! Enter 'H' or 'S'.")

        # Check Player Bust
        if self.player_hand.value > 21:
            self.display_hands(hide_dealer_card=False)
            print("\n💥 You busted! Dealer wins.")
            return

        # Dealer's Loop
        print("\nDealer reveals hidden card...")
        while self.dealer_hand.value < 17:
            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_hand.adjust_for_ace()

        self.display_hands(hide_dealer_card=False)

        # Game Resolution
        if self.dealer_hand.value > 21:
            print("\n🎉 Dealer busted! You win!")
        elif self.player_hand.value > self.dealer_hand.value:
            print("\n🎉 You win!")
        elif self.player_hand.value < self.dealer_hand.value:
            print("\n📉 Dealer wins.")
        else:
            print("\n🤝 It's a Push (Tie)!")

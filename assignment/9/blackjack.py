import random


class Card:
    SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return ", ".join([str(c) for c in self.cards])

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ", ".join([str(c) for c in self.cards])

    def get_value(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self.get_value() == other.get_value()

    def __lt__(self, other):
        return self.get_value() < other.get_value()


class BlackJackHand(Hand):
    """
        BlackJackHand should inherit from the Hand class
        missing methods: get_value() and is_bust()
    """
    def get_value():
        


class BlackJackGame:
    def start(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer_hand = BlackJackHand()
        self.player_hand = BlackJackHand()
        for i in range(2):
            self.dealer_hand.add_card(self.deck.deal())
            self.player_hand.add_card(self.deck.deal())
        self._loop()

    def _loop(self):
        print("Dealer's cards are: ", self.dealer_hand)
        print("Your cards are: ", self.player_hand)
        choice = None
        while choice != "s":
            choice = input('Press "h" to hit or "s" to stand: ')
            if choice == "h":
                card = self.deck.deal()
                self.player_hand.add_card(card)
                print("You drew {}".format(card))
                print("Now you have: ", self.player_hand)
                if self.player_hand.is_bust():
                    print("You went bust! Game over!")
                    return
        while self.dealer_hand.get_value() < 17:
            card = self.deck.deal()
            print("Dealer drew {}".format(card))
            self.dealer_hand.add_card(card)
            if self.dealer_hand.is_bust():
                print("The dealer went bust! You win!")
                return

        if self.player_hand > self.dealer_hand:
            print("You win!")
        elif self.player_hand < self.dealer_hand:
            print("You lose!")
        else:
            print("This is a tie!")
        print("Final scores: Dealer({}) You({})".format(self.dealer_hand.get_value(), self.player_hand.get_value()))

if __name__ == "__main__":
    """
    TODO: let the player play for as many rounds as s/he likes and keep a score of wins and loses
    """
    print("Let's play a game of blackjack!")
    game = BlackJackGame()
    game.start()

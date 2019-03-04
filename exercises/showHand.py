import random

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

deck = []

for rank in RANKS:
    for suit in SUITS:
        card = "{} of {}".format(rank, suit)
        deck.append(card)

print(deck)

namedCards = []
for i in range(5):
    index = random.randrange(len(deck))
    card = deck.pop(index)
    namedCards.append(card)

print(namedCards)

#pick up the biggest card
rankCounts = {}

maxNum = 0 
biggestCard = None
for selctedCard in namedCards:
    #pick up one card, which stores in the "namedCard" list.
    rank , suit = selctedCard.split(" of ") 
    #split the selected card (selctedCard) into two catagories: rank and suit.
    compare = RANKS.index(rank) * 10 + SUITS.index(suit) 
    #index "rank" and "suit" into their lists and output the value of their orders. Since "rank" should be considered first, we ten times it.
    if compare > maxNum:
        maxNum = compare
        biggestCard = selctedCard
    #calculate the times of ranks of each appearance of selectedCards
    if rank in rankCounts:
        rankCounts[rank] += 1
    else:
        rankCounts[rank] = 1

print(biggestCard)
print(rankCounts)
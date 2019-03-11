import random
from collections import defaultdict

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
SUITS = ['Diamonds', 'Clubs', 'Hearts', 'Spades']

def getDeck(): #return a deck of cards in tuples
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append((rank, suit))
    return deck

def dealCards(deck,n): #randomly deal n cards from deck
    cards = []
    if len(deck) < n: 
        n = len(deck)
    for i in range(n):
        index = random.randrange(len(deck)) #return a randome number from 0 to the length of the deck (which initial value is 52)
        card = deck.pop(index)
        cards.append(card)
    return cards 

def getTopCard(cards):
    topValue = 0
    topCard = None
    for card in cards:
        rank, suit = card
        value = RANKS.index(rank) * 10 + SUITS.index(suit)
        if value > topValue:
            topValue = value
            topCard = card
    return topCard

def getRankCounts(cards):
    rankCounts = defaultdict(int) #append a new-appeared value into the dictionary as an int
    for rank, suit in cards:
        rankCounts[rank] += 1
    return rankCounts

def getPatternValue(hand):
    #return the pattern value of a hand based on PATTERN_VALUE
    PATTERN_VALUE = {"straight flush": 80, "4 of a kind": 70, "full house": 60, "flush": 50, "straight": 40, "3 of a kind": 30, "2 pairs": 20, "1 pair": 10, "high card": 0}

    def isFlush(hand):
        selectedSuits = []
        for rank, suit in hand:
            selectedSuits.append(suit)
        return len(set(selectedSuits)) == 1

    def isStraight(hand):
        topCard = getTopCard(hand)
        topRankIndex = RANKS.index(topCard[0]) #get the position of the largest number of a hand
        straightRanks = RANKS[topRankIndex-4:topRankIndex+1] #make a list of straight from the previous values in RANKS to topCard
        ranks = []
        for rank, suit in hand:
            ranks.append(rank)
        return set(ranks) == set(straightRanks)

    #straight flush:
    isFlush(hand)
    isStraight(hand)
    if isFlush == True and isStraight == True:
        return PATTERN_VALUE["straight flush"]
    
    #4 of a kind:
    selectedRanks = []
    selectedSuits = []
    for rank, suit in hand:
        selectedRanks.append(rank)
        selectedSuits.append(suit)
    if 


deck = getDeck()
hand = dealCards(deck, 5)
print(hand)

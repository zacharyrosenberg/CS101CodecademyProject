import random

suits = ['spade', 'club', 'heart', 'diamond']
values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
nameToValue = {'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
playerHand = []
class Cards:
    def  __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return '({value}, {suit})'.format(value = self.value, suit = self.suit)

class Dealer(Cards):
    def __init__(self, hand = []):
        self.hand = hand
        self.total = 0
    
    def dealCards(self, hand):
        if len(self.hand) == 0:
            for i in range(0,2):
                self.hand.append(deck.pop(random.randrange(len(deck))))
                playerHand.append(deck.pop(random.randrange(len(deck))))
        for cards in self.hand:
            if cards.value in nameToValue:
                self.total += nameToValue[cards.value]
            else:
                self.total += cards.value
            

        


        
        
        


deck = [Cards(value, suit) for value in values for suit in suits]  
#print(deck)
casino = Dealer()
casino.dealCards(hand = [])
print(casino.hand)
#print(playerHand)
#print(deck)
print(casino.total)





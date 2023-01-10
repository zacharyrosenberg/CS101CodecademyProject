suits = ['spade', 'club', 'heart', 'diamond']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
class Cards:
    def  __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return '({value}, {suit})'.format(value = self.value, suit = self.suit)



Deck = [Cards(value, suit) for value in values for suit in suits]  
print(Deck)




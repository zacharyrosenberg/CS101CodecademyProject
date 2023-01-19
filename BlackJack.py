import random

suits = ['spade', 'club', 'heart', 'diamond']
values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
nameToValue = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
playerHand = []
playerTotal = 0

class Cards:
    def  __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return '({value}, {suit})'.format(value = self.value, suit = self.suit)

class Dealer(Cards):
    def __init__(self):
        self.hand = []
        self.total = 0
    
    def dealCards(self):
        for i in range(0,2):
            self.hand.append(deck.pop(random.randrange(len(deck))))
            playerHand.append(deck.pop(random.randrange(len(deck))))
        for cards in self.hand:
            self.total += nameToValue[cards.value]
    


    def dealerHit(self):
        while self.total < 17:
            self.hand.append(deck.pop(random.randrange(len(deck))))
            for cards in self.hand:
                if cards.value in nameToValue:
                    self.total += nameToValue[cards.value]
                else:
                    self.total += cards.value
        if self.total > 21:
            print('The dealer went bust! You win $')
        
class Player(Cards):
    def __init__(self):
        self.hand = playerHand
        self.total = playerTotal
        self.money = int(input('How much money do you want to bet?: '))

    def play(self):
        playerInput = input('Do you want to hit, stand, double down, or split?: ')
        if playerInput == 'hit' or playerInput == 'Hit':
            self.hand.append(deck.pop(random.randrange(len(deck))))
            if self.total > 22:
                print('You went over 21, you lose.')
            else:
                pass
        elif playerInput == 'stand' or playerInput == 'Stand':
            pass
        elif playerInput == 'double down' or playerInput == 'Double Down':
            self.money = self.money * 2 
        

###The dealerHit and play methods are bugged. Also, when you play again after already playing a hand, the hands do not reset

        



casino = Dealer()
person1 = Player()
gameOn = True
deck = [Cards(value, suit) for value in values for suit in suits]


def game():
    casino.dealCards()
    #casino.dealerHit()
    print(str(casino.hand) + ' casino hand')
    print(str(playerHand) + ' your hand')
    print(casino.total)
    print(person1.total)
    person1.play()





while gameOn:
    print('Welcome to Blackjack! Do you want to play?')
    userInput = input('Yes or No: ')
    if userInput == 'Yes' or userInput == 'yes':
       game()
    else:
        print('So long and have a nice day!')
        gameOn = False
        

    

  
#print(deck)

#casino.dealCards(hand = [])
#print(casino.hand)
#print(playerHand)
#print(deck)
#print(casino.total)
#print(playerTotal)





import random

suits = ['spade', 'club', 'heart', 'diamond']
values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
nameToValue = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}


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
            person1.hand.append(deck.pop(random.randrange(len(deck))))
        for i in range(0,1):
            self.hand.append(deck.pop(random.randrange(len(deck))))
        for cards in self.hand:
            self.total += nameToValue[cards.value]
        for cards in person1.hand:
            person1.total += nameToValue[cards.value]

    def dealerHit(self):
        while self.total < 17:
            self.hand.append(deck.pop(random.randrange(len(deck))))
            self.total += nameToValue[self.hand[-1].value]
        print(str(self.hand) + ' casino hand')
        if self.total > 21:
            print('The dealer went bust! You win $' + str(person1.money))
        elif self.total > person1.total:
            print('The dealer wins. You lose $' + str(person1.money) + ' :(.')
        elif self.total < person1.total:
            print('You win $' + str(person1.money) + '!')
        elif self.total == person1.total:
            print('You push!')
        else:
            pass

                
class Player(Cards):
    def __init__(self):
        self.hand = []
        self.total = 0
        self.money = int(input('Welcome to Blackjack with Chuck! How much money do you want to bet?: '))

    def play(self):
        global gameOn
        while gameOn:
            playerInput = input('Do you want to hit, stand, double down, or split?: ')
            if playerInput == 'hit' or playerInput == 'Hit':
                self.hand.append(deck.pop(random.randrange(len(deck))))
                self.total += nameToValue[self.hand[-1].value]
                print(str(person1.hand) + ' your hand')
                if self.total > 22:
                    print('You went over 21, you lose $' + str(self.money) + '.')
                    gameOn = False
                else:
                    pass
            elif playerInput == 'stand' or playerInput == 'Stand':
                print('You stand.')
                gameOn = False
            elif playerInput == 'double down' or playerInput == 'Double Down':
                print('You doubled you bet to $' + str(self.money * 2) + '.')
                self.money = self.money * 2 
                gameOn = False
        
def game():
    casino.dealCards()
    print(str(casino.hand) + ' casino hand')
    print(str(person1.hand) + ' your hand')
    person1.play()
    casino.dealerHit()
    question = input('Do you want to play again?: ')
    if question == 'Yes' or question == 'yes':
        person1.hand = []
        person1.total = 0
        casino.hand = []
        casino.total = 0
        deck = [Cards(value, suit) for value in values for suit in suits]
        game()
    else:
        print('Have a nice day!')
        gameOn = False
    
deck = [Cards(value, suit) for value in values for suit in suits]
casino = Dealer()
person1 = Player()
gameOn = True

while gameOn:
    game()
        

    
### KNOWN BUGS: - Saying yes to play again doesnt ask for user input.
### - Must add blackjack feature (ie dealt 21)
### - If I go over 21 I lose money, but my total is higher than casino, so it prints I win as well(dealer hit method)


  


#print(deck)

#casino.dealCards(hand = [])
#print(casino.hand)
#print(playerHand)
#print(deck)
#print(casino.total)
#print(playerTotal)





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
        global gameOn
        self.hand.append(deck.pop(random.randrange(len(deck))))
        for i in range(0,2):
            person1.hand.append(deck.pop(random.randrange(len(deck))))
        print(str(casino.hand) + ' casino hand')
        print(str(person1.hand) + ' your hand')
        value = []
        for cards in person1.hand:
            value.append(cards.value)
        if 'ace' in value and (10 in value or 'jack' in value or 'queen' in value or 'king' in value):
            questionLoop()
        else:
            pass
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
        self.secondHand = []
        self.total = 0
        self.secondHandTotal = 0
        self.money = float(input('Welcome to Blackjack with Chuck! How much money do you want to bet?: '))
        self.secondHandMoney = 0

    def play(self):
        global gameOn
        while gameOn:
            playerInput = input('Do you want to hit, stand, or double down?: ')
            if playerInput == 'hit' or playerInput == 'Hit':
                self.hand.append(deck.pop(random.randrange(len(deck))))
                self.total += nameToValue[self.hand[-1].value]
                print('You hit. Here is your hand: ' + str(person1.hand))
                if self.total > 22:
                    print('You went over 21, you lose $' + str(self.money) + '.')
                    questionLoop()
                else:
                    pass
            elif playerInput == 'stand' or playerInput == 'Stand':
                print('You stand.')
                gameOn = False
            elif playerInput == 'double down' or playerInput == 'Double Down':
                print('You doubled you bet to $' + str(self.money * 2) + '.')
                self.money = self.money * 2 
                gameOn = False
            #elif playerInput == 'split' or playerInput == 'Split':
                #value = []
                #for cards in self.hand:
                    #value.append(cards.value)
                #if value[0] == value[1]:
                    #self.secondHand.append(self.hand.pop(1))
                    #self.total -= self.secondHand[0].value
                    #self.secondHandTotal += self.secondHand.value
                    #print('You split. Here are your two hands:' + str(self.hand) + ' ' + str(self.secondHand))
                    #self.secondHandMoney = float(int('How much money do you want to bet for your second hand?: '))
                #else:
                    #print('You cannot split!')
            else:
                print('Not sure what you mean. Try again.')

def reset():
    global deck
    global gameOn
    person1.hand = []
    person1.total = 0
    person1.money = float(input('How much money do you want to bet?: '))
    casino.hand = []
    casino.total = 0
    deck = [Cards(value, suit) for value in values for suit in suits]
    gameOn = True
    
def questionLoop():
    question = input('Do you want to play again?: ')
    loop = True
    while loop:
        if question == 'Yes' or question == 'yes':
            loop = False
            reset()
            game()
        elif question == 'No' or question == 'no':
            loop = False
            print('Have a nice day!')
            gameOn = False
            exit()
        else:
            print('Not sure what you mean. Try again.')
            question = input('Do you want to play again?: ')

def game():
    casino.dealCards()
    person1.play()
    casino.dealerHit()
    questionLoop()
    
deck = [Cards(value, suit) for value in values for suit in suits]
casino = Dealer()
person1 = Player()
gameOn = True

while gameOn:
    game()
        

### FEATURES TO ADD:
### - Split function.
### - Let Ace be 1 or 11


  





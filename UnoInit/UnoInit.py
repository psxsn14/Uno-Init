#UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

#Suggestions:
# Please go through this architecture, sparingly get familiarised with my coding style, and let us know if there's something off, or if you have a much better structure.
# I have written some code to check certain things as you see below. I will flesh it out more by tomorrow.
# I will reference "to-be-written" code snippets in a numbered way for each function so that it's easy to communicate any difficulties. i.e "Stuck at <functionname> #2" as in the startGame function.
# Feel free to suggest any ideas in general without hesitation.
# Please familiarize yourself with gitlab/gitkraken by Friday and use this .py to try new things as it already has an implementation of a shuffled deck.

import random
import copy

class Uno:
    def __init__(self):
        self.greenCards = []
        self.yellowCards = []
        self.blueCards = []
        self.redCards = []
        self.blackCards = []

        self.AICards = []
        self.discardPile = []
        self.drawPile = []
        self.isGameOn = True
        self.playerList = []
        self.humanPlayer = None
    
    #Create a new shuffled deck.
    def createNewDeck(self):
        #Create and save all new UnoCard objects to their respective lists.
        
        self.greenCards = [UnoCard("Green", "Normal", i, i) for i in range(0,10)] + [UnoCard("Green", "Normal", i, i) for i in range(1,10)] \
                        + [UnoCard("Green", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Green", "Reverse", "None", 20) for _ in range(0,2)] \
                        + [UnoCard("Green", "Draw Two", "None", 20) for _ in range(0,2)]

        self.blueCards = [UnoCard("Blue", "Normal", i, i) for i in range(0,10)] + [UnoCard("Blue", "Normal", i, i) for i in range(1,10)] \
                       + [UnoCard("Blue", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Blue", "Reverse", "None", 20) for _ in range(0,2)] \
                       + [UnoCard("Blue", "Draw Two", "None", 20) for _ in range(0,2)] 

        self.yellowCards = [UnoCard("Yellow", "Normal", i, i) for i in range(0,10)] + [UnoCard("Yellow", "Normal", i, i) for i in range(1,10)] \
                         + [UnoCard("Yellow", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Yellow", "Reverse", "None", 20) for _ in range(0,2)] \
                         + [UnoCard("Yellow", "Draw Two", "None", 20) for _ in range(0,2)]

        self.redCards = [UnoCard("Red", "Normal", i, i) for i in range(0,10)] + [UnoCard("Red", "Normal", i, i) for i in range(1,10)] \
                      + [UnoCard("Red", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Red", "Reverse", "None", 20) for _ in range(0,2)] \
                      + [UnoCard("Red", "Draw Two", "None", 20) for _ in range(0,2)]

        self.blackCards = [UnoCard("Black", "ColorChange", "None", 50) for _ in range(0,4)] + [UnoCard("Black", "Draw Four", "None", 50) for _ in range(0,4)]
        
        #Combine, shuffle and return the deck as a list of UnoCard objects.
        shuffledDeck = self.greenCards + self.yellowCards + self.redCards + self.blueCards + self.blackCards
        
        random.shuffle(shuffledDeck)
        return shuffledDeck

    #Deal cards to a player and update the drawPile.
    def dealCards(self, playerDeck):
        for UnoCard in self.drawPile[0:7]:
            playerDeck.append(UnoCard)   
        
        #3)Drop those cards from the "drawPile".
            self.drawPile.pop(self.drawPile.index(UnoCard))
        return self.drawPile
        

    def startPreGame(self, shuffledNewDeck):
        # Create draw pile out of our shuffled deck.
        self.drawPile = shuffledNewDeck

        # Add human player to the list of player.
        self.humanPlayer = Player(1)
        self.playerList.append(self.humanPlayer)

        # Ask for number of players.
        AICount = int(input("Enter number of AI opponents to play against: "))
        for i in range(0, AICount):
            self.playerList.append(copy.deepcopy(AIPlayer(i+2)))
           
        for i in self.playerList:
            print("\n",id(i))

    #2) Deal 7 cards to player and AIs.
        
        print("\nPile before Player draw: ---- ----- --- \n")
        for i in self.drawPile:
           print(repr(i))
        
        for eachPlayer in self.playerList:
            self.drawPile = self.dealCards(eachPlayer.plDeck)
        
        #DEBUG Check all player decks.
        for i in self.playerList:
            print("\n")
            print(repr(i))



class Player():
    def __init__(self, playerNo, plDeck = []):
        self.playerNo = playerNo
        self.plDeck = plDeck

    def playTurn(self):
        #Select a card from your hand, and place it below the discard pile.
        pass

    def __repr__(self):
        playerTemp = []
        for i in self.plDeck:
            playerTemp.append(i)

        return repr(f"Name: {type(self)} | Deck: {playerTemp}")

class AIPlayer(Player):
    pass
    #Insert AI Code.
        
        

#Card class.
class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber = "None", cardValue = "None"):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue
        

    def __repr__(self):
        return repr(f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")


newGame = Uno()

newGame.startPreGame(newGame.createNewDeck())










#UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

#Suggestions:
# Please go through this architecture, sparingly get familiarised with my coding style, and let us know if there's something off, or if you have a much better structure.
# I have written some code to check certain things as you see below. I will flesh it out more by tomorrow.
# I will reference "to-be-written" code snippets in a numbered way for each function so that it's easy to communicate any difficulties. i.e "Stuck at <functionname> #2" as in the startGame function.
# Feel free to suggest any ideas in general without hesitation.
# Please familiarize yourself with gitlab/gitkraken by Friday and use this .py to try new things as it already has an implementation of a shuffled deck.

import random

class Uno:
    def __init__(self):
        self.greenCards = []
        self.yellowCards = []
        self.blueCards = []
        self.redCards = []
        self.blackCards = []

        self.playerCards = []
        self.AICards = []
        self.discardPile = []
        self.inUsePile = []
        self.isGameOn = True
    
    #Create a new shuffled deck.
    def createNewDeck(self):
        #Create and save all new UnoCard objects to their respective lists.
        
        self.greenCards = [UnoCard("Green", "Normal", i, i) for i in range(0,10)] + [UnoCard("Green", "Normal", i, i) for i in range(1,10)] + [UnoCard("Green", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Green", "Reverse", "None", 20) for _ in range(0,2)] + [UnoCard("Green", "DrawTwo", "None", 20) for _ in range(0,2)]

        self.blueCards = [UnoCard("Blue", "Normal", i, i) for i in range(0,10)] + [UnoCard("Blue", "Normal", i, i) for i in range(1,10)] + [UnoCard("Blue", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Blue", "Reverse", "None", 20) for _ in range(0,2)] + [UnoCard("Blue", "DrawTwo", "None", 20) for _ in range(0,2)]

        self.yellowCards = [UnoCard("Yellow", "Normal", i, i) for i in range(0,10)] + [UnoCard("Yellow", "Normal", i, i) for i in range(1,10)] + [UnoCard("Yellow", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Yellow", "Reverse", "None", 20) for _ in range(0,2)] + [UnoCard("Yellow", "DrawTwo", "None", 20) for _ in range(0,2)]

        self.redCards = [UnoCard("Red", "Normal", i, i) for i in range(0,10)] + [UnoCard("Red", "Normal", i, i) for i in range(1,10)] + [UnoCard("Red", "Skip", "None", 20) for _ in range(0,2)] + [UnoCard("Red", "Reverse", "None", 20) for _ in range(0,2)] + [UnoCard("Red", "DrawTwo", "None", 20) for _ in range(0,2)]

        self.blackCards = [UnoCard("Black", "ColorChange", "None", 50) for _ in range(0,4)] + [UnoCard("Black", "Draw4", "None", 50) for _ in range(0,4)]
        
        #Combine, shuffle and return the deck as a list of UnoCard objects.
        shuffledDeck = self.greenCards + self.yellowCards + self.redCards + self.blueCards + self.blackCards
        
        random.shuffle(shuffledDeck)
        return shuffledDeck

    #Deal cards to a player and update the inUsePile.
    def dealCards(self, playerHand, inUsePile):
        for UnoCard in inUsePile[0:7]:
            playerHand.append(UnoCard)   
        
        #3)Drop those cards from the "inUsePile".
            self.inUsePile.pop(inUsePile.index(UnoCard))
        return inUsePile
        

    def startPreGame(self, shuffledNewDeck):
        self.inUsePile = shuffledNewDeck
    #Do Pre-game stuff.
    #Gameplay loop:
    #1) Create a pile of shuffled cards. (DONE)
        
    #2) Deal 7 cards to player and AI.
    #DEBUG to check updated piles.
        print("\nPile before Player draw: ---- ----- --- \n")
        for i in self.inUsePile:
           print(repr(i))
        self.inUsePile = self.dealCards(self.playerCards, self.inUsePile)
        print("\nPlayer's first seven cards: ---- ----- --- \n")
        for i in self.playerCards:
            print(repr(i))

        #DEBUG to check updated piles.
        print("\nPile after Player draw: ---- ----- --- \n")
        for i in self.inUsePile:
           print(repr(i))
        
        #2) Deal cards to AI.
        self.inUsePile = self.dealCards(self.AICards, self.inUsePile)
        
        #DEBUG to check updated piles. 
        print("\nAI's first seven cards: ---- ----- --- \n")
        for i in self.AICards:
            print(repr(i))

        print("\nPile after AI draw: ---- ----- --- \n")    
        for i in self.inUsePile:
            print(repr(i))

        #3) Place remaining cards facedown to form a draw pile. (DONE)

        

    #Player either views their cards and / or makes a choice.
    def askPlayer(self):
        playerChoice = input("\nPress 1 to see your cards -- Press 2 to select a card...")
        if int(playerChoice) == 1:
            playerChoice = self.viewCardsAndMakeChoice()
            self.askPlayer()
        elif int(playerChoice) == 2:
            #self.selectACard(playerChoice)
            pass

    def viewCardsAndMakeChoice(self):
        for index,value in enumerate(self.playerCards):
            print(f"\nCard: {index + 1} | {repr(value)}")
        playerChoice = self.askPlayer()
        return playerChoice

    #CURRENT
    def selectACard(self, selectedCard):
        #Handle invalid cards.
        #if(selectedCard.cardColour)
        pass


    def askAI(self):
        print("\nAI MAKES A MOVE\n")



#Card class.
class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber = "None", cardValue = "None"):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue
        

    def __repr__(self):
        return repr(f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")

#MAIN
#Create a new Uno object. 
UnoObj = Uno()

#Call createNewDeck and create a shuffled deck, amd init pre-game facilities.
UnoObj.startPreGame(UnoObj.createNewDeck())

#Start gameplay loop.

while UnoObj.isGameOn:
    UnoObj.askPlayer()
    UnoObj.askAI()







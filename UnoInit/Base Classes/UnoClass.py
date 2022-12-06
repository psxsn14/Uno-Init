import random
import copy
from .. import PlayerClass
#Class handling the game.
class Uno:
    drawPile = []
    discardPile = []
    def __init__(self):
        #Instance variables for card groups.
        self.greenCards = []
        self.yellowCards = []
        self.blueCards = []
        self.redCards = []
        self.blackCards = []

        #Instance variables for game entities.
        self.AICards = []
        self.discardPile = []
        self.playerList = []
        self.isGameOver = False
        self.currentGameColour = ""
        #Top card from the discard pile that sets the current game colour.
        self.topDiscardPileCard = None
    
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

    #Deal cards to a player and update the self.drawPile.
    def dealCards(self, playerDeck):
        #Hand out top 7 cards from the draw pile to the current player's deck.
        for UnoCard in self.drawPile[0:7]:
            playerDeck.append(UnoCard)   
        
        #Drop those cards from the "self.drawPile".
            self.drawPile.pop(self.drawPile.index(UnoCard))
        return self.drawPile
        
    #Execute all the pre-game / pre - player activity routines.
    def startPreGame(self, shuffledNewDeck):
        # Create draw pile out of our shuffled deck.
        self.drawPile = shuffledNewDeck

        # Add human player to the list of player.
        self.humanPlayer = PlayerClass.Player(1)
        self.playerList.append(self.humanPlayer)

        # Ask for number of players.
        AICount = int(input("Enter number of AI opponents to play against: "))
        for i in range(0, AICount):
            self.playerList.append(copy.deepcopy(PlayerClass.AIPlayer(i+2)))

        #Deal 7 cards to player and AIs.
        #DEBUG
        print("\nPile before Player draw: ---- ----- --- \n")
        for i in self.drawPile:
           print(repr(i))
        ###
        
        for eachPlayer in self.playerList:
            self.drawPile = self.dealCards(eachPlayer.plDeck)
        
        #DEBUG Check all player decks.
        for i in self.playerList:
            print("\n")
            print(repr(i))
        
        #DEBUG
        print("\nPile after all player draw: ---- ----- --- \n")
        for i in self.drawPile:
           print(repr(i))
        ###

    def startGame(self):
        self.topDiscardPileCard = self.drawPile[0]
        print(f"\nTop card of the draw pile forms the discard pile: {self.topDiscardPileCard}")
        self.currentGameColour = self.topDiscardPileCard.cardColour
        self.discardPile.append(self.topDiscardPileCard)
        self.drawPile.pop(0)
        self.drawPile, self.discardPile = self.playerList[0].playTurn(self.drawPile, self.currentGameColour, self.discardPile)


#Uno Card class.
class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber = "None", cardValue = "None"):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue
        

    def __repr__(self):
        return repr(f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")
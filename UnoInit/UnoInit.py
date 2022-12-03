# UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

# Suggestions:
# Please go through this architecture, sparingly get familiarised with my coding style, and let us know if there's something off, or if you have a much better structure.
# I have written some code to check certain things as you see below. I will flesh it out more by tomorrow.
# I will reference "to-be-written" code snippets in a numbered way for each function so that it's easy to communicate any difficulties. i.e "Stuck at <functionname> #2" as in the startGame function.
# Feel free to suggest any ideas in general without hesitation.
# Please familiarize yourself with gitlab/gitkraken by Friday and use this .py to try new things as it already has an implementation of a shuffled deck.

# testesttetststseteststststesetsetstsetetestsees

# hihi
from ctypes.wintypes import VARIANT_BOOL
from pickle import NONE
import random
import copy
import pygame
pygame.init()
from pygame.locals import *
import time


screen = pygame.display.set_mode((1366,768))



# Class handling the game.
class Uno:
    drawPile = []
    discardPile = []

    def __init__(self):
        # Instance variables for card groups.
        self.greenCards = []
        self.yellowCards = []
        self.blueCards = []
        self.redCards = []
        self.blackCards = []

        # Instance variables for game entities.
        self.AICards = []
        self.discardPile = []
        self.playerList = []
        self.isGameOver = False
        self.currentGameColour = ""
        # Top card from the discard pile that sets the current game colour.
        self.topDiscardPileCard = None

        #Card variables
        self.image = pygame.image.load('card_back.png')
        self.image_small = pygame.transform.smoothscale(self.image,(100,150))
        self.image_small = pygame.transform.rotate(self.image_small,90)
        self.image_right = pygame.transform.rotate(self.image_small,180)
        self.image_top = pygame.transform.rotate(self.image_small,270)
        self.player_cards = pygame.image.load('blank.png').convert()
        self.player_cards = pygame.transform.smoothscale(self.player_cards,(100,150)).convert()
        self.card_played = pygame.image.load('blank.png').convert()

    # Create a new shuffled deck.
    def createNewDeck(self):
        # Create and save all new UnoCard objects to their respective lists.
        self.greenCards = [UnoCard("Green", "Normal", i, i, pygame.image.load('green'+ str(i)+'.png')) for i in range(0, 10)] + [UnoCard("Green", "Normal", i, i, pygame.image.load('green'+ str(i)+'.png'))
                                                                                      for i in range(1, 10)] \
                          + [UnoCard("Green", "Skip", "None", 20, pygame.image.load('greenskip'+ '.png')) for _ in range(0, 2)] + [
                              UnoCard("Green", "Reverse", "None", 20, pygame.image.load('greenreverse'+ '.png')) for _ in range(0, 2)] \
                          + [UnoCard("Green", "Draw Two", "None", 20, pygame.image.load('greenDrawTwo'+ '.png')) for _ in range(0, 2)]

        self.blueCards = [UnoCard("Blue", "Normal", i, i, pygame.image.load('blue'+ str(i)+'.png')) for i in range(0, 10)] + [UnoCard("Blue", "Normal", i, i, pygame.image.load('blue'+ str(i)+'.png')) for
                                                                                    i in range(1, 10)] \
                         + [UnoCard("Blue", "Skip", "None", 20, pygame.image.load('blueskip'+ '.png')) for _ in range(0, 2)] + [
                             UnoCard("Blue", "Reverse", "None", 20, pygame.image.load('bluereverse'+ '.png')) for _ in range(0, 2)] \
                         + [UnoCard("Blue", "Draw Two", "None", 20, pygame.image.load('blueDrawTwo'+ '.png')) for _ in range(0, 2)]

        self.yellowCards = [UnoCard("Yellow", "Normal", i, i, pygame.image.load('yellow'+ str(i)+'.png')) for i in range(0, 10)] + [
            UnoCard("Yellow", "Normal", i, i, pygame.image.load('yellow'+ str(i)+'.png')) for i in range(1, 10)] \
                           + [UnoCard("Yellow", "Skip", "None", 20, pygame.image.load('yellowskip'+ '.png')) for _ in range(0, 2)] + [
                               UnoCard("Yellow", "Reverse", "None", 20, pygame.image.load('yellowreverse'+ '.png')) for _ in range(0, 2)] \
                           + [UnoCard("Yellow", "Draw Two", "None", 20, pygame.image.load('yellowDrawTwo'+ '.png')) for _ in range(0, 2)]

        self.redCards = [UnoCard("Red", "Normal", i, i, pygame.image.load('red'+ str(i)+'.png')) for i in range(0, 10)] + [UnoCard("Red", "Normal", i, i, pygame.image.load('red'+ str(i)+'.png')) for i
                                                                                  in range(1, 10)] \
                        + [UnoCard("Red", "Skip", "None", 20, pygame.image.load('redskip'+ '.png')) for _ in range(0, 2)] + [
                            UnoCard("Red", "Reverse", "None", 20, pygame.image.load('redreverse'+ '.png')) for _ in range(0, 2)] \
                        + [UnoCard("Red", "Draw Two", "None", 20, pygame.image.load('redDrawTwo'+ '.png')) for _ in range(0, 2)]

        self.blackCards = [UnoCard("Black", "ColorChange", "None", 50, pygame.image.load('blackcolorchange.png')) for _ in range(0, 4)] + [
            UnoCard("Black", "Draw Four", "None", 50, pygame.image.load('blackDrawFour.png')) for _ in range(0, 4)]

        # Combine, shuffle and return the deck as a list of UnoCard objects.
        shuffledDeck = self.greenCards + self.yellowCards + self.redCards + self.blueCards + self.blackCards
        print(self.blackCards)
        random.shuffle(shuffledDeck)
        
        
        return shuffledDeck
        

    # Deal cards to a player and update the self.drawPile.
    def dealCards(self, playerDeck):
        # Hand out top 7 cards from the draw pile to the current player's deck.
        CardList = []
        i = 0
        for UnoCard in self.drawPile[0:7]:
            playerDeck.append(UnoCard)
            # Drop those cards from the "self.drawPile".
            self.drawPile.pop(self.drawPile.index(UnoCard))
            CardList.append(UnoCard.cardimage)
            x = pygame.transform.smoothscale(CardList[i],(100,150))
            i = i +1
            screen.blit(x,(200 + i*100, 500))
            pygame.display.update()
         

        return self.drawPile

    # Execute all the pre-game / pre - player activity routines.
    def startPreGame(self, shuffledNewDeck):
        
        #Interface set up
        BLUE = 70,130,180
        screen.fill(BLUE)
        fps = 60
        fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Uno') 
        start = True
        count = 21

            
        if count > 0:
            for l in range(7):
                #Left side comp cards
                x = 100 + l*60
                count -= 1
                screen.blit(self.image_small,(100,(x)))
                pygame.display.update()
                time.sleep(0.1)
                    
            for f in range(7):
                #Right side comp cards
                x = 100 + f*60
                count -= 1
                screen.blit(self.image_right,(1066,(x)))
                pygame.display.update()
                time.sleep(0.1)

            for k in range(7):
                #Right side comp cards
                x = 423 + k*50
                count -= 1
                screen.blit(self.image_top,(x,60))
                pygame.display.update()
                time.sleep(0.1)
        else:
            start = False
        print('test')

        # Create draw pile out of our shuffled deck.
        self.drawPile = shuffledNewDeck

        # Add human player to the list of player.
        self.humanPlayer = Player(1)
        self.playerList.append(self.humanPlayer)

        # Ask for number of players.
        AICount = int(input("Enter number of AI opponents to play against: "))
        for i in range(0, AICount):
            self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))

        # Deal 7 cards to player and AIs.
        # DEBUG
        print("\nPile before Player draw: ---- ----- --- \n")
        for i in self.drawPile:
            print(repr(i))
        ###

        for eachPlayer in self.playerList:
            self.drawPile = self.dealCards(eachPlayer.plDeck)

        # DEBUG Check all player decks.
        for i in self.playerList:
            print("\n")
            print(repr(i))

        # DEBUG
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
        self.drawPile, self.discardPile = self.playerList[0].playTurn(self.drawPile, self.currentGameColour,
                                                                      self.discardPile)


# Class for handling Player activities.
class Player():
    def __init__(self, playerNo, plDeck=[]):
        super().__init__()
        self.playerNo = playerNo
        self.plDeck = plDeck

    def playTurn(self, drawPile, currentGameColour, discardPile):
        # Select a card from your hand, and place it below the discard pile.

        print(f"Player {self.playerNo} -- Cards on hand:\n")
        for i in self.plDeck:
            print(i)

        # Initiate special rule.
        cardChoice = int(
            input("\nSPECIAL RULE: Select a card (1-7) from your hand and keep it beneath the discard pile..."))
        # Add player card to the discard pile.
        discardPile.append(self.plDeck[cardChoice - 1])
        # Remove card from player's deck.
        self.plDeck.pop(0)

        # Take top card from draw pile.
        print("\nPlayer 1 takes the top card from the draw pile to their hand...")
        self.plDeck.insert(0, drawPile[0])

        # Play a card or pick another card to pass.
        print("\nCards on hand pre execute:\n")
        for i in self.plDeck:
            print(i)

        print("Current game colour: ", currentGameColour)

        # Ask player to for their choice.
        playerChoice = int(input(
            "Press [1-n] and select a valid card to play or press 0 to draw a card from the draw pile and pass: "))
        # If 0, draw a card and pass.
        if (playerChoice == 0):
            self.plDeck.insert(0, drawPile[0])
            drawPile.pop(0)
            print("\nPlayer Deck after selecting card.....")
            for i in self.plDeck:
                print(i)

            print("\nDiscard pile after selecting card.....")
            for i in discardPile:
                print(i)
            print(f"\nPlayer {self.playerNo} turn complete.\n")
            return drawPile, discardPile

        #If 1-n, validate the card and proceed.
        if(playerChoice in range(1, (len(self.plDeck) + 1))):

        #If colour is same but number is different or a special card, can play.
            if(self.plDeck[playerChoice - 1].cardColour == currentGameColour):
                #If normal, play.
                if(self.plDeck[playerChoice - 1].cardType == "Normal"):
                    #Make the selection as the top card of the discard pile and add it to discard pile.
                    discardPile.insert(0, self.plDeck[playerChoice - 1])
                    #Remove card from player deck.
                    self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                    print("Player Deck after selecting card.....")
                    for i in self.plDeck:
                        print(i)
                    return drawPile, discardPile
            #If card is special, execute special card logic.

            #If number is same, but colour is different, can play. (More or less the same as above.)

            #If colour change, can play.

            #If draw4, can only play if no matching colour card on hand.

        #Return a tuple consisting of the current drawPile and discardPile.
        
        
        
        
        
        return drawPile,discardPile

    def __repr__(self):
        playerTemp = []
        for i in self.plDeck:
            playerTemp.append(i)

        return repr(f"Name: {type(self)} | Deck: {playerTemp}")


class AIPlayer(Player):
    pass
    # Insert AI Code.


# Card class.
class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber="None", cardValue="None", cardimage = 'None',x = 'None', y ='None'):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue
        self.cardimage = cardimage
        self.x = x
        self.y = y

    def __repr__(self):
        return repr(
            f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue} | Image: {self.cardimage}")

    def Image(self,x,y):
        z = self.cardimage
        screen.blit(z,(x,y))

start = True
while start:
    for event in pygame.event.get():
            if event.type == QUIT:
                    start = False
                    pygame.quit()
    newGame = Uno()

    newGame.startPreGame(newGame.createNewDeck())

    newGame.startGame()

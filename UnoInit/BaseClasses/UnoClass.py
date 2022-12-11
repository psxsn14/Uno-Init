from BaseClasses.PlayerClass import Player
from BaseClasses.AIPlayerClass import AIPlayer
import random
import copy
from BaseClasses import globals

import pygame
from pygame.locals import *
import time
import pygame.freetype


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
        # self.currentGameColour = ""
        # self.currentGameNumber = 0
        # self.currentGameType = ""

        # Top card from the discard pile that sets the current game colour.
        self.topDiscardPileCard = None

        pygame.init()

        # Card variables (pygame)
        self.image = pygame.image.load('Cards New/card_back.png')
        self.image_small = pygame.transform.smoothscale(self.image, (100, 150))
        self.image_small = pygame.transform.rotate(self.image_small, 90)
        self.image_right = pygame.transform.rotate(self.image_small, 180)
        self.image_top = pygame.transform.rotate(self.image_small, 270)
        self.player_cards = pygame.image.load('Cards New/blank.png').convert()
        self.player_cards = pygame.transform.smoothscale(self.player_cards, (100, 150)).convert()
        self.card_played = pygame.image.load('Cards New/blank.png').convert()

    # Create a new shuffled deck.
    def createNewDeck(self):
        # Create and save all new UnoCard objects to their respective lists.
        self.greenCards = [UnoCard("Green", "Normal", i, i, pygame.image.load('Cards New/green' + str(i) + '.png')) for
                           i in range(0, 10)] + [
                              UnoCard("Green", "Normal", i, i, pygame.image.load('Cards New/green' + str(i) + '.png'))
                              for i in range(1, 10)] \
                          + [UnoCard("Green", "Skip", "None", 20, pygame.image.load('Cards New/greenskip' + '.png')) for
                             _ in range(0, 2)] + [
                              UnoCard("Green", "Reverse", "None", 20,
                                      pygame.image.load('Cards New/greenreverse' + '.png')) for _ in range(0, 2)] \
                          + [UnoCard("Green", "Draw Two", "None", 20,
                                     pygame.image.load('Cards New/greenDrawTwo' + '.png')) for _ in range(0, 2)]

        self.blueCards = [UnoCard("Blue", "Normal", i, i, pygame.image.load('Cards New/blue' + str(i) + '.png')) for i
                          in range(0, 10)] + [
                             UnoCard("Blue", "Normal", i, i, pygame.image.load('Cards New/blue' + str(i) + '.png')) for
                             i in range(1, 10)] \
                         + [UnoCard("Blue", "Skip", "None", 20, pygame.image.load('Cards New/blueskip' + '.png')) for _
                            in range(0, 2)] + [
                             UnoCard("Blue", "Reverse", "None", 20, pygame.image.load('Cards New/bluereverse' + '.png'))
                             for _ in range(0, 2)] \
                         + [UnoCard("Blue", "Draw Two", "None", 20, pygame.image.load('Cards New/blueDrawTwo' + '.png'))
                            for _ in range(0, 2)]

        self.yellowCards = [UnoCard("Yellow", "Normal", i, i, pygame.image.load('Cards New/yellow' + str(i) + '.png'))
                            for i in range(0, 10)] + [
                               UnoCard("Yellow", "Normal", i, i,
                                       pygame.image.load('Cards New/yellow' + str(i) + '.png')) for i in range(1, 10)] \
                           + [UnoCard("Yellow", "Skip", "None", 20, pygame.image.load('Cards New/yellowskip' + '.png'))
                              for _ in range(0, 2)] + [
                               UnoCard("Yellow", "Reverse", "None", 20,
                                       pygame.image.load('Cards New/yellowreverse' + '.png')) for _ in range(0, 2)] \
                           + [UnoCard("Yellow", "Draw Two", "None", 20,
                                      pygame.image.load('Cards New/yellowDrawTwo' + '.png')) for _ in range(0, 2)]

        self.redCards = [UnoCard("Red", "Normal", i, i, pygame.image.load('Cards New/red' + str(i) + '.png')) for i in
                         range(0, 10)] + [
                            UnoCard("Red", "Normal", i, i, pygame.image.load('Cards New/red' + str(i) + '.png')) for i
                            in range(1, 10)] \
                        + [UnoCard("Red", "Skip", "None", 20, pygame.image.load('Cards New/redskip' + '.png')) for _ in
                           range(0, 2)] + [
                            UnoCard("Red", "Reverse", "None", 20, pygame.image.load('Cards New/redreverse' + '.png'))
                            for _ in range(0, 2)] \
                        + [UnoCard("Red", "Draw Two", "None", 20, pygame.image.load('Cards New/redDrawTwo' + '.png'))
                           for _ in range(0, 2)]

        self.blackCards = [UnoCard("Black", "ColorChange", "None", 50,
                                   pygame.image.load('Cards New/blackcolorchange.png')) for _ in range(0, 4)] + [
                              UnoCard("Black", "Draw Four", "None", 50,
                                      pygame.image.load('Cards New/blackDrawFour.png')) for _ in range(0, 4)]

        shuffledDeck = self.greenCards + self.yellowCards + self.redCards + self.blueCards + self.blackCards
        random.shuffle(shuffledDeck)
        return shuffledDeck

    # Deal cards to a player and update the self.drawPile.
    def dealCards(self, playerDeck):
        # Hand out top 7 cards from the draw pile to the current player's deck.
        for UnoCard in self.drawPile[0:7]:
            playerDeck.append(UnoCard)

            # Drop those cards from the "self.drawPile".
            self.drawPile.pop(self.drawPile.index(UnoCard))
        return self.drawPile

    # Execute all the pre-game / pre - player activity routines.
    def startPreGame(self, shuffledNewDeck, screen):

        # Interface set up
        BLUE = 70, 130, 180
        screen.fill(BLUE)
        fps = 60
        fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Uno')
        start = True
        count = 21
        # count = 7*globals.AIplayers

        print(globals.AIplayers)

        if count > 0:
            for l in range(7):
                if globals.AIplayers == 1:
                    count = count -7
                    pass
                else:
                    #Left side comp cards
                    x = 100 + l * 60
                    count -= 1
                    screen.blit(self.image_small, (100, (x)))
                    pygame.display.update()
                    time.sleep(0.1)

            for f in range(7):
                if globals.AIplayers == 1 or globals.AIplayers == 2:
                    count = count -7
                    pass
                else:
                    #Right side comp cards
                    x = 100 + f * 60
                    count -= 1
                    screen.blit(self.image_right, (1066, (x)))
                    pygame.display.update()
                    time.sleep(0.1)

            for k in range(7):
                #Top side comp cards
                x = 423 + k * 50
                count -= 1
                screen.blit(self.image_top, (x, 60))
                pygame.display.update()
                time.sleep(0.1)

            screen.blit(self.image_top, (750, 280))

        else:
            start = False

        # Create draw pile out of our shuffled deck.
        self.drawPile = shuffledNewDeck

        # Add human player to the list of player.
        self.humanPlayer = Player(1)
        self.playerList.append(self.humanPlayer)

        # Ask for number of players.
        while True:
            try:
                # AICount = int(input("Enter number of AI opponents to play against: "))

                for i in range(0, globals.AIplayers):
                    self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))
                break
            except:
                print("Invalid input, please enter a number")
        # AICount = int(input("Enter number of AI opponents to play against: "))
        # for i in range(0, AICount):
        #     self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))

        # Deal 7 cards to player and AIs.
        # DEBUG
        print("\nPile before Player draw: ---- ----- --- \n")
        print(len(self.drawPile))
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

        self.startGame(screen)

    def moveToNextPlayer(self, current):
        if globals.ascending:
            if current == len(self.playerList) - 1:
                current = 0
            else:
                current += 1
        else:
            if current == 0:
                current = len(self.playerList) - 1
            else:
                current -= 1
        # globals.current = current
        return current

    def winnerPlayer(self):
        for i in self.playerList:
            if len(i.plDeck) == 0:
                return i.playerNo

    def winnerScore(self):
        for i in self.playerList:
            for j in i.plDeck:
                globals.winnerScore += j.cardValue
        return globals.winnerScore

    def startGame(self, screen):

        # Pygame Top Card.
        x_top = self.drawPile[0].cardimage
        global Top_card
        Top_card = pygame.transform.smoothscale(x_top, (100, 150))
        screen.blit(Top_card, (400, 280))
        # screen.blit(self.image,(100,100))
        pygame.display.update()

        self.topDiscardPileCard = self.drawPile[0]
        print(f"\nTop card of the draw pile forms the discard pile: {self.topDiscardPileCard}")
        # if globals.currentGameType != 'Draw Four' or 'ChangeColor':
        globals.currentGameCard = self.drawPile[0]
        globals.currentGameColour = self.topDiscardPileCard.cardColour
        globals.currentGameNumber = self.topDiscardPileCard.cardNumber
        globals.currentGameType = self.topDiscardPileCard.cardType
        self.discardPile.append(self.topDiscardPileCard)
        self.drawPile.pop(0)
        ########## test ##########
        for i in self.playerList:
            print(i.playerNo)
            print(len(i.plDeck))
            print(i.plDeck)

        # For the first card
        # if globals.currentGameType == 'Draw Two':

        #########################    Real one
        exit_flag = False
        while not globals.GameOver:
            for i in self.playerList:
                if len(i.plDeck) == 0:
                    exit_flag = True
                    globals.GameOver = not globals.GameOver
                    break
            if exit_flag:
                break
            # while len(self.drawPile) != 0:
            print('Round ' + str(globals.gameRound))
            print('Player' + str(globals.current + 1))
            print(
                f"\nCurrent game card: {globals.currentGameColour}, {globals.currentGameNumber}, {globals.currentGameType}")
            self.drawPile, self.discardPile = self.playerList[globals.current].playTurn(self, self.drawPile,
                                                                                        self.discardPile, screen)

            globals.current = self.moveToNextPlayer(globals.current)
            globals.currentGameCard = self.discardPile[0]

            # print(globals.currentGameCard)
            # print(
            #     f"\nCurrent game card: {globals.currentGameColour}, {globals.currentGameNumber}, {globals.currentGameType}")

            if self.discardPile[0].cardType == "ColorChange":
                pass
            elif self.discardPile[0].cardType == "Draw Four":
                pass
            else:
                globals.currentGameColour = self.discardPile[0].cardColour
                globals.currentGameNumber = self.discardPile[0].cardNumber
                globals.currentGameType = self.discardPile[0].cardType
            # else:
            #     globals.currentGameNumber = self.discardPile[0].cardNumber
            #     globals.currentGameType = self.discardPile[0].cardType
            # else:
            #     globals.currentGameColour = globals.currentGameCard.cardColour
            #     globals.currentGameNumber = globals.currentGameCard.cardNumber
            #     globals.currentGameType = globals.currentGameCard.cardType
            # globals.currentGameType = self.discardPile[0].cardType
            # globals.currentGameColour = globals.currentGameCard.cardColour
            # globals.currentGameNumber = globals.currentGameCard.cardNumber
            # globals.currentGameType = globals.currentGameCard.cardType

            globals.gameRound += 1
            # print('Round ' + str(globals.gameRound))
            # print('Player' + str(globals.current+1))
            # print(globals.currentGameCard)
            print(
                f"\nCurrent game card: {globals.currentGameColour}, {globals.currentGameNumber}, {globals.currentGameType}")
            time.sleep(3)

        print("Game Over!")
        print("The Winner is Player" + str(self.winnerPlayer()))
        print("Score is " + str(self.winnerScore()))


# Card class.
class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber="None", cardValue="None", cardimage='None', x='None', y='None'):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue
        self.cardimage = cardimage
        self.x = x
        self.y = y

    # def Image(self,x,y, screen):
    #    z = self.cardimage
    #    screen.blit(z,(x,y))

    def __repr__(self):
        return repr(
            f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")

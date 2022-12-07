# UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

# <<<<<<< HEAD
# Suggestions: Please go through this architecture, sparingly get familiarised with my coding style, and let us know
# if there's something off, or if you have a much better structure. I have written some code to check certain things
# as you see below. I will flesh it out more by tomorrow. I will reference "to-be-written" code snippets in a
# numbered way for each function so that it's easy to communicate any difficulties. i.e "Stuck at <functionname> #2"
# as in the startGame function. Feel free to suggest any ideas in general without hesitation. Please familiarize
# yourself with gitlab/gitkraken by Friday and use this .py to try new things as it already has an implementation of
# a shuffled deck.
# =======
# Suggestions:
# Please go through this architecture, sparingly get familiarised with my coding style, and let us know if there's something off, or if you have a much better structure.
# I have written some code to check certain things as you see below. I will flesh it out more by tomorrow.
# I will reference "to-be-written" code snippets in a numbered way for each function so that it's easy to communicate any difficulties. i.e "Stuck at <functionname> #2" as in the startGame function.
# Feel free to suggest any ideas in general without hesitation.
# Please familiarize yourself with gitlab/gitkraken by Friday and use this .py to try new things as it already has an implementation of a shuffled deck.
# >>>>>>> wip-pygame-interface

# testesttetststseteststststesetsetstsetetestsees

# hihi
# from ctypes.wintypes import VARIANT_BOOL
from pickle import NONE
import random
import copy
import globals
import AI_Strategy

# from ctypes.wintypes import VARIANT_BOOL
from pickle import NONE
import random
import copy
import pygame

pygame.init()
from pygame.locals import *
import time
import pygame.freetype

screen = pygame.display.set_mode((1366, 768))
BLUE = 70, 130, 180


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

        # Create a new shuffled deck.

        self.currentGameColour = ""
        # Top card from the discard pile that sets the current game colour.
        self.topDiscardPileCard = None

        # Card variables
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

        # Combine, shuffle and return the deck as a list of UnoCard objects.
        shuffledDeck = self.greenCards + self.yellowCards + self.redCards + self.blueCards + self.blackCards
        print(self.blackCards)
        random.shuffle(shuffledDeck)

        return shuffledDeck

    # Deal cards to a player and update the self.drawPile.
    def dealCards(self, playerDeck):
        # Hand out top 7 cards from the draw pile to the current player's deck.

        # for UnoCard in self.drawPile[0:7]:
        #     playerDeck.append(UnoCard)

            # Drop those cards from the "self.drawPile".

        global CardList
        CardList = []
        i = 0
        for UnoCard in self.drawPile[0:7]:
            playerDeck.append(UnoCard)

            self.drawPile.pop(self.drawPile.index(UnoCard))

        return self.drawPile

    # Execute all the pre-game / pre - player activity routines.
    def startPreGame(self, shuffledNewDeck):
        # Create draw pile out of our shuffled deck.
        self.drawPile = shuffledNewDeck

        # Add human player to the list of player.
        self.humanPlayer = Player(1)
        self.playerList.append(self.humanPlayer)

        # Ask for number of players.

        while True:
            try:
                AICount = int(input("Enter number of AI opponents to play against: "))
                for i in range(0, AICount):
                    self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))
                break
            except:
                print("Invalid input, please enter a number")

        # Interface set up
        BLUE = 70, 130, 180
        screen.fill(BLUE)
        fps = 60
        fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Uno')
        start = True
        # count = 21
        count = AICount * 7

        if count > 0:
            for l in range(7):
                # Left side comp cards
                x = 100 + l * 60
                count -= 1
                screen.blit(self.image_small, (100, (x)))
                pygame.display.update()
                time.sleep(0.1)

            for f in range(7):
                # Right side comp cards
                x = 100 + f * 60
                count -= 1
                screen.blit(self.image_right, (1066, (x)))
                pygame.display.update()
                time.sleep(0.1)

            for k in range(7):
                # Right side comp cards
                x = 423 + k * 50
                count -= 1
                screen.blit(self.image_top, (x, 60))
                pygame.display.update()
                time.sleep(0.1)

            screen.blit(self.image_top, (650, 280))

        else:
            start = False
        print('test')

        # # Create draw pile out of our shuffled deck.
        # self.drawPile = shuffledNewDeck
        #
        # # Add human player to the list of player.
        # self.humanPlayer = Player(1)
        # self.playerList.append(self.humanPlayer)
        #
        # # Ask for number of players.
        #
        # while True:
        #     try:
        #         AICount = int(input("Enter number of AI opponents to play against: "))
        #         for i in range(0, AICount):
        #             self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))
        #         break
        #     except:
        #         print("Invalid input, please enter a number")



        # AICount = int(input("Enter number of AI opponents to play against: "))
        # for i in range(0, AICount):
        #     self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))

        # AICount = int(input("Enter number of AI opponents to play against: "))
        # for i in range(0, AICount):
        #     self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))
        # >>>>>>> wip-pygame-interface

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

    def startGame(self):
        self.topDiscardPileCard = self.drawPile[0]
        x_top = self.drawPile[0].cardimage
        global Top_card
        Top_card = pygame.transform.smoothscale(x_top, (100, 150))
        screen.blit(Top_card, (500, 280))
        # screen.blit(self.image,(100,100))
        pygame.display.update()

        print(f"\nTop card of the draw pile forms the discard pile: {self.topDiscardPileCard}")
        globals.currentGameCard = self.drawPile[0]
        globals.currentGameColour = self.topDiscardPileCard.cardColour
        globals.currentGameNumber = self.topDiscardPileCard.cardNumber
        globals.currentGameType = self.topDiscardPileCard.cardType
        self.discardPile.append(self.topDiscardPileCard)
        self.drawPile.pop(0)
        # <<<<<<< HEAD
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
                if len(i.plDeck) != 0:
                    exit_flag = True
                    globals.GameOver = not globals.GameOver
                    break
            if exit_flag:
                break
            # while len(self.drawPile) != 0:

            self.drawPile, self.discardPile = self.playerList[globals.current].playTurn(self.drawPile,
                                                                                        self.discardPile)

            globals.current = self.moveToNextPlayer(globals.current)
            globals.currentGameCard = self.discardPile[0]
            globals.currentGameNumber = self.discardPile[0].cardNumber
            globals.currentGameType = self.discardPile[0].cardType
            if globals.currentGameType != "ColorChange" or "Draw Four":
                globals.currentGameColour = self.discardPile[0].cardColour
            # globals.currentGameType = self.discardPile[0].cardType

            globals.gameRound += 1
            print('Round ' + str(globals.gameRound))

        print("Game Over!")
        print("The Winner is Player" + str(self.winnerPlayer()))
        print("Score is " + str(self.winnerScore()))
        # =======
        self.drawPile, self.discardPile = self.playerList[0].playTurn(self.drawPile, self.currentGameColour,
                                                                      self.discardPile)


# >>>>>>> wip-pygame-interface

# Interface for the discard pile


# Class for handling Player activities.
# <<<<<<< HEAD
class Player:
    def __init__(self, playerNo, plDeck=[]):
        # super().__init__()
        self.playerNo = playerNo
        self.plDeck = plDeck

    def playTurn(self, drawPile, discardPile):
        # Rules for the revealed card
        if globals.gameRound == 0:
            if globals.currentGameType == 'Draw Two':
                for UnoCard in drawPile[0:2]:
                    newGame.playerList[globals.current].plDeck.append(UnoCard)
                    drawPile.pop(drawPile.index(UnoCard))
                return drawPile, discardPile

            elif globals.currentGameType == 'Skip':
                # globals.current = newGame.moveToNextPlayer(globals.current)
                # print(globals.current)
                return drawPile, discardPile

            elif globals.currentGameType == 'Reverse':
                globals.ascending = not globals.ascending

            elif globals.currentGameType == 'ColorChange':
                while True:
                    newColour = input("\nPlease select a new color(Green, Blue, Yellow or Red): ")
                    if newColour == 'Green' or 'Blue' or 'Yellow' or 'Red':
                        break
                    else:
                        print("Please enter 'Green', 'Blue', 'Yellow' or 'Red'")
                globals.currentGameColour = newColour

            elif globals.currentGameType == 'Draw Four':
                # official rules: put the card back into the deck and draw a new card
                while globals.currentGameType == "Draw Four":
                    # Put the card back
                    drawPile.append(globals.currentGameCard)
                    discardPile.pop(0)
                    # draw a new card
                    globals.currentGameCard = drawPile[0]
                    globals.currentGameColour = globals.currentGameCard.cardColour
                    globals.currentGameNumber = globals.currentGameCard.cardNumber
                    globals.currentGameType = globals.currentGameCard.cardType
                    drawPile.pop(0)
                    discardPile.append(globals.currentGameCard)
                    # return drawPile, discardPile

                # popular rules: first player choose the color, next player draw 4 and skip
                while True:
                    newColour = input("\nPlease select a new color(Green, Blue, Yellow or Red): ")
                    if newColour == 'Green' or 'Blue' or 'Yellow' or 'Red':
                        break
                    else:
                        print("Please enter 'Green', 'Blue', 'Yellow' or 'Red'")
                globals.currentGameColour = newColour
                # Next player draw four and skip
                nextPlayer = newGame.moveToNextPlayer(globals.current)
                for UnoCard in drawPile[0:4]:
                    # print(nextPlayer)
                    newGame.playerList[nextPlayer].plDeck.append(UnoCard)
                    drawPile.pop(drawPile.index(UnoCard))
                # Skip the next person's round
                globals.current = newGame.moveToNextPlayer(globals.current)
                return drawPile, discardPile


# =======
class Player():
    def __init__(self, playerNo, plDeck=[]):
        super().__init__()
        self.playerNo = playerNo
        self.plDeck = plDeck

    def playTurn(self, drawPile, currentGameColour, discardPile):
        # >>>>>>> wip-pygame-interface
        # Select a card from your hand, and place it below the discard pile.

        print(f"Player {self.playerNo} -- Cards on hand:\n")
        for i in self.plDeck:
            print(i)

        # <<<<<<< HEAD
        # Initiate special rule.

        cardChoice = int(
            input("\nSPECIAL RULE: Select a card (1-7) from your hand and keep it beneath the discard pile..."))
        # Add player card to the discard pile.
        discardPile.append(self.plDeck[cardChoice - 1])
        # Remove card from player's deck.
        self.plDeck.pop(cardChoice - 1)

        # Take top card from draw pile.
        print(f"\nPlayer {self.playerNo} takes the top card from the draw pile to their hand...")

        # Set up the cards
        card_interface = [pygame.transform.smoothscale(self.plDeck[0].cardimage, (100, 150)),
                          pygame.transform.smoothscale(self.plDeck[1].cardimage, (100, 150)),
                          pygame.transform.smoothscale(self.plDeck[2].cardimage, (100, 150)),
                          pygame.transform.smoothscale(self.plDeck[3].cardimage, (100, 150)),
                          pygame.transform.smoothscale(self.plDeck[4].cardimage, (100, 150)),
                          pygame.transform.smoothscale(self.plDeck[5].cardimage, (100, 150)),
                          pygame.transform.smoothscale(self.plDeck[6].cardimage, (100, 150)),
                          ]

        # playersHand = pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150))
        screen.blit(pygame.transform.smoothscale(self.plDeck[0].cardimage, (100, 150)), (300, 500))
        screen.blit(pygame.transform.smoothscale(self.plDeck[1].cardimage, (100, 150)), (400, 500))
        screen.blit(pygame.transform.smoothscale(self.plDeck[2].cardimage, (100, 150)), (500, 500))
        screen.blit(pygame.transform.smoothscale(self.plDeck[3].cardimage, (100, 150)), (600, 500))
        screen.blit(pygame.transform.smoothscale(self.plDeck[4].cardimage, (100, 150)), (700, 500))
        screen.blit(pygame.transform.smoothscale(self.plDeck[5].cardimage, (100, 150)), (800, 500))
        screen.blit(pygame.transform.smoothscale(self.plDeck[6].cardimage, (100, 150)), (900, 500))

        pygame.display.update()

        # Initiate special rule.
        # cardChoice = int(
        # input("\nSPECIAL RULE: Select a card (1-7) from your hand and keep it beneath the discard pile..."))
        # Card choice select interface

        start = True
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            for i in range(1):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    first_card_rect = pygame.transform.smoothscale(card_interface[0], (100, 150)).get_rect(
                        topleft=(300, 500))
                    second_card_rect = pygame.transform.smoothscale(card_interface[1], (100, 150)).get_rect(
                        topleft=(400, 500))
                    third_card_rect = pygame.transform.smoothscale(card_interface[2], (100, 150)).get_rect(
                        topleft=(500, 500))
                    fourth_card_rect = pygame.transform.smoothscale(card_interface[3], (100, 150)).get_rect(
                        topleft=(600, 500))
                    fifth_card_rect = pygame.transform.smoothscale(card_interface[4], (100, 150)).get_rect(
                        topleft=(700, 500))
                    sixth_card_rect = pygame.transform.smoothscale(card_interface[5], (100, 150)).get_rect(
                        topleft=(800, 500))
                    seventh_card_rect = pygame.transform.smoothscale(card_interface[6], (100, 150)).get_rect(
                        topleft=(900, 500))
                    draw_pile_image = drawPile[0].cardimage

                    counter = 1
                    while counter > 0:
                        # Check if the card is clicked
                        if first_card_rect.collidepoint(x, y):
                            pygame.draw.rect(screen, BLUE, (300, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (300, 500))
                            pygame.display.update()
                            position = 1
                            counter = counter - 1

                        elif second_card_rect.collidepoint(x, y):
                            pygame.draw.rect(screen, BLUE, (400, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (400, 500))
                            pygame.display.update()
                            position = 2
                            counter = counter - 1

                        elif third_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (500, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (500, 500))
                            pygame.display.update()
                            position = 3
                            counter = counter - 1

                        elif fourth_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (600, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (600, 500))
                            pygame.display.update()
                            position = 4
                            counter = counter - 1

                        elif fifth_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (700, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (700, 500))
                            pygame.display.update()
                            position = 5
                            counter = counter - 1

                        elif sixth_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (800, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (800, 500))
                            pygame.display.update()
                            position = 6
                            counter = counter - 1

                        elif seventh_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (900, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (900, 500))
                            pygame.display.update()
                            position = 7
                            counter = counter - 1

                    cardChoice = position
        pygame.quit()

        # Add player card to the discard pile.
        discardPile.append(self.plDeck[cardChoice - 1])
        # Remove card from player's deck.
        self.plDeck.pop(0)

        # Take top card from draw pile.
        print("\nPlayer 1 takes the top card from the draw pile to their hand...")
        self.plDeck.insert(0, drawPile[0])
        drawPile.pop(0)

        # Play a card or pick another card to pass.
        print("\nCards on hand pre execute:\n")
        for i in self.plDeck:
            print(i)

        # print("Current game colour: ", globals.currentGameColour)
        print(
            f"\nCurrent game card: {globals.currentGameColour}, {globals.currentGameNumber}, {globals.currentGameType}")

        # inturn = True
        # Check the card is valid or not
        while True:
            # Ask player to for their choice.
            while True:
                try:
                    playerChoice = int(input(
                        "Press [1-n] and select a valid card to play or press 0 to draw a card from the draw pile and pass: "))
                    break
                except:
                    print("Invalid choice, please enter a number")
            # If 0, draw a card and pass.
            if playerChoice == 0:
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

            # If 1-n, validate the card and proceed.
            elif playerChoice in range(1, (len(self.plDeck) + 1)):
                # If black card
                if self.plDeck[playerChoice - 1].cardColour == "Black":
                    # Wild
                    if self.plDeck[playerChoice - 1].cardType == "ColorChange":
                        discardPile.insert(0, self.plDeck[playerChoice - 1])
                        self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                        # change the color
                        while True:
                            newColour = input("\nPlease select a new color(Green, Blue, Yellow or Red): ")
                            if newColour == 'Green' or 'Blue' or 'Yellow' or 'Red':
                                break
                            else:
                                print("Please enter 'Green', 'Blue', 'Yellow' or 'Red'")
                        globals.currentGameColour = newColour
                        return drawPile, discardPile

                    # Wild Draw
                    if self.plDeck[playerChoice - 1].cardType == "Draw Four":
                        discardPile.insert(0, self.plDeck[playerChoice - 1])
                        self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                        # change the color
                        while True:
                            newColour = input("\nPlease select a new color(Green, Blue, Yellow or Red): ")
                            if newColour == 'Green' or 'Blue' or 'Yellow' or 'Red':
                                break
                            else:
                                print("Please enter 'Green', 'Blue', 'Yellow' or 'Red'")
                        globals.currentGameColour = newColour
                        # Next player draw four and skip
                        nextPlayer = newGame.moveToNextPlayer(globals.current)
                        for UnoCard in drawPile[0:4]:
                            # print(nextPlayer)
                            newGame.playerList[nextPlayer].plDeck.append(UnoCard)
                            drawPile.pop(drawPile.index(UnoCard))
                        # Skip the next person's round
                        globals.current = newGame.moveToNextPlayer(globals.current)

                        return drawPile, discardPile

                # If normal card
                elif self.plDeck[playerChoice - 1].cardType == "Normal":
                    # Check color is the same or number is the same
                    if self.plDeck[playerChoice - 1].cardColour == globals.currentGameColour or \
                            self.plDeck[playerChoice - 1].cardNumber == globals.currentGameNumber:
                        # Make the selection as the top card of the discard pile and add it to discard pile.
                        discardPile.insert(0, self.plDeck[playerChoice - 1])
                        # Remove card from player deck.
                        self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                        print("Player Deck after selecting card.....")
                        for i in self.plDeck:
                            print(i)
                        return drawPile, discardPile
                    else:
                        print("It is not a valid card, please choose again")

                # If not a normal card (functional card)
                elif self.plDeck[playerChoice - 1].cardType != "Normal":
                    if self.plDeck[playerChoice - 1].cardColour == globals.currentGameColour or \
                            self.plDeck[playerChoice - 1].cardType == globals.currentGameType:
                        ######### Draw 2 ########
                        if self.plDeck[playerChoice - 1].cardType == "Draw Two":
                            discardPile.insert(0, self.plDeck[playerChoice - 1])
                            self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                            # You draw two cards
                            nextPlayer = newGame.moveToNextPlayer(globals.current)
                            for UnoCard in drawPile[0:2]:
                                # print(nextPlayer)
                                newGame.playerList[nextPlayer].plDeck.append(UnoCard)
                                drawPile.pop(drawPile.index(UnoCard))
                            # Skip the next person's round
                            globals.current = newGame.moveToNextPlayer(globals.current)
                            # Test
                            # print("Next player deck after the privious player use draw two card.....")
                            # for i in newGame.playerList[nextPlayer].plDeck:
                            #     print(i)

                            print("Player Deck after selecting card.....")
                            for i in self.plDeck:
                                print(i)
                            return drawPile, discardPile

                        ######## Reverse ########
                        if self.plDeck[playerChoice - 1].cardType == "Reverse":
                            globals.ascending = not globals.ascending
                            discardPile.insert(0, self.plDeck[playerChoice - 1])
                            # Remove card from player deck.
                            self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                            print("Player Deck after selecting card.....")
                            for i in self.plDeck:
                                print(i)
                            return drawPile, discardPile

                        ######## Skip ########
                        if self.plDeck[playerChoice - 1].cardType == "Skip":
                            discardPile.insert(0, self.plDeck[playerChoice - 1])
                            self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                            print(globals.current)
                            globals.current = newGame.moveToNextPlayer(globals.current)
                            print(globals.current)
                            return drawPile, discardPile

                    else:
                        print("It is not a valid card, please choose again")
            else:
                print("Choice out of range, please enter the correct number")

        # Return a tuple consisting of the current drawPile and discardPile.
        # return drawPile, discardPile
        print("Current game colour: ", currentGameColour)

        # Ask player to for their choice.
        playerChoice = int(input(
            "Press [1-n] and select a valid card to play or press 0 to draw a card from the draw pile and pass: "))
        # If 0, draw a card and pass.
        if (playerChoice == 0):
            self.plDeck.insert(0, drawPile[0])
            drawPile.pop(0)

            # Select from the draw pile if no card can be played interface
            start = True
            while start:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                for i in range(1):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos

                        draw_pile_rect = pygame.transform.smoothscale(draw_pile_image, (100, 150)).get_rect(
                            topleft=(650, 280))

                        if draw_pile_rect.collidepoint(x, y):
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (500, 500))
                            pygame.display.update()

            pygame.quit()

            print("\nPlayer Deck after selecting card.....")
            for i in self.plDeck:
                print(i)

            print("\nDiscard pile after selecting card.....")
            for i in discardPile:
                print(i)
            print(f"\nPlayer {self.playerNo} turn complete.\n")
            return drawPile, discardPile

        # If 1-n, validate the card and proceed.
        if (playerChoice in range(1, (len(self.plDeck) + 1))):

            # If colour is same but number is different or a special card, can play.
            if (self.plDeck[playerChoice - 1].cardColour == currentGameColour):
                # If normal, play.
                if (self.plDeck[playerChoice - 1].cardType == "Normal"):
                    # Make the selection as the top card of the discard pile and add it to discard pile.
                    discardPile.insert(0, self.plDeck[playerChoice - 1])
                    # Remove card from player deck.
                    self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                    print("Player Deck after selecting card.....")
                    for i in self.plDeck:
                        print(i)
                    return drawPile, discardPile
            # If card is special, execute special card logic.

            # If number is same, but colour is different, can play. (More or less the same as above.)

            # If colour change, can play.

            # If draw4, can only play if no matching colour card on hand.

        # Return a tuple consisting of the current drawPile and discardPile.
        return drawPile, discardPile

    # >>>>>>> wip-pygame-interface

    def __repr__(self):
        playerTemp = []
        for i in self.plDeck:
            playerTemp.append(i)

        return repr(f"Name: {type(self)} | Deck: {playerTemp}")


# <<<<<<< HEAD

class AIPlayer(Player):
    def __init__(self, playerNo, plDeck=[]):
        super().__init__(playerNo, plDeck)
        # self.playerNo = playerNo
        # self.plDeck = plDeck

    #
    def playTurn(self, drawPile, discardPile):
        # AI action
        # aicard = []
        ai = AI_Strategy.AI(self.plDeck, globals.currentGameCard, drawPile)
        ai_discard, _ = ai.change_card()
        # ai.can_play()
        ai_play, action = ai.play_action()
        print("AI discard: " + str(ai_discard))
        print("AI play: " + str(ai_play))
        print("AI action: " + action)

        # discard one
        discardPile.append(ai_discard)
        self.plDeck.remove(ai_discard)
        # draw one
        self.plDeck.insert(0, drawPile[0])
        drawPile.pop(0)

        # judge by action
        # draw means no card to play
        if action == 'draw':
            self.plDeck.insert(0, drawPile[0])
            drawPile.pop(0)
            return drawPile, discardPile
        elif action == 'play':
            if ai_play.cardType == "Normal":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                return drawPile, discardPile
            elif ai_play.cardType == "Reverse":
                globals.ascending = not globals.ascending
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                return drawPile, discardPile
            elif ai_play.cardType == "Skip":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                globals.current = newGame.moveToNextPlayer(globals.current)
                return drawPile, discardPile
            elif ai_play.cardType == "Draw Two":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)

                nextPlayer = newGame.moveToNextPlayer(globals.current)
                for UnoCard in drawPile[0:2]:
                    # print(nextPlayer)
                    newGame.playerList[nextPlayer].plDeck.append(UnoCard)
                    drawPile.pop(drawPile.index(UnoCard))
                # Skip the next person's round
                globals.current = newGame.moveToNextPlayer(globals.current)
                return drawPile, discardPile
        else:
            if ai_play.cardType == "ColorChange":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)

                globals.currentGameColour = action
                return drawPile, discardPile
            elif ai_play.cardType == "Draw Four":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)

                globals.currentGameColour = action

                nextPlayer = newGame.moveToNextPlayer(globals.current)
                for UnoCard in drawPile[0:4]:
                    # print(nextPlayer)
                    newGame.playerList[nextPlayer].plDeck.append(UnoCard)
                    drawPile.pop(drawPile.index(UnoCard))
                # Skip the next person's round
                globals.current = newGame.moveToNextPlayer(globals.current)

                return drawPile, discardPile

        # return drawPile, discardPile
        # print("###############################AI change card below")
        # ai.change_card()
        # print("###############################AI canplay below")
        # print("###############################AI play action below")
        # ai.play_action()
        # 无牌可出，摸牌
        # if command == "draw":
        #     pass
        # # 出一张牌
        # if command == "play":
        #     pass
        #
        # pass
    # Insert AI Code.


# Card class.
class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber="None", cardValue="None", cardimage='None', x='None', y='None'):
        self.cardimage = cardimage
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue
        self.x = x
        self.y = y

    def __repr__(self):
        return repr(
            f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")
        # aicard = []

        # ai = AI(aicard, newGame.topDiscardPileCard, newGame.drawPile)
        # ai = AI_Strategy.AI(aicard, newGame.topDiscardPileCard, newGame.drawPile)

        # newGame.startPreGame(newGame.createNewDeck())

        # newGame.startGame()
        self.cardimage = cardimage
        self.x = x
        self.y = y

    def __repr__(self):
        return repr(
            f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue} | Image: {self.cardimage}")

    def Image(self, x, y):
        z = self.cardimage
        screen.blit(z, (x, y))


start = True
while start:
    for event in pygame.event.get():
        if event.type == QUIT:
            start = False
            pygame.quit()
        newGame = Uno()

        newGame.startPreGame(newGame.createNewDeck())

        newGame.startGame()

pygame.quit()

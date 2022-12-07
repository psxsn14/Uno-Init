# UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

# Suggestions: Please go through this architecture, sparingly get familiarised with my coding style, and let us know
# if there's something off, or if you have a much better structure. I have written some code to check certain things
# as you see below. I will flesh it out more by tomorrow. I will reference "to-be-written" code snippets in a
# numbered way for each function so that it's easy to communicate any difficulties. i.e "Stuck at <functionname> #2"
# as in the startGame function. Feel free to suggest any ideas in general without hesitation. Please familiarize
# yourself with gitlab/gitkraken by Friday and use this .py to try new things as it already has an implementation of
# a shuffled deck.

# testesttetststseteststststesetsetstsetetestsees

# hihi
# from ctypes.wintypes import VARIANT_BOOL
from pickle import NONE
import random
import copy
import globals
import AI_Strategy


# Class handling the game.
class Uno:
    drawPile = []
    discardPile = []

    # global current
    # global ascending

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

        # ascending or not
        self.ascending = True

    # Create a new shuffled deck.
    def createNewDeck(self):
        # Create and save all new UnoCard objects to their respective lists.
        self.greenCards = [UnoCard("Green", "Normal", i, i) for i in range(0, 10)] + [UnoCard("Green", "Normal", i, i)
                                                                                      for i in range(1, 10)] \
                          + [UnoCard("Green", "Skip", "None", 20) for _ in range(0, 2)] + [
                              UnoCard("Green", "Reverse", "None", 20) for _ in range(0, 2)] \
                          + [UnoCard("Green", "Draw Two", "None", 20) for _ in range(0, 2)]

        # self.blueCards = [UnoCard("Blue", "Normal", i, i) for i in range(0, 10)] + [UnoCard("Blue", "Normal", i, i) for
        #                                                                             i in range(1, 10)] \
        #                  + [UnoCard("Blue", "Skip", "None", 20) for _ in range(0, 2)] + [
        #                      UnoCard("Blue", "Reverse", "None", 20) for _ in range(0, 2)] \
        #                  + [UnoCard("Blue", "Draw Two", "None", 20) for _ in range(0, 2)]
        #
        # self.yellowCards = [UnoCard("Yellow", "Normal", i, i) for i in range(0, 10)] + [
        #     UnoCard("Yellow", "Normal", i, i) for i in range(1, 10)] \
        #                    + [UnoCard("Yellow", "Skip", "None", 20) for _ in range(0, 2)] + [
        #                        UnoCard("Yellow", "Reverse", "None", 20) for _ in range(0, 2)] \
        #                    + [UnoCard("Yellow", "Draw Two", "None", 20) for _ in range(0, 2)]
        #
        # self.redCards = [UnoCard("Red", "Normal", i, i) for i in range(0, 10)] + [UnoCard("Red", "Normal", i, i) for i
        #                                                                           in range(1, 10)] \
        #                 + [UnoCard("Red", "Skip", "None", 20) for _ in range(0, 2)] + [
        #                     UnoCard("Red", "Reverse", "None", 20) for _ in range(0, 2)] \
        #                 + [UnoCard("Red", "Draw Two", "None", 20) for _ in range(0, 2)]
        #
        # self.blackCards = [UnoCard("Black", "ColorChange", "None", 50) for _ in range(0, 4)] + [
        #     UnoCard("Black", "Draw Four", "None", 50) for _ in range(0, 4)]

        # Combine, shuffle and return the deck as a list of UnoCard objects.
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
    def startPreGame(self, shuffledNewDeck):
        # Create draw pile out of our shuffled deck.
        self.drawPile = shuffledNewDeck

        # Add human player to the list of player.
        self.humanPlayer = Player(1)
        self.playerList.append(self.humanPlayer)

        # Ask for number of players.
        # while True:
        #     try:
        #         AICount = int(input("Enter number of AI opponents to play against: "))
        #         for i in range(0, AICount):
        #             self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))
        #         break
        #     except:
        #         print("Invalid input, please enter a number")
        AICount = int(input("Enter number of AI opponents to play against: "))
        for i in range(0, AICount):
            self.playerList.append(copy.deepcopy(AIPlayer(i + 2)))

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
        if self.ascending:
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
        print(f"\nTop card of the draw pile forms the discard pile: {self.topDiscardPileCard}")
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
        # exit_flag = False
        # while not globals.GameOver:
        #     for i in self.playerList:
        #         if len(i.plDeck) == 0:
        #             exit_flag = True
        #             globals.GameOver = not globals.GameOver
        #             break
        #     if exit_flag:
        #         break
        while len(self.drawPile) != 0:
            self.drawPile, self.discardPile = self.playerList[globals.current].playTurn(self.drawPile,
                                                                                        self.discardPile)

            globals.current = self.moveToNextPlayer(globals.current)
            globals.currentGameCard = self.discardPile[0]
            globals.currentGameNumber = self.discardPile[0].cardNumber
            globals.currentGameColour = self.discardPile[0].cardColour
            globals.currentGameType = self.discardPile[0].cardType

            globals.gameRound += 1
            print('Round ' + str(globals.gameRound))

        print("Game Over!")
        print("The Winner is Player" + str(self.winnerPlayer()))
        print("Score is " + str(self.winnerScore()))


# Class for handling Player activities.
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
                newGame.ascending = not newGame.ascending

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
        self.plDeck.pop(cardChoice - 1)

        # Take top card from draw pile.
        print(f"\nPlayer {self.playerNo} takes the top card from the draw pile to their hand...")
        self.plDeck.insert(0, drawPile[0])
        drawPile.pop(0)

        # Play a card or pick another card to pass.
        print("\nCards on hand pre execute:\n")
        for i in self.plDeck:
            print(i)

        # print("Current game colour: ", globals.currentGameColour)
        print(f"\nCurrent game card: {globals.currentGameColour}, {globals.currentGameNumber}, {globals.currentGameType}")

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
                            newGame.ascending = not newGame.ascending
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

    def __repr__(self):
        playerTemp = []
        for i in self.plDeck:
            playerTemp.append(i)

        return repr(f"Name: {type(self)} | Deck: {playerTemp}")


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
        if action == 'play':
            if ai_play.cardType == "Normal":
                pass
            elif ai_play.cardType == "Reverse":
                pass
            elif ai_play.cardType == "Reverse":
                pass
            elif ai_play.cardType == "Reverse":
                pass
            elif ai_play.cardType == "Reverse":
                pass
            elif ai_play.cardType == "Reverse":
                pass


        return drawPile, discardPile
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
    def __init__(self, cardColour, cardType, cardNumber="None", cardValue="None"):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue

    def __repr__(self):
        return repr(
            f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")


newGame = Uno()
# aicard = []

# ai = AI(aicard, newGame.topDiscardPileCard, newGame.drawPile)
# ai = AI_Strategy.AI(aicard, newGame.topDiscardPileCard, newGame.drawPile)


newGame.startPreGame(newGame.createNewDeck())

newGame.startGame()

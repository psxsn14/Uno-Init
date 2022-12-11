# import AI_Strategy
from pickletools import pybool
from BaseClasses import globals
import pygame


# Class for handling Player activities.
class Player:
    def __init__(self, playerNo, plDeck=[]):
        # super().__init__()
        self.playerNo = playerNo
        self.plDeck = plDeck

    def check(self, drawPile, discardPile, playerChoice, newGame):
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
                    globals.currentGameType = self.plDeck[playerChoice - 1].cardType
                    globals.currentGameNumber = self.plDeck[playerChoice - 1].cardNumber
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
                    globals.currentGameType = self.plDeck[playerChoice - 1].cardType
                    globals.currentGameNumber = self.plDeck[playerChoice - 1].cardNumber
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

    def playTurn(self, newGame, drawPile, discardPile, screen):
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
                    # drawPile.append(globals.currentGameCard)
                    # discardPile.pop(0)
                    # # draw a new card
                    # globals.currentGameCard = drawPile[0]
                    # globals.currentGameColour = globals.currentGameCard.cardColour
                    # globals.currentGameNumber = globals.currentGameCard.cardNumber
                    # globals.currentGameType = globals.currentGameCard.cardType
                    # drawPile.pop(0)
                    # discardPile.append(globals.currentGameCard)
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

        # cardChoice = int(
        # input("\nSPECIAL RULE: Select a card (1-7) from your hand and keep it beneath the discard pile..."))
        # Add player card to the discard pile.

        # Take top card from draw pile.
        print(f"\nPlayer {self.playerNo} takes the top card from the draw pile to their hand...")

        # Set up the cards - pygame.
        card_interface = []
        print(len(self.plDeck))
        for j in range(len(self.plDeck)):
            print(j)
            card_interface.append(pygame.transform.smoothscale(self.plDeck[j].cardimage, (100, 150)))
            screen.blit(pygame.transform.smoothscale(self.plDeck[j].cardimage, (100, 150)), (300 + j * 100, 500))
            pygame.display.update()

        print('cool')

            # pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150)),
            # pygame.transform.smoothscale(self.plDeck[2].cardimage,(100,150)),
            # pygame.transform.smoothscale(self.plDeck[3].cardimage,(100,150)),
            # pygame.transform.smoothscale(self.plDeck[4].cardimage,(100,150)),
            # pygame.transform.smoothscale(self.plDeck[5].cardimage,(100,150)),
            # pygame.transform.smoothscale(self.plDeck[6].cardimage,(100,150)),
            # ]

        # playersHand = pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150))

        # screen.blit(pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150)),(400, 500))
        # screen.blit(pygame.transform.smoothscale(self.plDeck[2].cardimage,(100,150)),(500, 500))
        # screen.blit(pygame.transform.smoothscale(self.plDeck[3].cardimage,(100,150)),(600, 500))
        # screen.blit(pygame.transform.smoothscale(self.plDeck[4].cardimage,(100,150)),(700, 500))
        # screen.blit(pygame.transform.smoothscale(self.plDeck[5].cardimage,(100,150)),(800, 500))
        # screen.blit(pygame.transform.smoothscale(self.plDeck[6].cardimage,(100,150)),(900, 500))

        pygame.display.update()

        # Initiate special rule.
        start = True
        cardChoice = 0
        counter = 1
        difference = abs(7-len(self.plDeck))
        while start:
            if counter > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos

                        first_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(300, 500))
                        second_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(400, 500))
                        third_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(500, 500))
                        fourth_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(600, 500))
                        fifth_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(700, 500))
                        sixth_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(800, 500))
                        seventh_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(900, 500))
                        Eight_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(950, 500))
                        ninth_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(1000, 500))
                        draw_pile_image = drawPile[0].cardimage

                        # Creating colour value for BLUE as part of refac.
                        BLUE = 70, 130, 180

                        # while counter > 0:
                        if first_card_rect.collidepoint(x, y):
                            pygame.draw.rect(screen, BLUE, (300, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (300, 500))
                            pygame.display.update()
                            cardChoice = 1
                            counter = counter - 1
                            start = False

                        elif second_card_rect.collidepoint(x, y):
                            pygame.draw.rect(screen, BLUE, (400, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (400, 500))
                            pygame.display.update()
                            cardChoice = 2
                            counter = counter - 1
                            start = False

                        elif third_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (500, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (500, 500))
                            pygame.display.update()
                            cardChoice = 3
                            counter = counter - 1
                            start = False

                        elif fourth_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (600, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (600, 500))
                            pygame.display.update()
                            cardChoice = 4
                            counter = counter - 1
                            start = False

                        elif fifth_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (700, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (700, 500))
                            pygame.display.update()
                            cardChoice = 5
                            counter = counter - 1
                            start = False

                        elif sixth_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (800, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (800, 500))
                            pygame.display.update()
                            cardChoice = 6
                            counter = counter - 1
                            start = False

                        elif seventh_card_rect.collidepoint(x, y):

                            pygame.draw.rect(screen, BLUE, (900, 500, 100, 150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image, (100, 150)), (900, 500))
                            pygame.display.update()
                            cardChoice = 7
                            counter = counter - 1
                            start = False

                        #for i in range(difference):
                            #pygame.draw.rect(screen,BLUE, (900-i*100, 500, 100, 150))
                            #pygame.display.update()



            elif cardChoice != 0:
                start = False
                return cardChoice

        #print('wtf')

        # Check the click interface works
        if(cardChoice > 1):
            discardPile.append(self.plDeck[cardChoice - 1])
        # Remove card from player's deck.
        self.plDeck.pop(cardChoice - 1)

        self.plDeck.insert(cardChoice - 1, drawPile[0])
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
        pygame.event.clear()
        image_small = pygame.transform.smoothscale(pygame.image.load('Cards New/card_back.png'), (100, 150))
        draw_new_card_rect = pygame.transform.smoothscale(image_small, (100, 150)).get_rect(topleft=(650, 280))

        #first_card_rect = pygame.transform.smoothscale(card_interface[j], (100, 150)).get_rect(topleft=(300, 500))



        while True:
            # Ask player to for their choice.
            while True:
                try:
                    counter1 = 1
                    while counter1 > 0:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos

                                if draw_new_card_rect.collidepoint(x, y):
                                    playerChoice = 0
                                    screen.blit(pygame.transform.smoothscale(drawPile[0].cardimage, (100, 150)),(950, 500))
                                    pygame.display.update()
                                    break

                                elif first_card_rect.collidepoint(x, y):
                                    playerChoice = 1

                                    # self.check(drawPile, discardPile, playerChoice, newGame)
                                    # result = self.check(drawPile, discardPile, playerChoice, newGame)
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        counter1 = counter1 - 1
                                        pygame.draw.rect(screen, BLUE, (300, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        # screen.blit(discardPile[0], (500, 280))
                                        pygame.display.update()

                                elif second_card_rect.collidepoint(x, y):
                                    playerChoice = 2
                                    # self.check(drawPile, discardPile, playerChoice, newGame)
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        pygame.draw.rect(screen, BLUE, (400, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        # screen.blit(discardPile[0], (500, 280))
                                        pygame.display.update()
                                        counter1 = counter1 - 1

                                elif third_card_rect.collidepoint(x, y):
                                    playerChoice = 3
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        pygame.draw.rect(screen, BLUE, (500, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        # screen.blit(discardPile[0], (500, 280))
                                        pygame.display.update()

                                        counter1 = counter1 - 1

                                elif fourth_card_rect.collidepoint(x, y):
                                    playerChoice = 4
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        pygame.draw.rect(screen, BLUE, (600, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        pygame.display.update()

                                        counter1 = counter1 - 1



                                elif fifth_card_rect.collidepoint(x, y):
                                    playerChoice = 5
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        pygame.draw.rect(screen, BLUE, (700, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        pygame.display.update()

                                        counter1 = counter1 - 1



                                elif sixth_card_rect.collidepoint(x, y):
                                    playerChoice = 6
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:

                                        pygame.draw.rect(screen, BLUE, (800, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        pygame.display.update()
                                        counter1 = counter1 - 1

                                elif seventh_card_rect.collidepoint(x, y):
                                    playerChoice = 7
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        pygame.draw.rect(screen, BLUE, (900, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        pygame.display.update()
                                        counter1 = counter1 - 1

                                #Extra cards
                                elif Eight_card_rect.collidepoint(x, y):
                                    playerChoice = 7
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        pygame.draw.rect(screen, BLUE, (950, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        pygame.display.update()
                                        counter1 = counter1 - 1

                                elif ninth_card_rect.collidepoint(x, y):
                                    playerChoice = 7
                                    if self.check(drawPile, discardPile, playerChoice, newGame) != None:
                                        pygame.draw.rect(screen, BLUE, (1050, 500, 100, 150))
                                        screen.blit(pygame.transform.smoothscale(discardPile[0].cardimage, (100, 150)),
                                                    (500, 280))
                                        pygame.display.update()
                                        counter1 = counter1 - 1



                            # self.check(drawPile, discardPile, playerChoice, newGame)

                    # playerChoice = int(input(
                    # "Press [1-n] and select a valid card to play or press 0 to draw a card from the draw pile and pass: "))

                    pygame.draw.rect(screen,BLUE, (300, 500, 750, 150))
                    if playerChoice == 0:
                        screen.blit(pygame.transform.smoothscale(drawPile[0].cardimage, (100, 150)),(900, 500))
                        pygame.display.update()


                    break
                except:
                    print("Invalid choice, please enter a number")
            break

        return drawPile, discardPile
            # # If 0, draw a card and pass.
            # if playerChoice == 0:
            #     self.plDeck.insert(0, drawPile[0])
            #     drawPile.pop(0)
            #     print("\nPlayer Deck after selecting card.....")
            #     for i in self.plDeck:
            #         print(i)
            #
            #     print("\nDiscard pile after selecting card.....")
            #     for i in discardPile:
            #         print(i)
            #     print(f"\nPlayer {self.playerNo} turn complete.\n")
            #     return drawPile, discardPile
            #
            # # If 1-n, validate the card and proceed.
            # elif playerChoice in range(1, (len(self.plDeck) + 1)):
            #     # If black card
            #     if self.plDeck[playerChoice - 1].cardColour == "Black":
            #         # Wild
            #         if self.plDeck[playerChoice - 1].cardType == "ColorChange":
            #             discardPile.insert(0, self.plDeck[playerChoice - 1])
            #             self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
            #             # change the color
            #             while True:
            #                 newColour = input("\nPlease select a new color(Green, Blue, Yellow or Red): ")
            #                 if newColour == 'Green' or 'Blue' or 'Yellow' or 'Red':
            #                     break
            #                 else:
            #                     print("Please enter 'Green', 'Blue', 'Yellow' or 'Red'")
            #             globals.currentGameColour = newColour
            #             return drawPile, discardPile
            #
            #         # Wild Draw
            #         if self.plDeck[playerChoice - 1].cardType == "Draw Four":
            #             discardPile.insert(0, self.plDeck[playerChoice - 1])
            #             self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
            #             # change the color
            #             while True:
            #                 newColour = input("\nPlease select a new color(Green, Blue, Yellow or Red): ")
            #                 if newColour == 'Green' or 'Blue' or 'Yellow' or 'Red':
            #                     break
            #                 else:
            #                     print("Please enter 'Green', 'Blue', 'Yellow' or 'Red'")
            #             globals.currentGameColour = newColour
            #             # Next player draw four and skip
            #             nextPlayer = newGame.moveToNextPlayer(globals.current)
            #             for UnoCard in drawPile[0:4]:
            #                 # print(nextPlayer)
            #                 newGame.playerList[nextPlayer].plDeck.append(UnoCard)
            #                 drawPile.pop(drawPile.index(UnoCard))
            #             # Skip the next person's round
            #             globals.current = newGame.moveToNextPlayer(globals.current)
            #
            #             return drawPile, discardPile
            #
            #     # If normal card
            #     elif self.plDeck[playerChoice - 1].cardType == "Normal":
            #         # Check color is the same or number is the same
            #         if self.plDeck[playerChoice - 1].cardColour == globals.currentGameColour or \
            #                 self.plDeck[playerChoice - 1].cardNumber == globals.currentGameNumber:
            #             # Make the selection as the top card of the discard pile and add it to discard pile.
            #             discardPile.insert(0, self.plDeck[playerChoice - 1])
            #             # Remove card from player deck.
            #             self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
            #             print("Player Deck after selecting card.....")
            #             for i in self.plDeck:
            #                 print(i)
            #             return drawPile, discardPile
            #         else:
            #             print("It is not a valid card, please choose again")
            #
            #     # If not a normal card (functional card)
            #     elif self.plDeck[playerChoice - 1].cardType != "Normal":
            #         if self.plDeck[playerChoice - 1].cardColour == globals.currentGameColour or \
            #                 self.plDeck[playerChoice - 1].cardType == globals.currentGameType:
            #             ######### Draw 2 ########
            #             if self.plDeck[playerChoice - 1].cardType == "Draw Two":
            #                 discardPile.insert(0, self.plDeck[playerChoice - 1])
            #                 self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
            #                 # You draw two cards
            #                 nextPlayer = newGame.moveToNextPlayer(globals.current)
            #                 for UnoCard in drawPile[0:2]:
            #                     # print(nextPlayer)
            #                     newGame.playerList[nextPlayer].plDeck.append(UnoCard)
            #                     drawPile.pop(drawPile.index(UnoCard))
            #                 # Skip the next person's round
            #                 globals.current = newGame.moveToNextPlayer(globals.current)
            #                 # Test
            #                 # print("Next player deck after the privious player use draw two card.....")
            #                 # for i in newGame.playerList[nextPlayer].plDeck:
            #                 #     print(i)
            #
            #                 print("Player Deck after selecting card.....")
            #                 for i in self.plDeck:
            #                     print(i)
            #                 return drawPile, discardPile
            #
            #             ######## Reverse ########
            #             if self.plDeck[playerChoice - 1].cardType == "Reverse":
            #                 globals.ascending = not globals.ascending
            #                 discardPile.insert(0, self.plDeck[playerChoice - 1])
            #                 # Remove card from player deck.
            #                 self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
            #                 print("Player Deck after selecting card.....")
            #                 for i in self.plDeck:
            #                     print(i)
            #                 return drawPile, discardPile
            #
            #             ######## Skip ########
            #             if self.plDeck[playerChoice - 1].cardType == "Skip":
            #                 discardPile.insert(0, self.plDeck[playerChoice - 1])
            #                 self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
            #                 print(globals.current)
            #                 globals.current = newGame.moveToNextPlayer(globals.current)
            #                 print(globals.current)
            #                 return drawPile, discardPile
            #
            #         else:
            #             print("It is not a valid card, please choose again")
            # else:
            #     print("Choice out of range, please enter the correct number")

    def __repr__(self):
        playerTemp = []
        for i in self.plDeck:
            playerTemp.append(i)

        return repr(f"Name: {type(self)} | Deck: {playerTemp}")

        #Helper function to display current turn. Pygame.
    def displayCurrentTurnIcon(screen, playerNo):
        CurrentTurnFont = pygame.font.Font("welcome page/font1.ttf", 45)
        Main_TEXT = CurrentTurnFont.render("Current Turn", True, "white")

        #if player no:
        #Render certain position

        if(playerNo == 0):
            Main_RECT = Main_TEXT.get_rect(topleft=(625, 670))
            screen.blit(Main_TEXT, Main_RECT)
            pygame.display.update()
    
        elif(playerNo == 1):
            Main_RECT = Main_TEXT.get_rect(topleft=(1000, 400))
            screen.blit(Main_TEXT, Main_RECT)
            pygame.display.update()

        elif(playerNo == 2):
            Main_RECT = Main_TEXT.get_rect(topleft=(200, 400))
            screen.blit(Main_TEXT, Main_RECT)
            pygame.display.update()

        elif(playerNo == 3):
            Main_RECT = Main_TEXT.get_rect(topleft=(670, 625))
            screen.blit(Main_TEXT, Main_RECT)
            pygame.display.update()



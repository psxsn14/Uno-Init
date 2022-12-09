#import AI_Strategy
from pickletools import pybool
from BaseClasses import globals
import pygame

# Class for handling Player activities.
class Player:
    def __init__(self, playerNo, plDeck=[]):
        # super().__init__()
        self.playerNo = playerNo
        self.plDeck = plDeck

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
        
        #Set up the cards - pygame.
        card_interface = []
        for j in range(len(self.plDeck)):
            
            card_interface.append(pygame.transform.smoothscale(self.plDeck[j].cardimage,(100,150)))
            screen.blit(pygame.transform.smoothscale(self.plDeck[j].cardimage,(100,150)),(300 + j*100, 500))
            
            #pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150)),
            #pygame.transform.smoothscale(self.plDeck[2].cardimage,(100,150)),
            #pygame.transform.smoothscale(self.plDeck[3].cardimage,(100,150)),
            #pygame.transform.smoothscale(self.plDeck[4].cardimage,(100,150)),
            #pygame.transform.smoothscale(self.plDeck[5].cardimage,(100,150)),
            #pygame.transform.smoothscale(self.plDeck[6].cardimage,(100,150)),
            #]

        #playersHand = pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150))
        

        
        #screen.blit(pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150)),(400, 500))
        #screen.blit(pygame.transform.smoothscale(self.plDeck[2].cardimage,(100,150)),(500, 500))
        #screen.blit(pygame.transform.smoothscale(self.plDeck[3].cardimage,(100,150)),(600, 500))
        #screen.blit(pygame.transform.smoothscale(self.plDeck[4].cardimage,(100,150)),(700, 500))
        #screen.blit(pygame.transform.smoothscale(self.plDeck[5].cardimage,(100,150)),(800, 500))
        #screen.blit(pygame.transform.smoothscale(self.plDeck[6].cardimage,(100,150)),(900, 500))

        pygame.display.update()

        # Initiate special rule.
        start = True
        while start:
            for event in pygame.event.get():
                    counter = 1
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        

                        first_card_rect = pygame.transform.smoothscale(card_interface[j],(100,150)).get_rect(topleft = (300,500))
                        second_card_rect = pygame.transform.smoothscale(card_interface[j],(100,150)).get_rect(topleft = (400,500))
                        third_card_rect = pygame.transform.smoothscale(card_interface[j],(100,150)).get_rect(topleft = (500,500))
                        fourth_card_rect = pygame.transform.smoothscale(card_interface[j],(100,150)).get_rect(topleft = (600,500))
                        fifth_card_rect = pygame.transform.smoothscale(card_interface[j],(100,150)).get_rect(topleft = (700,500))
                        sixth_card_rect = pygame.transform.smoothscale(card_interface[j],(100,150)).get_rect(topleft = (800,500))
                        seventh_card_rect = pygame.transform.smoothscale(card_interface[j],(100,150)).get_rect(topleft = (900,500))
                        draw_pile_image = drawPile[0].cardimage

                        #Creating colour value for BLUE as part of refac.
                        BLUE = 70,130,180 

                        #while counter > 0:
                        if  first_card_rect.collidepoint(x,y):
                            pygame.draw.rect(screen, BLUE, (300,500,100,150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image,(100,150)),(300, 500))
                            pygame.display.update()
                            cardChoice = 1
                            counter = counter -1

                        elif  second_card_rect.collidepoint(x,y):
                            pygame.draw.rect(screen, BLUE, (400,500,100,150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image,(100,150)),(400, 500))
                            pygame.display.update()
                            cardChoice = 2
                            counter = counter -1

                        elif third_card_rect.collidepoint(x,y):

                            pygame.draw.rect(screen, BLUE, (500,500,100,150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image,(100,150)),(500, 500))
                            pygame.display.update()
                            cardChoice = 3
                            counter = counter -1

                        elif fourth_card_rect.collidepoint(x,y):

                            pygame.draw.rect(screen, BLUE, (600,500,100,150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image,(100,150)),(600, 500))
                            pygame.display.update()
                            cardChoice = 4
                            counter = counter -1

                        elif fifth_card_rect.collidepoint(x,y):

                            pygame.draw.rect(screen, BLUE, (700,500,100,150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image,(100,150)),(700, 500))
                            pygame.display.update()
                            cardChoice = 5
                            counter = counter -1

                        elif  sixth_card_rect.collidepoint(x,y):

                            pygame.draw.rect(screen, BLUE, (800,500,100,150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image,(100,150)),(800, 500))
                            pygame.display.update()
                            cardChoice = 6
                            counter = counter -1

                        elif seventh_card_rect.collidepoint(x,y):

                            pygame.draw.rect(screen, BLUE, (900,500,100,150))
                            screen.blit(pygame.transform.smoothscale(draw_pile_image,(100,150)),(900, 500))
                            pygame.display.update()
                            cardChoice = 7
                            counter = counter -1
            if counter == 0:
                pygame.display.update()
                break
                
        #Check the click interface works 
        print('Card Choice:')
        print(cardChoice)

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
                    counter1 = 1
                    while counter1 > 0:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x,y = event.pos
                            
                            if  first_card_rect.collidepoint(x,y):
                                pygame.draw.rect(screen, BLUE, (300,500,100,150))
                                screen.blit(pygame.transform.smoothscale(self.plDeck[0].cardimage,(100,150)),(500,280))
                                pygame.display.update()
                                playerChoice = 1
                                counter1 = counter1 -1

                            elif  second_card_rect.collidepoint(x,y):
                                pygame.draw.rect(screen, BLUE, (400,500,100,150))
                                screen.blit(pygame.transform.smoothscale(self.plDeck[1].cardimage,(100,150)),(500, 280))
                                pygame.display.update()
                                playerChoice = 2
                                counter1 = counter1 -1

                            elif third_card_rect.collidepoint(x,y):

                                pygame.draw.rect(screen, BLUE, (500,500,100,150))
                                screen.blit(pygame.transform.smoothscale(self.plDeck[2].cardimage,(100,150)),(500, 280))
                                pygame.display.update()
                                playerChoice = 3
                                counter1 = counter1 -1

                            elif fourth_card_rect.collidepoint(x,y):

                                pygame.draw.rect(screen, BLUE, (600,500,100,150))
                                screen.blit(pygame.transform.smoothscale(self.plDeck[3].cardimage,(100,150)),(500, 280))
                                pygame.display.update()
                                playerChoice = 4
                                counter1 = counter1 -1

                            elif fifth_card_rect.collidepoint(x,y):

                                pygame.draw.rect(screen, BLUE, (700,500,100,150))
                                screen.blit(pygame.transform.smoothscale(self.plDeck[4].cardimage,(100,150)),(500, 280))
                                pygame.display.update()
                                playerChoice = 5
                                counter1 = counter1 -1

                            elif  sixth_card_rect.collidepoint(x,y):

                                pygame.draw.rect(screen, BLUE, (800,500,100,150))
                                screen.blit(pygame.transform.smoothscale(self.plDeck[5].cardimage,(100,150)),(500, 280))
                                pygame.display.update()
                                playerChoice = 6
                                counter1 = counter1 -1

                            elif seventh_card_rect.collidepoint(x,y):

                                pygame.draw.rect(screen, BLUE, (900,500,100,150))
                                screen.blit(pygame.transform.smoothscale(self.plDeck[6].cardimage,(100,150)),(500, 280))
                                pygame.display.update()
                                playerChoice = 7
                                counter1 = counter1 -1

                    #playerChoice = int(input(
                        #"Press [1-n] and select a valid card to play or press 0 to draw a card from the draw pile and pass: "))
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


    def __repr__(self):
        playerTemp = []
        for i in self.plDeck:
            playerTemp.append(i)

        return repr(f"Name: {type(self)} | Deck: {playerTemp}")



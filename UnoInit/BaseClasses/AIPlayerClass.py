from BaseClasses import AI_Strategy
from BaseClasses.PlayerClass import Player
from BaseClasses import globals
import time
import pygame


class AIPlayer(Player):

    def __init__(self, playerNo, plDeck=[]):
        super().__init__(playerNo, plDeck)
        # self.playerNo = playerNo
        # self.plDeck = plDeck

    def draw_left(self, screen, image_small):
        count = len(self.plDeck)
        if count > 0:
            for l in range(count):
                # Left side comp cards
                x = 100 + l * 60
                count -= 1
                screen.blit(image_small, (100, (x)))
                pygame.display.update()

    def draw_right(self, screen, image_right):
        count = len(self.plDeck)
        if count > 0:
            for f in range(7):
                # Right side comp cards
                x = 100 + f * 60
                count -= 1
                screen.blit(image_right, (1066, (x)))
                pygame.display.update()

    def draw_top(self, screen, image_top):
        print(len(self.plDeck))
        count = len(self.plDeck)
        if count > 0:
            for k in range(len(self.plDeck)):
                # Right side comp cards
                x = 423 + k * 50
                count -= 1
                screen.blit(image_top, (x, 60))
                pygame.display.update()

    def playTurn(self, newGame, drawPile, discardPile, screen):
        # AI action
        # aicard = []
        BLUE = 70, 130, 180
        ai = AI_Strategy.AI(self.plDeck, globals.currentGameCard, drawPile)
        ai_discard, _ = ai.change_card()
        # discard one
        discardPile.append(ai_discard)
        self.plDeck.remove(ai_discard)
        # draw one
        self.plDeck.insert(0, drawPile[0])
        drawPile.pop(0)
        # ai.can_play()
        ai_play, action = ai.play_action()
        # print("AI discard: " + str(ai_discard))
        print("AI play: " + str(ai_play))
        print("AI action: " + action)

        image_small = pygame.transform.smoothscale(pygame.image.load('Cards New/card_back.png'), (100, 150))
        image_small = pygame.transform.rotate(image_small, 90)

        # rectangle = pygame.transform.smoothscale(, (100, 150))

        image_right = pygame.transform.rotate(image_small, 180)
        image_top = pygame.transform.rotate(image_small, 270)

        # judge by action
        # draw means no card to play
        if action == 'draw':
            self.plDeck.insert(0, drawPile[0])
            drawPile.pop(0)
            # return drawPile, discardPile
        elif action == 'play':
            if ai_play.cardType == "Normal":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                # return drawPile, discardPile
            elif ai_play.cardType == "Reverse":
                globals.ascending = not globals.ascending
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                # return drawPile, discardPile
            elif ai_play.cardType == "Skip":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                globals.current = newGame.moveToNextPlayer(globals.current)
                # return drawPile, discardPile
            elif ai_play.cardType == "Draw Two":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)

                nextPlayer = newGame.moveToNextPlayer(globals.current)
                for UnoCard in drawPile[0:2]:
                    # print(nextPlayer)
                    newGame.playerList[nextPlayer].plDeck.append(UnoCard)
                    drawPile.pop(drawPile.index(UnoCard))
                
                image_small = pygame.transform.smoothscale(pygame.image.load('Cards New/card_back.png'), (100, 150))
                image_small = pygame.transform.rotate(image_small, 90)

                image_right = pygame.transform.rotate(image_small, 180)
                image_top = pygame.transform.rotate(image_small, 270)
                
                #AI Player 1 draw 4
                if nextPlayer == 1:
                    pygame.draw.rect(screen, BLUE, (100, 100, 150, 900))
                    count = len(self.plDeck) + 2
                    if count > 0:
                        for f in range(7):
                        # Right side comp cards
                            x = 100 + f * 60
                            count -= 1
                            screen.blit(image_right, (1066, (x)))
                            pygame.display.update()

                # if nextPlayer == 1:
                #     pygame.draw.rect(screen, BLUE, (100, 100, 150, 900))
                #     count = len(self.plDeck) + 2
                #     if count > 0:
                #         for f in range(7):
                #             # Right side comp cards
                #             x = 100 + f * 60
                #             count -= 1
                #             screen.blit(self.image_right, (1066, (x)))
                #             pygame.display.update()
                #
                # if nextPlayer == 2:
                #     pygame.draw.rect(screen, BLUE, (1066, 100, 150, 900))
                #     count = len(self.plDeck) + 2
                #     if count > 0:
                #         for f in range(7):
                #             # Right side comp cards
                #             x = 100 + f * 60
                #             count -= 1
                #             screen.blit(self.image_right, (1066, (x)))
                #             pygame.display.update()
                #
                # if nextPlayer == 3:
                #     pygame.draw.rect(screen, BLUE, (1066, 100, 150, 900))
                #     count = len(self.plDeck) + 2
                #     if count > 0:
                #         for f in range(7):
                #             # Right side comp cards
                #             x = 100 + f * 60
                #             count -= 1
                #             screen.blit(self.image_right, (1066, (x)))
                #             pygame.display.update()
                # Skip the next person's round
                globals.current = newGame.moveToNextPlayer(globals.current)
                # return drawPile, discardPile
        else:
            if ai_play.cardType == "ColorChange":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                globals.currentGameColour = action
                globals.currentGameType = ai_play.cardType
                globals.currentGameNumber = ai_play.cardNumber
                # return drawPile, discardPile
            elif ai_play.cardType == "Draw Four":
                discardPile.insert(0, ai_play)
                self.plDeck.remove(ai_play)
                globals.currentGameColour = action
                globals.currentGameType = ai_play.cardType
                globals.currentGameNumber = ai_play.cardNumber
                nextPlayer = newGame.moveToNextPlayer(globals.current)

                for UnoCard in drawPile[0:4]:
                    # print(nextPlayer)
                    newGame.playerList[nextPlayer].plDeck.append(UnoCard)
                    drawPile.pop(drawPile.index(UnoCard))

                # AI Player 1 draw 4
                # if globals.current == 1:
                #     pygame.draw.rect(screen, BLUE, (100, 100, 150, 900))
                #     count = len(self.plDeck) + 4
                #     if count > 0:
                #         for f in range(7):
                #             # Right side comp cards
                #             x = 100 + f * 60
                #             count -= 1
                #             screen.blit(image_right, (1066, (x)))
                #             pygame.display.update()
                #
                # if globals.current == 2:
                #     pygame.draw.rect(screen, BLUE, (1066, 100, 150, 900))
                #     count = len(self.plDeck) + 4
                #     if count > 0:
                #         for f in range(7):
                #             # Right side comp cards
                #             x = 100 + f * 60
                #             count -= 1
                #             screen.blit(image_right, (1066, (x)))
                #             pygame.display.update()
                #
                # if globals.current == 3:
                #     pygame.draw.rect(screen, BLUE, (1066, 100, 150, 900))
                #     count = len(self.plDeck) + 4
                #     if count > 0:
                #         for f in range(7):
                #             # Right side comp cards
                #             x = 100 + f * 60
                #             count -= 1
                #             screen.blit(image_right, (1066, (x)))
                #             pygame.display.update()

                # Skip the next person's round
                globals.current = newGame.moveToNextPlayer(globals.current)

                # return drawPile, discardPile
        if ai_play is not None:

            screen.blit(pygame.transform.smoothscale(ai_play.cardimage, (100, 150)), (400, 280))
            pygame.display.update()

            image_small = pygame.transform.smoothscale(pygame.image.load('Cards New/card_back.png'), (100, 150))
            image_small = pygame.transform.rotate(image_small, 90)

            # rectangle = pygame.transform.smoothscale(, (100, 150))

            image_right = pygame.transform.rotate(image_small, 180)
            image_top = pygame.transform.rotate(image_small, 270)

            # Refresh the screen by drawing over old cards
            pygame.draw.rect(screen, BLUE, (100, 100, 150, 900))
            pygame.display.update()
        # if count > 0:
        #     for l in range(7):
        #         if globals.AIplayers == 1:
        #             count = count - 7
        #             pass
        #         else:
        #             # Left side comp cards
        #             x = 100 + l * 60
        #             count -= 1
        #             screen.blit(self.image_small, (100, (x)))
        #             pygame.display.update()
        #             time.sleep(0.1)

        if globals.AIplayers == 1:
            rectCoord = [50, 50, 1300, 170]
            rect = pygame.Rect(rectCoord)
            pygame.draw.rect(screen, BLUE, rect)
            # pygame.draw
            pygame.display.update()
            time.sleep(3)

            self.draw_top(screen, image_top)
            pygame.display.update()

        # to refresh other AI players, when this is feature is ready.
        # pygame.draw.rect(screen, BLUE, (1066, 100, 150, 900))

        if globals.AIplayers == 2:
            self.draw_left(screen, image_small)
            self.draw_right(screen, image_right)
            pygame.display.update()

        # to refresh other AI players, when this is feature is ready.
        # pygame.draw.rect(screen, BLUE, (1066, 100, 150, 900))
        if globals.AIplayers == 3:
            self.draw_top(screen, image_top)
            self.draw_left(screen, image_small)
            self.draw_right(screen, image_right)
            pygame.display.update()

            # count = len(self.plDeck)
            # if count > 0:
            #     for l in range(count):
            #         # Left side comp cards
            #         x = 100 + l * 60
            #         count -= 1
            #         screen.blit(image_small, (100, (x)))
            #         pygame.display.update()
            #
            #
            # count = len(self.plDeck)
            # if count > 0:
            #     for f in range(7):
            #         # Right side comp cards
            #         x = 100 + f * 60
            #         count -= 1
            #         screen.blit(image_right, (1066, (x)))
            #         pygame.display.update()
            #
            # if globals.AIplayers == 1:
            #     count = len(self.plDeck)
            #     if count > 0:
            #         for k in range(7):
            #             # Right side comp cards
            #             x = 423 + k * 50
            #             count -= 1
            #             screen.blit(image_top, (x, 60))
            #             pygame.display.update()

        return drawPile, discardPile

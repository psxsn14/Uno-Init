from BaseClasses import AI_Strategy
from BaseClasses.PlayerClass import Player
from BaseClasses import globals
import pygame


class AIPlayer(Player):
    def __init__(self, playerNo, plDeck=[]):
        super().__init__(playerNo, plDeck)
        # self.playerNo = playerNo
        # self.plDeck = plDeck

    #
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
        print("AI discard: " + str(ai_discard))
        print("AI play: " + str(ai_play))
        print("AI action: " + action)

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
                return drawPile, discardPile
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
                # Skip the next person's round
                globals.current = newGame.moveToNextPlayer(globals.current)

                # return drawPile, discardPile
        if ai_play is not None:
            pygame.draw.rect(screen, BLUE, (600, 500, 100, 150))
            screen.blit(pygame.transform.smoothscale(ai_play.cardimage, (100, 150)),
                        (500, 280))
            pygame.display.update()

        return drawPile, discardPile

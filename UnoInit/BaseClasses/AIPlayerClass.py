
from BaseClasses import AI_Strategy
from BaseClasses.PlayerClass import Player
from BaseClasses import globals

class AIPlayer(Player):
    def __init__(self, playerNo, plDeck=[]):
        super().__init__(playerNo, plDeck)
        # self.playerNo = playerNo
        # self.plDeck = plDeck

    #
    def playTurn(self, newGame, drawPile, discardPile):
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
                self.plDeck.pop(ai_play)
                return drawPile, discardPile
            elif ai_play.cardType == "Skip":
                discardPile.insert(0, ai_play)
                self.plDeck.pop(ai_play)
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
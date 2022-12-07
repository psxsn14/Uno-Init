#UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

import BaseClasses.UnoClass
# I have written some code to check certain things as you see below. I will flesh it out more by tomorrow.

newGame = BaseClasses.UnoClass.Uno()
        
        

#Card class.
class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber = "None", cardValue = "None"):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue
        

    def __repr__(self):
        return repr(f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")

newGame = Uno()

newGame.startPreGame(newGame.createNewDeck())

newGame.startGame()









#UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

from .. import PlayerClass
from .. import UnoClass

newGame = UnoClass.Uno()

newGame.startPreGame(newGame.createNewDeck())

newGame.startGame()









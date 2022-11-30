import random

class UnoCard:
    def __init__(self, cardColour, cardType, cardFace=None, cardValue= None): # "20" --> 20
        self.cardFace = cardFace
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue   # huahui change

    # def __repr__(self):    # show card details
    #     return repr(
    #         f"Card Colour: {self.cardColour} | Card Face: {self.cardFace} |  Card Type: {self.cardType} | Card Value: {self.cardValue}")

    def __str__(self):    # show colour and face
        return self.cardColour + ' ' + str(self.cardFace)

class hh_test():
    def __init__(self):
        self.blackCards = []  # 11.28 new
        self.greenCards = []
        self.yellowCards = []
        self.blueCards = []
        self.redCards = []
        self.NewDeck = []
        self.playerCards = []
        self.AICards = []
        self.discardPile = []
        self.inUsePile = []

    # Create a new shuffled deck.
    def createNewDeck(self):
        # Create and save all new UnoCard objects to their respective lists.
        self.greenCards = [UnoCard("Green", "Normal", i,i) for i in range(0, 10)] + \
                          [UnoCard("Green", "Normal", i,i) for i in range(1, 10)] + \
                          [UnoCard("Green", "Special", "Skip", 20) for _ in range(0, 2)] +\
                          [UnoCard("Green", "Special", "Reverse", 20) for _ in range(0, 2)] +\
                          [UnoCard("Green", "Special", "Draw_2", 20) for _ in range(0, 2)]

        self.blueCards = [UnoCard("Blue", "Normal", i, i) for i in range(0, 10)] + \
                         [UnoCard("Blue", "Normal", i, i) for i in range(1, 10)]+\
                         [UnoCard("Blue", "Special", "Skip", 20) for _ in range(0, 2)] + \
                         [UnoCard("Blue", "Special", "Reverse", 20) for _ in range(0, 2)] +\
                         [UnoCard("Blue", "Special", "Draw_2", 20) for _ in range(0, 2)]
        
        self.yellowCards = [UnoCard("Yellow", "Normal", i, i) for i in range(0, 10)] +\
                           [UnoCard("Yellow", "Normal", i, i) for i in range(1, 10)] + \
                           [UnoCard("Yellow", "Special", "Skip", 20) for _ in range(0, 2)] + \
                           [UnoCard("Yellow", "Special", "Reverse", 20) for _ in range(0, 2)] + \
                           [UnoCard("Yellow", "Special", "Draw_2", 20) for _ in range(0, 2)]

        self.redCards = [UnoCard("Red", "Normal", i, i) for i in range(0, 10)] + \
                        [UnoCard("Red", "Normal", i, i) for i in range(1, 10)] + \
                        [UnoCard("Red", "Special", "Skip", 20) for _ in range(0, 2)] +\
                        [UnoCard("Red", "Special", "Reverse", 20) for _ in range(0, 2)] + \
                        [UnoCard("Red", "Special", "Draw_2", 20) for _ in range(0, 2)]

        self.blackCards = [UnoCard("Black", "Special", "Draw_4", 50)] * 4 +\
                          [UnoCard("Black", "Special", "Wild", 50)] * 4

        # Combine, shuffle and return the deck as a list of UnoCard objects.
        shuffledDeck = self.greenCards + self.yellowCards \
                       + self.redCards + self.blueCards + self.blackCards


        random.shuffle(shuffledDeck)   #  shuffle

        return shuffledDeck  # 108 cards



def show_all_cards(Obname):
    x = Obname()
    h = x.createNewDeck()
    [print(i) for i in h]
    return len(h)


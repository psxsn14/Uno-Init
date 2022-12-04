# This file creates a pile of cards which is orderly and not repeated. It is used for AI testing.

class UnoCard:
    def __init__(self, cardColour, cardType, cardNumber="None", cardValue="None"):
        self.cardNumber = cardNumber
        self.cardColour = cardColour
        self.cardType = cardType
        self.cardValue = cardValue

    def __repr__(self):
        return repr(f"Number on Card: {self.cardNumber} | Card Colour: {self.cardColour} | Card Type: {self.cardType} | Card Value: {self.cardValue}")

def createNewDeck():
    # Create and save all new UnoCard objects to their respective lists.
    greenCards = [UnoCard("Green", "Normal", i, i) for i in range(0, 10)] + [UnoCard("Green", "Skip", "None", 20)] + [
        UnoCard("Green", "Reverse", "None", 20)] \
                 + [UnoCard("Green", "Draw Two", "None", 20)]

    blueCards = [UnoCard("Blue", "Normal", i, i) for i in range(0, 10)] + [UnoCard("Blue", "Skip", "None", 20)] + [
        UnoCard("Blue", "Reverse", "None", 20)] \
                + [UnoCard("Blue", "Draw Two", "None", 20)]

    yellowCards = [UnoCard("Yellow", "Normal", i, i) for i in range(0, 10)] \
                  + [UnoCard("Yellow", "Skip", "None", 20)] + [
                      UnoCard("Yellow", "Reverse", "None", 20)] \
                  + [UnoCard("Yellow", "Draw Two", "None", 20)]

    redCards = [UnoCard("Red", "Normal", i, i) for i in range(0, 10)] \
               + [UnoCard("Red", "Skip", "None", 20)] + [
                   UnoCard("Red", "Reverse", "None", 20)] \
               + [UnoCard("Red", "Draw Two", "None", 20)]

    blackCards = [UnoCard("Black", "ColorChange", "None", 50)] + [
        UnoCard("Black", "Draw Four", "None", 50)]

    # Combine, shuffle and return the deck as a list of UnoCard objects.
    shuffledDeck = greenCards + yellowCards + redCards + blueCards + blackCards
    # random.shuffle(shuffledDeck)
    return shuffledDeck

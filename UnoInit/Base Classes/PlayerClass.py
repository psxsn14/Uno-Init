#Class for handling Player activities.
class Player():
    def __init__(self, playerNo, plDeck = []):
        super().__init__()
        self.playerNo = playerNo
        self.plDeck = plDeck

    def playTurn(self, drawPile, currentGameColour, discardPile):
        #Select a card from your hand, and place it below the discard pile.
        
        print(f"Player {self.playerNo} -- Cards on hand:\n")
        for i in self.plDeck:
            print(i)

        #Initiate special rule.
        cardChoice = int(input("\nSPECIAL RULE: Select a card (1-7) from your hand and keep it beneath the discard pile..."))
        #Add player card to the discard pile.
        discardPile.append(self.plDeck[cardChoice - 1])
        #Remove card from player's deck.
        self.plDeck.pop(0)

        #Take top card from draw pile.
        print("\nPlayer 1 takes the top card from the draw pile to their hand...")
        self.plDeck.insert(0, drawPile[0])

        #Play a card or pick another card to pass.
        print("\nCards on hand pre execute:\n")
        for i in self.plDeck:
            print(i)

        print("Current game colour: ",currentGameColour)

        #Ask player to for their choice.
        playerChoice = int(input("Press [1-n] and select a valid card to play or press 0 to draw a card from the draw pile and pass: "))
        #If 0, draw a card and pass.
        if(playerChoice == 0):
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
        
        #If 1-n, validate the card and proceed.
        if(playerChoice in range(1, (len(self.plDeck) + 1))):
        
        #If colour is same but number is different or a special card, can play.
            if(self.plDeck[playerChoice - 1].cardColour == currentGameColour):
                #If normal, play.
                if(self.plDeck[playerChoice - 1].cardType == "Normal"):
                    #Make the selection as the top card of the discard pile and add it to discard pile.
                    discardPile.append(self.plDeck[playerChoice - 1])
                    self.plDeck.pop(self.plDeck.index(self.plDeck[playerChoice - 1]))
                    print("Player Deck after selecting card.....")                   
                    for i in self.plDeck:
                        print(i)
                    return drawPile, discardPile
        #Remove card from player deck.

        #If special, execute stuff.
                 
        #If number is same, but colour is different, can play.
        
        #If colour change, can play.
        
        #If draw4, can only play if no matching colour card on hand.
        
        return drawPile,self.discardPile

    def __repr__(self):
        playerTemp = []
        for i in self.plDeck:
            playerTemp.append(i)

        return repr(f"Name: {type(self)} | Deck: {playerTemp}")

    class AIPlayer(PlayerClass.Player):
        pass
    #Insert AI Code.
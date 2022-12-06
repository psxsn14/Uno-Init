
import random
from fun import *

###################################################################################
# Since there is not yet a UNO logic,
# I wrote some temporary functions to test the AI, you can ignore these

def show_card_list(listofcard):
    [print(i) for i in listofcard]


# Deal cards to a player and update the inUsePile.
def deal_cards(hand_cards, draw_pile):  # 发牌，玩家手牌+7 牌堆-7
    for UnoCard in draw_pile[0:7]:
        hand_cards.append(UnoCard)
        draw_pile.pop(draw_pile.index(UnoCard))
    return hand_cards, draw_pile


def draw_a_card(hand_cards, draw_pile):  # 起牌
    hand_cards.append(draw_pile[0])
    draw_pile.pop(draw_pile.index(draw_pile[0]))
    return hand_cards, draw_pile


def play_a_card(the_card, hand_cards, discard_pile):
    if the_card is None:
        return hand_cards
    else:
        hand_cards.remove(the_card)
        discard_pile.append(the_card)
    return hand_cards


def show_num(AI_card, draw_pile, discard_pile):
    print("手牌：", len(AI_card), "牌堆长度", len(draw_pile), "弃牌长度", len(discard_pile))

def show_simple(listofcard):
    simple_list = []
    for i in listofcard:
        if i.cardNumber != 'None':
            simple_list.append(str(i.cardColour) +' '+ str(i.cardNumber))
        else:
            simple_list.append(str(i.cardColour) + ' '+ str(i.cardType))

    # for i in range(0,len(simple_list)):
    #     print(str(i+1) + ' ' + simple_list[i])
    return simple_list

####################################################################################

# print(len(AI_card))           # 7
# print(len(draw_pile))         # 100
# show_card_list(AI_card)       # random 7 cards
# show_card_list(discard_pile)  # top card without wildcard
####################################################################################
class AI:
    def __init__(self, handlist, topcard,
                 pile_card, human_hand=[],
                 ):

        self.hand_list = handlist  # the cards in AI's hand
        self.top_card = topcard  # the card on the top of discard pile
        self.pile_card = pile_card  # the rest cards in draw pile
        self.human_hand = human_hand  # the cards in Human-player's hand

        self.action = 'play'  # play, draw, pick(a colour)
        self.can_play_cards = []
        self.the_card = None

        # show_card_list(self.hand_list)
    def get_class_name(self):
        return self.__class__.__name__  # get the class name

    # sort hand_list by card Value
    def sort_card(self,listofcard):
        # print(self.hand_list)

        # show_card_list(self.hand_list)
        # print('------------------')
        # for i in self.hand_list:
        #     print(i.cardValue)
        listofcard.sort(key=lambda x: x.cardValue)
        # show_card_list(self.hand_list)
        return listofcard

    #  Before your turn starts, discard a card from your hand and get a new card
    def change_card(self):

        # Card is thrown randomly, no strategy
        # choose a random card to discard from hand_list
        discard_card = random.choice(self.hand_list)

        print("before playing , the discarded card:", show_simple([discard_card]))
        self.action = 'draw'  # get a new card
        print( self.get_class_name(), " needs to", self.action)

        return discard_card, self.action

    # match cards in hand and card on top of discard pile, return a list of available card
    def can_play(self, hand_list, top_card):
        can_play_cards = []
        # print("_________________________")
        # print('The card on the top of discard pile:',show_simple([self.top_card]))
        # print("_________________________")
        # print("AI cards:")
        # show_card_list(self.hand_list)
        # show_simple(self.hand_list)
        # print("_________________________")
        # print("The cards AI can play:")
        for i in hand_list:
            if i.cardNumber is not None : #数字牌情况:颜色相同或者数字相同
                if i.cardColour == top_card.cardColour or i.cardNumber == top_card.cardNumber :
                    can_play_cards.append(i)

            else:  # 功能牌情况：黑色牌或者功能相同
                if i.cardColour == 'Black' or i.cardcardType == top_card.cardType:
                    can_play_cards.append(i)

        # show_simple(self.can_play_cards)
        return can_play_cards

# What AI should do
    def play_action(self):

        if len(self.can_play(self.hand_list,self.top_card)) == 0:
            print("No card can play, draw a card")

            self.action = 'draw'
        else:
            self.the_card = random.choice(self.can_play(self.hand_list,self.top_card))
            self.action = 'play'
            # print("AI plays :",self.the_card)

            if self.the_card.cardColour == "Black":
                self.action = "Red" # When AI use Wild card, it picks red
        print("_________________________")
        print( self.__class__.__name__," decides: ", show_simple([self.the_card]),'  ',self.action)
        return self.the_card, self.action  #

# print(card)
# print(act)

# print('##########################')
# ai.can_play()
#
# print('##########################')
# # ai.play_action()
#
# card,act = ai.play_action()

# print(card.cardColour,card.cardNumber,card.cardType)
# print(act)

# print('##########################')


# print("###################################################")


class EasyAI(AI):
    def change_card(self):  # easy AI, always discard the biggest card
        x = self.sort_card(self.hand_list)
        show_simple(x)
        discard_card = self.hand_list[-1]
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'
        print(self.get_class_name(), " needs to", self.action)
        return discard_card, self.action


# easyai = EasyAI(aicard,top_card,[])
# easyai.change_card()
# easyai.can_play()
# easyai.play_action()


class MediumAI(AI):
    def change_card(self):  # medium AI, always discard the smallest card
        x = self.sort_card(self.hand_list)

        discard_card = self.hand_list[0]
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'
        print(self.get_class_name(), " needs to", self.action)
        return discard_card, self.action



class HardAI(AI):
    def change_card(self):  # hard AI, selects the most frequent colour, discard the smallest card
        x = self.sort_card(self.hand_list)
        colour_list = []
        for i in x:
            colour_list.append(i.cardColour)
        colour_list.remove('Black')             # remove black card
        # find the most frequent colour
        most_colour = max(set(colour_list), key=colour_list.count)
        # match x.cardColour with most_colour to a new list
        colour_match = [i for i in x if i.cardColour == most_colour]
        discard_card = colour_match[0]
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'
        print(self.get_class_name(), " needs to", self.action)
        return discard_card, self.action

class InvincibleAI(HardAI):
    pass



x = createNewDeck()
################################
 # show card with number
# for i in range(0,len(x)):
#     print(str(i)+':',x[i])
#     print(i)
#################################
aicard = []
for i in range(len(x)):
    if i in [38,  12, 3, 19,47,52,53]:
        aicard.append(x[i])
        x[i] = None

# print(aicard)

show_simple(aicard)

print('------------------')
top_card = x[0]
ai = AI(aicard,top_card,[])
ai.play_action()

print('------------------')

easyai = EasyAI(aicard,top_card,[])
easyai.play_action()

print('----------------- ')######')
hardai = HardAI(aicard,top_card,[])
hardai.play_action()

################################################
#case 1:
#


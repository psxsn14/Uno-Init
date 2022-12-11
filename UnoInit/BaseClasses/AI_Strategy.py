import globals
import random
from collections import Counter


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
    # if len(listofcard) == 0:
    #     return simple_list
    if listofcard is None:
        return simple_list
    print('listofcard')
    print(listofcard)
    for i in listofcard:

        if i.cardNumber != 'None':
            simple_list.append(str(i.cardColour) + ' ' + str(i.cardNumber))
        else:
            simple_list.append(str(i.cardColour) + ' ' + str(i.cardType))

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
    def sort_card(self, listofcard):
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

        # print("before playing , the discarded card:", show_simple([discard_card]))
        self.action = 'draw'  # get a new card
        print("AI hand card")
        for i in self.hand_list:
            print(i)
        # print(self.get_class_name(), " needs to", self.action)

        return discard_card, self.action

    # match cards in hand and card on top of discard pile, return a list of available card
    def can_play(self, ai_hand, top_card):
        can_play_cards = []
        # print("_________________________")
        # print('The card on the top of discard pile:',show_simple([self.top_card]))
        # print("_________________________")
        # print("AI cards:")
        # show_card_list(self.hand_list)
        # show_simple(self.hand_list)
        # print("_________________________")
        # print("The cards AI can play:")
        for i in ai_hand:
            if i.cardNumber != 'None':  # Normal card, match colour or number
                if i.cardColour == top_card.cardColour or i.cardNumber == top_card.cardNumber:
                    can_play_cards.append(i)

            else:  # Black card, or Function card, match colour or type
                if i.cardColour == 'Black' or i.cardType == top_card.cardType or i.cardColour == top_card.cardColour:
                    can_play_cards.append(i)

        # show_simple(can_play_cards)
        return can_play_cards

    # What AI should do
    def play_action(self):
        print("AI hand card after switch")
        for i in self.hand_list:
            print(i)

        if len(self.can_play(self.hand_list, self.top_card)) == 0:
            print("No card can play, draw a card")

            self.action = 'draw'
        else:
            self.the_card = random.choice(self.can_play(self.hand_list, self.top_card))
            self.action = 'play'
            # print("AI plays :",self.the_card)

            if self.the_card.cardColour == "Black":
                self.action = "Red"  # When AI use Wild card, it picks red
        print("_________________________")
        # print(self.__class__.__name__, " decides: ", show_simple([self.the_card]), '  ', self.action)
        return self.the_card, self.action  #

    def human_can_play_list(self, human_hand,
                            can_play_cards):  # if AI plays one of the cards in human_hand, human can play
        human_can_play = []
        for card in can_play_cards:
            if self.can_play(human_hand, card):
                human_can_play.append(card)
        return human_can_play

    def human_can_not_play_list(self, human_hand,
                                can_play_cards):  # if AI plays one of the cards in human_hand, human can not play
        human_can_not_play = []
        for card in can_play_cards:
            if not self.can_play(human_hand, card):
                human_can_not_play.append(card)
        return human_can_not_play

    def get_card_colour_of_list(self,
                                listofcard):  # get the colour of the cards in the list, and sort them by number of the card
        colour_list = []
        for card in listofcard:
            if card.cardColour != 'Black':
                colour_list.append(card.cardColour)
        return [i[0] for i in Counter(colour_list).most_common()]

    def color_ai_not_in_hu(self, aicard,
                           human_card):  # return the colour of the cards in AI's hand, but not in human's hand
        ai_color = self.get_card_colour_of_list(aicard)
        hu_color = self.get_card_colour_of_list(human_card)
        color_not_in_hu = []
        for i in aicard:
            if i.cardColour in [i for i in ai_color if i not in hu_color]:
                color_not_in_hu.append(i)
        return color_not_in_hu


class EasyAI(AI):
    def change_card(self):  # easy AI, always discard the biggest card
        x = self.sort_card(self.hand_list)
        show_simple(x)
        discard_card = self.hand_list[-1]
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'
        print(self.get_class_name(), " needs to", self.action)
        return discard_card, self.action


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
        colour_list.remove('Black')  # remove black card
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

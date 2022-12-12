
import globals

import random

from collections import Counter



def show_card_list(listofcard):
    [print(i) for i in listofcard]


def show_simple(listofcard):
    simple_list = []
    if listofcard == [None]:
        return 'None'

    for i in listofcard:

        if i.cardNumber != 'None':
            simple_list.append(str(i.cardColour) +' '+ str(i.cardNumber))
        else:
            simple_list.append(str(i.cardColour) + ' '+ str(i.cardType))

    # for i in range(0,len(simple_list)):
    #     print(str(i+1) + ' ' + simple_list[i])
    return simple_list


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


    def get_class_name(self):
        return self.__class__.__name__  # get the class name

    # sort hand_list by card Value
    def sort_card(self,listofcard):
        listofcard.sort(key=lambda x: x.cardValue)

        return listofcard

    #  Before your turn starts, discard a card from your hand and get a new card
    def change_card(self):

        # Card is thrown randomly, no strategy
        # choose a random card to discard from hand_list
        discard_card = random.choice(self.hand_list)

        # print("before playing , the discarded card:", show_simple([discard_card]))
        self.action = 'draw'  # get a new card
        # print( self.get_class_name(), " needs to", self.action)

        return discard_card, self.action

    # match cards in hand and card on top of discard pile, return a list of available card
    def can_play(self, ai_hand, top_card):
        can_play_cards = []

        for i in ai_hand:
            if i.cardNumber != 'None' :
                if i.cardColour == top_card.cardColour or i.cardNumber == top_card.cardNumber :
                    can_play_cards.append(i)

            else:
                if i.cardColour == 'Black' or i.cardType == top_card.cardType or i.cardColour == top_card.cardColour:
                    can_play_cards.append(i)

        # show_simple(can_play_cards)
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
                all_colour = ['Red', 'Blue', 'Green', 'Yellow']
                self.action = random.choice(all_colour)
        # print("_________________________")
        # print( self.__class__.__name__," decides: ", show_simple([self.the_card]),'  ',self.action)
        return self.the_card, self.action  #

    def human_can_play_list(self,human_hand, can_play_cards): # if AI plays one of the cards in human_hand, human can play
        human_can_play = []
        for card in can_play_cards:
            if self.can_play(human_hand, card):
                human_can_play.append(card)

        return human_can_play
    def human_can_not_play_list(self,human_hand, can_play_cards): # if AI plays one of the cards in human_hand, human can not play
        human_can_not_play = []
        for card in can_play_cards:
            if not self.can_play(human_hand, card):
                human_can_not_play.append(card)
        return human_can_not_play

    def get_card_colour_of_list(self,listofcard):# get the colour of the cards in the list, and sort them by sequence
        colour_list = []
        for card in listofcard:
            if card.cardColour != 'Black':
                colour_list.append(card.cardColour)
        return [i[0]for i  in Counter(colour_list).most_common() ]

    def color_ai_not_in_hu(self, aicard, human_card): # return the colour of the cards in AI's hand, but not in human's hand
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
        # show_simple(x)
        discard_card = self.hand_list[-1]
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'
        print(self.get_class_name(), " needs to", self.action)
        return discard_card, self.action

    def play_action(self):
        action_list = [] # In this list, the cards are sorted, in the front of the list, the cards can follow by human
        if len(self.can_play(self.hand_list,self.top_card)) == 0:
            print("No card can play, draw a card")

            self.action = 'draw'
        else:

            y = self.human_can_play_list(self.human_hand, self.can_play(self.hand_list,self.top_card))
            # put y into action_list
            for i in y:
                action_list.append(i)

            x = self.human_can_not_play_list(self.human_hand, self.can_play(self.hand_list,self.top_card))
            # put x into action_list
            for i in x:
                action_list.append(i)

            self.the_card = action_list[0]
            if action_list[0].cardColour != "Black":
                self.action = 'play'
            else:
                human_card_colour = self.get_card_colour_of_list(self.human_hand)

                if len(human_card_colour) != 0:
                    self.action = random.choice(human_card_colour)
                else:
                    self.action = random.choice(['Red', 'Blue', 'Green', 'Yellow'])
        # print(self.__class__.__name__, " decides: ", show_simple([self.the_card]), '  ', self.action)
        return self.the_card, self.action






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
        if 'Black' in colour_list: # remove black card
            colour_list.remove('Black')
        # find the most frequent colour
        most_colour = max(set(colour_list), key=colour_list.count)
        # match x.cardColour with most_colour to a new list
        colour_match = [i for i in x if i.cardColour == most_colour]
        discard_card = colour_match[0]
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'
        print(self.get_class_name(), " needs to", self.action)
        return discard_card, self.action

    def play_action(self):
        action_list = [] # In this list, the cards are sorted, in the front of the list, the cards can not be followed by human
        if len(self.can_play(self.hand_list,self.top_card)) == 0:
            print("No card can play, draw a card")
            self.action = 'draw'
        else:
          x = self.human_can_not_play_list(self.human_hand, self.can_play(self.hand_list,self.top_card))
          # put x into action_list
          for i in x:
              action_list.append(i)

          y = self.human_can_play_list(self.human_hand, self.can_play(self.hand_list,self.top_card))
          # put y into action_list
          for i in y:
              action_list.append(i)
          # print("action_list:",show_simple(action_list))

          self.the_card = action_list[0]

          if action_list[0].cardColour != "Black":
              self.action = 'play'
          else:
              human_card_colour = self.get_card_colour_of_list(self.human_hand)
              all_colour = ['Yellow', 'Blue', 'Green', 'Red']
              # all_colour - human_card_colour = the colour of the cards in AI's hand, but not in human's hand
              color_not_in_hu = [i for i in all_colour if i not in human_card_colour
                                 and i in self.get_card_colour_of_list(self.hand_list)]
              if len(color_not_in_hu) != 0:
                  self.action = random.choice(color_not_in_hu)
              else:
                  self.action = random.choice(all_colour)
        print(self.__class__.__name__, " decides: ", show_simple([self.the_card]), '  ', self.action)
        return self.the_card, self.action






class InvincibleAI(HardAI):
    def change_card(self):  # invincible AI, selects the card can be followed by human, discard the smallest card

        y = self.human_can_play_list(self.human_hand, self.can_play(self.hand_list, self.top_card))
        if len(y) != 0:
            discard_card = y[0]
        else:
            discard_card = self.hand_list[0]
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'
        print(self.get_class_name(), " needs to", self.action)
        return discard_card, self.action

    def play_action(self):
        action_list = []  # In this list, the cards are sorted, in the front of the list, the cards can not be followed by human
        if len(self.can_play(self.hand_list, self.top_card)) == 0:
            print("No card can play, draw a card")
            self.action = 'draw'
        else:
            x = self.human_can_not_play_list(self.human_hand, self.can_play(self.hand_list, self.top_card))
            # put x into action_list
            for i in x:
                action_list.append(i)
            y = self.human_can_play_list(self.human_hand, self.can_play(self.hand_list, self.top_card))
            # put y into action_list

            for i in y:
                action_list.append(i)
            # print("action_list:",show_simple(action_list))

            if len(self.human_hand) == 1 and action_list[0] in y:
                self.the_card = None
                self.action = 'draw'
            else:
                self.the_card = action_list[0]

                if action_list[0].cardColour != "Black":
                    self.action = 'play'
                else:
                    human_card_colour = self.get_card_colour_of_list(self.human_hand)
                    all_colour = ['Yellow', 'Blue', 'Green', 'Red']
                    # all_colour - human_card_colour = the colour of the cards in AI's hand, but not in human's hand
                    color_not_in_hu = [i for i in all_colour if i not in human_card_colour
                                       and i in self.get_card_colour_of_list(self.hand_list)]
                    if len(color_not_in_hu) != 0:
                        self.action = random.choice(color_not_in_hu)
                    else:
                        self.action = random.choice(all_colour)
        # print(self.__class__.__name__, " decides: ", show_simple([self.the_card]), '  ', self.action)
        return self.the_card, self.action





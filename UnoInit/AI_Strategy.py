# from UnoInit import *


#  AI的基本功能：根据规则，1-换牌 2-执行action
#  进阶AI：整理牌，

###################################################################################
# Since there is not yet a UNO logic,
# I wrote some temporary functions to test the AI, you can ignore these

def show_card_list(listofcard):
    [print(i) for i in listofcard]
#
#
# # Deal cards to a player and update the inUsePile.
# def deal_cards(hand_cards, draw_pile):  # 发牌，玩家手牌+7 牌堆-7
#     for UnoCard in draw_pile[0:7]:
#         hand_cards.append(UnoCard)
#         draw_pile.pop(draw_pile.index(UnoCard))
#     return hand_cards, draw_pile


# def draw_a_card(hand_cards, draw_pile):  # 起牌
#     hand_cards.append(draw_pile[0])
#     draw_pile.pop(draw_pile.index(draw_pile[0]))
#     return hand_cards, draw_pile
#
#
# def play_a_card(the_card, hand_cards, discard_pile):
#     if the_card is None:
#         return hand_cards
#     else:
#         hand_cards.remove(the_card)
#         discard_pile.append(the_card)
#     return hand_cards


# def shownum(AI_card, draw_pile, discard_pile):
#     print("手牌：", len(AI_card), "牌堆长度", len(draw_pile), "弃牌长度", len(discard_pile))


####################################################################################

# print(len(AI_card))           # 7
# print(len(draw_pile))         # 100
# show_card_list(AI_card)       # random 7 cards
# show_card_list(discard_pile)  # top card without wildcard

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

    # sort hand_list by card Value
    # def sort_card(self):
    #     # print(self.hand_list)
    #     # show_card_list(self.hand_list)
    #     # print('------------------')
    #     # for i in self.hand_list:
    #     #     print(i.cardValue)
    #     self.hand_list.sort(key=lambda x: x.cardValue)
    #     show_card_list(self.hand_list)
    #     return self.hand_list

    #  Before your turn starts, discard a card from your hand and get a new card
    def change_card(self):
        discard_card = self.hand_list[0]  # Card is thrown randomly, no strategy
        print("before playing , the discarded card:", discard_card)
        self.action = 'draw'  # get a new card
        print("AI needs to", self.action)
        # return str(discard_card),self.action
        return discard_card, self.action

    # match cards in hand and card on top of discard pile, return a list of available card
    def can_play(self):

        print('The card on the top of discard pile:', self.top_card)
        print("#####################")
        print("AI cards:")
        show_card_list(self.hand_list)
        print("#####################")
        print("The cards AI can play:")
        for i in self.hand_list:
            if i.cardNumber is not None:  # 数字牌情况:颜色相同或者数字相同
                if i.cardColour == self.top_card.cardColour or i.cardNumber == self.top_card.cardNumber:
                    self.can_play_cards.append(i)
                    print(i)
            else:  # 功能牌情况：黑色牌或者功能相同
                if i.cardColour == 'Black' or i.cardcardType == self.top_card.cardType:
                    self.can_play_cards.append(i)
                    print(i)
                pass

        return self.can_play_cards

    # What AI should do
    def play_action(self):

        if len(self.can_play_cards) == 0:
            print("No card can play, draw a card")
            self.action = 'draw'
        else:
            self.the_card = random.choice(self.can_play_cards)
            self.action = 'play'
            print("AI plays :", self.the_card)

            if self.the_card.cardColour == "Black":
                self.action = "red"  # When AI use Wild card, it picks red
        print("AI decides: ", self.the_card, '  ', self.action)
        return self.the_card, self.action  #


# ai.sort_card()
# print(ai.change_card())
# print(ai.action)


# #############################################   The code below just creates something to run ai, you can delete it
# after understanding # create discard_pile and draw_pile (avoid wild card be the first card)
#
# cards = hh_test()
# card = cards.createNewDeck()
#
# draw_pile = []
# discard_pile = []
# AI_card = []
#
# for i in card:
#     if i.cardColour == 'Black':
#         pass
#     else:
#         discard_pile.append(i)
#         if len(discard_pile) == 1:
#             break
#
# draw_pile = [i for i in card if i not in discard_pile]
# AI_card, _ = deal_cards(AI_card, draw_pile)
#
# ##############################################
# #
#
# ai = AI(AI_card, discard_pile[0],draw_pile,human_hand=[])
# ai.change_card()   # return: 1. a card to discard  2: action 'draw', means it should get a new card
# ai.can_play()      #
# ai.play_action()

# n = 5
#
# while n :
#
#
#     print('牌堆顶部',discard_pile[0])
#     ai.can_play_cards()
#     print("你的手牌：")
#     show_card_list(AI_card)
#     nowcard,action = (ai.play_action())
#     print("出的牌是：",nowcard)
#
#
#     if action =='play':
#         print("出牌")
#         play_a_card(nowcard,AI_card,discard_pile)
#     elif action =='draw':
#         print("起牌")
#         draw_a_card(AI_card,draw_pile)
#
#     shownum(AI_card,draw_pile,discard_pile)
#
#     n = n-1
##################################################


# from UnoInit make a handlist of cards


# newGame = Uno()
# newGame.startPreGame(newGame.createNewDeck())
# newGame.startGame()

##############################
#
# newGame = Uno()
#
# newGame.startPreGame(newGame.createNewDeck())
#
# newGame.startGame()

def execute():
    aicard = []
    # newGame.drawPile = newGame.dealCards(aicard)

    ai = AI(aicard, newGame.topDiscardPileCard, newGame.drawPile)
    ai.change_card()
    ai.can_play()
    ai.play_action()


##############################


class EasyAI(AI):
    pass


class MediumAI(AI):
    pass


class HardAI(AI):
    pass


class human_likeAI(MediumAI):
    pass


class InvincibleAI(HardAI):
    pass

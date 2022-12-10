# UNO RULES: https://www.unorules.org/how-many-cards-in-uno/

import random
import copy
from BaseClasses import globals
from BaseClasses.UnoClass import Uno
import pygame
from pygame.locals import *
import time
import pygame.freetype
from WelcomePage import *

pygame.init()

#Setting the screen
screen = pygame.display.set_mode((1366,768))

#main_menu()

start = True
while start:
        for event in pygame.event.get():
            if event.type == QUIT:
                    start = False
                    pygame.quit()

        newGame = Uno()

        newGame.startPreGame(newGame.createNewDeck(), screen)

pygame.quit()
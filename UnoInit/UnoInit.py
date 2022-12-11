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
from BaseClasses.PlayerClass import Player

pygame.init()

#Setting the screen
screen = pygame.display.set_mode((1366,768))

#main_menu()

newGame = Uno()

newGame.startPreGame(newGame.createNewDeck(), screen)

start = True
while start:
        for event in pygame.event.get():
            if event.type == QUIT:
                    start = False
                    pygame.quit()
        #Display current turn
        if(globals.current == 0):
            Player.showCurrentTurnIcon(screen, globals.current)
        elif(globals.current == 1):
            Player.showCurrentTurnIcon(screen, globals.current)


pygame.quit()

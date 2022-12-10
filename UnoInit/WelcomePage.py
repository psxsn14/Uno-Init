
import pygame,sys
from pygame.locals import *
from BaseClasses.UnoClass import Uno


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image=image
        self.x_pos=pos[0]
        self.y_pos=pos[1]
        self.font=font
        self.base_color=base_color
        self.hovering_color=hovering_color
        self.text_input=text_input
        self.text=self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image=self.text
        self.rect=self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.text_rect=self.text.get_rect(center=(self.x_pos,self.y_pos))
        
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text,self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right)and position[1]in range(self.rect.top,self.rect.bottom):
            return True
        return False
    
    def changeColor(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text=self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text=self.font.render(self.text_input, True, self.base_color)

def chooselevel():
    pygame.display.set_caption("chooselevel")
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.fill((70,130,180))# background color
        
        Main_TEXT = get_font(45).render("Choose the level of games", True, "white")
        Main_RECT = Main_TEXT.get_rect(center=(683, 84))
        SCREEN.blit(Main_TEXT, Main_RECT)
    
        PLAY_BACK = Button(image=None, pos=(683,660),
                     text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        EASY_LEVEL = Button(image=None, pos=(150,360),
                     text_input="EASY", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        EASY_LEVEL.changeColor(PLAY_MOUSE_POS)
        EASY_LEVEL.update(SCREEN)

        MIDDLE_LEVEL = Button(image=None, pos=(480,360),
                     text_input="MIDDLE", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        MIDDLE_LEVEL.changeColor(PLAY_MOUSE_POS)
        MIDDLE_LEVEL.update(SCREEN)

        DIFFICULT_LEVEL = Button(image=None, pos=(790,360),
                     text_input="HARD", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        DIFFICULT_LEVEL.changeColor(PLAY_MOUSE_POS)
        DIFFICULT_LEVEL.update(SCREEN)

        InvincibleAI_LEVEL = Button(image=None, pos=(1120,360),
                     text_input="ININCIBLEAI", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        InvincibleAI_LEVEL.changeColor(PLAY_MOUSE_POS)
        InvincibleAI_LEVEL.update(SCREEN)


        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if EASY_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    AIlevel="easy"
                    chooseAIplayer()
                if MIDDLE_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    AIlevel="medium"
                    chooseAIplayer()
                if DIFFICULT_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    AIlevel="hard"
                    chooseAIplayer()
                if InvincibleAI_LEVEL.checkForInput(PLAY_MOUSE_POS):
                    AIlevel="InvincibleAI"
                    chooseAIplayer()
                    
        pygame.display.update()

def chooseAIplayer():
    pygame.display.set_caption("chooseAIplayer")
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.fill((70,130,180))# background color
        
        Main_TEXT = get_font(45).render("Choose the number of AIplayers", True, "white")
        Main_RECT = Main_TEXT.get_rect(center=(683, 84))
        SCREEN.blit(Main_TEXT, Main_RECT)
    
        PLAY_BACK = Button(image=None, pos=(683,660),
                     text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        Player1 = Button(image=None, pos=(250,360),
                     text_input="Player1", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        Player1.changeColor(PLAY_MOUSE_POS)
        Player1.update(SCREEN)

        Player2 = Button(image=None, pos=(683,360),
                     text_input="Player2", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        Player2.changeColor(PLAY_MOUSE_POS)
        Player2.update(SCREEN)

        Player3 = Button(image=None, pos=(1116,360),
                     text_input="Player3", font=get_font(55), base_color="White", hovering_color="Green")#悬停的颜色
        Player3.changeColor(PLAY_MOUSE_POS)
        Player3.update(SCREEN)

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if Player1.checkForInput(PLAY_MOUSE_POS):
                    pass
                if Player2.checkForInput(PLAY_MOUSE_POS):
                    pass
                if Player3.checkForInput(PLAY_MOUSE_POS):
                    AIplayers = 3

                    newGame = Uno()

                    newGame.startPreGame(newGame.createNewDeck(), SCREEN)
                    pass

                
        pygame.display.update()

def rules():
    pygame.display.set_caption("RULES")
    
    
    while True:
        RULES_MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.fill((70,130,180))# background color
        SCREEN.blit(Ruleimage,(0,0))
        
        # RULES_TEXT = get_font(45).render("This is the Rules screen", True, "white")
        # RULES_RECT = RULES_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(RULES_TEXT, RULES_RECT)
    
        RULES_BACK = Button(image=None, pos=(850,710),text_input="BACK", font=get_font(45), base_color="White", hovering_color="Green")#悬停的颜色        
        PLAY_BUTTON=Button(image=None, pos=(450,710),text_input="PLAY",font=get_font(45), base_color="White", hovering_color="Green")
        
        for button in [PLAY_BUTTON,RULES_BACK]:
            button.changeColor(RULES_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    main_menu()
                if PLAY_BUTTON.checkForInput(RULES_MOUSE_POS):
                    chooselevel()
                
        pygame.display.update()   


# from button import Button

pygame.init()

#creat game window
SCREEN = pygame.display.set_mode((1366, 768))#size of screen
pygame.display.set_caption("Main Menu")
BG= pygame.image.load("welcome page/main menu-3.png")
Cardimage=pygame.transform.scale(BG,(700,450))
# buttonBG=pygame.image.load('button background.png')
# Buttonbg=pygame.transform.scale(buttonBG,(100,150))
Rule_BG= pygame.image.load("welcome page/rule.png")
Ruleimage=pygame.transform.scale(Rule_BG,(1366,680))
color = (255,255,255)
music=pygame.mixer.music.load('welcome page/BGmusic.mp3')
pygame.mixer.music.play(-1)
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("welcome page/font1.ttf", size)  

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.fill((70,130,180))#BG color
        SCREEN.blit(Cardimage,(330,30))#pho
    
        MENU_MOUSE_POS = pygame.mouse.get_pos()
    
    # MENU_TEXT=get_font(100).render("MAIN MENU",True,"#b68f40")
    # MENU_RECT=MENU_TEXT.get_rect(center=(640,100))
                
        PLAY_BUTTON=Button(image=None, pos=(683,550),text_input="PLAY",font=get_font(45), base_color="#d7fcd4", hovering_color="white")
        RULES_BUTTON=Button(image=None, pos=(683,640),text_input="RULES",font=get_font(45), base_color="#d7fcd4", hovering_color="white")
        QUIT_BUTTON=Button(image=None, pos=(683,730),text_input="QUIT",font=get_font(45), base_color="#d7fcd4", hovering_color="white")
                
    # SCREEN.blit(MENU_TEXT, MENU_RECT)
  
        for button in [PLAY_BUTTON,RULES_BUTTON,QUIT_BUTTON]:
             button.changeColor(MENU_MOUSE_POS)
             button.update(SCREEN)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    chooselevel()
                if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                    rules()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()

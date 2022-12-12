import pygame,sys
from pygame.locals import *
pygame.init()
SCREEN = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Ending")

def get_font(size): 
    return pygame.font.Font("welcome page/font1.ttf", size) 
# Code to write Button class referenced from https://github.com/baraltech/Menu-System-PyGame
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

def main_menu():
    clock = pygame.time.Clock()

    redbuttonBG= pygame.image.load("UnoInit/Cards New/redReverse.png")
    buttonBGred=pygame.transform.scale(redbuttonBG,(150,250))
    bluebuttonBG= pygame.image.load("UnoInit/Cards New/bluereverse.png")
    buttonBGblue=pygame.transform.scale(bluebuttonBG,(150,250))
    greenbuttonBG= pygame.image.load("UnoInit/Cards New/greenReverse.png")
    buttonBGgreen=pygame.transform.scale(greenbuttonBG,(150,250))
    yellowbuttonBG= pygame.image.load("UnoInit/Cards New/yellowReverse.png")
    buttonBGyellow=pygame.transform.scale(yellowbuttonBG,(150,250))
    reversign=pygame.image.load("UnoInit/Buttons New/reverse.png")
    graph=pygame.transform.scale(reversign,(300,250))
    graph0=pygame.image.load("UnoInit/Buttons New/reverse1.png")
    graph1=pygame.transform.scale(graph0,(300,250))
    graph3=pygame.transform.scale(reversign,(300,250))
    
    

    while True:
        clock.tick(60)
        SCREEN.fill((70,130,180))#BG color
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        QUIT_BUTTON=Button(image=None, pos=(1083,660),text_input="Qiut",font=get_font(45), base_color="#d7fcd4", hovering_color="white")
        
        Redreverse_BUTTON=Button(image=buttonBGred, pos=(200,300),text_input=" ",font=get_font(15),base_color="white",hovering_color="red")
        Bluereverse_BUTTON=Button(image=buttonBGblue, pos=(400,400),text_input="  ",font=get_font(15),base_color="white",hovering_color="blue")       
        Greenreverse_BUTTON=Button(image=buttonBGgreen, pos=(600,500),text_input="  ",font=get_font(12),base_color="white",hovering_color="green")
        Yellowreverse_BUTTON=Button(image=buttonBGyellow, pos=(800,600),text_input="  ",font=get_font(12),base_color="white",hovering_color="yellow")
        
        for button in [Redreverse_BUTTON,Bluereverse_BUTTON,Greenreverse_BUTTON,Yellowreverse_BUTTON,QUIT_BUTTON]:
             button.changeColor(MENU_MOUSE_POS)
             button.update(SCREEN)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if Redreverse_BUTTON.rect.collidepoint(event.pos):
                         graph=graph1
                    if Bluereverse_BUTTON.rect.collidepoint(event.pos):
                         graph=graph1
                    if Yellowreverse_BUTTON.rect.collidepoint(event.pos):
                         graph=graph1
                    if Greenreverse_BUTTON.rect.collidepoint(event.pos):
                         graph=graph1
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        SCREEN.blit(graph, (300,0))
        pygame.display.update()
main_menu()
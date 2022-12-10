import pygame,sys
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Ending")

def get_font(size): 
    return pygame.font.Font("welcome page/font1.ttf", size)  

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
    MBG= pygame.image.load("Buttons New/bluelight.png")
    MBGEimage=pygame.transform.scale(MBG,(100,100))
    redbuttonBG= pygame.image.load("Buttons New/red.png")
    buttonBGred=pygame.transform.scale(redbuttonBG,(50,50))
    bluebuttonBG= pygame.image.load("Buttons New/blue.png")
    buttonBGblue=pygame.transform.scale(bluebuttonBG,(50,50))
    greenbuttonBG= pygame.image.load("Buttons New/green.png")
    buttonBGgreen=pygame.transform.scale(greenbuttonBG,(50,50))
    yellowbuttonBG= pygame.image.load("Buttons New/yellow.png")
    buttonBGyellow=pygame.transform.scale(yellowbuttonBG,(50,50))


    redbuttonBG1= pygame.image.load("Buttons New/redlight.png")
    newbuttonBGred=pygame.transform.scale(redbuttonBG1,(150,150))
    bluebuttonBG1= pygame.image.load("Buttons New/bluelight.png")
    newbuttonBGblue=pygame.transform.scale(bluebuttonBG1,(150,150))
    yellowbuttonBG1= pygame.image.load("Buttons New/yellowlight.png")
    newbuttonBGyellow=pygame.transform.scale(yellowbuttonBG1,(150,150))
    greenbuttonBG1= pygame.image.load("Buttons New/greenlight.png")
    newbuttonBGgreen=pygame.transform.scale(greenbuttonBG1,(150,150))
    
    clock = pygame.time.Clock()
    # number=0
    graph=buttonBGgreen=pygame.transform.scale(greenbuttonBG,(50,50))

    while True:
        clock.tick(60)
        SCREEN.fill((70,130,180))#BG color
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        QUIT_BUTTON=Button(image=None, pos=(1083,660),text_input="Qiut",font=get_font(45), base_color="#d7fcd4", hovering_color="white")

        Red_BUTTON=Button(image=buttonBGred, pos=(200,300),text_input="Red",font=get_font(15),base_color="white",hovering_color="red")
        Blue_BUTTON=Button(image=buttonBGblue, pos=(200,400),text_input="Blue",font=get_font(15),base_color="white",hovering_color="blue")       
        Green_BUTTON=Button(image=buttonBGgreen, pos=(200,500),text_input="Green",font=get_font(12),base_color="white",hovering_color="green")
        Yellow_BUTTON=Button(image=buttonBGyellow, pos=(200,600),text_input="Yellow",font=get_font(12),base_color="white",hovering_color="yellow")
        

        for button in [Red_BUTTON,Blue_BUTTON,Green_BUTTON,Yellow_BUTTON,QUIT_BUTTON]:
             button.changeColor(MENU_MOUSE_POS)
             button.update(SCREEN)         


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    if Red_BUTTON.rect.collidepoint(event.pos):
                        graph=newbuttonBGred
                        choosecolor="red"
                    if Blue_BUTTON.rect.collidepoint(event.pos):
                        graph=newbuttonBGblue
                        choosecolor="blue"
                    if Yellow_BUTTON.rect.collidepoint(event.pos):
                        graph=newbuttonBGyellow
                        choosecolor="yellow"
                    if Green_BUTTON.rect.collidepoint(event.pos):
                        graph=newbuttonBGgreen
                        choosecolor="green"
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        SCREEN.blit(graph, (300,300))
        pygame.display.update()
main_menu()
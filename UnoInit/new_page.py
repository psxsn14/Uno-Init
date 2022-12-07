import pygame,sys
# import welcome_page
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("Ending")
BG= pygame.image.load("welcome page/ending.png")
BGEimage=pygame.transform.scale(BG,(1050,650))
MBG= pygame.image.load("UnoInit/Buttons New/bluelight.png")
MBGEimage=pygame.transform.scale(MBG,(100,100))
redbuttonBG= pygame.image.load("UnoInit/Buttons New/red.png")
buttonBGred=pygame.transform.scale(redbuttonBG,(50,50))
bluebuttonBG= pygame.image.load("UnoInit/Buttons New/blue.png")
buttonBGblue=pygame.transform.scale(bluebuttonBG,(50,50))
greenbuttonBG= pygame.image.load("UnoInit/Buttons New/green.png")
buttonBGgreen=pygame.transform.scale(greenbuttonBG,(50,50))
yellowbuttonBG= pygame.image.load("UnoInit/Buttons New/yellow.png")
buttonBGyellow=pygame.transform.scale(yellowbuttonBG,(50,50))
RbuttonBG= pygame.image.load("UnoInit/Buttons New/redlight.png")
RBGEimage=pygame.transform.scale(RbuttonBG,(100,100))


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("welcome page/font1.ttf", size)  

def play():
    pygame.display.set_caption("PLAY")
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
    
        SCREEN.fill("black")# background color
        
        PLAY_TEXT = get_font(45).render("This is the play screen", True, "white")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
    
        PLAY_BACK = Button(image=None, pos=(640,460),
                     text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")#悬停的颜色
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                
        pygame.display.update()

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

def pagetext(pos,col,font,tex):
        PAGE_TEXT=get_font(font).render(tex,True,col)
        PAGE_RECT=PAGE_TEXT.get_rect(center=pos)
        SCREEN.blit(PAGE_TEXT, PAGE_RECT)

# def redbutton_change():
        
        
        


def main_menu():
    
    while True:
        SCREEN.fill((70,130,180))#BG color
        SCREEN.blit(BGEimage,(175,25))#pho
        # SCREEN.blit(MBGEimage,(200,100))
    
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        pagetext((420,225),"#ffffff",25,"Player 1")
        pagetext((420,285),"#ffffff",25,"Player 2")
        pagetext((420,345),"#ffffff",25,"Player 3")
        pagetext((420,405),"#ffffff",25,"Player 4")

        pagetext((920,225),"#ffffff",25,"/250")
        pagetext((920,285),"#ffffff",25,"/250")
        pagetext((920,345),"#ffffff",25,"/250")
        pagetext((920,405),"#ffffff",25,"/250")
    

        PLAYagain_BUTTON=Button(image=None, pos=(283,660),text_input="Play Again",font=get_font(45), base_color="#d7fcd4", hovering_color="white")
        Mainmenu_BUTTON=Button(image=None, pos=(723,660),text_input="Main Menu",font=get_font(45), base_color="#d7fcd4", hovering_color="white")
        QUIT_BUTTON=Button(image=None, pos=(1083,660),text_input="Qiut",font=get_font(45), base_color="#d7fcd4", hovering_color="white")

        Red_BUTTON=Button(image=buttonBGred, pos=(200,300),text_input="Red",font=get_font(15),base_color="white",hovering_color="red")
        Blue_BUTTON=Button(image=buttonBGblue, pos=(200,400),text_input="Blue",font=get_font(15),base_color="white",hovering_color="blue")       
        Green_BUTTON=Button(image=buttonBGgreen, pos=(200,500),text_input="Green",font=get_font(12),base_color="white",hovering_color="green")
        Yellow_BUTTON=Button(image=buttonBGyellow, pos=(200,600),text_input="Yellow",font=get_font(12),base_color="white",hovering_color="yellow")
        for button in [Red_BUTTON,Blue_BUTTON,Green_BUTTON,Yellow_BUTTON]:
             button.changeColor(MENU_MOUSE_POS)
             button.update(SCREEN)    

        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if  Red_BUTTON.checkForInput(MENU_MOUSE_POS):
                    SCREEN.blit(RBGEimage,(200,100))
        pygame.display.update()
        
        
        
        
        for button in [PLAYagain_BUTTON,Mainmenu_BUTTON,QUIT_BUTTON]:
             button.changeColor(MENU_MOUSE_POS)
             button.update(SCREEN)
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if PLAYagain_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                # if Mainmenu_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     Mainmunu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()

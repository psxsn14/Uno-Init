import pygame

for i in range(0,10):
    green = []
    green.append(pygame.image.load('green'+ str(i)+'.png'))

for i in range(1,10):
    green.append(pygame.image.load('green'+ str(i)+'.png'))

for i in range (0,2):
    green.append(pygame.image.load('greenskip'+ '.png'))
for i in range (0,2):
    green.append(pygame.image.load('greenreverse'+ '.png'))
for i in range (0,2):
    green.append(pygame.image.load('greenDrawTwo'+ '.png'))

for i in range(0,10):
    red = []
    red.append(pygame.image.load('red'+ str(i)+'.png'))

for i in range(1,10):
    red.append(pygame.image.load('red'+ str(i)+'.png'))

for i in range (0,2):
    red.append(pygame.image.load('redskip'+ '.png'))
for i in range (0,2):
    red.append(pygame.image.load('redreverse'+ '.png'))
for i in range (0,2):    
    red.append(pygame.image.load('redDrawTwo'+ '.png'))

for i in range(0,10):
    blue = []
    blue.append(pygame.image.load('blue'+ str(i)+'.png'))

for i in range(0,10):
    blue.append(pygame.image.load('blue'+ str(i)+'.png'))

for i in range (0,2):  
    blue.append(pygame.image.load('blueskip'+ '.png'))
for i in range (0,2):  
    blue.append(pygame.image.load('bluereverse'+ '.png'))
for i in range (0,2):
    blue.append(pygame.image.load('blueDrawTwo'+ '.png'))

for i in range(0,10):
    yellow = []
    yellow.append(pygame.image.load('yellow'+ str(i)+'.png'))
for i in range(0,10):
    yellow.append(pygame.image.load('yellow'+ str(i)+'.png'))

for i in range (0,2):
    yellow.append(pygame.image.load('yellowskip'+ '.png'))
for i in range (0,2):
    yellow.append(pygame.image.load('yellowreverse'+ '.png'))
for i in range (0,2):
    yellow.append(pygame.image.load('yellowDrawTwo'+ '.png'))

    black = []
        for i in range(0,4):
            black.append(pygame.image.load('blackcolorchange.png'))
        for i in range(0,4):
            black.append(pygame.image.load('blackDrawFour.png'))
        
        listImages = green + red + blue + yellow + black

for i in range(1,len(shuffledDeck)): 
          UnoCard() = listImages[0]





          start = True
        count = 7
  start = True
        while start:
            for event in pygame.event.get():
                if event.type == QUIT:
                    start = False
                for g in range(7):
                    x = 300 + g*100
                    count -= 1
                    
                    pygame.display.update()
                    time.sleep(0.1)
        pygame.quit() 
                    
            
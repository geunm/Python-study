import pygame
import sys
from time import sleep

BLACK = (0,0,0)
Width = 480
Height = 640

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background, fighter
    pygame.init()
    gamePad = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption('pyShooting')
    background = pygame.image.load('./src/background.png')
    fighter = pygame.image.load('./src/fighter.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter

    #전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    #처음위치
    x = Width * 0.45
    y = Height * 0.9
    fighterX = 0

    while True:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT:
                    fighterX += 5

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
                
        drawObject(background, 0, 0)
        
        # 위치 재조정
        x += fighterX
        #왼쪽 끝까지 갔을 때
        if x < 0:
            x = 0
        #오른쪽 끝까지 갔을 때
        elif x > Width - fighterWidth:
            x = Width - fighterWidth

        drawObject(fighter, x, y)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

initGame()
runGame()


                            

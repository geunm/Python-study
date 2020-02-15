import pygame
import sys
import random
from time import sleep

Width = 480
Height = 640
rockImage = ['./src/rock01.png', './src/rock02.png', './src/rock03.png',\
             './src/rock04.png', './src/rock05.png', './src/rock06.png',\
             './src/rock07.png', './src/rock08.png', './src/rock09.png',\
             './src/rock10.png', './src/rock11.png', './src/rock12.png',\
             './src/rock13.png', './src/rock14.png', './src/rock15.png',\
             './src/rock16.png', './src/rock17.png', './src/rock18.png',\
             './src/rock19.png', './src/rock20.png', './src/rock21.png',\
             './src/rock22.png', './src/rock23.png', './src/rock24.png',\
             './src/rock25.png', './src/rock26.png', './src/rock27.png',\
             './src/rock28.png', './src/rock29.png', './src/rock30.png']

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background, fighter, missile
    pygame.init()
    gamePad = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption('pyShooting')
    background = pygame.image.load('./src/background.png')
    fighter = pygame.image.load('./src/fighter.png')
    missile = pygame.image.load('./src/missile.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter, missile

    #전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    #처음위치
    x = Width * 0.45
    y = Height * 0.9
    fighterX = 0

    #무기 좌표 리스트
    missileXY = []
    
    #운석 랜덤 생성
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    #운석 위치 초기 설정
    rockX = random.randrange(0, Width - rockWidth)
    rockY = 0
    rockSpeed = 2

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

                elif event.key == pygame.K_SPACE:
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

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

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                #총알 위로 10씩 이동
                bxy[1] -= 10
                missileXY[i][1] = bxy[1]

                #미사일이 화면을 벗어남
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass

        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        #운석이 특정한 속도로 떨어짐
        rockY += rockSpeed

        #운석이 떨어진경우 새로 그리기
        if rockY > Height:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, Width - rockWidth)
            rockY = 0
            
        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

initGame()
runGame()

import pygame
import random
import math
import time
pygame.init()
# 3840 x 2160
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("FETT NAJS SPEL")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

highscore = 0
highscorestr = str(highscore)
scoreint=0
scorestr=str(scoreint)

font = pygame.font.Font("agencyb.ttf",100)
text = font.render(scorestr,True,(183,255,250))
text_rect= text.get_rect(center=(1000//2,750//2))




playerimg = pygame.image.load("rocketfr.png")
playerx = 425
playery = 550
playerx_change = 0
#pxcp är hur mycket du flyttas när du klickar på pilarna
pxcp = 0.25

#skott
bulletimg = pygame.image.load("skott_racket.png")
bulletx = 0
bullety = 550
bulletx_change = 0
bullety_change = 1
bullet_state = "ready"

#hinder. stenar som faller
rockimg = pygame.image.load("rock.png")
rockx = random.randint(100,850)
rocky = 0
rocky_change =1
rock_state = "ready"

spel_state=0
def spelstate():
    global spel_state

    if spel_state == 1:
        spel_state = 0
    if spel_state == 0:
        spel_state = 1
        print("hejj")
buttonimg = pygame.image.load("button.png")
exitbuttonimg = pygame.image.load("exitbutton.png")
def score(score):
    global scoreint
    scoreint = score
    scorestr = str(scoreint)
    return scorestr
def highscore(score):
    global highscore
    if score<highscore:
        highscore = score
    return highscore

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x + 62.5,y+15))

def player(x,y):
    screen.blit(playerimg,(x,y))


#playerimg
def hinder(x,y):
    global rock_state
    screen.blit(rockimg,(x,y))
    rock_state = "faller"


def IsCollision(rockx,bulletx,rocky,bullety):
    distance = math.sqrt((rockx-bulletx)**2+(rocky-bullety)**2)
    if distance<75:
        return True
    else:
        return False

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect =self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self,buttontype):
        pos = pygame.mouse.get_pos()
        self.buttontype = buttontype
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked = True
                print("hej")
                if self.buttontype == "start":
                    spelstate()
                elif self.buttontype == "exit":
                    global running
                    running = False
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image,(self.rect.x,self.rect.y))

startbutton = Button(400,212.5,buttonimg)
exitbutton= Button(400,362.5,exitbuttonimg)



# game loop
running = True
while running:
    if spel_state == 0:
        screen.fill((0, 255, 255))
        startbutton.draw("start")
        exitbutton.draw("exit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        time.sleep(0.1)
        pygame.display.update()
    if spel_state == 1:
        screen.fill((0, 255, 255))

        scorestr = score(scoreint)
        text = font.render(scorestr, True, (183, 255, 250))

        screen.blit(text,text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerx_change -= pxcp

                if event.key == pygame.K_RIGHT:
                    playerx_change += pxcp

                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletx = playerx
                        fire_bullet(bulletx,bullety)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                    playerx_change = 0

        playerx += playerx_change
        if playerx<0:
            playerx =0
        elif playerx>850:
            playerx = 850
        player(playerx,playery)
        if bullety < 0:
            bullet_state = "ready"
            bulletx = 0
            bullety = 550
        if bullet_state == "fire":
            fire_bullet(bulletx,bullety)
            bullety -= bullety_change
        collision = IsCollision(rockx,bulletx,rocky,bullety)
        if collision:
            rockx = random.randint(100, 850)
            rocky = 0
            rock_state = "ready"
            bullet_state = "ready"
            rocky_change += 0.01
            scoreint += 1
            bulletx = 0
            bullety = 550
            pxcp+=0.01


        if rock_state == "faller":
            hinder(rockx,rocky)
            rocky += rocky_change
        if rock_state == "ready":
            hinder(rockx,rocky)
        if rocky > 750:
            scoreint = 0
            spel_state = 0
            rocky = 0
        time.sleep(0.01)
        pygame.display.update()

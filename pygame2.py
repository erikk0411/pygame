import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("GANSKA NAJS SPEL")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

gubbeimg = pygame.image.load("gubbe1.png")
linjeimg = pygame.image.load("linje1.png")
fiendeimg = pygame.image.load("fiende.png")
playery=550
playerx=0

def IsCollision(playerx,x,playery,y):
    distance1 = ((playerx+75)-(x+25))
#math.sqrt((playerx-x)**2+(playery-y)**2)
    if -20<distance1<20 and playery+50==y:
        return True
    else:
        return False


def player(x,y):
    screen.blit(gubbeimg,(x,y))


class Fiender():
    def __init__(self,fiendex,fiendey):
        self.fiendey = fiendey
        self.fiendex = fiendex
        screen.blit(fiendeimg,(self.fiendex,self.fiendey))



vaningy_change = 0
class Vaningar():
    def __init__(self,y):
        self.vaningy = y
        screen.blit(linjeimg,(0,self.vaningy))


def nyvaning():
    vaning = Vaningar(100)
    vaning2 = Vaningar(300)
    vaning3 = Vaningar(500)
    vaning4 = Vaningar(700)
etty=400
tvay=200
trey=0
fyray=-200
ettx=600
tvax=100
trex=500
fyrax=500

hastighet =0.4


vaningy=700
riktning ="hoger"
running = True
while running:
    screen.fill((0,255,255))
    if playerx >800:
        riktning = "vanster"
    if playerx <50:
        riktning = "hoger"
    if riktning == "hoger":
        playerx += hastighet
    if riktning == "vanster":
        playerx -= hastighet


    player(playerx,playery)
    nyvaning()
    Fiender(ettx,etty)
    Fiender(tvax,tvay)
    Fiender(trex,trey)
    Fiender(fyrax,fyray)
    collison1=IsCollision(playerx,ettx,playery,etty)
    collison2=IsCollision(playerx,tvax,playery,tvay)
    collison3=IsCollision(playerx,trex,playery,trey)
    collison4=IsCollision(playerx,fyrax,playery,fyray)
    if collison1:
        break
    if collison2:
        break
    if collison3:
        break
    if collison4:
        break


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hastighet +=0.005
                etty +=200
                tvay +=200
                trey +=200
                fyray +=200
                if etty>600:
                    etty=0
                    ettx= random.randint(0,950)
                if tvay>600:
                    tvay=0
                    tvax= random.randint(0,950)
                if trey>600:
                    trey=0
                    trex= random.randint(0,950)
                if fyray>600:
                    fyray=0
                    fyrax=random.randint(0,950)







        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pass


    pygame.display.update()
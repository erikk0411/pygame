import pygame
import random
#import math
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



vaningy = 0
def player(x,y):
    screen.blit(gubbeimg,(x,y))
vaningy_change = 0
class Vaningar():

    def __init__(self):
        self.image = linjeimg

    #def faller(self):
    def vaningflyttar(self):
        self.image.blit(linjeimg,(1,vaningy))


running = True
while running:
    screen.fill((255,255,255))
    if playerx >800:
        riktning = "vanster"
    if playerx <50:
        riktning = "hoger"
    if riktning == "hoger":
        playerx += 0.4
    if riktning == "vanster":
        playerx -= 0.4

    player(playerx,playery)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vaningy_change += 100

        if event.type == pygame.KEYUP:
            pass

    pygame.display.update()
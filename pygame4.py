# “pygame2” app
# olika skins på spelaren
# olika texturer på våningarna och fienderna
# highscore
# score
# unlocka skins med coins som spawnar på mappen
# levlarna kommer skapas varanan från type 1 och varanan från type 2 och kan därmed göra att ingen level kmr vara omöjlig
# varje våning är 400 pixlar
# spelaren är 150*150
import time
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((750, 800))
pygame.display.set_caption("GANSKA NAJS SPEL")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
buttonimg = pygame.image.load("button.png")
exitbuttonimg = pygame.image.load("exitbutton.png")
playerimg = pygame.image.load("ball_player.png")

vaning1img = pygame.image.load("vaning1.png")
vaning2img = pygame.image.load("vaning2.png")
mellanvaningimg = pygame.image.load("mellanvaning.png")


class Vaningar:
    def __init__(self, image, ychange):
        self.ychange = ychange
        self.y = 0 + self.ychange
        self.image = image
        self.ychange = ychange
    def visavaningar(self, ):
        screen.blit(self.image, (1, self.y))
    def Iscollision(self):
        pass

start = 0


def vaningarlista(typ):
    if typ == 1:
        vaning1 = Vaningar(vaning1img, 0)
        return vaning1
    if typ == 2:
        vaning2 = Vaningar(vaning2img, 0)
        return vaning2


def random_nummer():
    r = random.randint(1, 2)
    return r


class Iscollison():
    def __init__(self, typ,playerx,playery ):
        self.typ = typ
        self.playerx = playerx
        self.playery= playery
    def Iscollison(self):
        if typ == 1:
            if playerx:
                pass

#def skapavaning():


playery = 450
playerx = 375
direction = 1


def player(playery):
    global playerx
    global direction
    if playerx < 25:
        direction = 1
        # höger
    elif playerx > 675:
        direction = 2
        # vänster
        # print("hej")
    if direction == 1:
        playerx += 5
    elif direction == 2:
        playerx -= 5
    screen.blit(playerimg, (playerx, playery))


def playerychange(directiony, y):
    # directiony 1 = upp. direction 2 = ner
    if directiony == 1:
        y -= 10
        if y < 450:
            y = 450

    if directiony == 2:
        y += 10
        if y > 650:
            y = 650
    return y


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, buttontype):
        pos = pygame.mouse.get_pos()
        self.buttontype = buttontype
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

                if self.buttontype == "start":
                    spelstate()

                elif self.buttontype == "exit":
                    global running
                    running = False
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
typ = 1
typ2=2
nyvaning2 = vaningarlista(typ2)
nyvaning2.y -= 600
nyvaning= vaningarlista(typ)
nyvaning.y = 0
startbutton = Button(275, 250, buttonimg)
exitbutton = Button(275, 380, exitbuttonimg)
spel_state = 0
hinder_state = 2


directiony = 1


def spelstate():
    global spel_state
    if spel_state == 0:
        spel_state = 1
    elif spelstate == 1:
        spel_state = 0


nyvaning = vaningarlista(typ)
running = True
while running:
    if spel_state == 0:
        screen.fill((150, 150, 150))
        startbutton.draw("start")
        exitbutton.draw("exit")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    if spel_state == 1:
        screen.fill((150, 150, 150))
        screen.blit(mellanvaningimg, (0, 0))
        playery = playerychange(directiony, playery)
        player(playery)

        if hinder_state == 0:
            typ = random_nummer()

            hinder_state = 1
            print("hej")

        if hinder_state == 0.5:
            typ2 = random_nummer()
            hinder_state = 1.5

        if hinder_state == 1:
            nyvaning = vaningarlista(typ)
            nyvaning.y -=400
            hinder_state= 2

        if hinder_state == 1.5:
            nyvaning2 = vaningarlista(typ2)
            nyvaning2.y -=400
            hinder_state= 2

        nyvaning.visavaningar()
        nyvaning2.visavaningar()



        if nyvaning.y > 600:
            hinder_state=0
            print("1")
        if nyvaning2.y> 600:
            print("2")
            hinder_state = 0.5



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if playery == 450:

                        nyvaning.y += 200
                        nyvaning2.y+= 200
                    if playery > 450:
                        # playery = 450
                        directiony = 1
                if event.key == pygame.K_DOWN:
                    directiony = 2
                    # playery = 650

            if event.type == pygame.KEYUP:
                pass
    time.sleep(0.005)
    pygame.display.update()

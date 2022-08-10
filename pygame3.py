import pygame
import random

# import time
pygame.init()
screen = pygame.display.set_mode((702, 800))
pygame.display.set_caption("budget subway surfer")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
spelplan = pygame.image.load("subwaysurferkopiaplan.png")

buttonimg = pygame.image.load("button.png")
exitbuttonimg = pygame.image.load("exitbutton.png")

spel_state = 0

skottimg_symbol = pygame.image.load("skott_racket_lutande.png")
skott = 10
skottimg_symbol_stor = pygame.image.load("skott_racket_lutande_stor.png")


def visapowerups(skott):
    skottstr = str(skott)
    font = pygame.font.Font("agencyb.ttf", 40)
    text = font.render(skottstr + " X:", True, (183, 255, 250))
    screen.blit(text, (570, 20))
    screen.blit(skottimg_symbol, (625, 25))


# rand kommer vara hur många rundor (mellan 5 och 20) innan du får nästa powerup
rand = 5


def spawnapowerups(y, powerup_state):
    yint = int(y)
    powerup_stateint = int(powerup_state)
    if powerup_stateint > rand:
        screen.blit(skottimg_symbol_stor, (251, yint))
    else:
        pass


# varje bane är 234 pixlar bred
skottimg = pygame.image.load("skott_racket.png")


def skjut(fil, y):
    if fil == 1:
        screen.blit(skottimg, (102, y))
    if fil == 2:
        screen.blit(skottimg, (336, y))

    if fil == 3:
        screen.blit(skottimg, (570, y))


score = 0


def visascore(score):
    scorestr = str(score)
    font = pygame.font.Font("agencyb.ttf", 40)
    text = font.render("SCORE:" + scorestr, True, (183, 255, 250))
    screen.blit(text, (20, 20))


def highscoref(score):
    file = open("pg33highscore.txt", "r")
    highscore = file.readline()
    highscoreint = int(highscore)
    scorestr = str(score)
    if highscoreint < score:
        for line in highscore:
            filem = open("pg33highscore.txt", "w")
            filem.write(scorestr)
    else:
        pass


def visahighscore():
    file = open("pg33highscore.txt", "r")
    highscore = file.readline()
    font = pygame.font.Font("agencyb.ttf", 40)
    text = font.render("HIGHSCORE:" + highscore, True, (183, 255, 250))
    screen.blit(text, (20, 20))


def spelstate():
    global spel_state

    if spel_state == 1:
        spel_state = 0
    if spel_state == 0:
        spel_state = 1


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


startbutton = Button(251, 223, buttonimg)

exitbutton = Button(251, 353, exitbuttonimg)

spelare = pygame.image.load("rocketfr.png")
# 1=vänster fil 2 = mitten 3 = höger

spelarefil = 2

meteorimg = pygame.image.load("meteor.png")
stormeteorimg = pygame.image.load("meteorstor.png")

# 1 är att det ska spawna nya hinder 2 är att det finns hinder
hinder_state = 1


class Hinder():
    def __init__(self, x, y, sett):
        self.image = meteorimg
        self.x = x
        self.y = y
        if sett == self.x:
            pass
        else:
            screen.blit(meteorimg, (self.x, self.y))


class Storhinder():
    def __init__(self, x, y, sett):
        self.image = meteorimg
        self.x = x
        self.y = y
        if sett == self.x:
            pass
        else:
            screen.blit(stormeteorimg, (self.x, self.y))


# alla hinder patternes som kan skapas

# sett = om 1 filen blivit skjuten
# stva = om 2 filen blivit skjuten
# stre = om 3 filen blivit skjuten
def visa_hinder(typ, x, y, sett):
    if typ == 1:
        if sett != 900:
            if x == 1:
                hinderx = 17
            if x == 2:
                hinderx = 251
            if x == 3:
                hinderx = 479
            hinder1 = Hinder(hinderx, y, sett)
    if typ == 2:
        if sett != 17:
            hinder1 = Hinder(17, y, sett)
        if sett != 251:
            hinder2 = Hinder(251, y - 50, sett)
    if typ == 3:
        if sett != 75:
            hinder1 = Storhinder(75, y, sett)
    if typ == 4:
        if sett != 479:
            hinder1 = Hinder(479, y, sett)
        if sett != 251:
            hinder3 = Hinder(251, y - 50, sett)
    if typ == 5:
        if sett != 479:
            hinder1 = Hinder(479, y, sett)
        if sett != 201:
            hinder2 = Storhinder(201, y - 50, sett)
    if typ == 6:
        if sett != 17:
            hinder1 = Hinder(17, y, sett)
        if sett != 479:
            hinder2 = Hinder(479, y, sett)
        if sett != 251:
            hinder4 = Hinder(251, y - 400, sett)
    if typ == 7:
        if sett != 17:
            hinder1 = Hinder(17, y, sett)
        if sett != 479:
            hinder2 = Hinder(479, y, sett)


def Iscollision(typ, hindery, hinderfil):
    if typ == 1:
        if 550 > hindery > 480:
            if hinderfil == spelarefil:
                if sett != 900:
                    return True
    if typ == 2:
        if 550 > hindery > 480:
            if spelarefil == 1:
                if sett != 17:
                    return True
        if 550 > hindery - 50 > 480:
            if spelarefil == 2:
                if sett != 251:
                    return True
    if typ == 3:
        if 550 > hindery + 28 > 480:
            if spelarefil == 1 or spelarefil == 2:
                if sett != 75:
                    return True
    if typ == 4:
        if 550 > hindery > 480:
            if spelarefil == 3:
                if sett != 479:
                    return True
        if 550 > hindery - 50 > 480:
            if spelarefil == 2:
                if sett != 251:
                    return True
    if typ == 5:
        if 550 > hindery > 480:
            if spelarefil == 3:
                if sett != 479:
                    return True
        if 550 > hindery - 28 > 480:
            if spelarefil == 2 or spelarefil == 3:
                if sett != 201:
                    return True
    if typ == 6:
        if 550 > hindery > 480:
            if spelarefil == 3:
                if sett != 479:
                    return True
            if spelarefil == 1:
                if sett != 17:
                    return True
        if 550 > hindery - 400 > 480:
            if spelarefil == 2:
                if sett != 251:
                    return True
    if typ == 7:
        if 550 > hindery > 480:
            if spelarefil == 3:
                if sett != 479:
                    return True

            if spelarefil == 1:
                if sett != 17:
                    return True


def IscollisoinSkott(typ, hinderfil, skjutfil, skotty, hindery):
    if typ == 1:
        if skjutfil == hinderfil:
            if skotty - 200 < hindery:
                sett = 900
                return sett
    if typ == 2:
        if skjutfil == 1:
            if skotty - 200 < hindery:
                sett = 17
                return sett
        if skjutfil == 2:
            if skotty - 250 < hindery:
                sett = 251
                return sett

    if typ == 3:
        if skjutfil == 1:
            if skotty - 228 < hindery:
                sett = 75
                return sett

        if skjutfil == 2:
            if skotty - 228 < hindery:
                sett = 75
                return sett

    if typ == 4:
        if skjutfil == 3:
            if skotty - 200 < hindery:
                sett = 479
                return sett
        if skjutfil == 2:
            if skotty - 250 < hindery:
                sett = 251
                return sett

    if typ == 5:
        if skjutfil == 2:
            if skotty - 228 < hindery:
                sett = 201
                return sett
        if skjutfil == 3:
            if skotty - 200 < hindery:
                sett = 479
                return sett

    if typ == 6:
        if skjutfil == 1:
            if skotty - 200 < hindery:
                sett = 17
                return sett
        if skjutfil == 3:
            if skotty - 200 < hindery:
                sett = 479
                return sett
        if skjutfil == 2:
            if skotty - 600 < hindery:
                sett = 251
                return sett
    if typ == 7:
        if skjutfil == 1:
            if skotty - 200 < hindery:
                sett = 17
                return sett
        if skjutfil == 3:
            if skotty - 200 < hindery:
                sett = 479
                return sett
    else:
        sett = 0
        return sett


sett = 0
skotty = 630
skjutfil = 1
skjut_State = 0
powerup_state = 0
powerupy = -750
highscoretext = 0
hindery = -200
hindery_change = 1
hinderfil = 2
typ = 1
fil = 300
# varje bane är 234 pixlar bred
running = True
while running:
    if spel_state == 0:
        screen.fill((15, 15, 15))
        startbutton.draw("start")
        exitbutton.draw("exit")

        visahighscore()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    if spel_state == 1:

        highscoretext = highscoref(score)
        screen.blit(spelplan, (0, 0))
        screen.blit(spelare, (fil, 630))
        if typ == 6:
            if hindery > 1100:
                hindery = -200
                hindery_change += 0.02
                hinder_state = 1
                powerup_state += 1
        if typ < 6 or typ > 6:
            if hindery > 900:
                hindery = -200
                hindery_change += 0.02
                hinder_state = 1
                powerup_state += 1
        if hinder_state == 1:
            score += 1
            typ = random.randint(1, 7)
            hinderfil = spelarefil
            hinder_state = 2
            sett = 0
        if hinder_state == 2:
            visa_hinder(typ, hinderfil, hindery, sett)

        if powerup_state > rand:
            powerupy += hindery_change

        if 630 < powerupy < 750:
            if spelarefil == 2:
                powerupy = (-750)
                skott += 1
                powerup_state = 0
                rand = random.randint(5, 20)
        if powerupy > 800:
            powerupy = (-750)
            powerup_state = 0
            rand = random.randint(5, 20)
        spawnapowerups(powerupy, powerup_state)
        hindery += hindery_change
        visascore(score)
        visapowerups(skott)

        if Iscollision(typ, hindery, hinderfil) == True:
            hinder1 = Hinder(17, -200, sett)
            hinder2 = Hinder(17, -200, sett)
            hinder3 = Hinder(17, -200, sett)
            hindery = 0
            spel_state = 0
            score = 0
            hindery_change = 1
            skott = 0

        if spelarefil == 1:
            fil -= 7.5
            if fil < 75:
                fil = 75
        if spelarefil == 2:
            if fil < 300:
                fil += 7.5
            if fil > 300:
                fil -= 7.5
            if fil == 300:
                fil = 300
        if spelarefil == 3:
            if fil < 525:
                fil += 7.5
            if fil == 525:
                fil = 525

        if skjut_State == 1:
            skjut(skjutfil, skotty)
            skotty -= 3
            sett = IscollisoinSkott(typ, hinderfil, skjutfil, skotty, hindery)
            if sett != 0:
                skjut_State = 0
                skotty = 630
        if skotty < 0:
            skotty = 630
            skjut_State = 0
            sett = 0

        if spelarefil < 1:
            spelarefil = 1
        if spelarefil > 3:
            spelarefil = 3
        # vilken knapp du klickar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spelarefil -= 1
                if event.key == pygame.K_RIGHT:
                    spelarefil += 1
                if event.key == pygame.K_SPACE:
                    if skott > 0:
                        skjut_State = 1
                        skjutfil = spelarefil
                        skott -= 1
            if event.type == pygame.KEYUP:
                pass
        pygame.display.update()

import pygame
import random
#import time
pygame.init()
screen = pygame.display.set_mode((702, 800))
pygame.display.set_caption("budget subway surfer")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
spelplan = pygame.image.load("subwaysurferkopiaplan.png")

buttonimg = pygame.image.load("button.png")
exitbuttonimg = pygame.image.load("exitbutton.png")
hearticonimg = pygame.image.load("heartliten.png")
heartdropimg= pygame.image.load("heartstor.png")
spel_state = 0


liv = 3
def visapowerups(skott):
    skottstr = str(skott)
    font = pygame.font.Font("agencyb.ttf",40)
    text = font.render(skottstr+" X:",True,(183,255,250))
    screen.blit(text,(570,20))
    screen.blit(hearticonimg,(625,25))
#rand kommer vara hur många rundor (mellan 5 och 20) innan du får nästa powerup
rand = 5
def spawnapowerups(y,powerup_state):
    yint= int(y)
    powerup_stateint=int(powerup_state)
    if powerup_stateint>rand:
        screen.blit(heartdropimg,(251,yint))
    else:
        pass


score = 0

def visascore(score):
    scorestr = str(score)
    font = pygame.font.Font("agencyb.ttf",40)
    text = font.render("SCORE:"+scorestr, True, (183, 255, 250))
    screen.blit(text,(20,20))

def highscoref(score):
    file = open("pg33highscore.txt", "r")
    highscore = file.readline()
    highscoreint = int(highscore)
    scorestr = str(score)
    if highscoreint< score:
        for line in highscore:
            filem = open("pg33highscore.txt", "w")
            filem.write(scorestr)
    else:
        pass
def visahighscore():
    file = open("pg33highscore.txt", "r")
    highscore = file.readline()
    font = pygame.font.Font("agencyb.ttf", 40)
    text = font.render("HIGHSCORE:" + highscore , True, (183, 255, 250))
    screen.blit(text, (20, 20))


def spelstate():
    global spel_state

    if spel_state == 1:
        spel_state = 0
    if spel_state == 0:
        spel_state = 1

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

                if self.buttontype == "start":
                    spelstate()

                elif self.buttontype == "exit":
                    global running
                    running = False
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        screen.blit(self.image,(self.rect.x,self.rect.y))

startbutton = Button(251,223,buttonimg)

exitbutton= Button(251,353,exitbuttonimg)




spelare = pygame.image.load("rocketfr.png")
#1=vänster fil 2 = mitten 3 = höger

spelarefil = 2


meteorimg = pygame.image.load("meteor.png")
stormeteorimg = pygame.image.load("meteorstor.png")

#1 är att det ska spawna nya hinder 2 är att det finns hinder
hinder_state = 1
class Hinder():
    def __init__(self,x,y):
        self.image = meteorimg
        self.x = x
        self.y = y
        screen.blit(meteorimg,(self.x,self.y))


class Storhinder():
    def __init__(self,x,y):
        self.image = meteorimg
        self.x = x
        self.y = y
        screen.blit(stormeteorimg, (self.x, self.y))


#alla hinder patternes som kan skapas
def visa_hinder(typ,x,y):
    if typ == 1:
        if x== 1:
            hinderx=17
        if x==2:
            hinderx=251
        if x==3:
            hinderx=479
        hinder1=Hinder(hinderx,y)
    if typ ==2:
        hinder1=Hinder(17,y)
        hinder2= Hinder(251,y-50)
    if typ ==3:
        hinder1 = Storhinder(75,y)
    if typ==4:
        hinder1=Hinder(479,y)
        hinder3=Hinder(251,y-50)
    if typ ==5:
        hinder1 =Hinder(479,y)
        hinder2 = Storhinder(201,y-50)
    if typ == 6:
        hinder1 =Hinder(17,y)
        hinder2= Hinder(479,y)
        hinder4= Hinder(251,y-400)
    if typ == 7:
        hinder1= Hinder(17,y)
        hinder2= Hinder(479,y)


def Iscollision(typ,hindery,hinderfil):
    if typ ==1:
        if 550>hindery>480:
            if hinderfil == spelarefil:
                return True
    if typ == 2:
        if 550>hindery>480:
            if spelarefil == 1:
                return True
        if 550>hindery-50>480:
            if spelarefil == 2:
                return True
    if typ == 3:
        if 550>hindery+28>480:
            if spelarefil == 1 or spelarefil == 2:
                return True
    if typ == 4:
        if 550>hindery> 480:
            if spelarefil == 3:
                return True
        if 550>hindery-50>480:
            if spelarefil == 2:
                return True
    if typ == 5:
        if 550>hindery>480:
            if spelarefil ==3:
                return True
        if 550>hindery -28> 480:
            if spelarefil == 2 or spelarefil == 3:
                return True
    if typ == 6:
        if 550 > hindery > 480:
            if spelarefil ==3 or spelarefil== 1:
                return True
        if 550> hindery-400> 480:
            if spelarefil == 2:
                return True
    if typ ==7:
        if 550 > hindery > 480:
            if spelarefil ==3 or spelarefil== 1:
                return True



powerup_state=0
powerupy= -750
highscoretext = 0
hindery = -200
hindery_change = 2
hinderfil = 2
typ = 1
fil=300
#varje bane är 234 pixlar bred
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
            if hindery>1100:
                hindery = -200
                hindery_change += 0.02
                hinder_state = 1
                powerup_state +=1
        if typ<6 or typ>6:
            if hindery>900:
                hindery = -200
                hindery_change +=0.05
                hinder_state = 1
                powerup_state += 1
        if hinder_state == 1:
            score +=1
            typ = random.randint(1,7)
            hinderfil = spelarefil
            hinder_state = 2
        if hinder_state == 2:
            visa_hinder(typ,hinderfil,hindery)

        if powerup_state>rand:
            powerupy+=hindery_change

        if 630<powerupy<750:
            if spelarefil==2:
                powerupy = (-750)
                liv += 1
                powerup_state =0
                rand= random.randint(5,20)
        if powerupy>800:
            powerupy = (-750)
            powerup_state = 0
            rand = random.randint(5, 20)
        spawnapowerups(powerupy,powerup_state)
        hindery+= hindery_change
        visascore(score)
        visapowerups(liv)
        if Iscollision(typ,hindery,hinderfil) == True:
            if liv>0:
                liv-=1
                hindery=1500
            if liv ==0:
                hinder1=Hinder(17,-200)
                hinder2=Hinder(17,-200)
                hinder3=Hinder(17,-200)
                hindery = 0
                spel_state=0
                score =0
                hindery_change = 2
                liv =3

        if spelarefil == 1:
            fil-=7.5
            if fil<75:
                fil=75
        if spelarefil ==2:
            if fil<300:
                fil+=7.5
            if fil>300:
                fil-=7.5
            if fil == 300:
                fil=300
        if spelarefil == 3:
            if fil<525:
                fil+=7.5
            if fil== 525:
                fil= 525




        #vilken knapp du klickar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spelarefil -= 1
                if event.key == pygame.K_RIGHT:
                    spelarefil += 1
            if event.type == pygame.KEYUP:
                pass
        if spelarefil<1:
            spelarefil = 1
        if spelarefil>3:
            spelarefil = 3

        pygame.display.update()
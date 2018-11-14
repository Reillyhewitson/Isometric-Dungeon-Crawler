from ACaS import *
import os
import pickle
import random
import time

sf = "saves/" #save folder!
asset_folder = "ISG_assets/"
os.system("pip install -r requirements.txt")
import pygame
class troop(object):

    def __init__(self, points):
        self.points = points

    def attack(self, attack):
        self.attack = attack

    def health(self, hp):
        self.hp = hp

class pygameControl(object):

    def __init__(self, sizeX, sizeY):
        pygame.init()
        self.display = pygame.display.set_mode((sizeX, sizeY))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('--Unnamed--')
        self.sizeX = sizeX
        self.sizeY = sizeY

    def title(self, title):
        pygame.display.set_caption(title)

    def BlitIt(self, x, y, image):
        self.display.blit(image, (x, y))

    def BlackOut(self):
        self.display.fill((0,0,0))

"""

a fun gap!!!

"""

class level(object):

    def __init__(self, sizeY, sizeX):
        self.xmap = []
        self.ymap = []
        for count in range(sizeY):
            self.ymap.append("O")
        for count in range(sizeX):
            self.xmap.append("O")
        self.xPlayer = 0
        self.yPlayer = 0
        self.xCordrom = []
        self.yCordrom = []
        self.sizeCordrom = [] #Cord word does nothing it just sorta makes it seem part of the y and x Cordrom variables

    #def image(self, location):
        #self.image = pygame.image.load(asset_folder + location)

    def imageScaler(self, scale, x, y):
        self.image = pygame.transform.scale(self.image, (int(x*scale) , int(y*scale)))
        self.imageXsize = int(x*scale)
        self.imageYsize = int(y*scale)

    def change_layout(self, sizeY, sizeX):
        self.xmap = []
        self.ymap = []
        for count in range(sizeY):
            self.ymap.append("O")
        for count in range(sizeX):
            self.xmap.append("O")

    def player_on(self, locx, locy):
        self.xmap[locx] = "X"
        self.ymap[locy] = "X"

"""
    def move_player(self):
        if (self.ymap[0] = "X") and (self.xmap[len(self.xmap)//2]):
            self.yPlayer += 1
            #update player cords
            #make new room details
            #generate new room
"""

class monster(object):

    def __init__(self, name, health, attack_power):
        self.name = name
        self.hp = health
        self.attack = attack_power

    def level_effector(self, level, ammount_increase):
        ammount_increase += 1
        level -= 1
        for count in range(level):
            self.hp *= ammount_increase
            self.attack *= ammount_increase
            self.attack = int(self.attack)
            self.hp = int(self.hp)

    def defense(self, defense):
        self.defense = defence

    def type(self, type):
        self.type = type

    def image(self, location):
        self.image = pygame.image.load(asset_folder + location)

    def imageScaler(self, scale, x, y):
        self.image = pygame.transform.scale(self.image, (int(x*scale) , int(y*scale)))
        self.imageXsize = int(x*scale)
        self.imageYsize = int(y*scale)

class player(object):

    def __init__(self):
        self.directionPoint = 1
        self.directionList = ["backright.png", "frontright.png", "frontleft.png", "backleft.png"]
        self.moved = False

    def attack(self, attack):
        self.attack = attack

    def name(self, name):
        self.name = name

    def hp(self, hp):
        self.hp = hp

    def mp(self, mp):
        self.mp = mp

    def age(self, age):
        self.age = age

    def levelsetup(self):
        self.level = 1

    def level_adaptor(self):
        self.previousLevel = self.level
        self.level = 0
        for count in range(0, len(self.level_adv)):
            if self.xp >= self.level_adv[count]:
                self.level = count + 1
        self.level += 1

        if self.previousLevel != self.level:
            self.hp = 100 * self.level
            self.attack = 5 * self.level
            print(self.previousLevel)
            print(self.level)
            global occorunce
            occorunce = True

    def xp(self, xp):
        self.xp = xp

    def image(self, location):
        self.image = pygame.image.load(asset_folder + location)

    def level_advancement(self, max_level, incline, start_point):
        self.level_adv = []
        xp_climb = start_point
        for count in range(max_level):
            self.level_adv.append(int(xp_climb))
            xp_climb *= 1 + incline

    def defense(self, defense):
        self.defense = defense

    def type(self, type):
        self.type = type

    def imageScaler(self, scale, x, y):
        self.image = pygame.transform.scale(self.image, (int(x*scale) , int(y*scale)))
        self.imageXsize = int(x*scale)
        self.imageYsize = int(y*scale)

    def existance(self, x, y):
        self.x = x
        self.y = y

    def direction(self, angle):
        self.directionPoint += 1*angle
        if self.directionPoint == 4:
            self.directionPoint = 0
        elif self.directionPoint == -1:
            self.directionPoint = 3
        self.image = pygame.image.load(asset_folder + self.directionList[self.directionPoint])
        self.moved = True

    def move_forward(self): #the elses and passes makes it clean but are uselesss
        if self.directionPoint == 0:
            if dungeon.ymap[0] != "X":
                self.y -= 1
                self.moved = True
            else:
                pass
        elif self.directionPoint == 1:
            if dungeon.xmap[len(dungeon.xmap)-1] != "X":
                self.x += 1
                self.moved = True
            else:
                pass
        elif self.directionPoint == 2:
            if dungeon.ymap[len(dungeon.ymap)-1] != "X":
                self.y += 1
                self.moved = True
            else:
                pass
        elif self.directionPoint == 3:
            if dungeon.xmap[0] != "X":
                self.x -=1
                self.moved = True
            else:
                pass
        if self.moved == True:
            self.eventBegin = random.randint(1, 100)
            if self.eventBegin >= 90:
                self.scenePrep = "Battle"
            else:
                self.scenePrep = "Tileset"

class event_manager(object):

    def type_advantige(self):
        self.adv = {}

    def advantige_check(self, AType, DType):
        if DType in battle.adv[AType]:
            return True
        else:
            return False

    def running(self, running):
        if running == "on":
            self.running = True
        elif running == "off":
            self.running = False

def clicked():
    clickedSund = pygame.mixer.Sound(asset_folder + "clickity.ogg")
    clickedSund.play()

enemies = {
"enemy1" : ["Slime", 30, 2, 8, "slime.png", 346, 249, 225, 50, 0.9], #name, hp, attack, xp, image name, rescale x, rescale y, x location, y location, scale
"enemy2" : ["Wolf", 60, 5, 16, "wolf.png", 413, 390, 225, 50, 0.8],
"enemy3" : ["Ogre", 120, 15, 32, "ogre.png", 310, 390, 225, 30, 0.8]
}

possipleWepons = {
"Wepon1" : ["A basic sword made form cheap steel.", "Basic Sword", "Attack", 2],
"Wepon2" : ["A cane carved from a health tree.", "Cane of Life", "HP", 25],
"Wepon3" : ["A simple axe used for cutting trees", "Tree Cutter Axe", "Attack", 4],
"Wepon4" : ["Creak, aim, SNIPE!", "Wooden Bow and Arrow", "Attack", 3],
"Wepon5" : ["Whack! Smash 'der head in!'", "Mallace", "Attack", 6],
"Wepon6" : ["The trick to dent armor is a ball that can smash.", "Ball and Chain", "Attack", 5],
"Wepon7" : ["Like a Mallace but looks better.", "War Hammer", "Attack", 7]
}

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.music.set_volume(0)

oof = pygameControl(800, 600) #size of the screen
oof.title("Isometric Dungeon Crawler") #name of the screen

"""
monster = enemy("Dragon", 10, 4)
monster.level_effector(3, 0.4)
monster.type("Poison")
"""

"""
advant = {"Fire": ["Grass", "Tree", "Ice", "Poison"]}
"""
battle = event_manager() #runs battle events
"""
battle.type_advantige()
battle.adv = advant
print(battle.advantige_check(myplayer.type, monster.type))
"""


pygame.mixer.music.load(asset_folder + "dungeonTheme.ogg")

occorunce = False

captureX = 0
captureY = 0

saveImg = pygame.image.load(asset_folder + "saveImg.png")

click = 0
print("START!!!")
downKey = False
work = False #doenst seem to be used... hmmmm!!!!!! *loud hmm*
battle.running("on")
scene = "Menu"
BackgroundImg =  pygame.image.load(asset_folder + "menuDungeon.png")
startImg = pygame.image.load(asset_folder + "newgame.png")
continueImg = pygame.image.load(asset_folder + "continue.png")
soundImg = pygame.image.load(asset_folder + "sound.png")
soundImg = pygame.transform.scale(soundImg, (456//3, 390//3))
Sscale = 1
startImg = pygame.transform.scale(startImg, (int(362*Sscale) , int(76*Sscale)))
startImg = pygame.transform.scale(startImg, (int(306*Sscale) , int(78*Sscale)))

menuImg = pygame.image.load(asset_folder + "menu.png")
#menuImg = pygame.transform.scale(menuImg, (int())) #work here ----------------

itemDirectory = 1

musicUndergo = False

HaCimg = pygame.image.load(asset_folder + "HaC.png")
soundOn = -1
pygame.font.init()
itemDescription = False
myfont = pygame.font.Font("ARDARLING.ttf", 30)
while battle.running:

    if scene == "Menu":
        if musicUndergo == False:
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1)
            musicUndergo = True
        battleUndergo = False
        oof.BlitIt(0, 0, BackgroundImg)
        oof.BlitIt(400-362*Sscale//2, 100, startImg)
        oof.BlitIt(400-306*Sscale//2, 200, continueImg)
        oof.BlitIt(400-512*Sscale//2, 300, HaCimg)
        if soundOn == 1:
            soundImg = pygame.image.load(asset_folder + "sound.png")
        elif soundOn == -1:
            soundImg = pygame.image.load(asset_folder + "soundoof.png")
        soundImg = pygame.transform.scale(soundImg, (456//3, 390//3))
        oof.BlitIt(800-456//3, 600-390//3, soundImg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                battle.running("oof")
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked()
                x, y = event.pos
                x -= 800-456//3
                y -= 600-390//3
                if startImg.get_rect().collidepoint(x, y):
                    soundOn *= -1
                    if soundOn == -1:
                        pygame.mixer.music.set_volume(0)
                    elif soundOn == 1:
                        pygame.mixer.music.set_volume(0.6)
                x, y = event.pos
                x -= 400-362*Sscale//2
                y -= 100
                if startImg.get_rect().collidepoint(x, y):
                    scene = "Setup"
                x, y = event.pos
                x -= 400-306*Sscale//2
                y -= 200
                if continueImg.get_rect().collidepoint(x, y):
                    scene = "Continue"
                x, y = event.pos
                x -= 400-512*Sscale//2
                y -= 300
                if HaCimg.get_rect().collidepoint(x, y):
                    scene = "HaC"

    elif scene == "HaC":
        superSetY = 600
        setY = 600
        notes = ["Isometric Dungeon Crawler", "", "Programmer : Fabian", "Art : Google (stolen from online)", "Sound : Forgot about that", "", "",  "Help Section", "", "To regain health you need to level up", "Leveling up increases HP and Attack", "It also increases the attack and health of monsters", "And it unlocks new monsters to figth!", "It is important to study the monster's Attack and HP curves"]
        while superSetY != 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    battle.running("oof")
            oof.BlackOut()
            for worth in range(0, len(notes)):
                what2blit = notes[worth]
                textsurface = myfont.render(what2blit, False, (120, 120, 120))
                oof.BlitIt(420-len(what2blit)*7, setY + 60*worth, textsurface)
            else:
                setY -= 1
                superSetY = setY +60*worth
            pygame.display.update()
            time.sleep(0.0166666666666666666666666666666666666666667)
        scene = "Menu"

    elif scene == "Setup":
        wepon = {"item1" : ["Bare Knuckle Fighting", "None", "Attack", 0]}

        imageName = "0" #screenshot save name

        ds = random.randint(4,15) #dungeon size --maximum 15--

        myplayer = player() #make myplayer the player object
        myplayer.image("frontright.png") #get an image for the player
        myplayer.imageScaler(0.5, 67, 130) #scale the player image

        myplayer.level_advancement(69, 0.7, 20) #create a xp curve
        print(myplayer.level_adv)
        myplayer.hp(100) #give the player an hp value
        myplayer.attack(5) #give the player an attack power
        myplayer.existance(0,0) #give the player an x and y location
        myplayer.xp(0)

        myplayer.levelsetup()

        myplayer.level_adaptor()

        dungeon = level(ds, ds) #dungeon size
        dungeon.image = pygame.image.load(asset_folder + "floor.png") #gather floor image
        dungeon.imageScaler(0.2, 271, 155) #scale the floor image

        dungeon.player_on(myplayer.x,myplayer.y)

        oriloc =  oof.sizeX/2 - dungeon.imageXsize/2 #original location
        original_location_for_the_y_axis_of_the_frickin_floor = 100
        wBx = oriloc
        wBy = original_location_for_the_y_axis_of_the_frickin_floor

        captureX = wBx + 12# - int(dungeon.imageXsize/2)
        captureY = wBy - 45 #- int(dungeon.imageYsize/2)

        scene = "Tileset"

    elif scene == "Continue":

        myplayer = player() #make myplayer the player object
        myplayer.image("frontright.png") #get an image for the player
        myplayer.imageScaler(0.5, 67, 130) #scale the player image

        wepon = pickle.load(open(sf+"wepon.curruptedFile", "rb"))
        imageName = pickle.load(open(sf+"imageName.curruptedFile", "rb"))
        ds = pickle.load(open(sf+"ds.curruptedFile", "rb"))
        myplayer.level_adv = pickle.load(open(sf+"myplayer.level_adv.curruptedFile", "rb"))
        myplayer.attack = pickle.load(open(sf+"myplayer.attack.curruptedFile", "rb"))
        myplayer.x = pickle.load(open(sf+"myplayer.x.curruptedFile", "rb"))
        myplayer.y = pickle.load(open(sf+"myplayer.y.curruptedFile", "rb"))
        myplayer.xp = pickle.load(open(sf+"myplayer.xp.curruptedFile", "rb"))
        myplayer.level = pickle.load(open(sf+"myplayer.level.curruptedFile", "rb"))
        myplayer.hp = pickle.load(open(sf+ "myplayer.hp.curruptedFile", "rb"))
        myplayer.level_adaptor() #makes a level!
        dungeon = level(ds, ds)
        dungeon.xmap = pickle.load(open(sf+"dungeon.xmap.curruptedFile", "rb"))
        dungeon.ymap = pickle.load(open(sf+"dungeon.ymap.curruptedFile", "rb"))
        dungeon.xPlayer = pickle.load(open(sf+"dungeon.xPlayer.curruptedFile", "rb"))
        dungeon.yPlayer = pickle.load(open(sf+"dungeon.yPlayer.curruptedFile", "rb"))

        dungeon.player_on(myplayer.x,myplayer.y)
        dungeon.image = pygame.image.load(asset_folder + "floor.png") #gather floor image
        dungeon.imageScaler(0.2, 271, 155) #scale the floor image

        oriloc =  oof.sizeX/2 - dungeon.imageXsize/2 #original location
        original_location_for_the_y_axis_of_the_frickin_floor = 100
        wBx = oriloc
        wBy = original_location_for_the_y_axis_of_the_frickin_floor

        captureX = wBx + 12# - int(dungeon.imageXsize/2)
        captureY = wBy - 45 #- int(dungeon.imageYsize/2)
        scene = "Tileset"

    elif scene == "Death":
        deathImg = pygame.image.load(asset_folder + "you_died.png")
        oof.BlitIt(0, 239, deathImg)
        battleUndergo = True
        click += 1
        if click == 120:
            scene = "Menu"

    elif scene == "Battle":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                battle.running("off")
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked()
                x, y = event.pos
                y -= 520
                if clickableAttackImage.get_rect().collidepoint(x, y):
                    enemy.hp -= myplayer.attack + random.randint(-(myplayer.attack//2), (myplayer.attack//2))
                    myplayer.hp -= enemy.attack + random.randint(-(enemy.attack//2), (enemy.attack//2))
                x, y = event.pos
                x -= 550
                y -= 520
                if clickableRunImage.get_rect().collidepoint(x, y):
                    scene = "Tileset"
                x, y = event.pos
                x -= 270
                y -= 520
                if clickableDefendImage.get_rect().collidepoint(x, y):
                    hit = random.randint(1,3)
                    if hit == 1:
                        myplayer.hp -= enemy.attack + random.randint(-(enemy.attack//2), (enemy.attack//2))

        if battleUndergo == False:
            EC_Max = myplayer.level
            if EC_Max > len(enemies):
                EC_Max = len(enemies)
            EC = random.randint(1, EC_Max) #Enemy Choice
            MES = enemies["enemy" + str(EC)] #My Enemy Stats
            enemy = monster(MES[0], MES[1], MES[2])
            enemy.level_effector(myplayer.level-EC + 1, 0.4)
            enemy.image(MES[4])
            enemy.imageScaler(MES[9], MES[5], MES[6])
            battleUndergo = True
        oof.BlackOut()
        oof.BlitIt(0, 0, BackgroundImg)
        oof.BlitIt(MES[7], MES[8], enemy.image)
        what2blit = "Player HP : {0}".format(myplayer.hp)
        textsurface = myfont.render(what2blit, False, (120, 120, 120))
        oof.BlitIt(0, 0, textsurface)
        what2blit = "Enemy HP : {0}".format(enemy.hp)
        textsurface = myfont.render(what2blit, False, (120, 120, 120))
        oof.BlitIt(500, 0, textsurface)
        clickableAttackImage = pygame.image.load(asset_folder + "attack.png")
        oof.BlitIt(0, 520, clickableAttackImage)
        clickableDefendImage = pygame.image.load(asset_folder + "defend.png")
        oof.BlitIt(270, 521, clickableDefendImage)
        clickableRunImage = pygame.image.load(asset_folder + "run.png")
        oof.BlitIt(550, 521, clickableRunImage)

        if enemy.hp <= 0:
            scene = "Tileset"
            myplayer.xp += MES[3]
            myplayer.level_adaptor()
            battleUndergo = False
            del enemy
            if occorunce == True:
                what2blit = "Wepon" + str(random.randint(1, len(possipleWepons)))
                what2blit = possipleWepons[what2blit]
                weponNumber = len(wepon) + 1
                wepon["item" + str(weponNumber)] = what2blit
                occorunce = False

        elif myplayer.hp <= 0:
            scene = "Death"
            click = 0

    elif scene == "Escaped":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                battle.running("off")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    clicked()
                    scene = "Tileset"
                if event.key == pygame.K_RIGHT:
                    what2blit = "item" + str(itemDirectory)
                    what2blit = wepon[what2blit]
                    if what2blit[2] == "Attack":
                        myplayer.attack -= what2blit[3]
                    elif what2blit[2] == "Health":
                        myplayer.hp -= what2blit[3]
                    itemDirectory += 1
                    if what2blit[2] == "Attack":
                        myplayer.attack += what2blit[3]
                    elif what2blit[2] == "Health":
                        myplayer.hp += what2blit[3]
                    if itemDirectory > len(wepon):
                        itemDirectory = 1
                if event.key == pygame.K_SPACE:
                    if itemDescription == False:
                        itemDescription = True
                    else:
                        itemDescription = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked()
                x, y = event.pos
                x -= 800-159
                if saveImg.get_rect().collidepoint(x, y): #save
                    open(sf+"wepon.curruptedFile", 'w').close()
                    pickle.dump(wepon, open(sf+"wepon.curruptedFile", "wb"))
                    open(sf+"imageName.curruptedFile", 'w').close()
                    pickle.dump(imageName, open(sf+"imageName.curruptedFile", "wb"))
                    open(sf+"ds.curruptedFile", 'w').close()
                    pickle.dump(ds, open(sf+"ds.curruptedFile", "wb"))
                    open(sf+"myplayer.level_adv.curruptedFile", 'w').close()
                    pickle.dump(myplayer.level_adv, open(sf+"myplayer.level_adv.curruptedFile", "wb"))
                    open(sf+"myplayer.attack.curruptedFile", 'w').close()
                    pickle.dump(myplayer.attack, open(sf+"myplayer.attack.curruptedFile", "wb"))
                    open(sf+"myplayer.x.curruptedFile", 'w').close()
                    pickle.dump(myplayer.x, open(sf+"myplayer.x.curruptedFile", "wb"))
                    open(sf+"myplayer.y.curruptedFile", 'w').close()
                    pickle.dump(myplayer.y, open(sf+"myplayer.y.curruptedFile", "wb"))
                    open(sf+"dungeon.xmap.curruptedFile", 'w').close()
                    pickle.dump(dungeon.xmap, open(sf+"dungeon.xmap.curruptedFile", "wb"))
                    open(sf+"dungeon.ymap.curruptedFile", 'w').close()
                    pickle.dump(dungeon.ymap, open(sf+"dungeon.ymap.curruptedFile", "wb"))
                    open(sf+"dungeon.xPlayer.curruptedFile", 'w').close()
                    pickle.dump(dungeon.xPlayer, open(sf+"dungeon.xPlayer.curruptedFile", "wb"))
                    open(sf+"dungeon.yPlayer.curruptedFile", 'w').close()
                    pickle.dump(dungeon.yPlayer, open(sf+"dungeon.yPlayer.curruptedFile", "wb"))
                    open(sf+"myplayer.xp.curruptedFile", 'w').close()
                    pickle.dump(myplayer.xp, open(sf+"myplayer.xp.curruptedFile", "wb"))
                    open(sf+"myplayer.level.curruptedFile", 'w').close()
                    pickle.dump(myplayer.level, open(sf+"myplayer.level.curruptedFile", "wb"))
                    open(sf+"myplayer.hp.curruptedFile", 'w').close()
                    pickle.dump(myplayer.hp, open(sf+"myplayer.hp.curruptedFile", "wb"))
        oof.BlackOut()
        oof.BlitIt(800-159, 0, saveImg)
        what2blit = "HP : {0}".format(myplayer.hp)
        textsurface = myfont.render(what2blit, False, (120, 120, 120))
        oof.BlitIt(0, 0, textsurface)
        what2blit = "Level : {0}".format(myplayer.level)
        textsurface = myfont.render(what2blit, False, (120, 120, 120))
        oof.BlitIt(200, 0, textsurface)
        what2blit = "XP : {0}".format(myplayer.xp)
        textsurface = myfont.render(what2blit, False, (120, 120, 120))
        oof.BlitIt(400, 0, textsurface)
        what2blit = "item" + str(itemDirectory)
        what2blit = wepon[what2blit]
        what2blit = what2blit[1]
        textsurface = myfont.render(what2blit, False, (120, 120, 120))
        oof.BlitIt(0, 100, textsurface)
        anotherKeepSafeForHeight = 0
        onceAgainAnotherKeepSafe = 0

        if itemDescription == True:
            what2blit = "item" + str(itemDirectory)
            what2blit = wepon[what2blit]
            what2blit = "It increases {0} by {1}.".format(what2blit[2], what2blit[3])

            textsurface = myfont.render(what2blit, False, (120, 120, 120))
            oof.BlitIt(0, 170, textsurface)
            what2blit = "item" + str(itemDirectory)
            what2blit = wepon[what2blit]
            what2blit = "{0}".format(what2blit[0])
            textsurface = myfont.render(what2blit, False, (120, 120, 120))
            oof.BlitIt(0, 170+60, textsurface)

            """
            keepSafe = what2blit
            del anotherKeepSafeForHeight
            del onceAgainAnotherKeepSafe
            for description in range(-1, len(what2blit)//43 - 1):
                what2blit = keepSafe[(description+1)*43: (description+1)*43 + 43]
                textsurface = myfont.render(what2blit, False, (120, 120, 120))
                oof.BlitIt(0, (description + 3) * 69, textsurface)
                anotherKeepSafeForHeight = (description + 3) * 69
                onceAgainAnotherKeepSafe = (description+1)*43 + 44
            else:
                try:
                    what2blit = keepSafe[onceAgainAnotherKeepSafe:]
                    textsurface = myfont.render(what2blit, False, (120, 120, 120))
                    oof.BlitIt(0, anotherKeepSafeForHeight+100, textsurface)
                except:
                    textsurface = myfont.render(what2blit, False, (120, 120, 120))
                    oof.BlitIt(0, 150, textsurface)
                """

    elif scene == "Tileset":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                battle.running("off")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if downKey == True:
                        pass
                    elif downKey == False:
                        downKey = True
                        myplayer.direction(-1)
                        myplayer.imageScaler(0.5, 67, 130)
                elif event.key == pygame.K_RIGHT:
                    if downKey == True:
                        pass
                    elif downKey == False:
                        downKey = True
                        myplayer.direction(1)
                        myplayer.imageScaler(0.5, 67, 130)
                elif event.key == pygame.K_UP:
                    if downKey == True:
                        pass
                    elif downKey == False:
                        downKey = True
                        myplayer.move_forward()
                        scene = myplayer.scenePrep
                        print(scene)
                        #print(dungeon.ymap)
                elif event.key == pygame.K_s:
                    imageName = str((int(imageName)+1))
                    pygame.image.save(oof.display, "screenshots/" + imageName + ".png")
                elif event.key == pygame.K_ESCAPE:
                    clicked()
                    scene = "Escaped"
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP:
                    downKey = False


        #pygame.event.pump()
        oof.BlackOut()
        #oof.BlitIt(captureX, captureY, dungeon.image)

        for i in range(1,len(dungeon.ymap)+1):
            #work = True --see next triple quote to know use--
            for q in range(1,len(dungeon.xmap)+1):
                """
                if (i == 1 or i == len(dungeon.ymap)) and (q == len(dungeon.xmap)//2+1):
                    dungeon.image = pygame.image.load(asset_folder + "darkfloor.png")
                    dungeon.imageScaler(0.2, 271, 155)
                    oof.BlitIt(wBx, wBy, dungeon.image)
                    dungeon.image = pygame.image.load(asset_folder + "floor.png")
                    dungeon.imageScaler(0.2, 271, 155)
                    #print("Succesful Planting")

                elif (q == 1 or q == len(dungeon.xmap)) and (i == len(dungeon.ymap)//2+1):
                    dungeon.image = pygame.image.load(asset_folder + "darkfloor.png")
                    dungeon.imageScaler(0.2, 271, 155)
                    oof.BlitIt(wBx, wBy, dungeon.image)
                    dungeon.image = pygame.image.load(asset_folder + "floor.png")
                    dungeon.imageScaler(0.2, 271, 155)
                    #print("Succesful Planting")
                else:
                    oof.BlitIt(wBx, wBy, dungeon.image)
                    """
                oof.BlitIt(wBx, wBy, dungeon.image)
                #--------------------print(str(wBx) + " " + str(wBy) + " " + dungeon.xmap[q-1] + dungeon.ymap[i-1])
                if (dungeon.ymap[i-1] == "X") and (dungeon.xmap[q-1] == "X"):
                    #print(str(wBx) + " " + str(wBy))
                    captureX = wBx + 12# - int(dungeon.imageXsize/2)
                    captureY = wBy - 45 #- int(dungeon.imageYsize/2)
                    #--------------------print(captureY)
                    #-------------------------print("hi *kirby")
                wBx += int(dungeon.imageXsize/2)
                wBy += int(dungeon.imageYsize/2)
            else:
                wBx = oriloc
                wBy = original_location_for_the_y_axis_of_the_frickin_floor
                wBx -= i * int(dungeon.imageXsize/2)
                wBy += i * int(dungeon.imageYsize/2)
                #-----------------------------------print(i)

        else: #This else loop didnt use to be here so the character would starts at the wrong point
            wBx = oriloc
            wBy = original_location_for_the_y_axis_of_the_frickin_floor

        if myplayer.moved == True:
            myplayer.moved == False
            event = random.randint(1, 100)

        """ #use with one space rooms --its glitchy and something is wrong with the players location. i dont need a one space room as there is no where to go anyway--
        if work == False:
            for i in range(1,2):
                work = True
                for q in range(1,2):
                    oof.BlitIt(wBx, wBy, dungeon.image)
                    if (dungeon.ymap[i-1] == "X") and (dungeon.xmap[q-1] == "X"):
                    #if (i == 1) and (q == 1):
                        captureX = wBx + 12
                        captureY = wBy - 45
                    wBx += int(dungeon.imageXsize/2)
                    wBy += int(dungeon.imageYsize/2)
                else:
                    wBx = oriloc
                    wBy = original_location_for_the_y_axis_of_the_frickin_floor
                    wBx -= i * int(dungeon.imageXsize/2)
                    wBy += i * int(dungeon.imageYsize/2)
                    """

        """
        click+=1
        if click == 120:
            click = 0
            ds = random.randint(2,15) #dungeon size --maximum 15--
        """
        #print(dungeon.xmap)
        #print(dungeon.ymap)
        dungeon.change_layout(ds, ds)
        #print(ds)
        #------------------------------------print(str(captureX) + " " + str(captureY))
        dungeon.player_on(myplayer.x, myplayer.y)
        oof.BlitIt(captureX, captureY, myplayer.image)
    pygame.display.update()
    oof.clock.tick(60)

#left and right arrows to change directions and spacebar to move forward!!! --idea inspired from dad-- *I was planning on using isometric keyboard input but realised I had none :(. Maybe 7, 9, 1 and 3?

#x and y axis
#      x   x   x   x
#    y
#   y
#  y
# y

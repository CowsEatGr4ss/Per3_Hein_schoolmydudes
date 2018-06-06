from help_pack import *
import random
import os
import time

#imported gpio commands to make controller work
from time import sleep
from gpiozero import Button


width = 800
height = 600
FPS = 100


#identifies location of buttons on breadboard
left_button = Button(13)
right_button = Button(21)
middle_button = Button(26)

#function for movement in buttons
def movement(left_button, right_button):
    movement_inputs = [left_button.is_pressed, right_button.is_pressed]
    return movement_inputs

#function for firing projectile through button
def button_fire(middle_button):
    return middle_button.is_pressed

#-------[VOLITILE]------------------------------------#
gameDisplay = pygame.display.set_mode((width, height))
#-----------------------------------------------------#

#difinite
white = (255, 255, 255)
black = (0, 0, 0)
#-------[VOLITILE]------------------------------------#
background1 = pygame.image.load('b1.png')#update
background2 = pygame.image.load('b2.png')#update
#-----------------------------------------------------#

#assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "pz")

        
            
            
        



#initial
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Strider")
clock = pygame.time.Clock()

#-------[VOLITILE]------------------------------------#
def back (a,b):
    gameDisplay.blit(background1,(a,b))
a = 0
b = 0

def back2 (a,b):
    gameDisplay.blit(background2,(a1,b1))
a1 = 0
b1 = 0
#-----------------------------------------------------#
makeMusic('toto.mp3')#update
playMusic()


score = 0



class heart100(pygame.sprite.Sprite):#update
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400,20))
        self.image = pygame.image.load('100.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 700
        self.rect.bottom = 100
        self.speedx = 0

class heart75(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400,20))
        self.image = pygame.image.load('75.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 700
        self.rect.bottom = 100
        self.speedx = 0

class heart50(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400,20))
        self.image = pygame.image.load('50.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 700
        self.rect.bottom = 100
        self.speedx = 0

class heart25(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400,20))
        self.image = pygame.image.load('25.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 700
        self.rect.bottom = 100
        self.speedx = 0

class heart0(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400,20))
        self.image = pygame.image.load('0.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 700
        self.rect.bottom = 100
        self.speedx = 0





class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400,20))
        self.image = pygame.image.load('avatar1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height - 20
        self.speedx = 0
        self.shield = 104 #update

    def update(self):
        self.speedx = 0
        keystate = movement(left_button, right_button)
        if keystate[0]:
            self.speedx = -10
            self.image = pygame.image.load('avatar1.png')
        if keystate[1]:
            self.speedx = 10
            self.image = pygame.image.load('right.png')
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
    def fire(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((240, 40))
        self.image = pygame.image.load('1-11.png')#update
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-300, -100)
        self.speedy = random.randrange(3, 12)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height + 10:
            self.rect.x = random.randrange(0, width - self.rect.width)
            self.rect.y = random.randrange(-400, -100)
            self.speedy = random.randrange(5, 20)
            
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image = pygame.image.load('projectile1.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom<0:
            self.kill()

#class BigMob(pygame.sprite.Sprite):
    #def __init__(self):
        #self.image = pygame.Surface((100, 100))
        #self.image = pygame.image.load('1-1.png')
        #self.rect = self.image.get_rect()
        #self.rect.centerx = width/2
        #self.rect.bottom = height - 20
        #self.speedx = 0
#update
class Truck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((240, 40))
        self.image = pygame.image.load('planet14.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-300, -100)
        self.speedy = random.randrange(3, 12)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height + 10:
            self.rect.x = random.randrange(0, width - self.rect.width)
            self.rect.y = random.randrange(-400, -100)
            self.speedy = random.randrange(5, 20)


            
            
        
    
        

            
        
        
        
        

    
all_sprites = pygame.sprite.Group()



collect_mob = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()


all_sprites.add(player)

for i in range(14):
    m = Mob()
    all_sprites.add(m)
    collect_mob.add(m)
#update
for i in range(1):
    bm = Truck()
    all_sprites.add(bm)
    collect_mob.add(bm)

    
#loop
running = True

which_background = 'first'
last_time_background_changed = 0

while running:
    clock.tick(FPS)
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if button_fire(middle_button):
        player.fire()

        

            
            
        
    
    #update
    all_sprites.update()
    hits = pygame.sprite.groupcollide(collect_mob, bullets, True, True) #update

    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        collect_mob.add(m)
        score = score + 1
        

    hits = pygame.sprite.spritecollide(player, collect_mob, True)

        
    for hit in hits:
        player.shield = player.shield - 25 #update
        if player.shield <= 1:
            running = False
    
    
    #render
    #update
    if player.shield == 104:
        all_sprites.add(heart100())
        player.shield = 103

    if player.shield == 78:
        all_sprites.add(heart75())
        player.shield = 77

    if player.shield == 52:
        all_sprites.add(heart50())
        player.shield = 51

    if player.shield == 26:
        all_sprites.add(heart25())
        player.shield = 25

    if player.shield == 0:
        all_sprites.add(heart100())
        player.shield = 1

    
#--------------------[JR'S HELP]----------------------------------------
    if (pygame.time.get_ticks() - last_time_background_changed) > 500:#update
        if which_background == 'first':
            which_background = 'second'
        else:
            which_background = 'first'
            
        last_time_background_changed = pygame.time.get_ticks()

    if which_background == 'first':
        back(a, b)
    else:
        back2(a1,b1)
    
#-----------------------------------------------------------------------               
    all_sprites.draw(screen)

    myfont = pygame.font.SysFont("monospace", 33)
    scoretext = myfont.render("Score = "+str(score), 1, (255,255,255))
    screen.blit(scoretext, (25, 20))
    
    #after draw - flip display
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


    
pygame.quit()

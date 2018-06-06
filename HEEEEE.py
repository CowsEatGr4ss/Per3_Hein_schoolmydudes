import pygame
import random
import os
import time
from time import sleep
from gpiozero import Button

left_button = Button(13)
right_button = Button(21)
middle_button = Button(26)

def movement(left_button, right_button):
    movement_inputs = [left_button.is_pressed, right_button.is_pressed]
    return movement_inputs

def button_fire(middle_button):
    return middle_button.is_pressed

width = 800
height = 600
FPS = 100
#-------[VOLITILE]------------------------------------#
gameDisplay = pygame.display.set_mode((width, height))
#-----------------------------------------------------#

#difinite
white = (255, 255, 255)
black = (0, 0, 0)
#-------[VOLITILE]------------------------------------#
background1 = pygame.image.load('back1.png')
background2 = pygame.image.load('back2.png')
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((400,20))
        self.image = pygame.image.load('avatar1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height - 20
        self.speedx = 0

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
        self.image = pygame.image.load('avatar1.png')
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

            
        
        
        
        

    
all_sprites = pygame.sprite.Group()



collect_mob = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()

all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    collect_mob.add(m)
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
    hits = pygame.sprite.groupcollide(collect_mob, bullets, True, True)

    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        collect_mob.add(m)

    hits = pygame.sprite.spritecollide(player, collect_mob, False)

        
    if hits:
        running = False
    #render
    screen.fill(black)
#--------------------[JR'S HELP]----------------------------------------
    #if (pygame.time.get_ticks() - last_time_background_changed) > 500:
        #if which_background == 'first':
            #which_background = 'second'
        #else:
            #which_background = 'first'
            
        #last_time_background_changed = pygame.time.get_ticks()

    #if which_background == 'first':
        #back(a, b)
    #else:
        #back2(a1,b1)
    back(a, b)
#-----------------------------------------------------------------------               
    all_sprites.draw(screen)
    #after draw - flip display
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


    
pygame.quit()

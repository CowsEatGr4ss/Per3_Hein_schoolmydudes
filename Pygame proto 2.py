import pygame
import random
import os
import time
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
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
            self.image = pygame.image.load('avatar1.png')
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
            self.image = pygame.image.load('right.png')
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

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
            
class projectile(pygame.sprite.Sprite):
    def __ini__(sefl):
        pygame.sprite.Sprite.__init__(self)
        
        
        
        

    
all_sprites = pygame.sprite.Group()

collect_mob = pygame.sprite.Group()
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
        

            
            
        
    
    #update
    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, collect_mob, False)
    if hits:
        running = False
    #render
    screen.fill(black)
#--------------------[JR'S HELP]----------------------------------------
    if (pygame.time.get_ticks() - last_time_background_changed) > 500:
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
    #after draw - flip display
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)


    
pygame.quit()

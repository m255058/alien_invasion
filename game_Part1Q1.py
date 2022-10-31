import pygame
from pygame.sprite import Sprite
import sys

class Bullet(Sprite):
    '''A class to manage bullets fired'''

    def __init__(self,ai_game):
        '''create a bullet at the ships position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create a bullet rect a (0,0) and then correct position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullets position
        self.y = float (self.rect.y)

    def update(self):
        '''move bullets'''
        #update bullet position
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        '''draw bullet to the screen'''
        pygame.draw.rect(self.screen,self.color,self.rect)
#-----------------------------------------------------------------

class Settings:
    def __init__(self):
        '''initialize game settings'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (150,0,255)

        #ship speed
        self.ship_speed = 1.5

        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

#-----------------------------------------------
class Ship:
    def __init__(self, ai_game):
        '''initialize ship in starting position'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #start new ship at bottom center
        self.rect.midleft = self.screen_rect.midleft

        #store a decminal value for the ships horizontal position
        self.y = float(self.rect.y)

        #Movment flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''update the ships position'''
        #update the ships value not rect.x
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        #update rect object from self.x
        self.rect.y = self.y

    def blitme(self):
        '''draw ship in it's current location'''
        self.screen.blit(self.image, self.rect)

#------------------------------------------------------------

class AlienInvasion():
    '''initialize game'''
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''Main game loop'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        '''respond to key presses and mouse clicks'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''respond to keypressess'''
        if event.key == pygame.K_UP:
            # move right
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # move left
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            #fire bullet
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''respond to key releases'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_bullets(self):
        '''update position of bullets and get rid of old bullets'''
        self.bullets.update()
        # get rid of bullets that disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left <= self.screen.get_rect().width:
                self.bullets.remove(bullet)
    def _fire_bullet(self):
        '''create a new bullet and add it to the group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_screen(self):
        '''update the images on screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

ai = AlienInvasion()
ai.run_game()

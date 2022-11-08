import pygame

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
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decminal value for the ships horizontal position
        self.x = float(self.rect.x)

        #Movment flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''update the ships position'''
        #update the ships value not rect.x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        '''draw ship in it's current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center the ship on the screen'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
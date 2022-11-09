import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    '''A class to represent a single alien in the fleet'''
    def __init__(self,ai_game):
        '''initialize alien'''
        super().__init__()
        self.screen = ai_game.screen
        # Alien settings

        #load the alien image and set its rects
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position
        self.x = float(self.rect.x)
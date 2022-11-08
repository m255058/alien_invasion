import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A class to represent a single alien in the fleet'''
    def __init__(self, ai_game):
        '''initialize alien'''
        super().__init__()
        self.screen = ai_game.screen
        # load the alien image and set its rects
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store the alien's exact horizontal position
        self.x = float(self.rect.x)

class StarGame():
    '''initialize game'''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (0, 0, 0)
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        '''Main game loop'''
        while True:
            self._update_screen()

    def _update_screen(self):
        '''update the images on screen'''
        self.screen.fill(self.bg_color)
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _create_alien(self, alien_number, row_number):
        '''Create an alien and place it in the row'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        #alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        #self.aliens.add(alien)




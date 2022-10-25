import pygame
import sys
from settings import Settings
from ship import Ship
class AlienInvasion():
    '''initialize game'''
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
    def run_game(self):
        '''Main game loop'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    def _check_events(self):
        '''respond to key presses and mouse clicks'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move right
                    self.ship.moving_right = True
                elif event.key ==pygame.K_LEFT:
                    #move left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        '''update the images on screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

ai = AlienInvasion()
ai.run_game()

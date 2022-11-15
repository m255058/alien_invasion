import sys
import pygame
from star import Star

class StarGame:
    def __init__(self):
        '''initialize game'''
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (60,0,60)
        self.stars = pygame.sprite.Group()
        self._create_fleet()
    def run_game(self):
        '''Start main loop'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()
    def _create_fleet(self):
        '''create the fleet of stars'''
        #make one star
        star = Star(self)
        self.stars.add(star)

#----Main----------------------------------------

game = StarGame()
game.run_game()
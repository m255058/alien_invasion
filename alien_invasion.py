import pygame
import sys

class AlienInvasion():
    '''initialize game'''
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')
    def run_game(self):
        '''Main game loop'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

ai = AlienInvasion()
ai.run_game()

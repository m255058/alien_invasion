import pygame

WIDTH = 800
HEIGHT = 500

star = pygame.image.load('images/alien.png')
star.pos = 0, 0
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
while True:
    screen.fill(0, 0, 0)
    star.draw()

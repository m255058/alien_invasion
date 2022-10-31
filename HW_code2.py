import pygame

WIDTH = 500
HEIGHT = 300

ship = Actor('ship')
ship.pos = WIDTH/2,HEIGHT/2

def draw():
    screen.fill((150,0,255))
    ship.draw()

def update():
    movement()

def movement():
    '''moves the ship on specific keydowns and ups'''
    if keyboard.RIGHT and ship.right < WIDTH:
        ship.x += 4
    if keyboard.LEFT and ship.left > 0:
        ship.x -= 4
    if keyboard.UP and ship.top > 0:
        ship.y -= 4
    if keyboard.DOWN and ship.bottom < HEIGHT:
        ship.y += 4

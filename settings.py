class Settings:
    def __init__(self):
        '''initialize game settings'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (150,0,255)

        #ship speed
        self.ship_speed = 1.75

        #Bullet Settings
        self.bullet_speed = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
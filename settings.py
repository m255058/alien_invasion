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
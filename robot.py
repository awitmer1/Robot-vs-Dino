from weapon import Weapon

class Robot:

    def __init__(self):

        self.name = ''
        self.health = 100
        self.active_weapon = Weapon()
    
    def attack (self, dino):
        pass
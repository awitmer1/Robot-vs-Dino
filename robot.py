from weapon import Weapon

class Robot:

    def __init__(self, robot_name, weapon_name):

        self.name = robot_name
        self.health = 200
        self.active_weapon = Weapon(weapon_name)
    
    def attack (self):
        print(f'{self.name} attacks with {self.active_weapon.name} for {self.active_weapon.attack_power} damage')

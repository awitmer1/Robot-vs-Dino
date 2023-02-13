class Dino:

    def __init__(self, dino_name):
        self.name = dino_name
        self.attack_power = 25
        self.health = 500
    
    def attack (self):
        print(f'{self.name} attacks for {self.attack_power} damage')


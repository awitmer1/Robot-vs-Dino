from robot import Robot
from dino import Dino

class Battlefield:

    def __init__(self, robot_name, weapon_name, dino_name):
        self.robot = Robot(robot_name, weapon_name)
        self.dino = Dino(dino_name)

    def run_game (self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome (self):
        print(f"""
        Welcome to the battle arena!

        Dinosaur {self.dino.name} is starting with {self.dino.health} health.
        Robot {self.robot.name} is starting with {self.robot.health} and weilding a {self.robot.active_weapon.name}.

        Let the battle begin!
        """)

    def battle_phase (self):
        
        while self.robot.health > 0 or self.dino.health > 0:
            self.robot.attack() 
            self.dino.health -= self.robot.active_weapon.attack_power
            print(f"{self.dino.name} now has {self.dino.health} health.")
        
            self.dino.attack()
            self.robot.health -= self.dino.attack_power
            print(f"{self.robot.name} now has {self.robot.health} health.")

            if self.robot.health <= 0:
                self.display_winner()
                print(f"The {self.dino.name} is our champion!")
                break
            elif self.dino.health <= 0:
                self.display_winner()
                print(f"The {self.robot.name} is our champion!")
                break

    def display_winner (self):
        print(f"We have a winner!")
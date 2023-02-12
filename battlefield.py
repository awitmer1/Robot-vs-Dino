from robot import Robot
from dino import Dino

class Battlefield:

    def __init__(self, robot_name, weapon_name, dino_name):
        self.robot = Robot(robot_name, weapon_name)
        self.dino = Dino(dino_name)

    def run_game (self):
        pass

    def display_welcome (self):
        print("Welcome to the battle arena!")

    def battle_phase (self):
        print("Let the battle begin!")


    def display_winner (self):
        print("We have a winner!")


battlefield_one = Battlefield("Mecha Godzilla", "Mecha Sword", "Triceratops")

print("Testing")
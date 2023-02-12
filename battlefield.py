from robot import Robot
from dino import Dino

class Battlefield:

    def __init__(self):
        self.robot = Robot()
        self.dino = Dino()

    def run_game (self):
        pass

    def display_welcome (self):
        print("Welcome to the battle arena!")

    def battle_phase (self):
        print("Let the battle begin!")

    def display_winner (self):
        print("We have a winner!")
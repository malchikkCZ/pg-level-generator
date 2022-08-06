import pygame
from settings import *

from source.generator import LevelGenerator


class Level:

    def __init__(self, game):
        self.game = game
        self.level = {}

        self.level_generator = LevelGenerator()
        self.get_new_level()
    
    def get_new_level(self):
        self.level = self.level_generator.get_new_level()

    def draw(self):
        colors = {
            '0': 'darkgray',
            '1': 'brown',
            '8': 'yellow',
            '9': 'green'
        }

        for pos in self.level:
            pygame.draw.rect(
                self.game.screen, 
                colors[self.level[pos]], 
                (pos[0] * 10, pos[1] * 10, 10, 10)
            )

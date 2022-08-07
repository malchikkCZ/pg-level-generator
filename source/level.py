import pygame
from settings import *

from source.generator import LevelGenerator


class Level:

    def __init__(self, game, method='rooms'):
        self.game = game
        self.level = {}

        self.level_generator = LevelGenerator()
        self.method = method
        self.get_new_level()
    
    def get_new_level(self):
        self.level = self.level_generator.get_new_level(self.method)

    def draw(self):
        colors = {
            '0': 'darkgray',
            '1': 'brown',
            '8': 'blue',
            '9': 'green'
        }

        for pos in self.level:
            pygame.draw.rect(
                self.game.screen, 
                colors[self.level[pos]], 
                (pos[0] * 16, pos[1] * 16, 16, 16)
            )

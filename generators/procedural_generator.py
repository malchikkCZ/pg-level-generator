import random

import pygame
from settings import *


class ProceduralGenerator:

    def __init__(self):
        self.grid_width = GRID_WIDTH
        self.grid_height = GRID_HEIGHT
        self.grid_padding = GRID_PADDING

        self.possible_directions = [
            pygame.math.Vector2(1, 0),
            pygame.math.Vector2(0, 1),
            pygame.math.Vector2(-1, 0),
            pygame.math.Vector2(0, -1)
        ]

    def get_direction(self):
        return random.choice(self.possible_directions)

    def get_new_position(self, previous_pos, direction):
        new_pos = (
            min(
                max(
                    self.grid_padding,
                    previous_pos[0] + direction.x
                ), 
                self.grid_width - self.grid_padding - 1
            ), 
            min(
                max(
                    self.grid_padding,
                    previous_pos[1] + direction.y
                ),
                self.grid_height - self.grid_padding - 1
            )
        )

        return new_pos

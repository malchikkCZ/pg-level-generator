import random

from generators import RandomWalkCorridorGenerator, SimpleRandomWalkGenerator
from settings import *


class LevelGenerator:

    def __init__(self):
        self.level = {}

    def get_new_level(self):
        self.generate_level()
        return self.level

    def generate_level(self):
        self.level = {}
        start_pos = (GRID_WIDTH // 2, GRID_HEIGHT // 2)

        generated_map, room_positions, dead_ends = RandomWalkCorridorGenerator().generate(start_pos)
        end_pos = room_positions[-1]
        self.level.update({pos: '0' for pos in generated_map})

        room_nodes = []
        for room_node in dead_ends:
            if room_node not in room_nodes:
                generated_room = SimpleRandomWalkGenerator(False).generate(room_node)
                self.level.update({pos: '1' for pos in generated_room})
                room_nodes.append(room_node)

        room_count = len(room_positions) * 0.8
        while len(room_nodes) < room_count:
            room_node = random.choice(room_positions)
            if room_node not in room_nodes:
                generated_room = SimpleRandomWalkGenerator(False).generate(room_node)
                self.level.update({pos: '1' for pos in generated_room})
                room_nodes.append(room_node)

        self.level[start_pos] = '8'
        self.level[end_pos] = '9'

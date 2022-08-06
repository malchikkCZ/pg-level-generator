import random

from settings import *

from generators.procedural_generator import ProceduralGenerator


class SimpleRandomWalkGenerator(ProceduralGenerator):

    def __init__(self, start_randomly=True):
        super().__init__()
        self.start_randomly = start_randomly

    def generate(self, start_pos, iterations=10, walk_length=10):
        path = []
        path.append(start_pos)
        for _ in range(iterations):
            single_path = []
            previous_pos = start_pos
            while len(single_path) < walk_length:
                direction = self.get_direction()
                new_pos = self.get_new_position(previous_pos, direction)
                if new_pos not in single_path:
                    single_path.append(new_pos)
                previous_pos = new_pos

            path.extend(
                [pos for pos in single_path if pos not in path]
            )
            if self.start_randomly:
                start_pos = random.choice(path)

        return path

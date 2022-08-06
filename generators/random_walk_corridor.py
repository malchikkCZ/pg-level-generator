from settings import *

from generators.procedural_generator import ProceduralGenerator


class RandomWalkCorridorGenerator(ProceduralGenerator):

    def __init__(self):
        super().__init__()

    def generate(self, start_pos, corridor_length=14, corridor_count=5):
        corridor = [start_pos]
        room_positions = []
        for _ in range(corridor_count):
            previous_pos = start_pos
            direction = self.get_direction()
            for _ in range(corridor_length):
                new_pos = self.get_new_position(previous_pos, direction)
                if new_pos not in corridor:
                    corridor.append(new_pos)
                previous_pos = new_pos

            start_pos = previous_pos
            if start_pos not in room_positions:
                room_positions.append(start_pos)
        
        dead_ends = []
        for pos in corridor:
            neighbours_count = 0
            for direction in self.possible_directions:
                neighbour = self.get_new_position(pos, direction)
                if neighbour in corridor:
                    neighbours_count += 1
            if neighbours_count == 1:
                dead_ends.append(pos)

        return corridor, room_positions, dead_ends

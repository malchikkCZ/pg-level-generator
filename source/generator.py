import math
import random

from generators import (
    BinarySpacePartingGenerator,
    RandomWalkCorridorGenerator, 
    SimpleRandomWalkGenerator
)

from settings import *


class LevelGenerator:

    def __init__(self):
        self.level = {}
        self.start_pos = ()
        self.end_pos = ()

    def get_new_level(self, method):
        self.level = {}
        match method:
            case 'corridor':
                self.generate_level_corridor_first()
            case 'rooms':
                self.generate_level_rooms_first(True)

        self.decorate_level()
        self.level[self.start_pos] = '8'
        self.level[self.end_pos] = '9'

        return self.level

    def generate_level_corridor_first(self, start_randomly=False):
        start_pos = (GRID_WIDTH // 2, GRID_HEIGHT // 2)

        generated_map, room_positions, dead_ends = RandomWalkCorridorGenerator().generate(start_pos)
        end_pos = room_positions[-1]
        self.level.update({pos: '0' for pos in generated_map})

        room_nodes = []
        for room_node in dead_ends:
            if room_node not in room_nodes:
                generated_room = SimpleRandomWalkGenerator(start_randomly).generate(room_node)
                self.level.update({pos: '0' for pos in generated_room})
                room_nodes.append(room_node)

        room_count = len(room_positions) * 0.8
        while len(room_nodes) < room_count:
            room_node = random.choice(room_positions)
            if room_node not in room_nodes:
                generated_room = SimpleRandomWalkGenerator(start_randomly).generate(room_node)
                self.level.update({pos: '0' for pos in generated_room})
                room_nodes.append(room_node)

        self.start_pos = start_pos
        self.end_pos = end_pos

    def generate_level_rooms_first(self, walk_rooms_randomly=False):
        initial_space = []
        for y in range(GRID_HEIGHT):
            initial_row = []
            for x in range(GRID_WIDTH):
                initial_row.append((x, y))
            initial_space.append(initial_row)

        room_list = BinarySpacePartingGenerator().generate(initial_space)

        room_centers = []
        for room in room_list:
            nodes = []
            for row in room:
                for coord in row:
                    nodes.append(coord)
            center = room[len(room) // 2][len(room[0]) // 2]
            room_centers.append(center)

            if walk_rooms_randomly:
                generated_room = SimpleRandomWalkGenerator(False).generate(center, 100, len(room))
                generated_room = [node for node in generated_room if node in nodes]
            else:
                generated_room = nodes

            self.level.update({pos: '0' for pos in generated_room})

        start_pos = random.choice(room_centers)

        current_center = start_pos
        room_centers.remove(current_center)

        corridors = []
        while len(room_centers) > 0:
            closest = self.find_closest_point(current_center, room_centers)
            room_centers.remove(closest)
            new_corridor = self.create_corridor(current_center, closest)
            current_center = closest
            corridors.extend(new_corridor)

        self.level.update({pos: '0' for pos in corridors})
        end_pos = corridors[-1]

        self.start_pos = start_pos
        self.end_pos = end_pos

    def find_closest_point(self, current_center, room_centers):
        distance = math.inf
        for center in room_centers:
            current_distance = math.dist(current_center, center)
            if current_distance < distance:
                distance = current_distance
                closest = center

        return closest

    def create_corridor(self, start_pos, destination):
        corridor = []
        pos_x = start_pos[0]
        pos_y = start_pos[1]
        corridor.append((pos_x, pos_y))
        while pos_y != destination[1]:
            if destination[1] > pos_y:
                pos_y += 1
            else:
                pos_y -= 1
            corridor.append((pos_x, pos_y))
        while pos_x != destination[0]:
            if destination[0] > pos_x:
                pos_x += 1
            else:
                pos_x -= 1
            corridor.append((pos_x, pos_y))

        borders = []
        for node in corridor:
            x, y = node
            for dy in [-1, 0]:
                for dx in [-1, 0]:
                    if (x + dx, y + dy) not in corridor and (x + dx, y + dy) not in borders:
                        borders.append((x + dx, y + dy))
        corridor.extend(borders)

        return corridor

    def decorate_level(self):
        walls = {}
        for node in self.level.keys():
            x, y = node

            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if (x + dx, y + dy) not in self.level:
                        
                        walls.update({(x + dx, y + dy): '1'})

        self.level.update(walls)
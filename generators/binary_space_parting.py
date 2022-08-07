import random

from settings import *

from generators.procedural_generator import ProceduralGenerator


class BinarySpacePartingGenerator(ProceduralGenerator):

    def __init__(self):
        super().__init__()

    def generate(self, initial_space, min_width=15, min_height=15, offset=2):
        rooms_queue = []
        rooms_list = []

        rooms_queue.append(initial_space)
        while len(rooms_queue) > 0:
            room = rooms_queue.pop(0)
            size_x = len(room[0])
            size_y = len(room)
            if size_y >= min_height and size_x >= min_width:
                if random.random() < 0.5:
                    if size_y >= min_height * 2:
                        self.split_horizontaly(rooms_queue, room)
                    elif size_x >= min_width * 2:
                        self.split_verticaly(rooms_queue, room)
                    else:
                        rooms_list.append(self.set_offset(room, offset))
                else:
                    if size_x >= min_width * 2:
                        self.split_verticaly(rooms_queue, room)
                    elif size_y >= min_height * 2:
                        self.split_horizontaly(rooms_queue, room)
                    else:
                        rooms_list.append(self.set_offset(room, offset))

        return rooms_list

    def split_horizontaly(self, rooms_queue, room):
        size_y = len(room)

        split_y = random.randint(1, size_y - 1)
        splitted_room = []
        for _ in range(split_y):
            row = room.pop(0)
            splitted_room.append(row)

        rooms_queue.append(room)
        rooms_queue.append(splitted_room)

    def split_verticaly(self, rooms_queue, room):
        size_x = len(room[0])

        split_x = random.randint(1, size_x - 1)
        splitted_room = []
        for row in room:
            splitted_row = []
            for _ in range(split_x):
                col = row.pop(0)
                splitted_row.append(col)
            splitted_room.append(splitted_row)

        rooms_queue.append(room)
        rooms_queue.append(splitted_room)

    def set_offset(self, room, offset):
        for _ in range(offset):
            room.pop(0)
            room.pop()

            for row in room:
                row.pop()
                row.pop(0)

        return room
import pygame
import sys

from source import Level

from settings import *


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(GAME_RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1

        self.level = Level(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) \
                or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                self.level.get_new_level()

    def update(self):
        pygame.display.flip()
        self.delta_time = self.clock.tick(GAME_FPS)
        pygame.display.set_caption('Press SPACE to generate new map')

    def draw(self):
        self.screen.fill('black')
        self.level.draw()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
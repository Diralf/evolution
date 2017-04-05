import os
import random
import sys

import pygame
from pygame.locals import *

from app import globvars
from app.entity.human.man_human import ManHuman, FemaleHuman
from app.weather.weather_color import climate_color
from app.weather.weather_generator import create_earth_area
from core.entity.entity_group import EntityGroup
from core.geometry import convert
from core.graph.hexagon import make_hex_grid
from core.graph.point import Point


class Game:
    def __init__(self):
        pygame.init()
        self.screen = None
        self.background = None

        self.font_obj = pygame.font.Font('freesansbold.ttf', 12)

        self.planet_area = create_earth_area(globvars.grid_width, globvars.grid_height)
        self.all_sprites_list = EntityGroup()
        self.humans = []
        self.hexagon_grid_points = make_hex_grid(globvars.cell_size, globvars.cell_size, globvars.cell_size, globvars.grid_width, globvars.grid_height)

        self.fpsClock = pygame.time.Clock()
        self.init_window()
        self.init_background()
        self.init_humans()

    def init_window(self):
        os.environ['SDL_VIDEO_WINDOW_POS'] = '{0},{1}'.format(0, 30)
        self.screen = pygame.display.set_mode((globvars.screen_width, globvars.screen_height), 0, 32)
        os.environ['SDL_VIDEO_WINDOW_POS'] = ''

        pygame.display.set_caption('Evolution by Diralf')

    def init_humans(self):
        for i in range(globvars.human_count * 2):
            if i < globvars.human_count:
                hum = ManHuman(Point(random.randint(0, globvars.screen_width), random.randint(0, globvars.screen_height)))
            else:
                hum = FemaleHuman(Point(random.randint(0, globvars.screen_width), random.randint(0, globvars.screen_height)))
            self.humans.append(hum)
            self.all_sprites_list.add(hum.body)

    def init_background(self):
        self.background = pygame.Surface((globvars.screen_width, globvars.screen_height))
        self.background.fill(globvars.WHITE)

        for i in range(len(self.planet_area)):
            pygame.draw.polygon(self.background, climate_color(self.planet_area[i].temperature, 100), self.hexagon_grid_points[i])
            pygame.draw.polygon(self.background, (200, 200, 200), self.hexagon_grid_points[i], 1)

    def draw_text(self, surface, x, y, text, color=(0,0,0)):
        textSurfaceObj = self.font_obj.render(text, True, color, (0,0,0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (x, y)
        surface.blit(textSurfaceObj, textRectObj)

    def update_app(self, delta):
        for human in self.humans:
            human.update(delta)
        self.all_sprites_list.update()

    def draw_app(self, surface):
        surface.blit(self.background, (0, 0))

        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(surface, (0, 255, 0), (x, y), 3)

        # pos = convert.pixel_to_line(
        #     x - globvars.cell_size,
        #     y - globvars.cell_size,
        #     globvars.cell_size,
        #     globvars.grid_width)
        #
        # pygame.draw.polygon(surface, (0, 0, 255), self.hexagon_grid_points[pos])

        self.all_sprites_list.draw(surface)

        for human in self.humans:
            self.draw_text(surface, human.body.position.x + 24, human.body.position.y - 30,
                           'h {0}'.format(int(human.data.health.health)),(0, 255, 0))
            self.draw_text(surface, human.body.position.x + 24, human.body.position.y - 18,
                           'a {0}'.format(int(human.data.health.age)), (0, 255, 255))
            self.draw_text(surface, human.body.position.x + 24, human.body.position.y - 6,
                           't {0}'.format(int(human.data.temperature.temperature)), (255, 0, 0))
        # all_sprites_list.draw_debug(DISPLAYSURF)

    def start(self):
        # run the game loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.update_app(1)
            self.draw_app(self.screen)

            pygame.display.update()
            self.fpsClock.tick(globvars.FPS)

globvars.game = Game()
globvars.game.start()
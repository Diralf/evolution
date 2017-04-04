import pygame, sys
import random
from pygame.locals import *
from pygame.time import get_ticks

from app.entity.human.man_human import ManHuman, FemaleHuman
from app.graph.pygame_hexagon import draw_polygon_grid
from app.weather.weather_generator import earth_climate
from core.graph.point import Point

pygame.init()

# ---- init application -----------------

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# размер окна
w, h = 1200, 800

# set up the window
DISPLAYSURF = pygame.display.set_mode((w, h), 0, 32)
BACKGROUND = pygame.Surface((w, h))

pygame.display.set_caption('Evolution by Diralf')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# размер поля
grid_width = 38
grid_width = 30
grid_height = 26
grid_height = 22
# размер ячейки
size = 24

# ------- init game --------------

planet = earth_climate(grid_width, grid_height)

humans = []

human_count = 200
for i in range(human_count*2):
    if i < human_count:
        hum = ManHuman(Point(random.randint(0, w), random.randint(0, h)))
    else:
        hum = FemaleHuman(Point(random.randint(0, w), random.randint(0, h)))
    humans.append(hum)

# ---- init drawing

BACKGROUND.fill(WHITE)
draw_polygon_grid(BACKGROUND, size, size, size, grid_width, grid_height, planet)

# --- init obejcts

cirx = 0


def update_app(delta):
    for human in humans:
        human.update(delta)


def draw_app():
    DISPLAYSURF.blit(BACKGROUND, (0, 0))
    pygame.draw.circle(DISPLAYSURF, BLUE, (cirx, 50), 20, 0)

    humans_depth = {}

    for human in humans:
        pos = int(human.body.position.y)
        if -1 < pos < 900:
            if not (pos in humans_depth):
                humans_depth[pos] = []
            humans_depth[pos].append(human)

    for i in range(900):
        if i in humans_depth:
            for human in humans_depth[i]:
                human.draw(DISPLAYSURF)


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    cirx += 1
    update_app(1)
    draw_app()

    pygame.display.update()
    fpsClock.tick(FPS)

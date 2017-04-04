import random

from app.weather.weather_generator import *
from app.entity.human.man_human import *
from app.weather.weather_color import *
from core.geometry import convert
from core.graph.hexagon import polygon_grid, make_hex_grid
from libs.vectors import Vector
import pygame
import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')


# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)



# draw on the surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


# MAIN
game = [True]


def main():
    # размер окна
    w, h = 1200, 600
    win = GraphWin("My Circle", w, h)
    win.master.geometry('%dx%d+%d+%d' % (w, h, -10, 0))

# размер поля
    grid_width = 38
    grid_height = 26
# размер ячейки
    size = 20


    v1 = Vector(3, 5)
    v2 = Vector(5, 3)

    print(v1)
    print(v1 * 5)


    poly_grid = polygon_grid(
        Point(size, size), size, grid_width, grid_height)

    planet = earth_climate(grid_width, grid_height)

    for i in range(len(planet)):
        poly_grid[i].setFill(climate_color(planet[i].temperature, 100))

    for p in poly_grid:
        p.draw(win)

    humans = []
    human_count = 10
    for i in range(human_count*2):
        if i < human_count:
            hum = ManHuman(Point(random.randint(0, w), random.randint(0, h)))
        else:
            hum = FemaleHuman(Point(random.randint(0, w), random.randint(0, h)))
        hum.start_draw(win)
        humans.append(hum)

    def motion(event):
        pos = convert.pixel_to_line(
            event.x - 20,
            event.y - 20,
            20,
            grid_width)
        # poly_grid[pos].setFill("blue")

    def exit(event):
        game[0] = False

    win.bind('<Motion>', motion)
    win.bind('<Button-1>', exit)

    sleep_time = target_delta = 1. / 60
    target_time = time.time()
    fps_second = 0
    fps_count = 0

    while game[0]:

        # ---- LOGIC ----

        for hum in humans:
            hum.update(sleep_time)

        # ---- LOOP -----

        target_time += target_delta
        sleep_time = target_time - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            print('sleep_time', sleep_time)
            #time.sleep(1)

        fps_second += sleep_time
        fps_count += 1
        if fps_second >= 1:
            print('fps', fps_count)
            fps_second -= 1
            fps_count = 0
        if fps_second <= -1:
            #print('fps', fps_count, fps_second)
            fps_second = 0
            fps_count = 0

        if win.isClosed():
            game[0] = False

            # ----- END -----

    win.close()


main()

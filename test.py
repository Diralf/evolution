from geometry import convert
from geometry.vectors import Vector
from graph.hexagon import *
from weather.weather_generator import *
from weather.weather_color import *
from entity.human.man_human import *

# MAIN
game = [True]


def main():
    win = GraphWin("My Circle", 1200, 600)
    win.master.geometry('%dx%d+%d+%d' % (1200, 600, -10, 0))

    grid_width = 38
    grid_height = 26
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

    human = ManHuman(Point(100, 100))
    human.start_draw(win)
    human2 = FemaleHuman(Point(150, 150))
    human2.start_draw(win)

    def motion(event):
        pos = convert.pixel_to_line(
            event.x - 20,
            event.y - 20,
            20,
            grid_width)
        poly_grid[pos].setFill("blue")

    def exit(event):
        game[0] = False

    win.bind('<Motion>', motion)
    win.bind('<Button-1>', exit)

    sleep_time = target_delta = 1. / 60
    target_time = time.time()

    counter = 30

    while game[0]:
        human.update(sleep_time)
        human2.update(sleep_time)

        target_time += target_delta
        sleep_time = target_time - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

        if sleep_time != 0 and counter <= 0:
            counter = 30
            print('fps', 1. / sleep_time)

        if counter > 0:
            counter -= 1

    win.close()


main()

from geometry import convert
from graph.hexagon import *
from weather.weather_generator import *
from weather.weather_color import *
from entity.human.man_human import *

# MAIN

def main():
    win = GraphWin("My Circle", 1480, 800)

    grid_width = 42
    grid_height = 26
    size = 20

    poly_grid = polygon_grid(
        Point(20, 20), size, grid_width, grid_height)

    planet = earth_climate(grid_width, grid_height)

    for i in range(len(planet)):
        poly_grid[i].setFill(climate_color(planet[i].temperature, 100))

    for p in poly_grid:
        p.draw(win)

    human = ManHuman(Point(100, 100))
    human.draw(win)

    human2 = FemaleHuman(Point(150, 150))
    human2.draw(win)


    # def motion(event):
    #     pos = convert.pixel_to_line(
    #         event.x - 20,
    #         event.y - 20,
    #         20,
    #         grid_width)
    #     poly_grid[pos].setFill("blue")
    #
    # win.bind('<Motion>', motion)

    print(win.getMouse())
    win.close()


main()

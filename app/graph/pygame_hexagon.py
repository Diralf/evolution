import pygame

from app.weather.weather_color import climate_color
from core.graph.hexagon import make_hex_grid


def draw_polygon_grid(surf, x, y, size, count_w, count_h, planet):
    hex_grid_array = make_hex_grid(x, y, size, count_w, count_h)

    for i in range(len(planet)):
        pygame.draw.polygon(surf, climate_color(planet[i].temperature, 100), hex_grid_array[i])
        pygame.draw.polygon(surf, (200, 200, 200), hex_grid_array[i], 1)


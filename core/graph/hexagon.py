from math import pi, sin, cos, sqrt

from libs.graphics import *

RTC = sqrt(3)  # REGULAR_TRIANGLE coefficient
HRTC = sqrt(3) / 2  # half RTC


def hex_corner(center_x, center_y, size, i):
    angle_deg = 60 * i + 30
    angle_rad = pi / 180 * angle_deg
    return Point(center_x + size * cos(angle_rad),
                 center_y + size * sin(angle_rad))


def make_hexagon(center_x, center_y, size):
    corners = []
    for i in range(6):
        corners.append(hex_corner(center_x, center_y, size, i))
    return corners


def make_hex_line(start_x, start_y, size, count):
    width = RTC * size
    hex_line = []

    for i in range(count):
        hex_line.append(make_hexagon(start_x + width * i, start_y, size))

    return hex_line


def make_hex_grid(start_x, start_y, size, count_w, count_h):
    h_distance = size * 1.5
    half_width = HRTC * size
    hex_grid = []
    for i in range(count_h):
        hex_grid.extend(make_hex_line(start_x + half_width * (i % 2),
                                      start_y + h_distance * i,
                                      size,
                                      count_w))
    return hex_grid


def polygon_grid(start, size, count_w, count_h):
    poly_grid = []
    hex_line = make_hex_grid(start.x, start.y, size, count_w, count_h)

    for hx in hex_line:
        p = Polygon(hx)
        p.setOutline("#BBBBDD")
        poly_grid.append(p)

    return poly_grid

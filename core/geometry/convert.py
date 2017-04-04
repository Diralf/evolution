# CONVERSION
from math import floor, sqrt

from core.graph.point import Point


class Hex:
    def __init__(self, q, r):
        self.q = float(q)
        self.r = float(r)


class Cube:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class Offset:
    def __init__(self, col, row):
        self.x = col
        self.y = row


def cube_to_hex(c):  # axial
    q = c.x
    r = c.z
    return Hex(q, r)


def hex_to_cube(h):  # axial
    x = h.q
    z = h.r
    y = -x - z
    return Cube(x, y, z)


def hex_to_oddr(h):
    col = h.q + (h.r - (int(h.r) & 1)) / 2
    row = h.r
    return Offset(col, row)


def oddr_to_hex(o):
    q = o.x - (o.y - (int(o.y) & 1)) / 2
    r = o.y
    return Hex(q, r)


def line_to_oddr(pos, w):
    x = pos % w
    y = floor(pos / w)
    return Offset(x, y)


def oddr_to_line(off, w):
    return int(off.y * w + off.x)


def hex_to_line(h, w):
    return int(oddr_to_line(hex_to_oddr(h), w))


# ROUND

def cube_round(h):
    rx = round(h.x)
    ry = round(h.y)
    rz = round(h.z)

    x_diff = abs(rx - h.x)
    y_diff = abs(ry - h.y)
    z_diff = abs(rz - h.z)

    if x_diff > y_diff and x_diff > z_diff:
        rx = -ry - rz
    elif y_diff > z_diff:
        ry = -rx - rz
    else:
        rz = -rx - ry

    return Cube(rx, ry, rz)


def hex_round(h):
    return cube_to_hex(cube_round(hex_to_cube(h)))


# PIXEL
def hex_to_pixel(h, size):
    x = size * sqrt(3) * (h.q + h.r / 2)
    y = size * 3 / 2 * h.r
    return Point(x, y)


def offset_to_pixel(h, size):
    x = size * sqrt(3) * (h.x + 0.5 * (h.y & 1))
    y = size * 3 / 2 * h.y
    return Point(x, y)


def pixel_to_hex(x, y, size):
    q = (x * sqrt(3) / 3 - y / 3) / size
    r = y * 2 / 3 / size
    return hex_round(Hex(q, r))


def pixel_to_line(x, y, size, w):
    return hex_to_line(pixel_to_hex(x, y, size), w)

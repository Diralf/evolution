from weather.area import *


def earth_climate(width, height):
    planet = []
    top = -50
    middle = 100
    step = (middle - top) / (height/2)

    for i in range(height):
        if i < height / 2:
            temp = top + step*i
        else:
            temp = middle - step*(i - height/2)
        print(temp)
        for j in range(width):
            planet.append(Area(temp))

    return planet

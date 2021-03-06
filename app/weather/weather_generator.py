from core.weather.area import Area


def create_earth_area(width, height):
    planet = []
    top = -50
    middle = 100
    step = (middle - top) / (height/2)

    for i in range(height):
        if i < height / 2:
            temp = top + step*i
        else:
            temp = middle - step*(i - height/2)

        for j in range(width):
            planet.append(Area(temp))

    return planet

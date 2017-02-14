SNOW_START = -100
SNOW_END = 0
GRASS_START = 0
GRASS_END = 40
SAND_START = 40
SAND_END = 100


def color_rgb(r,g,b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r,g,b)


def climate_color(temperature, brightness):
    r = g = b = brightness
    color_range = 255 - brightness

    if SAND_START <= temperature:
        r_step = color_range / (SAND_END - SAND_START)
        change = brightness + (temperature - SAND_START) * r_step
        r = brightness + (temperature - SAND_START) * r_step * 2
        g = 255 - color_range/4 - change*0.5
        b = brightness

        if r > 255:
            r = 255

        if r < brightness + color_range*3/4:
            g = 255 - color_range/4 - change*0.25

    if GRASS_START <= temperature <= GRASS_END:
        g_step = color_range / (GRASS_END - GRASS_START)
        r = 255 - (temperature - GRASS_START) * g_step
        g = 255 - (temperature - GRASS_START) * g_step/4
        b = r

    if SNOW_START <= temperature <= SNOW_END:
        b_step = color_range / (SNOW_END - SNOW_START)
        r = brightness + (temperature - SNOW_START) * b_step
        g = r
        b = 255

    return color_rgb(int(r),int(g),int(b))


def temperature_color(temperature, brightness):
    if temperature > 0:
        r_step = brightness / 100
        b = int(255 - temperature * r_step)
        g = b
        r = 255
    else:
        b_step = brightness / 100
        r = int(temperature * b_step * -1)
        g = r
        b = 255
    return color_rgb(r,g,b)

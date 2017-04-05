import pygame
import random
from pygame.surface import Surface

from core.entity.entity_body import EntityBody
from core.graph.point import Point

def load_half_image(name):
    return pygame.image.load(name)

images_man = (
    load_half_image('asset/man.png'),
    load_half_image('asset/man2.png'),
    load_half_image('asset/man3.png'),
    load_half_image('asset/man4.png'),
    load_half_image('asset/man5.png'),
    # load_half_image('asset/man6.png'),
    load_half_image('asset/man7.png'),
    load_half_image('asset/man8.png')
)

images_female = (
    load_half_image('asset/female.png'),
    load_half_image('asset/female2.png'),
    load_half_image('asset/female3.png'),
    load_half_image('asset/female4.png'),
    load_half_image('asset/female5.png'),
    load_half_image('asset/female6.png'),
    load_half_image('asset/female7.png'),
    load_half_image('asset/female8.png')
)


class HumanBody(EntityBody):
    min_size = 5
    max_size = 15

    def __init__(self, surface, position=None, offset=None):
        # type: (Surface, Point) -> None
        super(HumanBody, self).__init__(surface, position, offset)


class ManHumanBody(HumanBody):
    def __init__(self, position):
        # type: (Point) -> None
        super(ManHumanBody, self).__init__(random.choice(images_man), position, Point(16, 32))


class FemaleHumanBody(HumanBody):
    def __init__(self, position):
        # type: (Point) -> None
        super(FemaleHumanBody, self).__init__(random.choice(images_female), position, Point(16, 32))

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

surf_man = pygame.image.load('asset/man.png')
# surf_man = pygame.Surface((6, 6), pygame.SRCALPHA, 32)
# #surf_man = surf_man.convert_alpha()
# pygame.draw.rect(surf_man, (0, 0, 0), (0, 0, 6, 6), 1)

surf_female = pygame.image.load('asset/female.png')
# surf_female = pygame.Surface((6, 6), pygame.SRCALPHA, 32)
# #surf_female = surf_female.convert_alpha()
# pygame.draw.circle(surf_female, (0, 0, 0), (3, 3), 3, 1)


class HumanBody(EntityBody):
    min_size = 5
    max_size = 15

    def __init__(self, surface, position=None):
        # type: (Surface, Point) -> None
        EntityBody.__init__(self, surface, position)


class ManHumanBody(HumanBody):
    def __init__(self, position):
        # type: (Point) -> None
        HumanBody.__init__(self, random.choice(images_man), position)


class FemaleHumanBody(HumanBody):
    def __init__(self, position):
        # type: (Point) -> None
        HumanBody.__init__(self, random.choice(images_female), position)

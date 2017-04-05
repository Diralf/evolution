from pygame.sprite import Sprite
from pygame.surface import Surface

from core.graph.point import Point


class EntityBody(Sprite):

    def __init__(self, surface, position=None, offset=None):
        # type: (Surface, Point, Point) -> None
        super(EntityBody, self).__init__()
        self.image = surface
        self.rect = self.image.get_rect()
        self.position = position or Point(0, 0)
        self.offset = offset or Point(0, 0)

        self.rect.move_ip(position.x, position.y)

    def update(self):
        self.rect.x = self.position.x - self.offset.x
        self.rect.y = self.position.y - self.offset.y

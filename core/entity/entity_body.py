from pygame.surface import Surface

from core.graph.point import Point


class EntityBody:

    def __init__(self, surface, position=None):
        # type: (Surface, Point) -> None
        self.surface = surface
        self.position = position or Point(0, 0)

    def draw(self, parent_surface):
        parent_surface.blit(self.surface, self.position.get_point())

from pygame.surface import Surface

from core.entity.entity_body import EntityBody
from core.entity.entity import Entity


class VisualEntity(Entity):
    def __init__(self, body):
        # type: (EntityBody) -> None
        Entity.__init__(self)
        self.body = body

    def draw(self, parent_surface):
        # type: (Surface) -> None
        self.body.draw(parent_surface)

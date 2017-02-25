from core.entity.entity_body import EntityBody
from core.entity.entity import Entity
from libs.graphics import GraphWin


class VisualEntity(Entity):
    def __init__(self, body):
        # type: (EntityBody) -> None
        Entity.__init__(self)
        self.body = body

    def start_draw(self, win):
        # type: (GraphWin) -> None
        self.body.start_draw(win)

    def draw(self):
        self.body.draw()

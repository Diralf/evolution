from app.entity.human.human import Human
from app.entity.human.human_body import HumanBody
from app.entity.human.human_data import HumanData
from core.entity.imovable import IMovable
from core.entity.visual_entity import VisualEntity

from app.entity.human.simple_behavior import SimpleBehavior


class VisualHuman(Human, VisualEntity, IMovable):
    def __init__(self, body, human_data=None):
        # type: (HumanBody, HumanData) -> None

        Human.__init__(self, human_data)
        VisualEntity.__init__(self, body)
        IMovable.__init__(self)

        self.behavior = SimpleBehavior(self)

    def move(self, dx, dy):
        # type: (float, float) -> None
        if dx != 0 or dy != 0:
            self.body.position.move(dx, dy)

    def update(self, delta):
        Human.update(self, delta)
        IMovable.update(self, delta)
        self.behavior.update(delta)




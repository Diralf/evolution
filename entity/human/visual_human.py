from entity.human.human import Human
from entity.human.human_body import HumanBody
from entity.human.parents import Parents
from entity.human.simple_behavior import SimpleBehavior
from entity.imovable import IMovable
from entity.visual_entity import VisualEntity


class VisualHuman(Human, VisualEntity, IMovable):
    def __init__(self, gender, parents, body):
        # type: (str, Parents, HumanBody) -> None
        Human.__init__(self, gender, parents)
        VisualEntity.__init__(self, body)
        IMovable.__init__(self)
        self.behavior = SimpleBehavior(self)

    def move(self, dx, dy):
        # type: (float, float) -> None
        self.body.figure.move(dx, dy)

    def update(self, delta):
        Human.update(self, delta)
        IMovable.update(self, delta)
        self.behavior.update(delta)




from app.entity.human.human_data import *

from core.entity.entity import *


class Human(Entity):
    def __init__(self, human_data=None):
        # type: (HumanData) -> None
        Entity.__init__(self)
        self.data = human_data or HumanData()

    def update(self, delta):
        self.data.health.age += 0.1
        self.data.temperature.temperature *= self.data.temperature.weight

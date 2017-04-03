from app.entity.human.human_data import *
from app.entity.human.parents import Parents

from core.entity.entity import *


class Human(Entity):
    def __init__(self, human_data=HumanData()):
        # type: (HumanData) -> None
        Entity.__init__(self)
        self.data = human_data

    def update(self, delta):
        self.data.health.age += 0.1
        self.data.temperature.temperature *= self.data.temperature.weight

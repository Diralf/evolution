from entity.entity import *


class Human(Entity):
    def __init__(self, gender, parents):
        Entity.__init__(self)
        self.gender = gender
        self.parents = parents
        self.age = 0.0
        self.temper = 36.6
        self.temper_coeff = 0.0  # coefficient of temperature change
        self.speed = 0.0

    def update(self):
        self.age += 0.1
        self.temper *= self.temper_coeff

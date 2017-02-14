from entity.human.human import *
from entity.human.human_body import *


class VisualHuman(Human):
    def __init__(self, gender, parents, body):
        # type: (str, Parents, HumanBody) -> None
        Human.__init__(self, gender, parents)
        self.body = body

    def draw(self, win):
        # type: (GraphWin) -> None
        self.body.draw(win)


class ManHuman(VisualHuman):
    def __init__(self, position):
        VisualHuman.__init__(self, 'M', None, ManHumanBody(5, position))


class FemaleHuman(VisualHuman):
    def __init__(self, position):
        VisualHuman.__init__(self, 'F', None, FemaleHumanBody(5, position))
        self.body = FemaleHumanBody(5, position)

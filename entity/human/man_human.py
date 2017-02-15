from entity.human.human_body import *
from entity.human.parents import *
from entity.human.visual_human import VisualHuman


class ManHuman(VisualHuman):
    def __init__(self, position, parents=Parents(())):
        VisualHuman.__init__(self, 'M', parents, ManHumanBody(position))


class FemaleHuman(VisualHuman):
    def __init__(self, position, parents=Parents(())):
        VisualHuman.__init__(self, 'F', parents, FemaleHumanBody(position))

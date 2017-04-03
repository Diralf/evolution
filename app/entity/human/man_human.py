from app.entity.human.human_body import *
from app.entity.human.human_data import *
from app.entity.human.parents import *
from app.entity.human.visual_human import VisualHuman


class ManHuman(VisualHuman):
    def __init__(self, position, human_data=HumanData()):
        # type: (Point, HumanData) -> None
        VisualHuman.__init__(self, ManHumanBody(position), human_data)
        self.data.social.gender = 'M'


class FemaleHuman(VisualHuman):
    def __init__(self, position, human_data=HumanData()):
        # type: (Point, HumanData) -> None
        VisualHuman.__init__(self, FemaleHumanBody(position), human_data)
        self.data.social.gender = 'F'

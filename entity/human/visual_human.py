from entity.human.human import Human
from entity.human.human_body import HumanBody
from entity.human.parents import Parents
from entity.visual_entity import VisualEntity


class VisualHuman(Human, VisualEntity):
    def __init__(self, gender, parents, body):
        # type: (str, Parents, HumanBody) -> None
        Human.__init__(self, gender, parents)
        VisualEntity.__init__(self, body)

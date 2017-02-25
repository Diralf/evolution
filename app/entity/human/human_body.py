from core.entity.entity_body import EntityBody
from libs.graphics import *


class HumanBody(EntityBody):
    min_size = 5
    max_size = 15

    def __init__(self, figure, position=Point(0, 0)):
        # type: (GraphicsObject, Point) -> None
        EntityBody.__init__(self, figure, position, None, HumanBody.min_size, HumanBody.max_size)


class ManHumanBody(HumanBody):
    def __init__(self, position, size=HumanBody.min_size):
        # type: (Point, float) -> None
        HumanBody.__init__(self,
                           Rectangle(
                               Point(
                                   position.x - size / 2,
                                   position.y - size / 2
                               ),
                               Point(
                                   position.x + size / 2,
                                   position.y + size / 2
                               )
                           ),
                           position
                           )


class FemaleHumanBody(HumanBody):
    def __init__(self, position, size=HumanBody.min_size):
        # type: (Point, float) -> None
        HumanBody.__init__(self, Circle(position, size / 2), position)

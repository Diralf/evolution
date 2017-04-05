from app import globvars
from app.entity.human.behavior.health_behavior import HealthBehavior
from app.entity.human.behavior.simple_behavior import SimpleBehavior
from app.entity.human.behavior.temperature_behavior import TemperatureBehavior
from app.entity.human.human import Human
from app.entity.human.human_body import HumanBody
from app.entity.human.human_data import HumanData
from core.entity.imovable import IMovable
from core.entity.visual_entity import VisualEntity
from core.geometry import convert


class VisualHuman(Human, VisualEntity, IMovable):
    def __init__(self, body, human_data=None):
        # type: (HumanBody, HumanData) -> None

        Human.__init__(self, human_data)
        VisualEntity.__init__(self, body)
        IMovable.__init__(self)

        self.behavior = SimpleBehavior(self)
        self.current_cell = None

    def move(self, dx, dy):
        # type: (float, float) -> None
        if dx != 0 or dy != 0:
            self.body.position.move(dx, dy)

    def update(self, delta):
        Human.update(self, delta)
        IMovable.update(self, delta)
        self.behavior.update(delta)

        pos = convert.pixel_to_line(
            self.body.position.x - globvars.cell_size,
            self.body.position.y - globvars.cell_size,
            globvars.cell_size,
            globvars.grid_width)

        planet_area = globvars.game.planet_area
        if 0 <= pos < len(planet_area):
            self.current_cell = planet_area[pos]
        else:
            self.current_cell = None

        TemperatureBehavior.update(self)
        HealthBehavior.update(self)





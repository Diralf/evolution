from app.entity.human.parents import Parents


class MovementData:
    def __init__(self, speed=0.1):
        # type: (float) -> None
        self.speed = speed
        self.isMove = False


class TemperatureData:
    def __init__(self, temperature=36.6, weight=0.):
        # type: (float, float) -> None
        self.temperature = temperature
        self.weight = weight


class HealthData:
    def __init__(self, health=100., age=0.):
        # type: (float, float) -> None
        self.health = health
        self.age = age


class SocialData:
    def __init__(self, gender='U', parents=Parents(())):
        # type: (str, Parents) -> None
        self.gender = gender
        self.parents = parents

class TravelData:
    def __init__(self, duration_stop=3., duration_move=3.):
        # type: (float, float) -> None
        self.duration_stop = duration_stop
        self.duration_move = duration_move

class HumanData:
    def __init__(self,
                 d_health=HealthData(),
                 d_social=SocialData(),
                 d_temperature=TemperatureData(),
                 d_movement=MovementData(),
                 d_travel=TravelData()):
        # type: (HealthData, TemperatureData, MovementData) -> None
        self.health = d_health
        self.social = d_social
        self.temperature = d_temperature
        self.movement = d_movement
        self.travel = d_travel

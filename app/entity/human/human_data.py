from app.entity.human.parents import Parents


class MovementData:
    def __init__(self, speed=0.5):
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
    def __init__(self, gender='U', parents=None):
        # type: (str, Parents) -> None
        self.gender = gender
        self.parents = parents or Parents(())


class TravelData:
    def __init__(self, duration_stop=60., duration_move=20.):
        # type: (float, float) -> None
        self.duration_stop = duration_stop
        self.duration_move = duration_move


class HumanData:
    def __init__(self,
                 d_health=None,
                 d_social=None,
                 d_temperature=None,
                 d_movement=None,
                 d_travel=None):
        # type: (HealthData, SocialData, TemperatureData, MovementData, TravelData) -> None

        self.health = d_health or HealthData()
        self.social = d_social or SocialData()
        self.temperature = d_temperature or TemperatureData()
        self.movement = d_movement or MovementData()
        self.travel = d_travel or TravelData()

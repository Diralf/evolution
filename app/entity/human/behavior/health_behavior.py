from app import globvars


class HealthBehavior:
    def __init__(self):
        pass

    @staticmethod
    def update(human):
        # type: (VisualHuman) -> None
        data_health = human.data.health
        data_temperature = human.data.temperature

        if data_health.health <= 0:
            data_health.health = 0
            human.data.movement.speed = 0
            return

        data_health.age += globvars.aging

        HealthBehavior.apply_temperature_on_health(data_health, data_temperature)
        HealthBehavior.recovery_health(data_health)

    @staticmethod
    def recovery_health(data_health):
        recovery = data_health.recovery if 0 < data_health.health < 99 else 0
        age_influence = data_health.age * globvars.age_influence_coff
        data_health.health += recovery - age_influence

    @staticmethod
    def apply_temperature_on_health(data_health, data_temperature):
        diff = abs(globvars.normal_temperature - data_temperature.temperature) - globvars.range_normal_temperature
        diff = diff if diff >= 0 else 0
        step = diff * globvars.temperature_influence_on_health
        data_health.health -= step

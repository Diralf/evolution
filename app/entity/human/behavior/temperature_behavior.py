from app import globvars


class TemperatureBehavior:

    def __init__(self):
        pass

    @staticmethod
    def update(human):
        area_temp = human.current_cell.temperature if human.current_cell else -1000
        temp_data = human.data.temperature
        temp_data.temperature = TemperatureBehavior.apply_out_temperature(temp_data.temperature, area_temp)
        temp_data.temperature = TemperatureBehavior.return_temperature(temp_data.temperature, temp_data.increase, temp_data.decrease)

    @staticmethod
    def apply_out_temperature(inside_temp, outside_temp):
        diff = inside_temp - outside_temp
        step = diff * globvars.area_temperature_influence
        return inside_temp - step

    @staticmethod
    def return_temperature(inside_temp, inc, dec):
        deviation = globvars.normal_temperature - inside_temp
        coff = inc if deviation >= 0 else dec
        step = deviation * coff
        return inside_temp + step

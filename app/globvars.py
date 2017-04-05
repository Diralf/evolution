FPS = 30
# размер окна
screen_width, screen_height = 1280, 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

grid_width = 30
grid_height = 22
cell_size = 24

grid_width = 60
grid_height = 44
cell_size = 12


human_count = 50

game = None


aging = 0.1                                             # скорось старения
normal_temperature = 36.6                               # нормальная температура
range_normal_temperature = 2                            # допустимое отклонение от нормальной температуры
area_temperature_influence = 0.01
temperature_influence_on_health = 0.5                   # влияние температуры на здоровье
max_age = 60                                            # возраст при котором здоровье начнет падать
normal_helth_recovery = 1.                              # нормальная скорость восстановления здороья
age_influence_coff = normal_helth_recovery/max_age      # коэффициент влияния возраста на здоровье
import random


class SimpleBehavior:
    def __init__(self, visual_human):
        # type: (VisualHuman) -> None
        self.human = visual_human
        self.human.set_speed(0)
        self.movement = self.human.data.movement
        self.travel = self.human.data.travel
        self.interval = 0

    def update(self, delta):
        if self.interval <= 0:
            if self.movement.isMove:
                self.interval = random.randint(0, self.travel.duration_stop)
                self.human.set_speed(0)
                self.movement.isMove = False
            else:
                self.interval = random.randint(0, self.travel.duration_move)
                self.human.set_direction_in(random.randint(0, 359))
                self.human.set_speed(self.movement.speed)
                self.movement.isMove = True
        else:
            self.interval -= delta

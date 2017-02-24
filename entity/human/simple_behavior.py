import random


class SimpleBehavior:
    def __init__(self, visual_human):
        # type: (VisualHuman) -> None
        self.visual_human = visual_human
        self.max_interval = 0.5
        self.interval = 0
        self.isMove = False
        self.speed = 0.22
        self.visual_human.set_speed(0)

    def update(self, delta):
        if self.interval <= 0:
            self.interval = random.randint(0, 300)*0.01
            if self.isMove:
                self.visual_human.set_speed(0)
                self.isMove = False
            else:
                self.visual_human.set_direction_in(random.randint(0, 359))
                self.visual_human.set_speed(self.speed)
                self.isMove = True
        else:
            self.interval -= delta

from libs.vectors import Vector


class IMovable:

    start_direction = Vector(1, 0)

    def __init__(self, direction=Vector(1,0), vspeed=Vector(0,0)):
        # type: (Vector, Vector) -> None
        self.direction = direction
        self.vspeed = vspeed
        self.speed = vspeed.norm()
        self.is_changed = False

    def move(self, dx, dy):
        # type: (float, float) -> None
        pass

    def set_speed(self, speed):
        # type: (float) -> None
        self.speed = speed
        self.vspeed = self.direction * speed
        self.is_changed = True

    def set_direction_in(self, angle):
        # type: (float) -> None
        self.direction = IMovable.start_direction.rotate(angle)
        self.set_speed(self.speed)

    def set_direction_on(self, dangle):
        # type: (float) -> None
        self.direction = self.direction.rotate(dangle)
        self.set_speed(self.speed)

    def update(self, delta):
        # type: (float) -> None
        self.move(self.vspeed.getX(), self.vspeed.getY())

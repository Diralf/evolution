from graph.graphics import Circle, Point, update
from graph.iscalable import IScalable


class ScalableCircle(Circle, IScalable):
    def __init__(self, center, radius):
        Circle.__init__(self, center, radius)
        self.start_radius = radius

    def scale(self, scale):
        # type: (float) -> None
        IScalable.scale(self, scale)
        self.radius = self.start_radius * scale
        center = self.getCenter()
        self.p1 = Point(center.getX() - self.radius, center.getY() - self.radius)
        self.p2 = Point(center.getX() + self.radius, center.getY() + self.radius)

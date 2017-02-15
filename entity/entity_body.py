from graph.graphics import GraphWin
from graph.graphics import GraphicsObject
from graph.graphics import Point


class EntityBody:

    def __init__(self, figure, position=Point(0, 0), color="#999999", min_size=5, max_size=15):
        # type: (GraphicsObject, Point, str, float, float) -> None
        self.figure = figure
        self.position = position
        self.size = min_size
        self.max_size = max_size
        self.color = color

    def add_size(self, dsize):
        # type: (float) -> None
        if self.size > self.max_size:
            self.size = self.max_size
        else:
            self.size += dsize

    def change_color(self, color):
        # type: (str) -> None
        self.color = color

    def start_draw(self, win):
        # type: (GraphWin) -> None
        self.figure.draw(win)
        self.figure.setFill(self.color)

    def draw(self):
        self.figure.setFill(self.color)

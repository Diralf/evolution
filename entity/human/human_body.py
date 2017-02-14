from graph.graphics import *


class HumanBody:

    min_size = 5
    max_size = 20

    def __init__(self, figure, position = Point(0,0)):
        self.figure = figure
        self.size = HumanBody.min_size
        self.color = "#999999"
        self.position = position

    def add_size(self, dsize):
        if self.size > HumanBody.max_size:
            self.size = HumanBody.max_size
        else:
            self.size += dsize

    def change_color(self, color):
        self.color = color

    def draw(self, win):
        self.figure.draw(win)
        self.figure.setFill(self.color)


class ManHumanBody(HumanBody):
    def __init__(self, size, position):
        HumanBody.__init__(self,
            Rectangle(
                Point(
                    position.x - size/2,
                    position.y - size/2
                ),
                Point(
                    position.x + size/2,
                    position.y + size/2
                )
            ),
            position
        )

class FemaleHumanBody(HumanBody):
    def __init__(self, size, position):
        HumanBody.__init__(self,Circle(position, size/2), position)

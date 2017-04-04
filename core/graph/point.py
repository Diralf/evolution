class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy